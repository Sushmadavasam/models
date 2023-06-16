# Generated by Django 4.2.1 on 2023-06-16 07:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='emp',
            name='id',
        ),
        migrations.AlterField(
            model_name='department',
            name='DEPTNAME',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='department',
            name='DEPTNO',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='emp',
            name='EMPNO',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
