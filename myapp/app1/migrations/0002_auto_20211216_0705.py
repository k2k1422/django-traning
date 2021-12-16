# Generated by Django 3.1.5 on 2021-12-16 07:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.AutoField(db_column='book_id', editable=False, primary_key=True, serialize=False)),
                ('author_name', models.CharField(db_column='author_name', max_length=64)),
                ('gener', models.CharField(db_column='gener', max_length=64)),
                ('publication', models.CharField(db_column='publication', max_length=64)),
                ('issued_to', models.ForeignKey(db_column='issued_to', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'book',
            },
        ),
    ]
