# Generated by Django 5.1.5 on 2025-02-05 15:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hr', '0004_alter_employee_department'),
    ]

    operations = [
        migrations.CreateModel(
            name='Compensation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.AlterField(
            model_name='employee',
            name='department',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='employ_boy', to='hr.department'),
        ),
        migrations.AddField(
            model_name='employee',
            name='compensation',
            field=models.ManyToManyField(to='hr.compensation'),
        ),
    ]
