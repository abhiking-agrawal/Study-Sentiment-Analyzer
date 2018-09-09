import nltk

#Specify the file paths
positiveReviewsFileName = "./rt-polaritydata/rt-polarity.pos"
negativeReviewsFileName = "./rt-polaritydata/rt-polarity.neg"

#Read the files and collect the data
with open(positiveReviewsFileName,'r') as f:
    positiveReviews = f.readlines()
with open(negativeReviewsFileName,'r') as f:
    negativeReviews = f.readlines()

#Split data for training and testing
testTrainingSplitIndex = 2500

testNegativeReviews = negativeReviews[testTrainingSplitIndex+1:]
testPositiveReviews = positiveReviews[testTrainingSplitIndex+1:]

trainingNegativeReviews = negativeReviews[:testTrainingSplitIndex]
trainingPositiveReviews = positiveReviews[:testTrainingSplitIndex]


#Compute sentiment for test data and label the data 1/-1
def getTestReviewSentiments(naiveBayesSentimentCalculator):
  testNegResults = [naiveBayesSentimentCalculator(review) for review in testNegativeReviews]
  testPosResults = [naiveBayesSentimentCalculator(review) for review in testPositiveReviews]
  labelToNum = {'positive':1,'negative':-1}
  numericNegResults = [labelToNum[x] for x in testNegResults]
  numericPosResults = [labelToNum[x] for x in testPosResults]
  return {'results-on-positive':numericPosResults, 'results-on-negative':numericNegResults}


#Generate the accuracy statistics
def runDiagnostics(reviewResult):
  positiveReviewsResult = reviewResult['results-on-positive']
  negativeReviewsResult = reviewResult['results-on-negative']
  numTruePositive = sum(x > 0 for x in positiveReviewsResult)
  numTrueNegative = sum(x < 0 for x in negativeReviewsResult)
  pctTruePositive = float(numTruePositive)/len(positiveReviewsResult)
  pctTrueNegative = float(numTrueNegative)/len(negativeReviewsResult)  
  totalAccurate = numTruePositive + numTrueNegative
  total = len(positiveReviewsResult) + len(negativeReviewsResult)
  print("Accuracy on positive reviews = " +"%.2f" % (pctTruePositive*100) + "%")
  print("Accurance on negative reviews = " +"%.2f" % (pctTrueNegative*100) + "%")
  print("Overall accuracy = " + "%.2f" % (totalAccurate*100/total) + "%")


#GAther the list of all words available in corpus
def getVocabulary():
  positiveWordList = [word for line in trainingPositiveReviews for word in line.split()]
  negativeWordList = [word for line in trainingNegativeReviews for word in line.split()]
  allWordList = [item for sublist in [positiveWordList,negativeWordList] for item in sublist]
  allWordSet = list(set(allWordList))
  vocabulary = allWordSet
  return vocabulary

#Generate train data with label
def getTrainingData():
  negTaggedTrainingReviewList = [{'review':oneReview.split(),'label':'negative'} for oneReview in trainingNegativeReviews] 
  posTaggedTrainingReviewList = [{'review':oneReview.split(),'label':'positive'} for oneReview in trainingPositiveReviews] 
  fullTaggedTrainingData = [item for sublist in [negTaggedTrainingReviewList,posTaggedTrainingReviewList] for item in sublist]
  trainingData = [(review['review'],review['label']) for review in fullTaggedTrainingData]
  return trainingData

#Extract the feature tuple
def extract_features(review):
  review_words=set(review)
  features={}
  for word in vocabulary:
      features[word]=(word in review_words)
  return features 

#Train the classifier with Naive Bayes algorithm
def getTrainedNaiveBayesClassifier(extract_features, trainingData):
  trainingFeatures=nltk.classify.apply_features(extract_features, trainingData)
  trainedNBClassifier=nltk.NaiveBayesClassifier.train(trainingFeatures)
  return trainedNBClassifier

vocabulary = getVocabulary()
trainingData = getTrainingData()
trainedNBClassifier = getTrainedNaiveBayesClassifier(extract_features,trainingData)


#
def naiveBayesSentimentCalculator(review):
  problemInstance = review.split()
  problemFeatures = extract_features(problemInstance)
  return trainedNBClassifier.classify(problemFeatures)

naiveBayesSentimentCalculator("What an awesome movie")
naiveBayesSentimentCalculator("What a terrible movie")
print("Getting results : ")
runDiagnostics(getTestReviewSentiments(naiveBayesSentimentCalculator))



