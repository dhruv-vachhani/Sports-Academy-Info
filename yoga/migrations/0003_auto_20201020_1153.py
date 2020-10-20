# Generated by Django 3.1 on 2020-10-20 11:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('yoga', '0002_auto_20201017_0456'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='trainer',
            options={'ordering': ['name']},
        ),
        migrations.AlterModelOptions(
            name='yoga',
            options={'ordering': ['name']},
        ),
        migrations.CreateModel(
            name='TrainingLevel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('training_name', models.CharField(max_length=200)),
                ('training_type', models.CharField(max_length=200)),
                ('yoga', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='yoga.yoga')),
            ],
            options={
                'ordering': ['training_name', 'training_type'],
            },
        ),
    ]
