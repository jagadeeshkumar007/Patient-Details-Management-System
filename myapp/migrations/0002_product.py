# Generated by Django 4.1.4 on 2023-01-05 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('op1', models.CharField(max_length=100)),
                ('op2', models.CharField(max_length=100)),
                ('op3', models.CharField(max_length=100)),
                ('op4', models.CharField(max_length=100)),
            ],
        ),
    ]
