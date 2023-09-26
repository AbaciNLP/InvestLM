![r.jpg](https://x.imgs.ovh/x/2023/09/14/6502da25e646d.jpg)
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
Please give the bullet point summarization of the following long earnings call transcripts.   

**Input:**
For the third quarter of 2021, revenues increased to $225.3 million compared to $116.6 million in the third quarter of the prior year.Operating profit for the third quarter was $8 million compared to an operating loss of $31.8 million in the same quarter of the prior year.EBITDA for the third quarter was $26.5 million compared to EBITDA of negative $12.3 million in the same quarter of the prior year.Our diluted earnings per share for the third quarter were $0.02 compared to an $0.08 loss per share in the same quarter of the prior year.Cost revenues -- cost of revenues during the third quarter of 2021 was $170.6 million or 75.7% of revenues compared to $100.9 million or 86.5% of revenues during the third quarter of 2020.Selling, general and administrative expenses were $31.4 million in the third quarter of 2021 compared to $32.4 million in the third quarter of the prior year.Selling, general and administrative expenses decreased from 27.8% of revenues in the third quarter of last year to 14% of revenues in the third quarter of 2021 due to leverage of higher revenues over costs that are relatively fixed during the short term.Depreciation was $18.1 million in the third quarter of 2021 compared to $18.7 million in the same quarter of the prior year.Our Technical Services segment revenues for the third quarter were $211.8 million compared to $109.3 million in the same quarter last year due to significantly higher activity and some pricing improvement.Segment operating profit in the third quarter of 2021 was $8.3 million compared to a $24.9 million operating loss in the third quarter of the prior year.Our Support Services segment revenues for the third quarter of this year were $13.5 million compared to $7.3 million in the same quarter last year.Segment operating loss in the third quarter was $55,000 compared to an operating loss of $3.8 million in the third quarter of the prior year.On a sequential basis, RPC's third quarter revenues increased 19.4% to $225.3 million from $188.8 million in the prior quarter.Cost of revenues during the third quarter of 2021 increased 17% to $170.6 million compared to $145.8 million in the prior quarter.As a percentage of revenues, cost of revenues decreased slightly from 77.2% in the second quarter of this year to 75.7% in the third quarter of 2021, reflecting some pricing improvement and operating expense leverage.Selling, general and administrative expenses during the third quarter of 2021 increased 6.9% to $31.4 million from $29.4 million in the prior quarter, resulting in positive operating expense leverage.As a result of these improvements, operating profit during the third quarter of 2021 was $8 million compared to an operating loss of $1.2 million in the prior quarter.RPC's EBITDA was $26.5 million in the third quarter compared to EBITDA of $17.3 million in the prior quarter.Our Technical Services segment revenues increased by $35.7 million or 20.3% in the third quarter due to increased activity levels and some pricing improvement in the segment service lines.RPC's Technical Services segment generated an $8.3 million operating profit in the current quarter compared to an operating profit of $1.4 million in the prior quarter.Our Support Services segment revenues increased by 6.6% to $13.5 million in the third quarter.Operating loss was $55,000 in the current quarter compared to an operating loss of $2.4 million in the prior quarter.This equipment was added late in the third quarter and is reflected as a finance lease on our balance sheet with a balloon payment due at the end of 12 months.Third quarter 2021 capital expenditures were $19 million, excluding the equipment acquired under a finance lease in the third quarter.We currently estimate full year 2021 capital expenditures, excluding lease financed equipment, to be approximately $65 million, comprised primarily of capitalized maintenance for existing equipment and selected growth opportunities.At the end of the third quarter, RPC's cash balance was approximately $81 million, and we remain debt-free.

**Response:** 
Third Quarter 2021 Summary

Q3 2021 Revenue increased 91.3% YoY to $225.3 million. Operating profit was $8 million compared to an operating loss of $31.8 million in the same quarter last year. EBITDA for the third quarter was $26.5 million compared to negative $12.3 million in the same quarter of the prior year. Diluted EPS for the third quarter were $0.02 compared to an $0.08 loss per share in the same quarter of the prior year. Cost of revenues for the third quarter of 2021 were 75.7% of revenues compared to 86.5% of revenues in the same quarter of the prior year. SG&A expenses decreased from 27.8% of revenues in the third quarter of last year to 14% of revenues this quarter due to leverage of higher revenues over costs that are relatively fixed in the short term. Technical Services segment revenues for the third quarter were $211.8 million compared to $109.3 million in the same quarter last year due to higher activity and some pricing improvement. Segment operating profit in the third quarter of 2021 was $8.3 million compared to a $24.9 million operating loss in the third quarter of the prior year. Support Services segment revenues for the third quarter of this year were $13.5 million compared to $7.3 million in the same quarter last year. The company reported sequential revenue increase of 19.4% in Q3 2021 to $225.3 million, compared to $188.8 million in the previous quarter. Cost of revenues in the third quarter of 2021 increased 17% to $170.6 million compared to $145.8 million in the prior quarter. As a percentage of revenues, cost of revenues decreased slightly from 77.2% in the second quarter to 75.7% in the third quarter of 2021, reflecting some pricing improvement and operating expense leverage. RPC's Technical Services segment revenues increased by $35.7 million or 20.3% in the third quarter due to increased activity levels.


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
