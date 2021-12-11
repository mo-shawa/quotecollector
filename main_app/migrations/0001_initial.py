# Generated by Django 3.2.9 on 2021-12-10 21:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Quote',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quote', models.TextField()),
                ('author', models.CharField(max_length=150)),
                ('categories', models.ManyToManyField(to='main_app.Category')),
            ],
        ),
        migrations.CreateModel(
            name='Fan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('date', models.DateField(verbose_name='Fan Acquisition Date')),
                ('fantype', models.CharField(choices=[('C', 'Casual'), ('S', 'Stan'), ('R', 'Rabid')], default='C', max_length=1)),
                ('quote', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.quote')),
            ],
            options={
                'ordering': ['-fantype'],
            },
        ),
    ]
