import unittest

from topwords import TopWords, WordNetHelper


class TestTopWords(unittest.TestCase):

    def setUp(self):
        self.corpus_path = 'test_corpus.txt'
        self.file_path = 'test_target.txt'
        self.cutoff = 100
        self.tw = TopWords(self.file_path, self.cutoff, self.corpus_path)

    def test_basic_stuff(self):
        """test it loads corpus words, loading target, get top"""
        # all here since it takes forever to init TopWords due to pos_tag the target words

        # test get all thesaurus by inc frequency
        expected = ['offer', 'create', 'offers', 'creating', 'him', 'some', 'one', 'their']
        self.assertEqual(self.tw.all_words, expected)

        # test load target words lemmatized with stop words removed
        expected = {'way', 'cccc', 'wanna', 'color', 'font', 'asdf', 'tell', 'com', 'create', 'time', 'hotmail', 'fella', 'offer', 'west'}

        print('target words', self.tw.target_words)
        self.assertEqual(self.tw.target_words, expected)

        # test correctly fetch top words
        expected = ['offer', 'create']
        self.assertEqual(self.tw.top_words, expected)
