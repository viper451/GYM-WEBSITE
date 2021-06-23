# Generated by Django 3.0.2 on 2021-06-23 15:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('login', '0026_remove_fit_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='fit',
            name='username',
            field=models.ForeignKey(max_length=30, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]
