# ##########################################################################################
# module        NLP_HW01_Q1_language_model
# ##########################################################################################
# path          ...\repository\src\NLP_HW01_Q1_language_model.py
# Purpose       Language Model
# description   encapsulate language model code
# ##########################################################################################
import nltk
import math
from collections import *
import NLP_HW01_Q1_pre_processing as preproc


# implementation parameters
contextDelimiter = ","

def train_word_lm(fname, order=2):
    # assumption: receive a file with line delimiter line feed for sentences

    with open(fname) as f:
        data = f.read()

    # pre-process ptb-like text
    preprocessData = preproc.preProcessPtb(data, order)

    # split to list of tokens by space delimiter
    words = nltk.word_tokenize(preprocessData)

    # count instances of occurrences of order-th word conditioned on order-1 history
    lm = defaultdict(Counter)
    i = 0
    while i < len(words)-(order+1):
        history, word = contextDelimiter.join(words[i:i+(order-1)]), words[i+(order-1)]
        lm[history][word] += 1
        i = i+1

    # normalization
    def normalize(counter):
        # assume to receive a Counter object
        norm = float(sum(counter.values()))
        return [(word, count/norm) for word, count in counter.items()]
    normLm = {history: normalize(count) for history, count in lm.items()}
    return normLm

def trainAllOrder(fname, order):
    lmList = [train_word_lm(fname, currOrder+1) for currOrder in range(order)]
    return lmList

def removeTail(inStr, delimiter):
    splitStrList = inStr.split(delimiter)
    splitStrList = splitStrList[1:]
    outStr = delimiter.join(splitStrList)
    return outStr

def prob(token: str, context: str, lmList: [str], order: int) -> float:
    lm = lmList[order - 1]
    if order == 1:
        # base case for back-off
        lst = lm['']
        for word, wordProb in lst:
            if word == token:
                return wordProb
            else:
                # print("Warning: hardcoded smoothing was done, word %s not found" % word)
                return 0.0000001
    if context in lm:
        # order > 1
        lst = lm[context]
        for word, wordProb in lst:
            if word == token:
                # found conditional probability
                return wordProb
    # back-off
    return prob(token, removeTail(context,contextDelimiter), lmList[0:order-1], order-1)

def logprob(p):
    return math.log(p, 2)

def entropy(text, order, lmList):
    e = 0.0
    words_list = nltk.word_tokenize(text)

    for i in range(order - 1, len(words_list)):
        context = contextDelimiter.join(words_list[i - order + 1:i])
        token = words_list[i]
        probability = prob(token, context, lmList, order)
        e -= logprob(probability)
    return e / float(len(words_list) - (order - 1))

def perplexity(text, order, lmList):
    preprocessText = preproc.preProcessPtb(text, order)
    return pow(2.0, entropy(preprocessText, order, lmList))