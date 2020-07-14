# Generated by Django 3.0.8 on 2020-07-12 09:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='polls',
            name='persons',
        ),
        migrations.AddField(
            model_name='persons',
            name='polls',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='polls.Polls', verbose_name='Голосования'),
        ),
    ]