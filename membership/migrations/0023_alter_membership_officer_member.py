# Generated by Django 3.2.19 on 2023-07-10 06:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('membership', '0022_auto_20230705_1238'),
    ]

    operations = [
        migrations.AlterField(
            model_name='membership_officer',
            name='Member',
            field=models.CharField(blank=True, choices=[('mutai', 'mutai'), ('k1', 'k1'), ('test', 'test'), ('sam', 'sam'), ('atl', 'atl'), ('koech', 'koech'), ('scola', 'scola'), ('bruce', 'bruce'), ('Scolasticah', 'Scolasticah')], max_length=150, null=True),
        ),
    ]
