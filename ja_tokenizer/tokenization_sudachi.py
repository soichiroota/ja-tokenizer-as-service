from sudachipy import tokenizer, dictionary


class SudachiTokenizer:
    def __init__(self, split_mode=None):
        self.tokenizer = dictionary.Dictionary().create()
        if split_mode == 'A':
            self.split_mode = tokenizer.Tokenizer.SplitMode.A
        elif split_mode == 'B':
            self.split_mode = tokenizer.Tokenizer.SplitMode.B
        else:
            self.split_mode = tokenizer.Tokenizer.SplitMode.C

    def tokenize(self, text):
        return [m.surface() for m in self.tokenizer.tokenize(
            text, self.split_mode
        )]