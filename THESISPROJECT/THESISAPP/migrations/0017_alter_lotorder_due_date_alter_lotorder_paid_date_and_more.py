# Generated by Django 4.0.2 on 2022-11-19 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('THESISAPP', '0016_user_address_user_age_user_contacts_user_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lotorder',
            name='due_date',
            field=models.DateField(null=True, verbose_name='due date'),
        ),
        migrations.AlterField(
            model_name='lotorder',
            name='paid_date',
            field=models.DateField(null=True, verbose_name='paid date'),
        ),
        migrations.AlterField(
            model_name='product',
            name='date_created',
            field=models.DateField(auto_now_add=True, null=True, verbose_name='date created'),
        ),
    ]
