# Generated by Django 4.2.10 on 2024-04-03 19:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('license_app', '0003_admin_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='admin_user',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='admin_user',
            name='is_staff',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='admin_user',
            name='is_superuser',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='admin_user',
            name='last_login',
            field=models.DateTimeField(blank=True, null=True, verbose_name='last login'),
        ),
        migrations.AlterField(
            model_name='admin_user',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
        migrations.AlterField(
            model_name='admin_user',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='admin_user',
            name='password',
            field=models.CharField(max_length=128, verbose_name='password'),
        ),
    ]