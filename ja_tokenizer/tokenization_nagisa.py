import nagisa


class NagisaTokenizer:
    def tokenize(self, text):
        words = nagisa.tagging(text)
        return dict(words=words.words, postags=words.postags)