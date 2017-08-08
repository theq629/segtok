import sys
import segtok.tokenizer

tokenizer = segtok.tokenizer.word_tokenizer_with_spans

text = sys.stdin.read()
for token, span in tokenizer(text):
    orig_token = text[span[0]:span[1]].replace("\n", "")
    print token, span
    if orig_token != token:
        print >> sys.stderr, "error: got %s but span %s gives %s" % (repr(token), repr(span), repr(orig_token))
