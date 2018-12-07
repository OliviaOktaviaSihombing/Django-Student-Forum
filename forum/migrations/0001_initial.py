# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-10 13:53
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='t_grup',
            fields=[
                ('id_grup', models.IntegerField(primary_key=True, serialize=False)),
                ('nama_grup', models.CharField(max_length=255)),
                ('deskripsi_grup', models.TextField()),
                ('jumlah_topik_grup', models.IntegerField()),
                ('jumlah_anggota_grup', models.IntegerField()),
                ('avatar_grup', models.CharField(max_length=255)),
                ('date_created_grup', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='t_kategori',
            fields=[
                ('id_kategori', models.IntegerField(primary_key=True, serialize=False)),
                ('judul_kategori', models.CharField(max_length=255)),
                ('deskripsi_kategori', models.TextField()),
                ('date_created_kategori', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='t_tipe_kategori',
            fields=[
                ('id_tipe_kategori', models.IntegerField(primary_key=True, serialize=False)),
                ('nama_kategori', models.CharField(max_length=255)),
                ('deskripsi_tipe_kategori', models.TextField()),
                ('date_created_tipe_kategori', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='t_tipe_notifikasi',
            fields=[
                ('id_tipe_notifikasi', models.IntegerField(primary_key=True, serialize=False)),
                ('nama_tipe_notifikasi', models.CharField(max_length=255)),
                ('date_created_tipe_notifikasi', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='t_topik',
            fields=[
                ('id_topik', models.IntegerField(primary_key=True, serialize=False)),
                ('judul_topik', models.CharField(max_length=255)),
                ('isi_topik', models.TextField()),
                ('jumlah_komentar_topik', models.IntegerField()),
                ('tags', models.TextField(null=True)),
                ('date_created_topik', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='t_user',
            fields=[
                ('email', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('full_name', models.CharField(max_length=200)),
                ('password', models.CharField(max_length=200)),
                ('verified', models.BooleanField(default=False)),
                ('jumlah_subscriber', models.IntegerField(default=0)),
                ('jumlah_topik_user', models.IntegerField(default=0)),
                ('avatar_user', models.CharField(default='user_default.png', max_length=50)),
                ('fakultas', models.CharField(max_length=100)),
                ('jurusan', models.CharField(max_length=100)),
                ('klub', models.CharField(max_length=255, null=True)),
                ('date_created_user', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='t_user_grup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='forum.t_user')),
                ('id_grup', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='forum.t_grup')),
            ],
        ),
        migrations.AddField(
            model_name='t_topik',
            name='email',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='forum.t_user'),
        ),
        migrations.AddField(
            model_name='t_topik',
            name='id_grup',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='forum.t_grup'),
        ),
        migrations.AddField(
            model_name='t_topik',
            name='id_kategori',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='forum.t_kategori'),
        ),
        migrations.AddField(
            model_name='t_kategori',
            name='id_tipe_kategori',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='forum.t_tipe_kategori'),
        ),
        migrations.AddField(
            model_name='t_grup',
            name='moderator',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='forum.t_user'),
        ),
    ]