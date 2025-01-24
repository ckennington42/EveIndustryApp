from django.http import HttpResponse, JsonResponse
from django.template import loader
from django.utils.decorators import method_decorator
from esi.decorators import tokens_required

from apps.inventory import assetsProvider
from apps.inventory.models import Asset
from config import settings


@tokens_required(scopes=settings.SCOPES)
def inventory_view(request, tokens):

    groups = assetsProvider.get_manufacting_and_research_asset_groups([], None)
    assets = Asset.objects.filter(type__market_group__group_id__in=groups, character=tokens[0].character_id).order_by(
        'type__name')

    context = {'assets': list(assets.values())}
    template = loader.get_template('inventory/index.html')
    return HttpResponse(template.render(context, request))


@tokens_required(scopes=settings.SCOPES)
def refresh_inventory(request, tokens):
    assetsProvider.load_assets(tokens[0])
    groups = assetsProvider.get_manufacting_and_research_asset_groups([], None)
    assets = Asset.objects.filter(type__market_group__group_id__in=groups, character=tokens[0].character_id).order_by(
        'type__name')
    context = {'assets': list(assets.values())}
    return JsonResponse(context)

@tokens_required(scopes=settings.SCOPES)
def clear_inventory(request, tokens):

    Asset.objects.filter(character=tokens[0].character_id).delete()
    context = {'assets': []}
    return JsonResponse(context)
