import os
import json

import responder
from ja_tokenizer import Tokenizer


env = os.environ
DEBUG = env['DEBUG'] in ['1', 'True', 'true']
LIBRARY = env['LIBRARY']
ARGS = env.get('ARGS')
DICT_TYPE = env.get('DICT_TYPE')
SPLIT_MODE = env.get('SPLIT_MODE')

api = responder.API(debug=DEBUG)
tokenizer = Tokenizer(LIBRARY, ARGS, DICT_TYPE, SPLIT_MODE)


@api.route("/")
async def tokenize(req, resp):
    body = await req.text
    texts = json.loads(body)
    tokenized_texts = [tokenizer.tokenize(text) for text in texts]
    resp_dict = dict(data=tokenized_texts)
    resp.media = resp_dict


if __name__ == "__main__":
    api.run()