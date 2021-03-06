# Generated by Django 2.0.1 on 2018-02-13 03:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('relation', '0002_auto_20180212_1357'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='personrelations',
            name='is_friend',
        ),
        migrations.AddField(
            model_name='personrelations',
            name='is_follow',
            field=models.BooleanField(choices=[(False, '否'), (True, '是')], default=False, verbose_name='是否关注'),
        ),
        migrations.AlterField(
            model_name='personrelations',
            name='is_block',
            field=models.BooleanField(choices=[(False, '否'), (True, '是')], default=False, verbose_name='是否屏蔽'),
        ),
    ]
