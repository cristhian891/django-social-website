from django.views.generic import TemplateView, ListView

from posts.models import Post



class WelcomePage(TemplateView):
    template_name = 'main_page.html'


class ThanksPage(TemplateView):
    template_name = 'thanks.html'


class HomePage(ListView):
    template_name = 'index.html'

    queryset = Post.objects.all()

    def get_context_data(self, **kwargs):
        context = super(HomePage, self).get_context_data(**kwargs)
        context['posts'] = Post.objects.all()[:1]
        return context
