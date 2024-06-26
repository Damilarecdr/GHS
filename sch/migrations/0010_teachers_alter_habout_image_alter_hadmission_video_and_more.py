# Generated by Django 4.2.5 on 2024-06-17 04:37

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sch', '0009_remove_whyus_icon'),
    ]

    operations = [
        migrations.CreateModel(
            name='Teachers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='uploads/teachers/images/')),
            ],
        ),
        migrations.AlterField(
            model_name='habout',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='uploads/images/habout/'),
        ),
        migrations.AlterField(
            model_name='hadmission',
            name='video',
            field=models.FileField(null=True, upload_to='uploads/videos', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['MOV', 'avi', 'mp4', 'webm', 'mkv'])]),
        ),
        migrations.AlterField(
            model_name='slide',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/slides/'),
        ),
    ]
