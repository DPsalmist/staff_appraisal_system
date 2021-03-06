# Generated by Django 3.2.4 on 2022-07-06 03:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('appraisal_component', '0005_auto_20220706_0346'),
    ]

    operations = [
        migrations.AddField(
            model_name='cpcassessment',
            name='which_appraisal',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='which_lecturer', to='appraisal_component.lecturercomment'),
        ),
        migrations.AlterField(
            model_name='lecturercomment',
            name='get_appraisal',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='lecturer_comment', to='appraisal_component.hodassessment'),
        ),
        migrations.AlterField(
            model_name='lecturercomment',
            name='get_lecturer',
            field=models.ForeignKey(blank=True, default='No comment', on_delete=django.db.models.deletion.CASCADE, related_name='lecturer_name', to=settings.AUTH_USER_MODEL),
        ),
    ]
