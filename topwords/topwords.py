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

# @imporvement
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
            return None

    @classmethod
    def stanford_tagger(cls, tokens):
        tagged = cls.pos_tagger.tag(tokens)
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
        tokens = list(tokens - self.stop_words)

        # tokens = [x.lower() for x in re.findall(r'[a-zA-Z]+', f.read())]
        print('after stops, num tokens: {}'.format(len(tokens)))

        # BS cuz not a sentence
        # limit length of sentence
        chunk_size = 500  # 500 words
        start = 0
        lemmatized = set()
        while start < len(tokens):
            print('pos tagging starting at {}/{}'.format(start, len(tokens)))
            tagged = self.wn.stanford_tagger(tokens[start: start + chunk_size])
            # lemmatized = set([self.wn.lemmatize(wd, pos) for wd, pos in wd_pos.items()])
            lemmatized.update([self.wn.lemmatize(wd, pos)
                               for wd, pos in tagged])
            start += chunk_size

        return lemmatized

    @staticmethod
    def neat_print(words):
        """print words at most 120 chars per line. show line number too"""
        final = []
        l = 0
        max_line_wrap = 80
        temp = []
        for w in words:
            if l + len(w) > max_line_wrap:
                # push temp and reset
                final.append(temp)
                temp = [w]
                l = len(w) + 1  # 1 for space
            else:
                temp.append(w)
                l += len(w) + 1
        # append the final bits
        final.append(temp)

        # print stuff with line number
        for idx, line in enumerate(final):
            print('{num:0>3}|{words}'.format(num=idx, words=' '.join(line)))
            if (idx + 1) % 5 == 0:
                print('\n')

    def get_top_words(self):
        """return the top cutoff words appear in the movie"""
        words = []
        for w in self.all_words:
            if len(words) == self.cutoff:
                break

            if w in self.target_words:
                words.append(w)

        print('\n================= TOP words ==================')
        self.neat_print(words)

        print('\n==================== words not in thesaurus ================')
        self.neat_print(self.target_words - set(self.all_words))

        return words


if __name__ == '__main__':
    args = sys.argv[1:]
    kwargs = {'path': args[0]}
    if len(args) >= 2:
        kwargs['cutoff'] = int(args[1])
    if len(args) >= 3:
        kwargs['corpus_path'] = args[2]

    tw = TopWords(**kwargs)
