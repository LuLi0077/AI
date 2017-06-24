import numpy as np
import keras
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM


# Transform the input series and window-size into a set of input/output pairs
def window_transform_series(series, window_size):
    # containers for input/output pairs
    X = []
    y = []
    
    # loop through and append input/output to X/y
    for i in range(len(series)-window_size):
        X.append(series[i:i+window_size])
        y.append(series[i+window_size])
        
    # reshape each 
    X = np.asarray(X)
    X.shape = (np.shape(X)[0:2])
    y = np.asarray(y)
    y.shape = (len(y),1)   
    return X,y


# Build an RNN to perform regression on our time series input/output data
def build_part1_RNN(step_size, window_size):
    # model specifications
    model = Sequential()
    model.add(LSTM(5, input_shape=(window_size, 1)))
    model.add(Dense(1))

    # use keras documentation recommended optimizer initialization
    optimizer = keras.optimizers.RMSprop(lr=0.001, rho=0.9, epsilon=1e-08, decay=0.0)

    # compile the model
    model.compile(loss='mean_squared_error', optimizer=optimizer)


# Remove any non-english ones
chars = ['$','%','&','(',')','*','-','/','0','1','2','3','4','5','6','7','8','9','@','à','â','è','é']

def clean_text(text):
    for c in chars:
        text = text.replace(c, ' ')
        
    # shorten any extra dead space created above
    text = text.replace('  ', ' ')


# Transforms the input text and window-size into a set of input/output pairs
def window_transform_text(text, window_size, step_size):
    # containers for input/output pairs
    inputs = []
    outputs = []
    j = 0
    # loop through and append input/output
    size = np.floor((len(text)-window_size)/step_size)
    for i in range(int(size)):       
        inputs.append(text[j:j+window_size])
        outputs.append(text[j+window_size])
        j += step_size   
    return inputs, outputs
