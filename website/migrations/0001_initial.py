# Generated by Django 5.0.1 on 2024-01-06 23:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('video_file', models.FileField(upload_to='videos/')),
                ('transcript', models.TextField(blank=True, null=True)),
                ('resume', models.TextField(blank=True, null=True)),
                ('date_uploaded', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
