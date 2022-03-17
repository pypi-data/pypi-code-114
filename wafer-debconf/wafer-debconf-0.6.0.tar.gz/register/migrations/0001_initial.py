# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-02-04 19:33
from __future__ import unicode_literals

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
            name='Accomm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('requirements', models.TextField(blank=True)),
                ('childcare', models.BooleanField()),
                ('childcare_needs', models.TextField(blank=True)),
                ('childcare_details', models.TextField(blank=True)),
                ('special_needs', models.TextField(blank=True)),
                ('family_usernames', models.TextField(blank=True)),
                ('room', models.CharField(blank=True, default='', max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='AccommNight',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(unique=True)),
            ],
            options={
                'ordering': ['date'],
            },
        ),
        migrations.CreateModel(
            name='Attendee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nametag_2', models.CharField(blank=True, max_length=50)),
                ('nametag_3', models.CharField(blank=True, max_length=50)),
                ('emergency_contact', models.TextField(blank=True)),
                ('announce_me', models.BooleanField()),
                ('register_announce', models.BooleanField()),
                ('register_discuss', models.BooleanField()),
                ('coc_ack', models.BooleanField(default=False)),
                ('fee', models.CharField(blank=True, max_length=5)),
                ('arrival', models.DateTimeField(blank=True, null=True)),
                ('departure', models.DateTimeField(blank=True, null=True)),
                ('final_dates', models.BooleanField(default=False)),
                ('reconfirm', models.BooleanField(default=False)),
                ('t_shirt_size', models.CharField(blank=True, max_length=8)),
                ('shoe_size', models.CharField(blank=True, max_length=8)),
                ('gender', models.CharField(blank=True, max_length=1)),
                ('country', models.CharField(blank=True, max_length=2)),
                ('languages', models.CharField(blank=True, max_length=50)),
                ('pgp_fingerprints', models.TextField(blank=True)),
                ('invoiced_entity', models.TextField(blank=True)),
                ('billing_address', models.TextField(blank=True)),
                ('notes', models.TextField(blank=True)),
                ('completed_register_steps', models.IntegerField(default=0)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, related_name='attendee', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('diet', models.CharField(blank=True, max_length=16)),
                ('special_diet', models.TextField(blank=True)),
                ('attendee', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='food', to='register.Attendee')),
            ],
        ),
        migrations.CreateModel(
            name='Meal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(db_index=True)),
                ('meal', models.CharField(max_length=16)),
            ],
            options={
                'ordering': ['date'],
            },
        ),
        migrations.CreateModel(
            name='Queue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=32)),
                ('size', models.IntegerField(null=True)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='QueueSlot',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('attendee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='queues', to='register.Attendee')),
                ('queue', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='slots', to='register.Queue')),
            ],
            options={
                'ordering': ['timestamp'],
            },
        ),
        migrations.AlterUniqueTogether(
            name='meal',
            unique_together=set([('date', 'meal')]),
        ),
        migrations.AddField(
            model_name='food',
            name='meals',
            field=models.ManyToManyField(to='register.Meal'),
        ),
        migrations.AddField(
            model_name='accomm',
            name='attendee',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='accomm', to='register.Attendee'),
        ),
        migrations.AddField(
            model_name='accomm',
            name='nights',
            field=models.ManyToManyField(to='register.AccommNight'),
        ),
        migrations.AlterUniqueTogether(
            name='queueslot',
            unique_together=set([('attendee', 'queue')]),
        ),
    ]
