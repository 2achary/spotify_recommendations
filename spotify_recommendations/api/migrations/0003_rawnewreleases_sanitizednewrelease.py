# Generated by Django 3.0.3 on 2020-02-23 15:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_token_token_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='RawNewReleases',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('response', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='SanitizedNewRelease',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('release_name', models.CharField(max_length=255)),
                ('artists', models.CharField(max_length=255)),
                ('raw_response', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.RawNewReleases')),
            ],
        ),
    ]