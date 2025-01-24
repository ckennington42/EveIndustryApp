from esi.clients import EsiClientProvider
from django.db import transaction

from apps.inventory.models import *

from apps.app.models import MarketGroup

esi = EsiClientProvider()

def load_assets(token):
    # get assets
    results = esi.client.Assets.get_characters_character_id_assets(
        # required parameter for endpoint
        character_id=token.character_id,
        # provide a valid access token, which wil be refresh the token if required
        token=token.valid_access_token()
    ).results()


    with transaction.atomic():
        for asset in results:
            try:
                if type := InvType.objects.get(type_id=asset['type_id']):
                    a, created = Asset.objects.get_or_create(type=type, location_id=asset['location_id'], character=token.character_id)
                    a.item_id = asset['item_id']
                    a.location_type = asset['location_type']
                    a.location_flag = asset['location_flag']
                    a.quantity = asset['quantity']
                    a.save()
            except Exception as e:
                #print(str(e))
                pass





def get_manufacting_and_research_asset_groups(groups, id=None):

    if not id:
        id = 475

    for group in MarketGroup.objects.filter(parent_id=id):
        groups.append(group.group_id)
        groups = get_manufacting_and_research_asset_groups(groups, group.group_id)

    return groups