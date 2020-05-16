import MeCab


class MecabTokenizer:
    def __init__(self, args=None):
        if args:
            self.tokenizer = MeCab.Tagger(args)
        else:
            self.tokenizer = MeCab.Tagger()

    def tokenize(self, text):
        return self.tokenizer.parse(text)