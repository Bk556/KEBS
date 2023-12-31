# Generated by Django 3.2.19 on 2023-06-15 08:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('membership', '0008_length_of_tenure'),
    ]

    operations = [
        migrations.CreateModel(
            name='Courses_related_to_quality_management',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Course', models.CharField(max_length=30)),
                ('Course_duration_in_years', models.IntegerField(max_length=3)),
                ('Organization', models.CharField(max_length=30)),
                ('Certificate_awarded', models.CharField(max_length=30)),
                ('certificate_file', models.FileField(upload_to='documents/')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
