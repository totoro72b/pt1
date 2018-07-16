import unittest

from topwords import TopWords, WordNetHelper


class TestTopWords(unittest.TestCase):

    def setUp(self):
        self.corpus_path = 'test_corpus.txt'
        self.file_path = 'test_target.txt'
        self.cutoff = 100
        self.tw = TopWords(self.file_path, self.cutoff, self.corpus_path)

    def test_load_corpus(self):
        """test it loads corpus words with increasing frequency"""
        expected = ['offer', 'create', 'offers', 'creating', 'him', 'some', 'one', 'their']
        self.assertEqual(self.tw.all_words, expected)

    def test_load_source(self):
        """test load target words lemmatized"""
        # test source words
        expected = set([
            'to',
            'wanna',
            'create',
            'him',
            'font',
            'a',
            'fella',
            'out',
            'cccc',
            'west',
            'color',
            'time',
            'tell',
            'com',
            'you',
            'hotmail',
            'way',
            'offer',
            'have',
            'some',
            'i',
            'this',
            'there',
            'asdf',
        ]
        )

        self.assertEqual(self.tw.target_words, expected)

    def test_get_top_words(self):
       """test correctly fetch top words"""
       expected = ['offer', 'create', 'him', 'some']
       self.assertEqual(self.tw.top_words, expected)


class TestWordNetHelper(unittest.TestCase):
    def test_lemmatize(self):
        line = 'i ran running today and hikes hiking with other girls and ate burgers'.split()
        wnh = WordNetHelper()
        actual = wnh.lemmatize(line)
        expected = 'i run run today and hike hike with other girl and eat burger'
        self.assertEqual(actual, expected.split())

