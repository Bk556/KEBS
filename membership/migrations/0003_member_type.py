# Generated by Django 3.2.19 on 2023-06-14 09:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('membership', '0002_registration_type_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Member_type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('member_type', models.CharField(choices=[('Student member', 'Student member'), ('Affiliate member', 'Affiliate member'), ('Associate member', 'Associate memeber'), ('Full member', 'Full member')], max_length=30)),
                ('years_trained', models.TextField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
