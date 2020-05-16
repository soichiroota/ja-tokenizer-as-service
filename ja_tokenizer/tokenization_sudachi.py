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
        return [
            dict(
                surface=m.surface(),
                dictionary_form=m.dictionary_form(),
                reading_form=m.reading_form(),
                part_of_speech=m.part_of_speech(),
                normalized_form=m.normalized_form()
            ) for m in self.tokenizer.tokenize(
            text, self.split_mode
        )]