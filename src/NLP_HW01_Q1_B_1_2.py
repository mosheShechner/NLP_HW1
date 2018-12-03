# ##########################################################################################
# module        NLP_HW01_Q1_B_1_2
# ##########################################################################################
# path          ...\repository\src\NLP_HW01_Q1_B_1_2.py
# Purpose       Execution
# description   encapsulate question 1 bullet 1.2 executable code
# ##########################################################################################
import NLP_HW01_Q1_language_model as LM
import operator

# train/ test files paths
pathTrain = "C:\\Users\\moshe\\PycharmProjects\\NLP_HW01\\data_text_in\\ptb.train.txt"
pathTest = "C:\\Users\\moshe\\PycharmProjects\\NLP_HW01\\data_text_in\\ptb.test.txt"

order = 3
lm = LM.train_word_lm(pathTrain, order)


if (order == 1):
    highFreq = [(word, prob) for word, prob in lm[''] if prob > 0.0001]
    highFreqSorted = sorted(lm[''], key=operator.itemgetter(1), reverse=True)
    print(highFreq)
    print(highFreqSorted[0:10])
    print("conclusion: order 1 implemented as expected; distribution of uni-gram given null history")
elif (order == 2):
    print(lm['latest'][0:5])
    print(lm['i'][0:5])
    print(lm['S'][0:5])
    print(lm['UNK'][0:5])
    print(lm['N'][0:5])
    print(lm['appear'])
elif (order == 3):
    print(lm['latest,results'])
    print(lm['appear,in'])
else:
    print("TBD implement prints for higher order then 2")
