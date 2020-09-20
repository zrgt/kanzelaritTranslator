import string

import nltk
from nltk import word_tokenize
from nltk.probability import FreqDist
from nltk.corpus import stopwords


def rm_chars_from(text, chars):
    return "".join([char for char in text if char not in chars])


with open("mod_ukrf") as file:
    text = file.read()

text_len = len(text)

text = text.lower()
text = rm_chars_from(text, string.punctuation)
text = rm_chars_from(text, string.digits)


text_tokens = word_tokenize(text)
text = nltk.Text(text_tokens)

fdist = FreqDist(text)
print(fdist.most_common(20))

rus_stopwords = stopwords.words("russian")
text_tokens = [token.strip() for token in text_tokens if token not in rus_stopwords]
text = nltk.Text(text_tokens)


fdist = FreqDist(text)
print(fdist.most_common(20))
# fdist.plot(30, cumulative=False)

# with open("mod_ukrf", mode="w") as file:
#     file.write(text)

from nltk.collocations import *
bigram_measures = nltk.collocations.BigramAssocMeasures()
trigram_measures = nltk.collocations.TrigramAssocMeasures()

## Bigrams
bigrams = BigramCollocationFinder.from_words(text_tokens)
# only bigrams that appear 3+ times
bigrams.apply_freq_filter(3)

## Trigrams
trigrams = TrigramCollocationFinder.from_words(text_tokens)
# only trigrams that appear 3+ times
trigrams.apply_freq_filter(3)


print(bigrams.nbest(bigram_measures.likelihood_ratio, 50))
print(trigrams.nbest(trigram_measures.likelihood_ratio, 50))

with open("grams", mode="w") as file:
    file.writelines([str(i)+"\n" for i in fdist.most_common(100)])
    file.writelines(["\n" for i in range(10)])
    file.writelines([str(i) + "\n" for i in bigrams.nbest(bigram_measures.likelihood_ratio, 100)])
    file.writelines(["\n" for i in range(10)])
    file.writelines([str(i) + "\n" for i in trigrams.nbest(trigram_measures.likelihood_ratio, 100)])