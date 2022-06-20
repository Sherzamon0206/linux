# Generated by Django 4.0.5 on 2022-06-20 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AdminPanel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200, null=True, verbose_name='Admin ismi')),
                ('admin_id', models.IntegerField(blank=True, null=True, verbose_name='telegram id')),
            ],
            options={
                'verbose_name': 'Admin',
                'verbose_name_plural': 'Admin_panel',
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exeterenal_id', models.PositiveIntegerField(verbose_name='user id')),
                ('username', models.TextField(blank=True, null=True, verbose_name='username')),
                ('f_name', models.TextField(verbose_name='First_name')),
                ('l_name', models.TextField(null=True, verbose_name='Lastname')),
            ],
            options={
                'verbose_name': 'Profili',
            },
        ),
    ]