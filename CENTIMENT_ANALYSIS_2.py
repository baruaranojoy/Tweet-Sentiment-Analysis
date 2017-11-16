import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.corpus import state_union
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet
import random
from nltk.corpus import movie_reviews
from nltk.corpus import sentiwordnet as swn

## test data
text = "RT @UJ1701: #Governance \ud83d\ude37\ud83d\ude37\n\nRs. 2000 notes printed when #Rajan was RBI Governor but bear Patel's signature\u2026 "

## tokenization
word = word_tokenize(text)

## stop word filtration
stop_words = set(stopwords.words("english"))
filt_sent = []
for w in word:
    if w not in stop_words:
        filt_sent.append(w)

print filt_sent


## lemitizing words
lemmatizer = WordNetLemmatizer()
lemitize_sent = []
count = 0
for w in filt_sent:
    m = str(filt_sent[count])
    k = lemmatizer.lemmatize(m)
    lemitize_sent.append(k)
    count = count + 1
print '\n'
print lemitize_sent


## part od speech taging
alpha = [lemitize_sent]
for w in alpha:
    tagged = nltk.pos_tag(lemitize_sent)

print '\n'
print tagged
print '\n'

#### lemma creation
count = 0
lem = []
for w in lemitize_sent:
    sasha = wordnet.synsets(lemitize_sent[count])
    if len(sasha)>=1:
        sasha = sasha[0]
        lem.append(sasha)
    count = count + 1
    
print '\n'
print lem
print '\n'



##  chota
def procress(dat):
    dat = str(dat)
    size = len(dat)
    kk = ""
    ret = ""
    for k in range (size-10):
        #ret.append(dat[k+8])
        kk = dat[k+8]
        ret = ret + kk
    ret = str(ret)
    #print ret
    return ret

    
count = 0
total_neg = 0.0
total_pos = 0.0
for w in lem:
    data = lem[count]
    count = count + 1
    da = procress(data)
    #print da
    breakdown = swn.senti_synset(da)
    #print '\n'
    print breakdown
    total_pos = total_pos + breakdown.pos_score()
    total_neg = total_neg + breakdown.neg_score() 


print '\n'
print "Posetive score : "
print total_pos
print "Negative score : "
print total_neg

## printing the lemma or synonims for a word
#sasha = wordnet.synsets("cool")
#sasha = sasha[0]
#sashaa = sasha.lemmas()
#print '\n'
#print sasha






#breakdown = swn.senti_synset('inch.n.01')
#print '\n'
#print breakdown






























