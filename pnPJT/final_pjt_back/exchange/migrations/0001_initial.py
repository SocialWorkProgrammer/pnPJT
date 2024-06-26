# Generated by Django 4.2.8 on 2024-05-21 04:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Exchange',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cur_unit', models.CharField(max_length=30)),
                ('cur_nm', models.CharField(max_length=60)),
                ('ttb', models.CharField(max_length=40)),
                ('tts', models.CharField(max_length=40)),
                ('deal_bas_r', models.CharField(max_length=20)),
                ('bkpr', models.CharField(max_length=20)),
                ('yy_efee_r', models.CharField(max_length=20)),
                ('ten_dd_efee_r', models.CharField(max_length=20)),
                ('kftc_deal_bas_r', models.CharField(max_length=30)),
                ('kftc_bkpr', models.CharField(max_length=30)),
            ],
        ),
    ]
