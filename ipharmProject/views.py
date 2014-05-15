from django.views.generic.base import TemplateView


class Home(TemplateView):
    template_name = 'index.html'

    # def get(self, request, *args, **kwargs):
    #     return render(request, self.template_name)

