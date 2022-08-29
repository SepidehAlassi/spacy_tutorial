# NLP with spaCy Tutorial

For this tutorial, you need to install [spacy](https://spacy.io/usage)

For mac users, try installing with
`pip3 install spacy==3.2.0`

We will use the pre-trained statisticallanguage models of spaCy, download 
1. the small English model with 

`python3 -m spacy download en_core_web_sm`

2. the large German language model with

`python3 -m spacy download de_core_news_lg`

Furthermore, for sentiment anlaysis, we will add the [spacytextblob](https://pypi.org/project/spacytextblob/) pipe to spaCy's default pipeline. 
Install it with

`pip3 install spacytextblob`

To store the resulting SVG diagrams as PNG, we use `svglib` library, install it with:
`pip3 install svglib`






