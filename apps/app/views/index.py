from django.http import HttpResponse, JsonResponse
from django.template import loader
from django.views import View



class IndexView(View):
    def get(self, request):
        context = {}
        template = loader.get_template('app/login.html')
        if request.user.is_authenticated:
            template = loader.get_template('app/index.html')

        return HttpResponse(template.render(context, request))