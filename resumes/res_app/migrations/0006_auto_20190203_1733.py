# Generated by Django 2.1.5 on 2019-02-03 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('res_app', '0005_auto_20190203_1719'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resume',
            name='projects',
            field=models.ManyToManyField(null=True, to='res_app.Project'),
        ),
    ]
