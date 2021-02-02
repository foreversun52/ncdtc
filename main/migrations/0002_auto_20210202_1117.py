# Generated by Django 2.1.15 on 2021-02-02 03:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Submit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ncRNA_Name', models.CharField(max_length=200)),
                ('ncRNA_ID', models.CharField(max_length=200)),
                ('Disease', models.CharField(max_length=200)),
                ('Drug_Name', models.CharField(max_length=200, null=True)),
                ('Drug_ID', models.CharField(max_length=200, null=True)),
                ('Drug_Response', models.CharField(max_length=200, null=True)),
                ('Expression_pattern', models.CharField(max_length=200)),
                ('PubMed_ID', models.CharField(max_length=200)),
                ('Email', models.CharField(max_length=200)),
                ('Description', models.CharField(max_length=200)),
            ],
            options={
                'db_table': '提交信息表',
            },
        ),
        migrations.AlterModelTable(
            name='noncorna',
            table='NoncoRNA',
        ),
    ]