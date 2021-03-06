# Generated by Django 3.1.4 on 2020-12-29 10:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Homework',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=200)),
                ('deadline', models.IntegerField(default=7)),
                ('created', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='HomeworkResult',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('solution', models.CharField(max_length=2000)),
                ('created', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_name', models.CharField(max_length=200)),
                ('first_name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_name', models.CharField(max_length=200)),
                ('first_name', models.CharField(max_length=200)),
                ('homework_done', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.homeworkresult')),
            ],
        ),
        migrations.AddField(
            model_name='homeworkresult',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.student'),
        ),
        migrations.AddField(
            model_name='homeworkresult',
            name='homework',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.homework'),
        ),
    ]
