# Generated by Django 4.2.3 on 2024-01-25 04:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MarketGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group_id', models.IntegerField(default=0, unique=True)),
                ('parent_id', models.IntegerField(default=0)),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='InvType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_id', models.IntegerField(unique=True)),
                ('group_id', models.IntegerField(default=0)),
                ('name', models.CharField(max_length=200)),
                ('volume', models.DecimalField(decimal_places=2, default=0.0, max_digits=14)),
                ('published', models.BooleanField(default=False)),
                ('icon_id', models.IntegerField(default=0)),
                ('graphic_id', models.IntegerField(default=0)),
                ('market_group', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='market_group', to='inventory.marketgroup')),
            ],
        ),
    ]
