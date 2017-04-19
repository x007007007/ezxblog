# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-19 15:25
from __future__ import unicode_literals

import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0008_alter_user_username_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=30, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'abstract': False,
                'verbose_name_plural': 'users',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('article', 'article'), ('comment', 'comment')], max_length=32)),
                ('message', models.TextField(max_length=1024)),
                ('on_comment', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ezxblogcore.Comment')),
            ],
        ),
        migrations.CreateModel(
            name='CreateModifyTime',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_time', models.DateTimeField(auto_now_add=True, null=True)),
                ('modified_time', models.DateTimeField(auto_now=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('createmodifytime_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='ezxblogcore.CreateModifyTime')),
                ('lang', models.CharField(blank=True, choices=[('el', 'el'), ('lt', 'lt'), ('gl', 'gl'), ('eu', 'eu'), ('nl', 'nl'), ('ga', 'ga'), ('ca', 'ca'), ('km', 'km'), ('de', 'de'), ('en-gb', 'en-gb'), ('io', 'io'), ('zh-tw', 'zh-tw'), ('is', 'is'), ('zh-hk', 'zh-hk'), ('hr', 'hr'), ('es', 'es'), ('nn', 'nn'), ('sw', 'sw'), ('es-ar', 'es-ar'), ('hsb', 'hsb'), ('et', 'et'), ('ja', 'ja'), ('lb', 'lb'), ('kk', 'kk'), ('tr', 'tr'), ('nb', 'nb'), ('ne', 'ne'), ('mr', 'mr'), ('uk', 'uk'), ('gd', 'gd'), ('be', 'be'), ('br', 'br'), ('sq', 'sq'), ('fr', 'fr'), ('az', 'az'), ('en', 'en'), ('fy', 'fy'), ('lv', 'lv'), ('sv', 'sv'), ('cs', 'cs'), ('os', 'os'), ('mn', 'mn'), ('tt', 'tt'), ('he', 'he'), ('hu', 'hu'), ('zh-hans', 'zh-hans'), ('no', 'no'), ('hi', 'hi'), ('fa', 'fa'), ('pl', 'pl'), ('my', 'my'), ('fi', 'fi'), ('da', 'da'), ('udm', 'udm'), ('zh-sg', 'zh-sg'), ('es-ni', 'es-ni'), ('zh-hant', 'zh-hant'), ('cy', 'cy'), ('ko', 'ko'), ('es-ve', 'es-ve'), ('ru', 'ru'), ('it', 'it'), ('ar', 'ar'), ('ml', 'ml'), ('ur', 'ur'), ('kn', 'kn'), ('ro', 'ro'), ('af', 'af'), ('sr', 'sr'), ('bg', 'bg'), ('bs', 'bs'), ('ka', 'ka'), ('zh-my', 'zh-my'), ('sr-latn', 'sr-latn'), ('pt', 'pt'), ('dsb', 'dsb'), ('zh-mo', 'zh-mo'), ('te', 'te'), ('id', 'id'), ('en-au', 'en-au'), ('eo', 'eo'), ('es-co', 'es-co'), ('es-mx', 'es-mx'), ('pa', 'pa'), ('ia', 'ia'), ('sk', 'sk'), ('ast', 'ast'), ('pt-br', 'pt-br'), ('ta', 'ta'), ('th', 'th'), ('bn', 'bn'), ('mk', 'mk'), ('vi', 'vi'), ('zh-cn', 'zh-cn'), ('sl', 'sl')], max_length=16, null=True)),
                ('name', models.CharField(max_length=254)),
                ('title', models.CharField(blank=True, max_length=254, null=True)),
                ('content_type', models.CharField(choices=[('html', 'html'), ('md', 'md')], max_length=16)),
                ('content', models.TextField()),
                ('description', models.TextField(blank=True, null=True)),
            ],
            bases=('ezxblogcore.createmodifytime',),
        ),
        migrations.CreateModel(
            name='Media',
            fields=[
                ('createmodifytime_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='ezxblogcore.CreateModifyTime')),
                ('name', models.CharField(max_length=254)),
                ('type', models.CharField(db_index=True, max_length=32)),
                ('file', models.FileField(upload_to='media/%Y/%m/%d/')),
            ],
            bases=('ezxblogcore.createmodifytime',),
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('createmodifytime_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='ezxblogcore.CreateModifyTime')),
                ('name', models.CharField(db_index=True, max_length=254)),
            ],
            bases=('ezxblogcore.createmodifytime',),
        ),
        migrations.CreateModel(
            name='Url',
            fields=[
                ('createmodifytime_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='ezxblogcore.CreateModifyTime')),
                ('path', models.CharField(db_index=True, max_length=254, unique=True)),
                ('type', models.CharField(choices=[('article', 'article')], max_length=32)),
                ('full_url', models.TextField(blank=True, max_length=2046, null=True)),
            ],
            bases=('ezxblogcore.createmodifytime',),
        ),
        migrations.AddField(
            model_name='media',
            name='tags',
            field=models.ManyToManyField(to='ezxblogcore.Tag'),
        ),
        migrations.AddField(
            model_name='comment',
            name='on_article',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ezxblogcore.Article'),
        ),
        migrations.AddField(
            model_name='article',
            name='medium',
            field=models.ManyToManyField(to='ezxblogcore.Media'),
        ),
        migrations.AddField(
            model_name='article',
            name='tags',
            field=models.ManyToManyField(to='ezxblogcore.Tag'),
        ),
        migrations.AlterUniqueTogether(
            name='article',
            unique_together=set([('lang', 'name')]),
        ),
    ]