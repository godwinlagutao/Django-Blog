# Generated by Django 5.1 on 2024-08-18 23:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0003_post_subheading_alter_post_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='subheading',
            field=models.CharField(blank=True, default=1, max_length=250, null=True),
        ),
    ]
