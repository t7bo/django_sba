# Generated by Django 4.2.10 on 2024-02-26 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prediction', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loanapplication',
            name='create_job',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='loanapplication',
            name='no_emp',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='loanapplication',
            name='retained_job',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='loanapplication',
            name='term',
            field=models.IntegerField(),
        ),
    ]