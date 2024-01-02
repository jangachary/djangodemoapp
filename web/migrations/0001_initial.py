# Generated by Django 5.0.1 on 2024-01-02 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MyModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('role', models.CharField(choices=[('admin', 'Admin'), ('user', 'User')], default=None, max_length=10)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
    ]