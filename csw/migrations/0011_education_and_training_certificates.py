# Generated by Django 4.0.4 on 2022-06-04 18:40

from django.db import migrations, models
import django.forms.fields


class Migration(migrations.Migration):

    dependencies = [
        ('csw', '0010_csw_passport_pho'),
    ]

    operations = [
        migrations.AddField(
            model_name='education_and_training',
            name='certificates',
            field=models.FileField(null=True, upload_to=django.forms.fields.FilePathField, verbose_name='Certificates'),
        ),
    ]
