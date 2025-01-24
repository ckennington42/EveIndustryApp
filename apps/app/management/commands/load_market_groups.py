from csv import DictReader
from django.core.management import BaseCommand

from apps.app.models import MarketGroup
from apps.inventory.models import *


class Command(BaseCommand):

    help = "Loads data from invMarketGroups.csv"

    def handle(self, *args, **options):

        # Show this before loading the data into the database

        print("Removing existing marketGroup data")
        MarketGroup.objects.all().delete()

        print("Loading marketGroup data")
        # Code to load the data into database
        with open('./data/invMarketGroups.csv', 'r', encoding='utf-8') as file:
            for row in DictReader(file):
                try:

                    marketGroup = MarketGroup(
                        group_id=row['marketGroupID'],
                        parent_id=0 if row['parentGroupID'] == 'None' else row['parentGroupID'],
                        name=row['marketGroupName'],
                        icon_id=0 if row['iconID'] == 'None' else row['iconID'],
                        has_types=row['hasTypes']
                    )

                    marketGroup.save()

                except Exception as e:
                    print("unable to load", row, e)

        print("done")