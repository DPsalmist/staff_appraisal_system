# Generated by Django 3.2.4 on 2022-07-05 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appraisal_component', '0003_rename_lectutercomment_lecturercomment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hodassessment',
            name='contribution_to_university_or_country',
            field=models.CharField(choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E')], max_length=200),
        ),
        migrations.AlterField(
            model_name='hodassessment',
            name='current_research',
            field=models.CharField(choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E')], max_length=200),
        ),
        migrations.AlterField(
            model_name='hodassessment',
            name='general_assessment',
            field=models.CharField(choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E')], max_length=200),
        ),
        migrations.AlterField(
            model_name='hodassessment',
            name='other_departmental_responsibilities',
            field=models.CharField(choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E')], max_length=200),
        ),
        migrations.AlterField(
            model_name='hodassessment',
            name='postgraduate_supervision',
            field=models.CharField(choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E')], max_length=200),
        ),
        migrations.AlterField(
            model_name='hodassessment',
            name='quality_of_publications',
            field=models.CharField(choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E')], max_length=200),
        ),
        migrations.AlterField(
            model_name='hodassessment',
            name='quality_of_research',
            field=models.CharField(choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E')], max_length=200),
        ),
        migrations.AlterField(
            model_name='hodassessment',
            name='quality_of_teaching',
            field=models.CharField(choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E')], max_length=200),
        ),
    ]
