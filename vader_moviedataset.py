import nltk
from nltk.sentiment import vader
sia = vader.SentimentIntensityAnalyzer()

#importing the data
positiveFileName = "./rt-polaritydata/rt-polarity.pos"
with open(positiveFileName, 'r') as f :
    positiveReviews = f.readlines()
negativeFileName = "./rt-polaritydata/rt-polarity.neg"
with open(negativeFileName, 'r') as f :
    negativeReviews = f.readlines()

#function to return the vander sentiment
def vaderSentiment(review):
    return sia.polarity_scores(review)['compound']

#function to collect sentiments for all positive/negative reviews
def getReviewSentiments(sentimentCalculator): 
  negReviewResult = [sentimentCalculator(oneNegativeReview) for oneNegativeReview in negativeReviews]
  posReviewResult = [sentimentCalculator(onePositiveReview) for onePositiveReview in positiveReviews]
  return {'results-on-positive':posReviewResult, 'results-on-negative':negReviewResult}

#To generate the accuracy stats
def runDiagnostics(reviewResult):
  positiveReviewsResult = reviewResult['results-on-positive']
  negativeReviewsResult = reviewResult['results-on-negative']
  pctTruePositive = float(sum(x > 0 for x in positiveReviewsResult))/len(positiveReviewsResult)
  pctTrueNegative = float(sum(x < 0 for x in negativeReviewsResult))/len(negativeReviewsResult)
  totalAccurate = float(sum(x > 0 for x in positiveReviewsResult)) + float(sum(x < 0 for x in negativeReviewsResult))
  total = len(positiveReviewsResult) + len(negativeReviewsResult)
  print("Accuracy on positive reviews = " +"%.2f" % (pctTruePositive*100) + "%")
  print("Accurance on negative reviews = " +"%.2f" % (pctTrueNegative*100) + "%")
  print("Overall accuracy = " + "%.2f" % (totalAccurate*100/total) + "%")

runDiagnostics(getReviewSentiments(vaderSentiment))
