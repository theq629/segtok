def split_with_spans(regex, text):
    last_end = 0
    for match in regex.finditer(text):
        yield text[last_end:match.start()], (last_end, match.start())
        for group_i, match_group in enumerate(match.groups()):
            yield match_group, (match.start(group_i), match.end(group_i))
        last_end = match.end()
    yield text[last_end:len(text)], (last_end, len(text))
