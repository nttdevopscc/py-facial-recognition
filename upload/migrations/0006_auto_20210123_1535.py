# Generated by Django 3.1.5 on 2021-01-23 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('upload', '0005_auto_20210123_1535'),
    ]

    operations = [
        migrations.AlterField(
            model_name='faceimage',
            name='face_hash',
            field=models.BinaryField(blank=True, null=True),
        ),
    ]
