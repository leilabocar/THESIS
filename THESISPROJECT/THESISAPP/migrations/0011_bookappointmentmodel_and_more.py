# Generated by Django 4.0.2 on 2022-11-01 10:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('THESISAPP', '0010_buyersformmodel_alter_applicationformmodel_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='BookAppointmentModel',
            fields=[
                ('id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL, verbose_name='id')),
                ('reason', models.CharField(max_length=250, null=True, verbose_name='reason')),
                ('fullname', models.CharField(max_length=250, null=True, verbose_name='fullname')),
                ('contacts', models.CharField(max_length=11, null=True, verbose_name='contacts')),
                ('email', models.CharField(max_length=250, null=True, verbose_name='email')),
                ('date', models.DateField(null=True, verbose_name='date')),
            ],
        ),
        migrations.AlterField(
            model_name='applicationformmodel',
            name='email',
            field=models.EmailField(max_length=99, null=True, verbose_name='email'),
        ),
        migrations.AlterField(
            model_name='buyersformmodel',
            name='email',
            field=models.EmailField(max_length=99, null=True, verbose_name='email'),
        ),
    ]
