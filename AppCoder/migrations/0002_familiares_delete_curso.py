# Generated by Django 4.0.4 on 2022-05-29 21:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppCoder', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Familiares',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40)),
                ('apellido', models.CharField(max_length=40)),
                ('fecha', models.CharField(max_length=40)),
                ('edad', models.IntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='Curso',
        ),
    ]
