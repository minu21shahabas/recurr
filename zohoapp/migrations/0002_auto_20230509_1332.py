# Generated by Django 3.2.18 on 2023-05-09 13:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('zohoapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('term', models.TextField(max_length=255)),
                ('days', models.TextField(max_length=255)),
            ],
        ),
        migrations.AlterField(
            model_name='invoice',
            name='terms',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='zohoapp.payment'),
        ),
    ]
