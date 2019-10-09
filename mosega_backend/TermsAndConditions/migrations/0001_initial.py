# Generated by Django 2.2.3 on 2019-10-09 02:46

from django.db import migrations, models
import jsonfield.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TermsAndConditionsModel',
            fields=[
                ('Term', jsonfield.fields.JSONField(default=dict)),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('term_url', models.CharField(default='', max_length=3000)),
                ('term_heading', models.CharField(default='', max_length=1000)),
            ],
        ),
    ]
