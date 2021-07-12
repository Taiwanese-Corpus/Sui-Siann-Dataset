# Generated by Django 3.2.4 on 2021-07-12 01:39

from django.db import migrations, models
import django.db.models.deletion
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('SuiSiannAdminApp', '0015_auto_20210712_0916'),
    ]

    operations = [
        migrations.AlterField(
            model_name='句表',
            name='kaldi切音時間',
            field=jsonfield.fields.JSONField(default=[], editable=False),
        ),
        migrations.AlterField(
            model_name='句表',
            name='來源',
            field=models.ForeignKey(default=1, editable=False, on_delete=django.db.models.deletion.CASCADE, related_name='句', to='SuiSiannAdminApp.文章表'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='句表',
            name='修改時間',
            field=models.DateTimeField(editable=False, null=True),
        ),
        migrations.AlterField(
            model_name='句表',
            name='原始漢字',
            field=models.TextField(editable=False),
        ),
        migrations.AlterField(
            model_name='句表',
            name='原始羅馬字',
            field=models.TextField(editable=False),
        ),
    ]
