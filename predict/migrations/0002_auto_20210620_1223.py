# Generated by Django 3.2 on 2021-06-20 11:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('predict', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='isSubscribed',
            field=models.BooleanField(default=False),
        ),
        migrations.CreateModel(
            name='myPrediction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('first', models.CharField(max_length=30)),
                ('second', models.CharField(max_length=30)),
                ('third', models.CharField(max_length=30)),
                ('fourth', models.CharField(max_length=30)),
                ('fifth', models.CharField(max_length=30)),
                ('sixth', models.CharField(max_length=30)),
                ('seventh', models.CharField(max_length=30)),
                ('eighth', models.CharField(max_length=30)),
                ('ninth', models.CharField(max_length=30)),
                ('tenth', models.CharField(max_length=30)),
                ('eleventh', models.CharField(max_length=30)),
                ('twelfth', models.CharField(max_length=30)),
                ('thirteenth', models.CharField(max_length=30)),
                ('fourteenth', models.CharField(max_length=30)),
                ('fifteenth', models.CharField(max_length=30)),
                ('sixteenth', models.CharField(max_length=30)),
                ('seventeenth', models.CharField(max_length=30)),
                ('eighteenth', models.CharField(max_length=30)),
                ('nineteenth', models.CharField(max_length=30)),
                ('twentieth', models.CharField(max_length=30)),
                ('currentScore', models.IntegerField(default=0)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='leagueMember',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=30)),
                ('leagueName', models.CharField(max_length=30)),
                ('isManager', models.BooleanField(default=False)),
                ('userid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='leagueList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('leagueName', models.CharField(max_length=30, unique=True)),
                ('numbMembers', models.IntegerField(default=1)),
                ('key', models.CharField(max_length=6)),
                ('userManager', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
