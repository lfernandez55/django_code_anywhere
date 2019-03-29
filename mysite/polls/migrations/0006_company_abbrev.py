# Generated by Django 2.1.3 on 2018-12-10 07:19

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0005_company_employee'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='abbrev',
            field=models.CharField(default=django.utils.timezone.now, max_length=60),
            preserve_default=False,
        ),
    ]