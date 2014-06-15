from django.contrib.auth.decorators import login_required
import markdown


class LoginRequiredMixin:
    """
    Mixin to wrap view in the login_required decorator.
    """

    @classmethod
    def as_view(cls, **kwargs):
        view = super().as_view(**kwargs)
        return login_required(view)


class MarkdownMixin:
    """
    Simple mixin that requires a field called 'body'
    """

    def get_body(self):
        return markdown.markdown(self.body)
