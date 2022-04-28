# Generated by Django 4.0.3 on 2022-04-19 17:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Site', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Grading',
            fields=[
                ('ide', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('review_text', models.TextField(verbose_name='sharh qoldirish')),
                ('grade', models.IntegerField(blank=True, choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], null=True, verbose_name='baho')),
                ('otel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Site.hotel', verbose_name='Otel nomi')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='foydalanuvchi')),
            ],
        ),
        migrations.AddField(
            model_name='hotel',
            name='grade',
            field=models.ManyToManyField(to='Site.grading', verbose_name='baho'),
        ),
    ]
