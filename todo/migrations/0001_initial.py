# Generated by Django 3.1.12 on 2021-09-17 22:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import tasks.utils


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('detail', models.TextField(blank=True)),
                ('completed', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('due_by', models.DateTimeField(default=tasks.utils.next_day)),
                ('author', models.ForeignKey(default='auth.User', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]