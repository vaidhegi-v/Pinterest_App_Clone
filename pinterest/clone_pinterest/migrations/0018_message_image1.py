# Generated by Django 4.2.4 on 2023-11-09 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clone_pinterest', '0017_message_update'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='image1',
            field=models.ImageField(blank=True, null=True, upload_to='msgs'),
        ),
    ]
