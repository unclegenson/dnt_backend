# Generated by Django 5.1.3 on 2024-11-15 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserApp',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('user_name', models.CharField(max_length=150)),
                ('user_telid', models.IntegerField(unique=True)),
                ('created_time', models.DateTimeField(auto_now=True)),
                ('referral_count', models.IntegerField(default=0)),
            ],
        ),
    ]
