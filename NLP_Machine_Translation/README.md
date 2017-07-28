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
* Sebastian Ruder, 2017. [Deep Learning for NLP Best Practices](http://ruder.io/deep-learning-nlp-best-practices/): Talks about several cutting-edge mechanisms being developed for NLP and how to best apply them, such as: multi-task learning, attention, hyperparameter optimization, ensembling.
* Chris Manning and Richard Socher, 2017. [Natural Language Processing with Deep Learning](http://web.stanford.edu/class/cs224n/)(course). Great for learning about: advanced word embeddings, dependency parsing, coreference resolution, gated recurrent units.
* Dan Jurafsky and James H. [Speech and Language Processing](http://www.cs.colorado.edu/~martin/slp2.html), 2nd ed. [[3rd ed. drafts](https://web.stanford.edu/~jurafsky/slp3/) | [2017 course](http://web.stanford.edu/class/cs124/)] A comprehensive study of language processing and the related fields of speech recognition and synthesis. Covers in depth: statistical parsing, information retrieval, question-answering, summarization.
