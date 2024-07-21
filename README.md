![r.jpg](resource/logo.jpeg)
---
# InvestLM: A Large Language Model for Investment using Financial Domain Instruction Tuning

This is the repo for a new financial domain large language model, **InvestLM**, tuned on LLaMA-65B[1], using a carefully curated instruction dataset related to financial investment. We provide guidance on how to use InvestLM for inference.

[Paper link](https://arxiv.org/abs/2309.13064)

# Overview

Inspired by less-is-more-for-alignment (LIMA)[2], we manually curate a small yet diverse instruction dataset, covering a wide range of financial related topics, from Chartered Financial Analyst (CFA) exam questions to SEC filings to Stackexchange quantitative finance discussions. InvestLM shows strong capabilities in understanding financial text and provides helpful responses to investment related questions.

This repo contains:

- The download link for InvestLM's parameters
- The code for interacting with InvestLM

# InvestLM parameters

We use the Low-rank adaptation (LoRa) method [3] to tune LLaMA-65B's parameters in order to enhance the training efficiency. 

[The Lora weights for InvestLM](https://gohkust-my.sharepoint.com/:f:/g/personal/imyiyang_ust_hk/EkzSzd6oJ9JNj7rLZPh7178BUxvcpNCmqOnvFWOiIu7xCw?e=XhUGdG)

# Inference 

First, please install the required packages.
```
pip install -r requirements.txt
```
Then, run inference.py. You need to provide the path to the downloaded Lora parameters. The code will automatically load LLaMA-65B parameters from Huggingface. 

```
python inference.py \
    --base_model "Neko-Institute-of-Science/LLaMA-65B-HF" \
    --lora_weights ""
```

# Examples of InvestLM's Responses
## Investment Advice
**Instruction:**
The railroad company saw earnings roll a bit off track when it reported July 20. The company slightly missed analysts’ revenue expectations and reported earnings per share (EPS) that matched Wall Street’s estimates. That EPS performance might be fine for many companies, but it rang warning bells for CSX investors because it was the first time in five years that CSX failed to surpass EPS estimates. The company saw declining volume in a number of key products it transports, including agricultural and food, chemicals, and forest. Volume growth in coal provided some locomotion. Intermodal, which means using two transport modes to move freight (which often means converting freight from highway to intermodal rail), continued to struggle in the latest quarter. Railroads have grappled with worker shortages and supply chain issues. The latest CSX earnings raises questions about overall U.S. economic health. 

Given the recent performance of the railroad company, is it advisable to buy, hold, or sell stocks in the sector?

**Response:** Based on the information provided, the stock performance appears to be mixed. While revenue missed expectations, EPS met estimates, and coal volume provided some growth. On the other hand, declining volume in key product categories along with ongoing labor shortages and supply chain issues raise concerns. Overall, the outlook seems uncertain. As a result, a "hold" recommendation may be more appropriate than an outright "buy" or "sell" at this time. Investors should continue to monitor the economic indicators and company fundamentals before making an investment decision.

## Earnings transcript summarization
**Instruction:**
Based on the Earnings call transcript, summarize it and give me your view about the company.

**Input:**
And I'm confident that our disciplined approach to operating the business will result in our continued success throughout the balance of fiscal 2021.\nCoupled with the cost reduction actions we recently implemented, USG delivered an adjusted EBITDA margin of nearly 25%, up from approximately 19% in the prior year's Q1.\nFollowing up on the strong cash flow performance of the past year, we kicked-off fiscal 2021 with a record amount of cash flow, resulting in a free cash flow conversion ratio of 127% of net earnings.\nToday, we have approximately $740 million of liquidity at our disposal between cash on hand and available credit capacity while carrying a modest leverage ratio of 0.38.\nWe reported adjusted earnings per share of $0.55 a share, which increased $0.12 or 28% from the $0.43 we reported in prior year Q1.\nThe $0.55 also exceeded the consensus estimate of $0.45.\nGiven the backdrop of today's COVID operating environment, I'm pleased to report that we deliver Q1 adjusted EBITDA of over $29 million, which is approximately 4.5% higher than Q1 of last year, despite the noted sales decline in A&D that Vic mentioned, related to softness within commercial aerospace, which historically is one of our most profitable operating units.\nTotal sales in Q1 decreased $9 million compared to Q1 of last year, but Navy and space sales were up $4 million in A&D, which helped to mitigate the decline in commercial aerospace and Test and USG sales were up a combined $2 million.\nWe took several cost reduction actions recently, and as a result, we increased our Q1 gross margin by 150 basis points to 39.4% and reduced our SG&A spending by nearly 3%.\nEntered orders were solid, as we booked $158 million in new business and ended the quarter with a backlog of $512 million with a book-to-bill of 97%.\nOur Test business delivered a really solid Q1 by significantly beating our internal expectations and delivering an EBITDA margin of nearly 13% versus 11% last Q1. 

**Response:** 
Overall, USG's executives presented a positive outlook for the company's future based on their strong operational performance and financial metrics. Despite the impact of the coronavirus crisis, they expressed confidence in the company's ability to continue driving profitability through prudent cost management and demand diversification. The executives emphasized the company's record level of cash flows, high liquidity, and low debt ratios. They also highlighted robust order growth and expanded margins driven by productivity enhancements. While acknowledging the challenges posed by the pandemic, the executives expressed optimism that the company would maintain its momentum through innovation and operational discipline. In my opinion, the executives demonstrated clear leadership and communicated effectively in the face of unpredictable circumstances. Their concrete evidence of progress on cash generation, margin expansion, and order volume suggests effective stewardship of the business. The upbeat tone regarding inventiveness and cost control indicates competence and preparation.


# Ethics Statement
It is essential to recognize that the responses from InvestLM  should not be construed as definitive investment advice. All investment strategies and decisions should be made after careful consideration of one's financial situation, risk tolerance, and investment goals. We strongly advocate for potential investors to consult with professional financial advisors and consider multiple information sources before making any investment decisions. Relying solely on InvestLM 's outputs without thorough due diligence can lead to unintended financial consequences. Thorough analyses should be conducted to understand the strengths and weaknesses of InvestLM.

# License
InvestLM adopts the same licensing terms as LLaMA, which is a noncommercial license for research only.

# Citation

Please cite the repo if you use it in your research.

    @misc{yang2023investlm,
          title={InvestLM: A Large Language Model for Investment using Financial Domain Instruction Tuning}, 
          author={Yi Yang and Yixuan Tang and Kar Yan Tam},
          year={2023},
          eprint={2309.13064},
          archivePrefix={arXiv},
          primaryClass={q-fin.GN}
    }

# Contact
Please post a Github issue or contact [imyiyang@ust.hk](imyiyang@ust.hk) if you have any questions.

# References
[1] Touvron, Hugo, et al. "Llama: Open and efficient foundation language models." *arXiv preprint arXiv:2302.13971* (2023).

[2] Zhou, Chunting, et al. "Lima: Less is more for alignment." *arXiv preprint arXiv:2305.11206* (2023).

[3] Hu, Edward J., et al. "Lora: Low-rank adaptation of large language models." *arXiv preprint arXiv:2106.09685* (2021).
