def without_spans(items_with_spans):
    for item_text, item_span in items_with_spans:
        yield item_text
