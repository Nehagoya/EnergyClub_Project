# Generated by Django 3.1.5 on 2021-01-15 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_alumni'),
    ]

    operations = [
        migrations.CreateModel(
            name='achievement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('awardedby', models.TextField()),
                ('issueyear', models.CharField(max_length=4)),
                ('summary', models.TextField()),
            ],
        ),
    ]