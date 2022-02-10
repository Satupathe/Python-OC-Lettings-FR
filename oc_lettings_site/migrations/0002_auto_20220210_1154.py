# Generated by Django 3.0 on 2022-02-10 10:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('oc_lettings_site', '0001_initial'),
    ]

    operations = [
        migrations.SeparateDatabaseAndState(
            state_operations=[
                migrations.DeleteModel(
                    name='Address',
                ),
                migrations.DeleteModel(
                    name='Letting'
                )
            ],
            database_operations=[
                migrations.AlterModelTable(
                    name='Address',
                    table='lettings_Address',
                ),
                migrations.AlterModelTable(
                    name='Letting',
                    table='lettings_Letting',
                ),
            ]
        ),
    ]   

