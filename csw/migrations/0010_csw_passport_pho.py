# Generated by Django 4.0.4 on 2022-06-04 18:28

from django.db import migrations, models
import django.forms.fields


class Migration(migrations.Migration):

    dependencies = [
        ('csw', '0009_private_practice'),
    ]

    operations = [
        migrations.AddField(
            model_name='csw',
            name='passport_pho',
            field=models.ImageField(blank=True, null=True, upload_to=django.forms.fields.FilePathField, verbose_name='Passport Photo'),
        ),
    ]
