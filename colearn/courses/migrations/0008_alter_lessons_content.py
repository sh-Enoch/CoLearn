# Generated by Django 5.1.4 on 2025-01-08 01:08

import django_ckeditor_5.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0007_resource'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lessons',
            name='content',
            field=django_ckeditor_5.fields.CKEditor5Field(verbose_name='Content'),
        ),
    ]
