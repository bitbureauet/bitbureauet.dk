import markdown


class MarkdownMixin:
    """
    Simple mixin that requires a field called 'body'
    """

    def get_body(self):
        return markdown.markdown(self.body)
