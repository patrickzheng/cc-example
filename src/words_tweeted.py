# example of program that calculates the total number of times each word has been tweeted.
import sys
def words_tweeted(inputFilename, outputFilename):
    wordDict = {}
    with open(inputFilename) as f:
        for line in f:
            for word in line.split( ):
                if word not in wordDict.keys():
                    wordDict[word] = 1
                else:
                    wordDict[word] = wordDict[word] + 1
    f = open(outputFilename,'w')
    for key in sorted(wordDict.keys()):
        f.write(key + ' ' + str(wordDict[key]) + '\n')
    f.close()
inputFilename = sys.argv[1]
outputFilename = sys.argv[2]
words_tweeted(inputFilename, outputFilename)