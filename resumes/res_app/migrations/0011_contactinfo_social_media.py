# Generated by Django 2.1.7 on 2019-02-17 00:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('res_app', '0010_socialmedia'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactinfo',
            name='social_media',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='res_app.SocialMedia'),
        ),
    ]