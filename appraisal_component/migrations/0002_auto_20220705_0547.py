# Generated by Django 3.2.4 on 2022-07-05 05:47

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('appraisal_component', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cpcassessment',
            old_name='contribution_to_university_or_country',
            new_name='contribution_to_university_or_country_grade',
        ),
        migrations.RenameField(
            model_name='cpcassessment',
            old_name='signature',
            new_name='dean_signature',
        ),
        migrations.RenameField(
            model_name='cpcassessment',
            old_name='quality_of_publication',
            new_name='quality_of_publication_grade',
        ),
        migrations.RenameField(
            model_name='cpcassessment',
            old_name='quality_of_research',
            new_name='quality_of_research_grade',
        ),
        migrations.RenameField(
            model_name='cpcassessment',
            old_name='quality_of_teaching',
            new_name='quality_of_teaching_grade',
        ),
        migrations.RenameField(
            model_name='staffappraisal',
            old_name='dissertation_of_thesis',
            new_name='publications',
        ),
        migrations.RemoveField(
            model_name='cpcassessment',
            name='admistrative_experience_score',
        ),
        migrations.RemoveField(
            model_name='cpcassessment',
            name='interview_experience_score',
        ),
        migrations.AddField(
            model_name='cpcassessment',
            name='administrative_experience_score',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)]),
        ),
        migrations.AddField(
            model_name='cpcassessment',
            name='board_recommendations',
            field=models.CharField(blank=True, max_length=500),
        ),
        migrations.AddField(
            model_name='cpcassessment',
            name='interview_performance_score',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10)]),
        ),
        migrations.AddField(
            model_name='cpcassessment',
            name='percentage',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='cpcassessment',
            name='professional_qualification_score',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)]),
        ),
        migrations.AddField(
            model_name='cpcassessment',
            name='recognized_publication_score',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(30)]),
        ),
        migrations.AlterField(
            model_name='cpcassessment',
            name='academic_qualification_score',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10)]),
        ),
        migrations.AlterField(
            model_name='cpcassessment',
            name='contribution_to_university_or_country_score',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)]),
        ),
        migrations.AlterField(
            model_name='cpcassessment',
            name='current_research_score',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10)]),
        ),
        migrations.AlterField(
            model_name='cpcassessment',
            name='teaching_score',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(25)]),
        ),
        migrations.AlterField(
            model_name='hodassessment',
            name='contribution_to_university_or_country',
            field=models.CharField(choices=[(10, 'A'), (8, 'B'), (6, 'C'), (4, 'D'), (2, 'E')], max_length=200),
        ),
        migrations.AlterField(
            model_name='hodassessment',
            name='current_research',
            field=models.CharField(choices=[(10, 'A'), (8, 'B'), (6, 'C'), (4, 'D'), (2, 'E')], max_length=200),
        ),
        migrations.AlterField(
            model_name='hodassessment',
            name='general_assessment',
            field=models.CharField(choices=[(10, 'A'), (8, 'B'), (6, 'C'), (4, 'D'), (2, 'E')], max_length=200),
        ),
        migrations.AlterField(
            model_name='hodassessment',
            name='other_departmental_responsibilities',
            field=models.CharField(choices=[(10, 'A'), (8, 'B'), (6, 'C'), (4, 'D'), (2, 'E')], max_length=200),
        ),
        migrations.AlterField(
            model_name='hodassessment',
            name='postgraduate_supervision',
            field=models.CharField(choices=[(10, 'A'), (8, 'B'), (6, 'C'), (4, 'D'), (2, 'E')], max_length=200),
        ),
        migrations.AlterField(
            model_name='hodassessment',
            name='quality_of_publications',
            field=models.CharField(choices=[(10, 'A'), (8, 'B'), (6, 'C'), (4, 'D'), (2, 'E')], max_length=200),
        ),
        migrations.AlterField(
            model_name='hodassessment',
            name='quality_of_research',
            field=models.CharField(choices=[(10, 'A'), (8, 'B'), (6, 'C'), (4, 'D'), (2, 'E')], max_length=200),
        ),
        migrations.AlterField(
            model_name='hodassessment',
            name='quality_of_teaching',
            field=models.CharField(choices=[(10, 'A'), (8, 'B'), (6, 'C'), (4, 'D'), (2, 'E')], max_length=200),
        ),
        migrations.CreateModel(
            name='LectuterComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('get_comment', models.TextField()),
                ('date_signed', models.DateTimeField(auto_now_add=True)),
                ('get_signature', models.CharField(blank=True, choices=[('select', 'select'), ('Signed & Approved', 'Signed & Approved'), ('Unsigned &Unapproved', 'Unsigned &Unapproved')], default='select', max_length=200)),
                ('get_appraisal', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='lecturer_comment', to='appraisal_component.staffappraisal')),
                ('get_lecturer', models.ForeignKey(blank=True, default='No comment', on_delete=django.db.models.deletion.CASCADE, related_name='lecturer_comment', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
