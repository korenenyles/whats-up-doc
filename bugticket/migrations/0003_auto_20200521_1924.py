# Generated by Django 3.0.6 on 2020-05-21 19:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bugticket', '0002_auto_20200521_1652'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='ticket_status',
            field=models.CharField(choices=[('NEW', 'New'), ('IN PROGRESS', 'In Progress'), ('DONE', 'Done'), ('INVALID', 'Invalid'), ('NONE', 'None')], default='NEW', max_length=15),
        ),
    ]
