# Generated by Django 4.2.5 on 2024-06-17 04:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sch', '0007_hadmission'),
    ]

    operations = [
        migrations.CreateModel(
            name='Whyus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heading', models.CharField(max_length=30)),
                ('description', models.TextField(blank=True, null=True)),
                ('icon', models.ImageField(blank=True, null=True, upload_to='icon/')),
            ],
        ),
        migrations.AlterField(
            model_name='habout',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='about/images/'),
        ),
    ]
