import os

from JapaneseTokenizer import (
    MecabWrapper, JumanWrapper, JumanppWrapper, KyteaWrapper)

from ja_tokenizer import (
    tokenization_mecab,
    tokenization_sudachi,
    tokenization_nagisa,
    tokenization_sentencepiece)


class MecabTokenizer:
    def __init__(self, dict_type=None):
        if dict_type:
            self.tokenizer = MecabWrapper(dictType=dict_type)
        else:
            self.tokenizer = MecabWrapper(dictType=None)

    def tokenize(self, text):
        tokenized_objects = self.tokenizer.tokenize(
            text
        ).tokenized_objects
        return [dict(
            analyzed_line=obj.analyzed_line,
            word_surface=obj.word_surface,
            word_stem=obj.word_stem,
            pos=list(obj.tuple_pos),
            misc_info=obj.misc_info
        ) for obj in tokenized_objects]


class JumanTokenizer:
    def __init__(self):
        self.tokenizer = JumanWrapper()

    def tokenize(self, text):
        tokenized_objects = self.tokenizer.tokenize(
            text
        ).tokenized_objects
        return [dict(
            analyzed_line=obj.analyzed_line,
            word_surface=obj.word_surface,
            word_stem=obj.word_stem,
            pos=list(obj.tuple_pos),
            misc_info=obj.misc_info
        ) for obj in tokenized_objects]

    
class JumanppTokenizer:
    def __init__(self):
        self.tokenizer = JumanppWrapper()

    def tokenize(self, text):
        tokenized_objects = self.tokenizer.tokenize(
            text
        ).tokenized_objects
        return [dict(
            analyzed_line=obj.analyzed_line,
            word_surface=obj.word_surface,
            word_stem=obj.word_stem,
            pos=list(obj.tuple_pos),
            misc_info=obj.misc_info
        ) for obj in tokenized_objects]


class KyteaTokenizer:
    def __init__(self):
        self.tokenizer = KyteaWrapper()

    def tokenize(self, text):
        tokenized_objects = self.tokenizer.tokenize(
            text
        ).tokenized_objects
        return [dict(
            analyzed_line=obj.analyzed_line,
            word_surface=obj.word_surface,
            word_stem=obj.word_stem,
            pos=list(obj.tuple_pos),
            misc_info=obj.misc_info
        ) for obj in tokenized_objects]     


class Tokenizer:
    def __init__(self, library=None, args=None, dict_type=None, split_mode=None):
        if library == 'sentencepiece':
            cur_dir = os.path.dirname(__file__)

            self.tokenizer = tokenization_sentencepiece.FullTokenizer(
                model_file=os.path.join(
                    cur_dir, 'model', 'wiki-ja.model'
                ),
                vocab_file=os.path.join(
                    cur_dir, 'model', 'wiki-ja.vocab'
                ),
                do_lower_case=True
            )
        elif library == 'mecab':
            self.tokenizer = MecabTokenizer(dict_type)
        elif library == 'juman':
            self.tokenizer = JumanTokenizer()
        elif library == 'jumanpp':
            self.tokenizer = JumanTokenizer()
        elif library == 'kytea':
            self.tokenizer = KyteaTokenizer()
        elif library == 'sudachi':
            self.tokenizer = tokenization_sudachi.SudachiTokenizer(
                split_mode
            )
        elif library == 'nagisa':
            self.tokenizer = tokenization_nagisa.NagisaTokenizer()
        else:
            self.tokenizer = tokenization_mecab.MecabTokenizer(args)
    
    def tokenize(self, text):
        return self.tokenizer.tokenize(text)