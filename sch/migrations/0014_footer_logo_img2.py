# Generated by Django 4.2.5 on 2024-06-17 06:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sch', '0013_logo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Footer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='logo',
            name='img2',
            field=models.ImageField(blank=True, null=True, upload_to='uploads/logo/images/'),
        ),
    ]