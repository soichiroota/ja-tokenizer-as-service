import nagisa


class NagisaTokenizer:
    def tokenize(self, text):
        words = nagisa.tagging(text)
        return words.words