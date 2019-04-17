# Generated by Django 2.1.7 on 2019-03-27 09:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('engineer', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notifyinfo',
            name='errortype',
            field=models.CharField(choices=[('Car', '车辆违规信息'), ('Person', '人员违规信息'), ('Other', '其他违规信息')], max_length=20),
        ),
        migrations.AlterModelTable(
            name='notifyinfo',
            table='notifyinfo',
        ),
        migrations.AlterModelTable(
            name='pic',
            table='pic',
        ),
        migrations.AlterModelTable(
            name='safeuser',
            table='safeuser',
        ),
        migrations.AlterModelTable(
            name='userinfo',
            table='userinfo',
        ),
        migrations.AlterModelTable(
            name='work',
            table='work',
        ),
    ]
