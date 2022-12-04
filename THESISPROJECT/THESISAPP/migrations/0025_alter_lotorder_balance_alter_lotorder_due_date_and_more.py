# Generated by Django 4.0.2 on 2022-12-03 05:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('THESISAPP', '0024_alter_lotorder_balance_alter_lotorder_customer_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lotorder',
            name='balance',
            field=models.FloatField(blank=True, default=None, null=True, verbose_name='balance'),
        ),
        migrations.AlterField(
            model_name='lotorder',
            name='due_date',
            field=models.DateField(blank=True, default=None, null=True, verbose_name='due date'),
        ),
        migrations.AlterField(
            model_name='lotorder',
            name='paid_date',
            field=models.DateField(blank=True, default=None, null=True, verbose_name='paid date'),
        ),
        migrations.AlterField(
            model_name='lotorder',
            name='pay',
            field=models.FloatField(blank=True, default=None, null=True, verbose_name='pay'),
        ),
        migrations.AlterField(
            model_name='lotorder',
            name='product',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='THESISAPP.product', verbose_name='product'),
        ),
        migrations.AlterField(
            model_name='lotorder',
            name='status',
            field=models.CharField(blank=True, choices=[('Fully Paid', 'Fully Paid'), ('Partially Paid', 'Partially Paid')], default=None, max_length=200, null=True, verbose_name='status'),
        ),
        migrations.AlterField(
            model_name='paymenthistory',
            name='balance',
            field=models.FloatField(blank=True, default=None, null=True, verbose_name='balance'),
        ),
        migrations.AlterField(
            model_name='paymenthistory',
            name='customer',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='customer'),
        ),
        migrations.AlterField(
            model_name='paymenthistory',
            name='due_date',
            field=models.DateField(blank=True, default=None, null=True, verbose_name='due date'),
        ),
        migrations.AlterField(
            model_name='paymenthistory',
            name='paid_date',
            field=models.DateField(blank=True, default=None, null=True, verbose_name='paid date'),
        ),
        migrations.AlterField(
            model_name='paymenthistory',
            name='pay',
            field=models.FloatField(blank=True, default=None, null=True, verbose_name='pay'),
        ),
        migrations.AlterField(
            model_name='paymenthistory',
            name='product',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='THESISAPP.product', verbose_name='product'),
        ),
        migrations.AlterField(
            model_name='paymenthistory',
            name='status',
            field=models.CharField(blank=True, choices=[('Fully Paid', 'Fully Paid'), ('Partially Paid', 'Partially Paid')], default=None, max_length=200, null=True, verbose_name='status'),
        ),
        migrations.AlterField(
            model_name='paymenthistory',
            name='terms',
            field=models.CharField(blank=True, choices=[('Cash', 'Cash'), ('1 Year', '1 Year'), ('2 Years', '2 Years'), ('3 Years', '3 Years'), ('Full Down', 'Full Down'), ('Reservation', 'Reservation')], max_length=50, null=True, verbose_name='terms'),
        ),
    ]