# Generated by Django 3.1.5 on 2021-01-12 15:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bank', '0002_wallet_money'),
    ]

    operations = [
        migrations.CreateModel(
            name='Loglist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('money_delta', models.DecimalField(decimal_places=2, default=0.0, max_digits=30)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bank.client')),
                ('wallet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bank.wallet')),
            ],
        ),
    ]
