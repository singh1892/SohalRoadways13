# Generated by Django 3.2 on 2021-04-25 04:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('collectionDt', models.DateField()),
                ('DispatchDt', models.DateField()),
                ('ShipNo', models.IntegerField()),
                ('SDMNo', models.IntegerField()),
                ('ModelNo', models.TextField()),
                ('ChassisNo', models.TextField()),
                ('From', models.TextField()),
                ('To', models.TextField()),
                ('DealerName', models.TextField()),
                ('DelDate', models.DateField()),
                ('Status', models.TextField()),
                ('Drivername', models.TextField()),
                ('contact', models.IntegerField()),
                ('Distance', models.IntegerField()),
                ('Average', models.FloatField()),
                ('HSDpump', models.FloatField()),
                ('CashOnHand', models.FloatField()),
                ('DeiselDRate', models.FloatField()),
                ('TotalDeisel', models.FloatField()),
                ('DriverPayment', models.FloatField()),
                ('Tax', models.FloatField()),
                ('OtherExpenses', models.FloatField()),
                ('TotalBillAmnt', models.FloatField()),
                ('Taxableamnt', models.FloatField()),
                ('Igst', models.FloatField()),
                ('TotalBillingAmount', models.FloatField()),
                ('Poddt', models.DateField()),
                ('BillNo', models.TextField()),
                ('BillDt', models.DateField()),
            ],
        ),
    ]