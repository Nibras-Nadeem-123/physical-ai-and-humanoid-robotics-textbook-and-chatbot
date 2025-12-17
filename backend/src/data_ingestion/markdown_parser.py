from markdown_it import MarkdownIt

def parse_markdown(content: str) -> str:
    """
    Parses Markdown content and returns the raw text.
    """
    md = MarkdownIt()
    # This is a simplification. In a real scenario, you would
    # likely want to extract more structure from the markdown,
    # not just render it to a string. For now, we'll just
    # render it and assume the output is close enough to raw text.
    # A better approach would be to walk the token stream and extract text.
    tokens = md.parse(content)
    text_content = ""
    for token in tokens:
        if token.type == 'inline':
            text_content += token.content
    return text_content