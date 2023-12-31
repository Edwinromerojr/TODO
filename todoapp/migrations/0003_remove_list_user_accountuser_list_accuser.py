# Generated by Django 4.1.4 on 2023-08-25 17:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('todoapp', '0002_list_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='list',
            name='user',
        ),
        migrations.CreateModel(
            name='AccountUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='list',
            name='accUser',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='todoapp.accountuser'),
        ),
    ]
