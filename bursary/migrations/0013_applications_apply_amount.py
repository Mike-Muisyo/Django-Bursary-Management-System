# Generated by Django 4.1.1 on 2023-02-28 20:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bursary', '0012_student_constituency_alter_student_profile_pic_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='applications',
            name='apply_amount',
            field=models.FloatField(choices=[('10000', '10000'), ('15000', '15000')], null=True),
        ),
    ]
