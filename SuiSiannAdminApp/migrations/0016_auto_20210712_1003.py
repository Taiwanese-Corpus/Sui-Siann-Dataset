# Generated by Django 3.2.4 on 2021-07-12 02:03

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
            field=models.ForeignKey(default=0, editable=False, on_delete=django.db.models.deletion.PROTECT, related_name='句', to='SuiSiannAdminApp.文章表'),
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
        migrations.AlterField(
            model_name='句表',
            name='音檔',
            field=models.FileField(editable=False, upload_to=''),
        ),
        migrations.AddConstraint(
            model_name='句表',
            constraint=models.UniqueConstraint(condition=models.Q(('音檔', ''), _negated=True), fields=('音檔',), name='imtong_bokang'),
        ),
    ]
