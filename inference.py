import fire
import transformers
from transformers import AutoTokenizer,GenerationConfig
import torch
from peft import PeftModel

PROMPT_DICT = {
    "prompt_input": (
        "Below is an instruction that describes a task, paired with further context. "
        "Write a response that appropriately completes the request.\n\n"
        "Instruction:\n{instruction}\n\n Input:\n{input}\n\n Response:"
    ),
    "prompt_no_input": (
        "Below is an instruction that describes a task. "
        "Write a response that appropriately completes the request.\n\n"
        "Instruction:\n{instruction}\n\nResponse:"
    ),
}

def generate_prompt(instruction, input=None):
    if input:
        return PROMPT_DICT["prompt_input"].format(instruction=instruction,input=input)
    else:
        return PROMPT_DICT["prompt_no_input"].format(instruction=instruction)


def main(
    base_model: str = "",
    lora_weights: str = "",
    cache_dir: str = "",
):
        print("use Linear Scaled RoPE...")  
        from util.llama_rope_scaled_monkey_patch import replace_llama_rope_with_scaled_rope
        replace_llama_rope_with_scaled_rope()

        model = transformers.AutoModelForCausalLM.from_pretrained(
                            base_model,
                            torch_dtype=torch.float16,
                            cache_dir=cache_dir,
                            device_map="auto",
                    )

        model = PeftModel.from_pretrained(
                    model,
                    lora_weights,
                    device_map="auto",
                    cache_dir=cache_dir,
                    torch_dtype=torch.float16,
                )
        tokenizer =  AutoTokenizer.from_pretrained(base_model,use_fast=False,cache_dir=cache_dir)
        tokenizer.pad_token = tokenizer.unk_token
        model.eval()

        def generator(
                instruction,
                input=None,
                temperature=0.1,
                top_p=0.75,
                top_k=40,
                num_beams=1,
                max_new_tokens=512,
                **kwargs,
        ):

            ins_f = generate_prompt(instruction,input)
            inputs  =  tokenizer(ins_f, return_tensors="pt")
            input_ids = inputs["input_ids"].cuda()
            generation_config = GenerationConfig(
                    temperature=temperature,
                    top_p=top_p,
                    top_k=top_k,
                    do_sample=True,
                    num_beams=num_beams,
                    **kwargs,
                )

            # Without streaming
            with torch.no_grad():
                generation_output = model.generate(
                        input_ids=input_ids,
                        generation_config=generation_config,
                        return_dict_in_generate=True,
                        output_scores=False,
                        max_new_tokens=max_new_tokens,
                    )
            s = generation_output.sequences[0]
            output = tokenizer.decode(s)
            response = output.split("Response:")[1].strip()
            return response
        print("finish loading model..")

        prompt = """Nvidia led the tech sector higher yesterday as it continues its bull run after KeyBanc Capital Markets raised their price target from $550 to $620 last week. Micron Technologies closed +2.5% higher after gapping up with Apple and Google, both gaining nearly +1%.
            
        Based on the news, should I buy Nvidia or sell Nvidia stocks?"""
        
        result = generator(instruction = prompt,
                                input = None,
                                temperature = 0.1,
                                top_p = 0.75,
                                top_k = 40,
                                num_beams = 1,
                                max_new_tokens = 512)
        print(result)

if __name__ == "__main__":
    fire.Fire(main)

  


   