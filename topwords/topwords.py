# 1. get all common words inenglish ranked by frequency
# 2. get srt movie script files.
# 3. get top 100 words in movie by inc frequency
import re
import sys
import operator
import nltk
from nltk.corpus import wordnet
from nltk.tokenize import word_tokenize
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.tag import StanfordPOSTagger


CORPUS_PATH = 'common_words.txt'

class WordNetHelper(object):

    lem = WordNetLemmatizer()
    jar = './pos_tagger/stanford-postagger-3.9.1.jar'
    model = './pos_tagger/models/english-bidirectional-distsim.tagger'

    pos_tagger = StanfordPOSTagger(model, jar, encoding='utf8')

    @staticmethod
    def wordnet_pos_code(tag):
        if tag.startswith('NN'):
            return wordnet.NOUN
        elif tag.startswith('VB'):
            return wordnet.VERB
        elif tag.startswith('JJ'):
            return wordnet.ADJ
        elif tag.startswith('RB'):
            return wordnet.ADV
        else:
            print('tag ={}. no match'.format(tag))
            return None

    @classmethod
    def stanford_tagger(cls, tokens):
        print('tagging {}'.format(tokens))
        tagged = cls.pos_tagger.tag(tokens)
        print('tagged {}'.format(tagged))
        return tagged

    def lemmatize(self, tokens):
        """lemmatize to its own original form (past tense -> present, etc.)"""
        # wd_tags = nltk.pos_tag([x.lower() for x in word_tokenize(line)])  # word -> tag
        wd_tags = self.stanford_tagger(tokens)  # word -> tag
        lemmatized = []
        for wd, tag in wd_tags:
            tag = self.wordnet_pos_code(tag)
            if tag:
                lemmatized.append(self.lem.lemmatize(wd, tag))
            else:
                lemmatized.append(self.lem.lemmatize(wd))
        return lemmatized


class TopWords(object):
    """find the most rare words in a source"""

    def __init__(self, path, cutoff=100, corpus_path=CORPUS_PATH):
        """provide the path of a source file, and it'll get the top words for you!"""
        self.wn = WordNetHelper()
        self.path = path
        self.corpus_path = corpus_path
        self.cutoff = cutoff
        self.all_words = self.load_corpus()
        self.target_words = self.load_target_words()
        self.top_words = self.get_top_words()


    def load_corpus(self):
        """load a file where each line contains a word and a number indicates frquence
           return a list of words with increasing frequency
        """
        f = open(self.corpus_path, 'r')
        d = {}
        for l in f:
            parsed = re.findall(r'[\w]+', l)
            d[parsed[0].lower()] = int(parsed[1])

        # return all words in inc frequency
        return [x[0] for x in sorted(d.items(), key=operator.itemgetter(1))]

    def load_target_words(self):
        """given a file path, lemmatize all words and return in a set """

        f = open(self.path, 'r', errors='ignore', encoding='utf-8')
        words = set()
        for l in f:
            tokens = [x.lower() for x in re.findall(r'[a-zA-Z]+', l)]
            if tokens:
                lematized_tokens = self.wn.lemmatize(tokens)
                words.update(lematized_tokens)
        # 1. just try to put all the words in a bag and lemmatize one by one?

        return words

    def get_top_words(self):
        """return the top cutoff words appear in the movie"""
        words = []
        for w in self.all_words:
            if len(words) == self.cutoff:
                break

            if w in self.target_words:
                words.append(w)

        return words


if __name__ == '__main__':
    args = sys.argv[1:]
    kwargs = {'path': args[0]}
    if len(args) >= 2:
        kwargs['cutoff'] = int(args[1])
    if len(args) >= 3:
        kwargs['corpus_path'] = args[2]

    tw = TopWords(**kwargs)
    print(tw.top_words)

