# Generated by Django 3.2.19 on 2023-06-20 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('membership', '0012_statement_of_the_applicant'),
    ]

    operations = [
        migrations.AddField(
            model_name='applicant_details',
            name='nature_of_organization',
            field=models.CharField(blank=True, choices=[('private', 'private'), ('public', 'public')], max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='applicant_details',
            name='organization_address',
            field=models.CharField(max_length=100),
        ),
    ]
