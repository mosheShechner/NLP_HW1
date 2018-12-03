
import os
import nltk
from nltk import ngrams
import statistics
import matplotlib.pyplot as plt

def printNumberOfWords(tokens):
    numOfWords = len(tokens)
    print ("Number of words: " + str(numOfWords))
    return numOfWords

def printNumberOfCharacters(tokens):
    i=0
    sum1 = 0
    while i < len(tokens):
        sum1 = sum1 + len(tokens[i])
        i = i+1
    print ("The total number of characters " + str(sum1))

def printNumberOfDistWords(tokens):
    numOfDistWords = len(set(tokens))
    print("The total number of distinct words " + str(numOfDistWords))
    return numOfDistWords


def printNMostCommon(n,text):
    fdist = nltk.FreqDist(text)
    sum = 0
    for pair in fdist.most_common(n):
        sum = sum + pair[1]
    print("Number of tokens corresponding to the top-" + str(n) + " most frequent words in the vocabulary " + str(sum))


def printTokenTypeRatio(numOfWords,numOfDist):
    ratio = numOfWords/numOfDist
    print("The token/type ratio " + str(ratio))

def printMeanAndStdev(tokens):
    lengths = [len(token) for token in tokens]
    print("The average number and standard deviation of characters per token " + str(statistics.mean(lengths)) +
          ", " + str(statistics.stdev(lengths)))


def printNumberOfDistNgrams(n,text):
    grams = ngrams(text, n)
    lst = [x for x in grams]
    count = len(set(lst))
    print("Number of distinct n-grams (of words) that appear in the dataset for n=" + str(n) + ": " + str(count))

def printNumberOfDistCharNgrams(n,text):
    lst = [text[i:i+n] for i in range(len(text)-n)]
    count = len(set(lst))
    print("Number of distinct n-grams (of chars) that appear in the dataset for n=" + str(n) + ": " + str(count))


def printStatistics(fileName):
    scriptPath = os.path.dirname(os.path.realpath('__file__'))
    relFilePath = "\\input_text_files\\" + fileName
    scriptPathPrev = os.path.split(scriptPath)[0]
    inputFilePath = scriptPathPrev + relFilePath


    f = open(inputFilePath)
    r_txt = f.read()
    tokens_list = nltk.word_tokenize(r_txt)
    txt = nltk.Text(tokens_list)

    nOfWords = printNumberOfWords(tokens_list)
    printNumberOfCharacters(tokens_list)
    nOfDist = printNumberOfDistWords(tokens_list)
    printNMostCommon(1000, txt)
    printTokenTypeRatio(nOfWords, nOfDist)
    printMeanAndStdev(tokens_list)
    printNumberOfDistNgrams(2, txt)
    printNumberOfDistNgrams(3, txt)
    printNumberOfDistNgrams(4, txt)
    printNumberOfDistCharNgrams(1, r_txt)
    printNumberOfDistCharNgrams(2, r_txt)
    printNumberOfDistCharNgrams(3, r_txt)
    printNumberOfDistCharNgrams(4, r_txt)
    printNumberOfDistCharNgrams(5, r_txt)
    printNumberOfDistCharNgrams(6, r_txt)


def plotLoglog(fileName):
    scriptPath = os.path.dirname(os.path.realpath('__file__'))
    relFilePath = "\\input_text_files\\" + fileName
    scriptPathPrev = os.path.split(scriptPath)[0]
    inputFilePath = scriptPathPrev + relFilePath


    f = open(inputFilePath)
    r_txt = f.read()
    tokens_list = nltk.word_tokenize(r_txt)
    txt = nltk.Text(tokens_list)
    fdist = nltk.FreqDist(txt)
    plt.loglog([val for word, val in fdist.most_common(4000)])
    plt.show()







