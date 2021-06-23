# Generated by Django 3.2 on 2021-06-19 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0006_rename_username1_fit_username'),
    ]

    operations = [
        migrations.CreateModel(
            name='Registeration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=20)),
                ('lastname', models.CharField(max_length=20)),
                ('age', models.IntegerField(max_length=20)),
                ('gender', models.CharField(choices=[('MALE', 'MALE'), ('FEMALE', 'FEMALE'), ('OTHERS', 'OTHERS')], default='MALE', max_length=20)),
                ('phonenumber', models.IntegerField(max_length=10)),
                ('offer', models.CharField(choices=[('Gold', 'Gold  ₹1999'), ('Silver', 'Silver  ₹3999'), ('Bronze', 'Bronze  ₹5999')], default='Gold  ₹1999', max_length=20)),
                ('modeofpayment', models.CharField(choices=[('G-Pay', 'G-Pay'), ('PayPal', 'PayPal'), ('Paytm', 'Paytm')], default='G-Pay', max_length=20)),
            ],
        ),
    ]
