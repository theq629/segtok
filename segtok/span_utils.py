def make_sub(outer_with_span, inner_with_span):
    outer_text, outer_span = outer_with_span
    inner_text, inner_span = inner_with_span
    return inner_text, (outer_span[0] + inner_span[0], outer_span[0] + inner_span[1])

def test_sequencer_with_spans(tester, sequencer, normalize_item=lambda x: x):
    """
    Wrap a function that provides a sequence of items with spans to work as a regular spanless sequence, and also test that its token values match the values its spans give in the original text.
    """
    def wrapped(text):
        items_with_spans = list(sequencer(text))
        items = [t for t, s in items_with_spans]
        tester.assertSequenceEqual(items, [normalize_item(text[s[0]:s[1]]) for _, s in items_with_spans])
        return items
    return wrapped
