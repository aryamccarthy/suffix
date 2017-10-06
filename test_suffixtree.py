from suffixtree import SuffixTree


class TestSuffixTree(object):
    def setup(self):
        self.t = SuffixTree("there would have been a time for such a word")

    def test_has_substring_no(self):
        assert not self.t.has_substring('nope')

    def test_has_substring_yes(self):
        assert self.t.has_substring('would have been')

    def test_has_suffix_no(self):
        assert not self.t.has_suffix('would have been')

    def test_has_suffix_yes(self):
        assert self.t.has_suffix('such a word')
