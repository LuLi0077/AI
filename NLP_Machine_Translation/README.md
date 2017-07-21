# Machine Translation

Build a deep neural network that functions as part of an end-to-end machine translation pipeline. The pipeline will accept English text as input and return the French translation.

* Load and inspect data
* Preprocess
	- tokenize the words into ids 
	- add padding to make all the sequences the same length
* Models
	- Model 1 is a simple RNN
	- Model 2 is a RNN with Embedding
	- Model 3 is a Bidirectional RNN
	- Model 4 is an Encoder-Decoder RNN
	- Model 5 is the final RNN
* Prediction


## Natural Language Processing pipeline

* text_processing (`text_processing.ipynb`): capture text data -> cleaning -> normalization -> tokenization -> stop word removal -> part-of-speech tagging -> named entity recognition -> stemming and lemmatization


* feature_extraction: transform text using Bag-of-Words, TF-IDF, Word2Vec and GloVe, and use t-SNE to visualize word embeddings


* modeling: language models, sentiment analysis, topic modeling, search and ranking, machine translation


## Resource

* [Pandas: Working with Text data](https://pandas.pydata.org/pandas-docs/stable/text.html) 
* [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
* The most common datasets used for machine translation are from [WMT](http://www.statmt.org/).
