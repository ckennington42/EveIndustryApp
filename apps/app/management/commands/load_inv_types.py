from csv import DictReader
from django.core.management import BaseCommand

from apps.app.models import InvType, MarketGroup

class Command(BaseCommand):
    help = "Loads data from typeIDs.yaml"

    print("Removing existing invType data")
    InvType.objects.all().delete()



    def handle(self, *args, **options):
        with open('./data/invTypes.csv', 'r', encoding='utf-8') as file:
            for row in DictReader(file):
                if row['marketGroupID'] == 'None':
                    row['marketGroupID'] = 0

                try:
                    invType = InvType(
                        type_id=row['typeID'],
                        group_id=0 if row['groupID'] == 'None' else row['groupID'],
                        name=row['typeName'],
                        volume=row['volume'] if isinstance(row['volume'], int) else 0,
                        published=row['published'],
                        icon_id=0 if row['iconID'] == 'None' else row['iconID'],
                        graphic_id=0 if row['graphicID'] == 'None' else row['graphicID'],
                        market_group=None if row['marketGroupID'] == 0 else MarketGroup.objects.get(group_id=row['marketGroupID'])
                    )


                    invType.save()

                except Exception as e:
                    print("unable to load", row, e)

        print('done')