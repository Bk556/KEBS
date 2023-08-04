# Generated by Django 3.2.19 on 2023-07-03 12:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('membership', '0015_academic_qualification_course_duration_in_years'),
    ]

    operations = [
        migrations.AlterField(
            model_name='information_on_present_position',
            name='any_other_specify',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='information_on_present_position',
            name='description_on_current_quality',
            field=models.TextField(max_length=50),
        ),
        migrations.CreateModel(
            name='Membership_officer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(default='pending', max_length=50)),
                ('Comments', models.CharField(max_length=100)),
                ('Member', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Me', to=settings.AUTH_USER_MODEL)),
                ('Membership_officer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Mo', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
