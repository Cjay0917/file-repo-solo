# Generated by Django 4.0.1 on 2022-02-02 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('repo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='image',
            field=models.ImageField(default='default.jpg', upload_to='profile-images'),
        ),
    ]
