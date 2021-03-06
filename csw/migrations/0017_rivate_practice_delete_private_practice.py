# Generated by Django 4.0.4 on 2022-06-07 03:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('csw', '0016_user_profile_delete_profile'),
    ]

    operations = [
        migrations.CreateModel(
            name='rivate_practice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jurisdiction', models.CharField(max_length=70, null=True, verbose_name='Jurisdiction')),
                ('area_of_practice', models.CharField(max_length=70, null=True, verbose_name='Area of Practice eg Counselling')),
                ('name_of_practise', models.CharField(max_length=70, null=True, verbose_name='Name Of Practise')),
                ('address', models.CharField(max_length=70, null=True, verbose_name='Address')),
                ('mobile_number', models.CharField(max_length=70, null=True, verbose_name='Mobile Number')),
                ('email', models.EmailField(max_length=70, null=True, verbose_name='Email')),
                ('any_discipinary', models.CharField(choices=[('N', 'NO'), ('Y', 'Yes'), ('I', 'If Yes Give Reason')], max_length=20, null=True, verbose_name='Have you ever practiced as a Registered Social Worker')),
            ],
        ),
        migrations.DeleteModel(
            name='private_practice',
        ),
    ]
