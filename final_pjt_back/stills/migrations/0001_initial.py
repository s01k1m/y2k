# Generated by Django 3.2.18 on 2023-05-19 11:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('movie_title', models.IntegerField()),
                ('movie_id', models.CharField(max_length=20)),
                ('overview', models.TextField()),
                ('movie_release_date', models.DateField()),
                ('genre', models.CharField(blank=True, max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Still',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('still_image', models.ImageField(null=True, upload_to='')),
                ('still_color', models.CharField(blank=True, max_length=6)),
                ('movie_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stills.movie')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Collection',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('collection_name', models.CharField(max_length=20)),
                ('stills', models.ManyToManyField(related_name='stills', to='stills.Still')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
