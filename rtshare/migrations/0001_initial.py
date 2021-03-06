# Generated by Django 3.0.5 on 2020-05-02 11:10

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Share',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('uid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('is_locked', models.BooleanField(default=False)),
                ('is_edit_allowed', models.BooleanField(default=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
