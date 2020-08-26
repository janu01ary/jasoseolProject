# Generated by Django 3.1 on 2020-08-25 16:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0004_auto_20200826_0112'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jasoseol',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auth.user'),
        ),
    ]
