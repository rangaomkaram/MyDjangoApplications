# Generated by Django 4.0.4 on 2022-06-17 04:41

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('projectweb', '0005_review_created_review_updated_alter_review_id_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('name', models.CharField(max_length=200)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AddField(
            model_name='project',
            name='tags',
            field=models.ManyToManyField(blank=True, to='projectweb.tag'),
        ),
    ]