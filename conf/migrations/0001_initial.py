# Generated by Django 5.0.2 on 2024-07-29 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CRMEntry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('crm_no', models.IntegerField()),
                ('expert_name', models.CharField(max_length=255)),
                ('expert_email', models.EmailField(max_length=254)),
                ('company_phone', models.CharField(max_length=20)),
                ('company_name', models.CharField(max_length=255)),
                ('location', models.CharField(max_length=255)),
                ('delivery_date', models.DateField()),
                ('status', models.CharField(max_length=50)),
            ],
        ),
    ]