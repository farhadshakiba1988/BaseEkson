# Generated by Django 5.0.2 on 2024-08-10 04:24

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
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
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Lead',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=15)),
                ('company', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=100)),
                ('date', models.DateField()),
                ('status', models.CharField(choices=[('won', 'سرنخ موفق'), ('lost', 'سرنخ ناموفق')], max_length=50)),
                ('additional_info_1', models.TextField(blank=True, null=True)),
                ('additional_info_2', models.TextField(blank=True, null=True)),
                ('approval_status', models.CharField(choices=[('approved', 'تایید شده'), ('rejected', 'رد شده'), ('pending', 'در انتظار')], default='pending', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='LeadInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=15)),
                ('company', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=100)),
                ('date', models.DateField()),
                ('status', models.CharField(choices=[('won', 'سرنخ موفق'), ('lost', 'سرنخ ناموفق')], max_length=50)),
                ('additional_info_1', models.TextField(blank=True, null=True)),
                ('additional_info_2', models.TextField(blank=True, null=True)),
                ('approval_status', models.CharField(choices=[('approved', 'تایید شده'), ('rejected', 'رد شده'), ('pending', 'در انتظار')], default='pending', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='TaskReport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True)),
                ('status', models.CharField(choices=[('primary', 'Primary'), ('secondary', 'Secondary'), ('success', 'Success'), ('danger', 'Danger'), ('warning', 'Warning'), ('info', 'Info'), ('pink', 'Pink')], max_length=10)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('full_name', models.CharField(max_length=255)),
                ('employee_number', models.CharField(max_length=50, unique=True)),
                ('role', models.CharField(choices=[('customer', 'Customer'), ('employee', 'Employee'), ('vendor', 'Vendor'), ('manager', 'Manager')], max_length=10)),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.department')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='person', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('notification_id', models.AutoField(primary_key=True, serialize=False)),
                ('message', models.TextField()),
                ('sent_date', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('read', 'Read'), ('unread', 'Unread')], max_length=10)),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.person')),
            ],
        ),
        migrations.CreateModel(
            name='CRMNum',
            fields=[
                ('crm_id', models.AutoField(primary_key=True, serialize=False)),
                ('crm_number', models.CharField(max_length=20, unique=True)),
                ('issue_date', models.DateTimeField(auto_now_add=True)),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.person')),
            ],
        ),
        migrations.CreateModel(
            name='Approval',
            fields=[
                ('approval_id', models.AutoField(primary_key=True, serialize=False)),
                ('related_entity', models.CharField(max_length=50)),
                ('entity_id', models.IntegerField()),
                ('status', models.CharField(choices=[('approved', 'Approved'), ('pending', 'Pending'), ('rejected', 'Rejected')], max_length=10)),
                ('approval_date', models.DateTimeField(auto_now_add=True)),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.person')),
            ],
        ),
        migrations.CreateModel(
            name='Sale',
            fields=[
                ('sale_id', models.AutoField(primary_key=True, serialize=False)),
                ('sale_date', models.DateTimeField(auto_now_add=True)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('description', models.TextField()),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.person')),
            ],
        ),
        migrations.CreateModel(
            name='SalesPersonReport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('person', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='sales_report', to='web.person')),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('task_id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('due_date', models.DateTimeField()),
                ('status', models.CharField(choices=[('completed', 'Completed'), ('in_progress', 'In Progress'), ('cancelled', 'Cancelled')], default='new', max_length=20)),
                ('progress', models.IntegerField(default=0)),
                ('priority', models.CharField(choices=[('low', 'Low'), ('medium', 'Medium'), ('high', 'High')], default='medium', max_length=10)),
                ('assignment_date', models.DateTimeField(auto_now_add=True)),
                ('assigned_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='assigned_tasks', to=settings.AUTH_USER_MODEL)),
                ('assigned_to', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='assigned_tasks', to='web.person')),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tasks', to='web.person')),
                ('tags', models.ManyToManyField(related_name='tasks', to='web.tag')),
                ('team_members', models.ManyToManyField(related_name='tasks', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]