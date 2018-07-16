import re
import sys
import operator
import nltk
from nltk.corpus import wordnet
from nltk.tokenize import word_tokenize
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.tag import StanfordPOSTagger
from nltk.corpus import stopwords


CORPUS_PATH = 'common_words.txt'

#@imporvement
# super simplified approach since i only care about verb, adj, adv, noun

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


    def lemmatize(self, token, pos_tag):
        """lemmatize to its own original form (past tense -> present, etc.)"""
        tag = self.wordnet_pos_code(pos_tag)
        if tag:
            return self.lem.lemmatize(token, tag)
        return self.lem.lemmatize(token)


class TopWords(object):
    """find the most rare words in a source"""

    def __init__(self, path, cutoff=100, corpus_path=CORPUS_PATH):
        """provide the path of a source file, and it'll get the top words for you!"""
        self.wn = WordNetHelper()
        self.path = path
        self.corpus_path = corpus_path
        self.cutoff = cutoff

        self.stop_words = set(stopwords.words('english'))

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
        # ignore words with ' for now, since the word frequency file doesn't contain such words

        tokens = set([x.lower() for x in re.findall(r'[a-zA-Z]+', f.read())])
        # remove stop words
        print ('before num tokens are', len(tokens), tokens)
        tokens = tokens - self.stop_words
        print ('after num tokens are', len(tokens), tokens)

        # tokens = [x.lower() for x in re.findall(r'[a-zA-Z]+', f.read())]

        # bs cuz not a sentence
        tagged = self.wn.stanford_tagger(list(tokens))

        # lemmatized = set([self.wn.lemmatize(wd, pos) for wd, pos in wd_pos.items()])
        lemmatized = set([self.wn.lemmatize(wd, pos) for wd, pos in tagged])

        return lemmatized

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

