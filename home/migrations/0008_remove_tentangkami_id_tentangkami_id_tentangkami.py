# Generated by Django 5.2 on 2025-04-30 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_remove_tentangkami_id_tentangkami_tentangkami_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tentangkami',
            name='id',
        ),
        migrations.AddField(
            model_name='tentangkami',
            name='id_tentangkami',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
