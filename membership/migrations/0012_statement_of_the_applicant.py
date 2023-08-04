# Generated by Django 3.2.19 on 2023-06-15 09:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('membership', '0011_code_of_conduct'),
    ]

    operations = [
        migrations.CreateModel(
            name='Statement_of_the_applicant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Full_name_of_the_applicant', models.CharField(max_length=50)),
                ('Date', models.DateField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]