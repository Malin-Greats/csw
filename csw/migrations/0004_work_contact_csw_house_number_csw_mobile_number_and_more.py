# Generated by Django 4.0.4 on 2022-06-03 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('csw', '0003_remove_csw_description_csw_gender_csw_city_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Work_contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('organisation', models.CharField(max_length=70, null=True, verbose_name='Organisation')),
                ('department', models.CharField(max_length=70, null=True, verbose_name='Department')),
                ('address', models.CharField(max_length=70, null=True, verbose_name='Address')),
                ('city', models.CharField(max_length=70, null=True, verbose_name='City')),
                ('country', models.CharField(max_length=70, null=True, verbose_name='Country')),
                ('mobile_number', models.IntegerField(max_length=70, null=True, verbose_name='Mobile Number')),
                ('email_address', models.EmailField(max_length=70, null=True, verbose_name='Email Address')),
            ],
        ),
        migrations.AddField(
            model_name='csw',
            name='house_number',
            field=models.CharField(max_length=70, null=True, verbose_name='House Number'),
        ),
        migrations.AddField(
            model_name='csw',
            name='mobile_number',
            field=models.IntegerField(max_length=70, null=True, verbose_name='Mobile Number'),
        ),
        migrations.AlterField(
            model_name='csw',
            name='title',
            field=models.IntegerField(choices=[(1, 'Mr'), (2, 'Mrs'), (3, 'Miss'), (4, 'Other')], max_length=20, null=True, verbose_name='Title'),
        ),
    ]