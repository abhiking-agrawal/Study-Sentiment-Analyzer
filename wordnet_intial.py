from nltk.corpus import sentiwordnet as swn
list(swn.senti_synsets('slow'))

listW = list(swn.senti_synsets('slow'))
listW[0]

listW[0].pos_score()
listW[0].neg_score()