# ##########################################################################################
# module        NLP_HW01_Q1_B_1_1_1
# ##########################################################################################
# path          C:\Users\moshe\PycharmProjects\NLP_HW01\NLP_HW01_Q1_B_1_1_1.py
# Purpose       Execution
# description   encapsulate pre process execution code
# ##########################################################################################
import NLP_HW01_Q1_pre_processing as preproc
import os

def preprocessSingleFile(targetUrl, outFilePath, top=10000, verbose = True):
    # get a file
    rawText = preproc.getTextFromUrl(targetUrl, verbose)

    # pre process text
    outText = preproc.preProcessText(rawText, top, "UNK")

    numOfSnetencesToPrint = 3
    preproc.printLstSentences(outText, numOfSnetencesToPrint, outFilePath, verbose)

    # stage 3 - generating output file
    if verbose:
        print("writting preprocessed file to %s" %outFilePath)

    outFile = open(outFilePath, "w")
    outFile.write(outText)
    outFile.close()
    return

def ptb_preprocess(filenames, top=10000):
    # assume output_text_files exist in prev sub directory
    fileCnt = 1
    for caption, targetURL in filenames:
        scriptPath = os.path.dirname(os.path.realpath('__file__'))
        relFilePath = "\\output_text_files\\" + caption + ".txt"
        scriptPathPrev = os.path.split(scriptPath)[0]
        # scriptPathPrev = scriptPath
        outFilePath = scriptPathPrev + relFilePath

        strPrint = "Fetching and preprocessing the text: '" + caption + "'"
        print(strPrint)
        underline = "="*len(strPrint)
        print(underline)
        preprocessSingleFile(targetURL, outFilePath, top, True)
        print()
        fileCnt += 1



def padSingleFile(fName, padBy = "S", order = 2):
    # get a file
    inputFile = open(fName)

    # pad by sentence
    fileText = inputFile.read()
    paddedFileText = preproc.padBySentences(fileText, padBy, order)

    # stage 3 - generating ouput file
    fileOutName = fName + ".padded.txt"
    outFile = open(fileOutName, "w")
    outFile.write(paddedFileText)
    outFile.close()
    return

# =========
# main code
# =========

# hardcoded URL list
# topFreqWords = 10_000
# targetUrlList = [("the_crime_and_the_punishment", "http://www.gutenberg.org/files/2554/2554-h/2554-h.htm"),
#                  ("ruth_scroll", "http://www.gutenberg.org/cache/epub/8008/pg8008.html"),
#                  ("shakespeare_work", "https://cs.stanford.edu/people/karpathy/char-rnn/shakespeare_input.txt")]

# targetUrlList = [("ruth_scroll", "http://www.gutenberg.org/cache/epub/8008/pg8008.html")]
# foreach URL generate ptb-like .text file
# ptb_preprocess(targetUrlList, topFreqWords)

# pad between sentences the ptb-like files
# padSingleFile("C:\\Users\\moshe\\PycharmProjects\\NLP_HW01\\pg8008.html.txt", "S", 3)
# padSingleFile("C:\\Users\\moshe\\PycharmProjects\\NLP_HW01\\2554-h.htm.txt",  "S", 3)
# padSingleFile("C:\\Users\\moshe\\PycharmProjects\\NLP_HW01\\2554-h.htm.txt",  "S", 3)

# http://www.gutenberg.org/files/2554/2554-h/2554-h.htm // crime and punishment
# http://www.gutenberg.org/cache/epub/8008/pg8008.html  // ruth scroll
# =>
# C:\Users\moshe\PycharmProjects\NLP_HW01\pg8008.html.txt
# C:\\Users\\moshe\\PycharmProjects\\NLP_HW01\\pg8008.html.txt