# Sign Language Recognition System

## Introduction
The overall goal of this project is to build a word recognizer for American Sign Language video sequences, demonstrating the power of probabalistic models. In particular, this project employs [hidden Markov models (HMM's)](https://en.wikipedia.org/wiki/Hidden_Markov_model) to analyze a series of measurements taken from videos of American Sign Language (ASL) collected for research (see the [RWTH-BOSTON-104 Database](http://www-i6.informatik.rwth-aachen.de/~dreuw/database-rwth-boston-104.php)). In this video, the right-hand x and y locations are plotted as the speaker signs the sentence.

![ASLR demo](http://www-i6.informatik.rwth-aachen.de/~dreuw/images/demosample.png)


## Main Project: `asl_recognizer.ipynb`

### Part 1: Data

A data handler designed for this database is provided as the `AslDb` class in the `asl_data` module.  This handler creates the initial [pandas](http://pandas.pydata.org/pandas-docs/stable/) dataframe from the corpus of data included in the `data` directory as well as dictionaries suitable for extracting data in a format friendly to the [hmmlearn](https://hmmlearn.readthedocs.io/en/latest/) library.  We'll use those to create models in Part 2.

### Part 2: Model selection

Train each word in the training set with a range of values for the number of hidden states, and then score these alternatives with the model selector, choosing the "best" according to each strategy.

`my_model_selectors.py` - 
- `SelectorCV `: Log likelihood using cross-validation folds (CV)
- `SelectorBIC`: Bayesian Information Criterion (BIC)
- `SelectorDIC`: Discriminative Information Criterion (DIC) 

### Part 3: Build a Recognizer


### Part 4: Improve the WER with language models


## Other Information

### Raw Data

The data in the `data/` directory was derived from the [RWTH-BOSTON-104 Database](http://www-i6.informatik.rwth-aachen.de/~dreuw/database-rwth-boston-104.php). The handpositions (`hand_condensed.csv`) are pulled directly from the database [boston104.handpositions.rybach-forster-dreuw-2009-09-25.full.xml](boston104.handpositions.rybach-forster-dreuw-2009-09-25.full.xml). The three markers are:

*   0  speaker's left hand
*   1  speaker's right hand
*   2  speaker's nose
*   X and Y values of the video frame increase left to right and top to bottom.

Take a look at the sample [ASL recognizer video](http://www-i6.informatik.rwth-aachen.de/~dreuw/download/021.avi) to see how the hand locations are tracked.

The videos are sentences with translations provided in the database. For purposes of this project, the sentences have been pre-segmented into words based on slow motion examination of the files. These segments are provided in the `train_words.csv` and `test_words.csv` files in the form of start and end frames (inclusive).

The videos in the corpus include recordings from three different ASL speakers. The mappings for the three speakers to video are included in the `speaker.csv` file.


### Resources
