from django.http import HttpResponse, JsonResponse
from django.template import loader
from django.utils.decorators import method_decorator
from esi.decorators import tokens_required
from apps.app.models import InvType, MarketGroup
from apps.inventory import assetsProvider
from apps.inventory.models import Asset
from config import settings


@tokens_required(scopes=settings.SCOPES)
def inventory_view(request, tokens):
    context = {}
    blueprints = InvType.objects.filter(market_group__group_id=2)
    print(list(blueprints.values()))

    template = loader.get_template('estimator/index.html')
    return HttpResponse(template.render(context, request))