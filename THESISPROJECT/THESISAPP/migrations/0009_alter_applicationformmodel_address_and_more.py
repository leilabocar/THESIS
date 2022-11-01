# Generated by Django 4.0.2 on 2022-11-01 07:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('THESISAPP', '0008_alter_applicationformmodel_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applicationformmodel',
            name='address',
            field=models.CharField(max_length=99, null=True, verbose_name='address'),
        ),
        migrations.AlterField(
            model_name='applicationformmodel',
            name='age',
            field=models.IntegerField(null=True, verbose_name='age'),
        ),
        migrations.AlterField(
            model_name='applicationformmodel',
            name='block',
            field=models.CharField(max_length=30, null=True, verbose_name='block'),
        ),
        migrations.AlterField(
            model_name='applicationformmodel',
            name='contacts',
            field=models.CharField(max_length=11, null=True, verbose_name='contacts'),
        ),
        migrations.AlterField(
            model_name='applicationformmodel',
            name='date',
            field=models.DateField(null=True, verbose_name='date'),
        ),
        migrations.AlterField(
            model_name='applicationformmodel',
            name='email',
            field=models.EmailField(max_length=99, null=True, verbose_name='email'),
        ),
        migrations.AlterField(
            model_name='applicationformmodel',
            name='fullname',
            field=models.CharField(max_length=99, null=True, verbose_name='fullname'),
        ),
        migrations.AlterField(
            model_name='applicationformmodel',
            name='gender',
            field=models.CharField(max_length=30, null=True, verbose_name='gender'),
        ),
        migrations.AlterField(
            model_name='applicationformmodel',
            name='lotno',
            field=models.CharField(max_length=30, null=True, verbose_name='lot_no.'),
        ),
        migrations.AlterField(
            model_name='applicationformmodel',
            name='phase',
            field=models.CharField(max_length=30, null=True, verbose_name='phase'),
        ),
    ]