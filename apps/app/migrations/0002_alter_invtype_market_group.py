# Generated by Django 4.2.9 on 2024-02-11 20:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invtype',
            name='market_group',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='market_group', to='app.marketgroup'),
        ),
    ]
