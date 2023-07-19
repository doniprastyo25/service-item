# Generated by Django 4.2.3 on 2023-07-11 10:46

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ItemModel',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=60)),
                ('item_type', models.CharField(choices=[('hats', 'hats'), ('tops', 'tops'), ('shorts', 'shorts')], max_length=9)),
                ('regular_price', models.IntegerField()),
                ('vip_price', models.IntegerField(null=True)),
                ('wholesale_price', models.IntegerField(null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]