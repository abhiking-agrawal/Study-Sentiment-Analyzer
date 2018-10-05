import nltk

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem.snowball import SnowballStemmer

stemmer = SnowballStemmer("english")

positiveWords = []
negativeWords = []
neutralWords = []
positiveWordsFileName = "./rt-polaritydata/pos.txt"
negativeWordsFileName = "./rt-polaritydata/neg.txt"
neutralWordsFileName = "./rt-polaritydata/neu.txt"

posF = open(positiveWordsFileName,"r")
negF = open(negativeWordsFileName,'r') 
# neuF = open(neutralWordsFileName,'r') 
for word in posF.readlines():
    positiveWords.append(word.rstrip('\n'))
for word in negF.readlines():
    negativeWords.append(word.rstrip('\n'))
# for word in neuF.readlines():
#     neutralWords.append(word.rstrip('\n'))

def getSentiment(obj):
    if obj["neg"] != 0:
        return "Negative"
        # if obj["neg"] >= obj["pos"]:
        #     return "Negative"
        # else:
        #     return "Positive"
    elif obj["pos"] != 0:
        return "Positive"
        # if obj["pos"] >= obj["neu"]:
        #     return "Positive"
        # else:
        #     return "Neutral"
    else:
        return "Neutral"

def computeSentiments(words):
    res = {"pos" : 0, "neg":0,"neu" : 0}
    stemmers = []
    for word in words:
        word = stemmer.stem(word)
        stemmers.append(word)
        if word in positiveWords:
           # print(word + "==> pos")
            res["pos"] += 1
        elif word in negativeWords:
            #print(word + "==> neg")
            res["neg"] += 1
        else:
            #print(word + "==> neu")
            res["neu"] += 1
    print("Root words ", stemmers)
    return res
stop_words = set(stopwords.words('english'))

# print(computeSentiments(filtered_sentence))

#print(max(res, key=res.get))

# print(filtered_sentence)
exit = True
while exit:
    sentence = input("Enter a sentence.\n")
    sentence = sentence.lower()
    word_tokens = word_tokenize(sentence)
    print("\nTokenized Output : " , word_tokens)
    filtered_sentence = [w for w in word_tokens if not w in stop_words]
    print("Stop words Removed : " , filtered_sentence)
    res = computeSentiments(filtered_sentence)
    print("Categorized Frequence : " , res)
    print("Classifier Output ==> " +getSentiment(res))

    flag = input("\nDo you wana exit? 0 - exit  1- continue\n")
    if flag == "0":
        exit = False


posF.close()
negF.close()
# neuF.close()