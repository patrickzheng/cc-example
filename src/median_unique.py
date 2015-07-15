# example of program that calculates the median number of unique words per tweet.
import sys
def median_unique(inputFilename, outputFilename):
    countDict = {}
    outputFile = open(outputFilename,'w')
    with open(inputFilename) as inputFile:
        for line in inputFile:
            tweetWordCount = len(line.split( ))
            if tweetWordCount not in countDict.keys():
                countDict[tweetWordCount] = 1
            else:
                countDict[tweetWordCount] = countDict[tweetWordCount] + 1  
            medianPosition = float(sum(countDict.values()))/2
            medianValue1 = 0
            medianValue2 = 0
            for key in sorted(countDict.keys()):
                medianPosition = medianPosition - countDict[key];
                if medianPosition == 0: 
                    medianValue1 = key
                elif medianPosition < 0:
                    medianValue2 = key
                    if medianValue1 == 0:
                        medianValue1 = key
                    break
            outputFile.write(str(float(medianValue1 + medianValue2) / 2) + '\n')
    outputFile.close()
inputFilename = sys.argv[1]
outputFilename = sys.argv[2]
median_unique(inputFilename, outputFilename)