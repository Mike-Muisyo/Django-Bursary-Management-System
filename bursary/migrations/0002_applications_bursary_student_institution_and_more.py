# Generated by Django 4.1.1 on 2023-02-01 07:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bursary', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Applications',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('status', models.CharField(choices=[('Pending', 'Pending'), ('Disbursement in Progress', 'Disbursement in Progress'), ('Fully Disbursed', 'Fully Disbursed')], max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Bursary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
                ('amount', models.FloatField(null=True)),
                ('category', models.CharField(choices=[('County', 'County'), ('Constituency', 'Constituency')], max_length=200, null=True)),
                ('batch_number', models.CharField(max_length=200, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='student',
            name='institution',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='year_of_study',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
