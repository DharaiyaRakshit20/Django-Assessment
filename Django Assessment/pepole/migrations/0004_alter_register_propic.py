# Generated by Django 4.2.4 on 2023-08-05 06:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pepole', '0003_register_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='register',
            name='propic',
            field=models.FileField(default='pepole.jpg', upload_to='media/'),
        ),
    ]