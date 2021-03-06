# Generated by Django 2.0.1 on 2018-02-19 05:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('relation', '0005_auto_20180217_0042'),
    ]

    operations = [
        migrations.CreateModel(
            name='CommentSign',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(blank=True, max_length=1000, null=True, verbose_name='文字')),
                ('create_time', models.DateTimeField(auto_now=True, verbose_name='创建时间')),
                ('act_one', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comment_sign_act_person', to=settings.AUTH_USER_MODEL, verbose_name='行为方')),
                ('comment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='relation.Comment', verbose_name='评论')),
                ('target_one', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comment_sign_target_person', to=settings.AUTH_USER_MODEL, verbose_name='目标')),
            ],
            options={
                'verbose_name': '评论标记',
                'verbose_name_plural': '评论标记',
                'db_table': 'comment_sign',
            },
        ),
        migrations.AlterField(
            model_name='tweetsign',
            name='act_one',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tweet_sign_act_person', to=settings.AUTH_USER_MODEL, verbose_name='行为方'),
        ),
        migrations.AlterField(
            model_name='tweetsign',
            name='target_one',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tweet_sign_target_person', to=settings.AUTH_USER_MODEL, verbose_name='目标'),
        ),
    ]
