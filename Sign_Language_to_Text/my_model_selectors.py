import math
import statistics
import warnings

import numpy as np
from hmmlearn.hmm import GaussianHMM
from sklearn.model_selection import KFold
from asl_utils import combine_sequences


class ModelSelector(object):
    '''
    base class for model selection (strategy design pattern)
    '''

    def __init__(self, all_word_sequences: dict, all_word_Xlengths: dict, this_word: str,
                 n_constant=3, min_n_components=2, max_n_components=10,
                 random_state=14, verbose=False):
        self.words = all_word_sequences
        self.hwords = all_word_Xlengths
        self.sequences = all_word_sequences[this_word]
        self.X, self.lengths = all_word_Xlengths[this_word]
        self.this_word = this_word
        self.n_constant = n_constant
        self.min_n_components = min_n_components
        self.max_n_components = max_n_components
        self.random_state = random_state
        self.verbose = verbose

    def select(self):
        raise NotImplementedError

    def base_model(self, num_states):
        # with warnings.catch_warnings():
        warnings.filterwarnings("ignore", category=DeprecationWarning)
        warnings.filterwarnings("ignore", category=RuntimeWarning)
        try:
            hmm_model = GaussianHMM(n_components=num_states, covariance_type="diag", n_iter=1000,
                                    random_state=self.random_state, verbose=False).fit(self.X, self.lengths)
            if self.verbose:
                print("model created for {} with {} states".format(self.this_word, num_states))
            return hmm_model
        except:
            if self.verbose:
                print("failure on {} with {} states".format(self.this_word, num_states))
            return None


class SelectorConstant(ModelSelector):
    """ select the model with value self.n_constant

    """

    def select(self):
        """ select based on n_constant value

        :return: GaussianHMM object
        """
        best_num_components = self.n_constant
        return self.base_model(best_num_components)


class SelectorBIC(ModelSelector):
    """ select the model with the lowest Baysian Information Criterion(BIC) score

    Bayesian information criteria: BIC = -2 * logL + p * logN
    where L is the likelihood of the fitted model, p is the number of parameters,
    and N is the number of data points.

    The lower the BIC value the better the model.
    """

    def select(self):
        """ select the best model for self.this_word based on
        BIC score for n between self.min_n_components and self.max_n_components

        :return: GaussianHMM object
        """
        warnings.filterwarnings("ignore", category=DeprecationWarning)

        bic = {}
        N, d = self.X.shape
        for n in range(self.min_n_components, self.max_n_components+1):
            try:
                p = (n+1)*(n-1) + 2*d*n
                model = self.base_model(n)
                logL = model.score(self.X, self.lengths)
                bic[n] = -2 * logL + p * np.log(N)
            except:
                pass

        best_num_components = self.n_constant
        score = math.inf
        for n in bic:
            if bic[n] < score:
                best_num_components = n
                score = bic[n]

        return self.base_model(best_num_components)


class SelectorDIC(ModelSelector):
    ''' select best model based on Discriminative Information Criterion

    Biem, Alain. "A model selection criterion for classification: Application to hmm topology optimization."
    Document Analysis and Recognition, 2003. Proceedings. Seventh International Conference on. IEEE, 2003.
    http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.58.6208&rep=rep1&type=pdf
    DIC = log(P(X(i)) - 1/(M-1)SUM(log(P(X(all but i))
    '''

    def select(self):
        warnings.filterwarnings("ignore", category=DeprecationWarning)

        log = {}
        sum_log = 0
        for n in range(self.min_n_components, self.max_n_components+1):
            try:
                model = self.base_model(n)
                logL = model.score(self.X, self.lengths)
                log[n] = logL
                sum_log += logL
            except:
                pass

        dic = 0
        M = len(log)
        best_num_components = self.n_constant
        score = -math.inf
        if M > 1:
            for n in log:
                dic = log[n] - 1/(M-1)*(sum_log-log[n])
                if dic > score:
                    best_num_components = n
                    score = dic
        if M == 1:
            best_num_components = log.items()

        return self.base_model(best_num_components)


class SelectorCV(ModelSelector):
    ''' select best model based on average log Likelihood of cross-validation folds

    '''

    def select(self):
        warnings.filterwarnings("ignore", category=DeprecationWarning)

        cv = {}
        split_method = KFold()
        for n in range(self.min_n_components, self.max_n_components+1):
            try:
                score = []
                if len(self.sequences) > 2:
                    for cv_train_idx, cv_test_idx in split_method.split(self.sequences):
                        self.X, self.lengths = combine_sequences(cv_train_idx, self.sequences)
                        X, lengths = combine_sequences(cv_test_idx, self.sequences)
                        model = self.base_model(n)
                        score.append(model.score(X, lengths))
                else:
                    model = self.base_model(n)
                    score.append(model.score(self.X, self.lengths))
                cv[n] = np.mean(score)
            except:
                pass

        best_num_components = self.n_constant
        score = -math.inf
        for n in cv:
            if cv[n] > score:
                best_num_components = n
                score = cv[n]

        return self.base_model(best_num_components)
