# Generated by Django 2.1.3 on 2019-01-03 03:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SuiSiannAdminApp', '0009_句表_加原始漢羅欄位'),
    ]

    operations = [
        migrations.AlterField(
            model_name='句表',
            name='原始漢字',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='句表',
            name='原始臺羅',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='句表',
            name='漢字',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='句表',
            name='臺羅',
            field=models.CharField(max_length=200),
        ),
    ]
