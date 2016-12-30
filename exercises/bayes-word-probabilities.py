import re
import operator
from collections import Counter

def FirstExercise():
    sentence = "So if you could just go ahead and pack up your stuff and move it down there, that would be terrific, OK?"

    sentence = re.sub('[^A-Za-z0-9 ]+', '', sentence).lower()

    words = sentence.split(' ')
    word_counter = Counter(words)

    you_change = float(word_counter['you']) / len(words)
    if_change = float(word_counter['if']) / len(words)

    print "Original sentence, no special: {0}".format(sentence)
    print "Word count: {0}".format(len(words))
    print "'you' change: {0}".format(you_change)
    print "'if' occurrences: {0}".format(if_change)

#FirstExercise()

def NextWordProbability(sample, word):
    sentence = re.sub('[^A-Za-z0-9 ]+', '', sample).lower()

    words = sentence.split(' ')

    occurrences = {}

    for i, w in enumerate(words):
        if i == len(words):
            break

        if w == word:
            next_word = words[i + 1]
            if next_word in occurrences:
                occurrences[next_word] = occurrences[next_word] + 1
            else:
                occurrences[next_word] = 1

    word_counter = Counter(words)

    return occurrences

sample_memo = '''
Milt, we're gonna need to go ahead and move you downstairs into storage B. We have some new people coming in, and we need all the space we can get. So if you could just go ahead and pack up your stuff and move it down there, that would be terrific, OK?
Oh, and remember: next Friday... is Hawaiian shirt day. So, you know, if you want to, go ahead and wear a Hawaiian shirt and jeans.
Oh, oh, and I almost forgot. Ahh, I'm also gonna need you to go ahead and come in on Sunday, too...
Hello Peter, whats happening? Ummm, I'm gonna need you to go ahead and come in tomorrow. So if you could be here around 9 that would be great, mmmk... oh oh! and I almost forgot ahh, I'm also gonna need you to go ahead and come in on Sunday too, kay. We ahh lost some people this week and ah, we sorta need to play catch up.
'''

#occurrences = NextWordProbability(sample_memo, "you")

#print "Occurrences: {0}".format(occurrences)

corrupted_memo = '''
Yeah, I'm gonna --- you to go ahead --- --- complain about this. Oh, and if you could --- --- and sit at the kids' table, that'd be ---
'''

data_list = sample_memo.strip().split()

words_to_guess = ["ahead","could"]

def LaterWords(sample,word,distance):
    '''@param sample: a sample of text to draw from
    @param word: a word occuring before a corrupted sequence
    @param distance: how many words later to estimate (i.e. 1 for the next word, 2 for the word after that)
    @returns: a single word which is the most likely possibility
    '''

    sentence = re.sub('[\.,]+', '', sample)
    #sentence = sample
    #word = word.lower()

    words = sentence.split()

    occurrences = {}

    for i, w in enumerate(words):
        if i == len(words) + 1 - distance:
            break

        if w == word:
            later_word = words[i + distance]
            if later_word in occurrences:
                occurrences[later_word] = occurrences[later_word] + 1
            else:
                occurrences[later_word] = 1

    word_counter = Counter(words)

    if len(occurrences) == 0:
        return ""

    ranked = sorted(occurrences.items(), key=operator.itemgetter(1), reverse=True)
    top = ranked[0][1]
    result = []

    for w, i in ranked:
        if i == top:
            result.append(w)
        else:
            break

    return ",".join(result)

print LaterWords(sample_memo, "terrific", 2)
