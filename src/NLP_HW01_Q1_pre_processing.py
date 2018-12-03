# ##########################################################################################
# module        NLP_HW01_Q1_pre_processing
# ##########################################################################################
# path          ...\NLP_HW01\src\NLP_HW01_Q1_pre_processing.py
# Purpose       pre-process
# description   encapsulate pre process code:
#               HTML pre-process
#               ptb-like pre-process
# ##########################################################################################
from urllib import request
from nltk import word_tokenize, sent_tokenize
import re
import collections
from bs4 import BeautifulSoup

# ##########################################################################################
# HTML pre-process
# ##########################################################################################
def getTextFromUrl(targetUrl="http://www.gutenberg.org/files/2554/2554-h/2554-h.htm", verbose = True):
    response = request.urlopen(targetUrl)
    rawText = response.read().decode('utf8')
    if verbose: print("getTextFromUrl: length = %8d charachters; type: = %s; tagret URL: %s"
                        %(len(rawText) ,str(type(rawText)), targetUrl))
    return rawText

def wordTokenize(rawText):
    return word_tokenize(rawText)

def replaceNums(token, replaceWith = "N"):
    if re.match("^[0-9]+$", token):
        return replaceWith
    else:
        return token

def erasePunctuation(tokenList):
    newList = []
    for token in tokenList:
        if not(re.match("^\W+$", token)):
            newList.append(token)
    return newList

def getMostCommonTokenHist(strList, n):
    tokenCounter = collections.Counter(strList)
    return tokenCounter.most_common(n)

def replaceUncommonToken(commonTokenList, token, replaceStr):
    if token in commonTokenList:
        return token
    else:
        return replaceStr

def preProcessText(rawText, top=10000, replaceStr = "<unk>"):
    # remove HTML related code
    rawText = BeautifulSoup(rawText, "html.parser").get_text()

    ## stage 1 - analyzing 10K most frequent words
    # generate linked list of word-tokens
    tokenList = wordTokenize(rawText)
    # upperCase => lowerCase
    tokenList = [token.lower() for token in tokenList]
    # replace numbers to "N"
    tokenList = [replaceNums(token, "N") for token in tokenList]
    # erase punctuation
    tokenList = erasePunctuation(tokenList)

    # generate most common list
    commonTokenHist = getMostCommonTokenHist(tokenList, top)
    commonTokenList = [token for (token, count) in commonTokenHist]

    ## stage 2 - edit per sentence
    # sentence tokenize
    sentenceList = sent_tokenize(rawText)
    # generate an edited output list
    editedSentenceList = []
    for sentence in sentenceList:
        sentenceTokens = wordTokenize(sentence)
        # upperCase => lowerCase
        sentenceTokens = [token.lower() for token in sentenceTokens]
        # replace numbers with a char
        sentenceTokens = [replaceNums(token) for token in sentenceTokens]
        # erase punctuation
        sentenceTokens = erasePunctuation(sentenceTokens)
        # labeling '<unk>' for low frequency tokens
        sentenceTokens = [replaceUncommonToken(commonTokenList, token, replaceStr) for token in sentenceTokens]
        # concatenation of all tokens, with space between
        editedSentence = ' '.join(map(str, sentenceTokens))
        # add the edited sentence to output list
        editedSentenceList.append(editedSentence + '\n')
    #
    editedText = ''.join(map(str, editedSentenceList))
    editedText = editedText.strip()
    return editedText

def padBySentences(rawText, padBy, order):
    # split to sentences
    sentenceList = rawText.split('\n')
    pad = (padBy + " ") * (order - 1)
    paddedText = ""
    for sentence in sentenceList:
        paddedSentence = pad+sentence
        paddedText = paddedText+" "+paddedSentence
    paddedText = paddedText.strip()
    return paddedText

def printLstSentences(inText, k, textName, verbose = False):
    # assume input is in format of PTB i.e. has line feed delimiter between sentences
    if verbose: print("Last %2d sentences from %s" %(k, textName))
    sentenceList = inText.split('\n')
    if k<len(sentenceList) : sentenceList = sentenceList[len(sentenceList)-k:len(sentenceList)]
    cnt = 0
    for sentence in sentenceList:
        print("%2d: '%s'" %(cnt, sentence))
        cnt += 1

# #####################################################################################
# ptb-like pre-process
# #####################################################################################

#def replaceUncommonTokensInList(tokenList, top, replaceStr):
#    #  not used TBD: update to receive text and return replaced text
#    commonTokenHist = getMostCommonTokenHist(tokenList, top)
#    commonTokenList = [token for (token, count) in commonTokenHist]
#    return [replaceUncommonToken(commonTokenList, token, replaceStr) for token in tokenList]

def replaceUncommonTokens(textIn, top, replaceStr):
    # recives textIn consisting tokens separated by space
    # returns the text with uncommon tokens replaced by content of replaceStr
    # uncommon is calculated with respect to top first frequent tokens in textIn
    tokenList = wordTokenize(textIn)
    commonTokenHist = getMostCommonTokenHist(tokenList, top)
    commonTokenList = [token for (token, count) in commonTokenHist]
    tokenListReplaced = [replaceUncommonToken(commonTokenList, token, replaceStr) for token in tokenList]
    textOut = " ".join(map(str, tokenListReplaced))
    return textOut

def replaceLF(inStr, repStr):
    # recives string inStr
    # returns the edited inStr: every character x20x0A (space + line-feed) replaced by 'repStr'
    outStr = inStr.replace('\u0020\u000a', repStr)
    return outStr

def replaceUnk(inStr, repStr):
    outStr = inStr.replace('<unk>', repStr)
    return outStr

def preProcessPtb(inText, order):
    # replace line feed charachter with padding of length order+1
    padBy = "S"
    pad = (" " + padBy) * (order - 1)
    paddedData = replaceLF(inText, pad)

    # replace <unk> to UNK
    preprocessData = replaceUnk(paddedData, 'UNK')

    return preprocessData