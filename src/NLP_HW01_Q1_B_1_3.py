# ##########################################################################################
# module        NLP_HW01_Q1_B_1_3
# ##########################################################################################
# path          ...\NLP_HW01\src\NLP_HW01_Q1_B_1_3.py
# Purpose       Execution
# description   encapsulate question 1 bullet 1.3 executable code
# ##########################################################################################
import NLP_HW01_Q1_language_model   as LM
import matplotlib.pyplot as plt

# # test perplexity for orders [maxOrder]:
# lmList = LM.trainAllOrder(trainPath, maxOrder)
# for i in range(maxOrder):
#     lm = lmList[i]
#     dictITemList = [(k,v) for k,v in lm.items()]
#     context, wordList = dictITemList[0]
#     print("location = %d, context = %s" % (i, context) )
#
# orderList = range(maxOrder)
# for order in orderList:
#     perp = LM.perplexity(testText, order+1, lmList)
#     print("the perplexity for %d gram is: %s" %(order+1, str(perp)))

def plotPerplexity(xValues, yValues):
    plt.plot(xValues, yValues)
    plt.show()

def testPerplexity(trainPath, testPath, maxOrder):
    # train the model
    lmList = LM.trainAllOrder(trainPath, maxOrder)

    # get the test text
    testFile = open(testPath)
    testText = testFile.read()

    # test perplexity
    orderList = range(maxOrder)
    prepList = []
    for order in orderList:
        perp = LM.perplexity(testText, order + 1, lmList)
        prepList.append(perp)
        #print("the perplexity for %d gram is: %s" % (order + 1, str(perp)))
    #print()

    prepList.pop(0)
    orderList = [(i+1) for i in range(maxOrder)]
    orderList.pop(0)
    plotPerplexity(orderList, prepList)

# # train/ test files paths and parameters
# trainPath       = "C:\\Users\\moshe\\PycharmProjects\\NLP_HW01\\data_text_in\\ptb.train.txt"
# testPath        = "C:\\Users\\moshe\\PycharmProjects\\NLP_HW01\\data_text_in\\ptb.test.txt"
# maxOrder = 4
# 
# # main code
# testPerplexity(trainPath, testPath, maxOrder)