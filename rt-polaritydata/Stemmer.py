from nltk.stem.snowball import SnowballStemmer

stemmer = SnowballStemmer("english")

print(stemmer.stem("great"))
print(stemmer.stem("greater"))
print(stemmer.stem("greatful"))
print(stemmer.stem("greatness"))
print(stemmer.stem("greatest"))
