# Generated by Django 2.0 on 2019-12-05 07:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('author_name', models.CharField(max_length=200, primary_key=True, serialize=False)),
                ('author_email', models.EmailField(max_length=254, unique=True)),
                ('author_phone', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('book_id', models.AutoField(primary_key=True, serialize=False)),
                ('book_name', models.CharField(max_length=200)),
                ('price', models.FloatField(default=0)),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='front.Author')),
            ],
        ),
        migrations.CreateModel(
            name='Publisher',
            fields=[
                ('pub_name', models.CharField(max_length=200, primary_key=True, serialize=False)),
                ('address', models.CharField(max_length=200)),
                ('pub_email', models.EmailField(max_length=254, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='book',
            name='publisher',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='front.Publisher'),
        ),
    ]
