# Generated by Django 4.1.4 on 2023-01-06 22:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0012_rename_remarks_reports_rem'),
    ]

    operations = [
        migrations.AddField(
            model_name='reports',
            name='urlf',
            field=models.CharField(default='XXXXXXX', max_length=1000),
        ),
    ]
