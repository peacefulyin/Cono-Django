# Generated by Django 2.0.1 on 2018-02-16 16:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('relation', '0004_auto_20180217_0037'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='评论者'),
        ),
        migrations.AlterField(
            model_name='personrelations',
            name='act_one',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='act_person', to=settings.AUTH_USER_MODEL, verbose_name='行为方'),
        ),
        migrations.AlterField(
            model_name='personrelations',
            name='target_one',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='target_person', to=settings.AUTH_USER_MODEL, verbose_name='目标'),
        ),
        migrations.AlterField(
            model_name='tweetrelations',
            name='tweet',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tweet.Tweet', verbose_name='收藏文章'),
        ),
        migrations.AlterField(
            model_name='tweetrelations',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='收藏者'),
        ),
        migrations.AlterField(
            model_name='tweetsign',
            name='act_one',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sign_act_person', to=settings.AUTH_USER_MODEL, verbose_name='行为方'),
        ),
        migrations.AlterField(
            model_name='tweetsign',
            name='target_one',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sign_target_person', to=settings.AUTH_USER_MODEL, verbose_name='目标'),
        ),
        migrations.AlterField(
            model_name='tweetsign',
            name='tweet',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tweet.Tweet', verbose_name='文章'),
        ),
    ]
