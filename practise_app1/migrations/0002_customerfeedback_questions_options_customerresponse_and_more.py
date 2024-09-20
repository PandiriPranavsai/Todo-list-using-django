# Generated by Django 5.0.3 on 2024-09-20 05:12

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('practise_app1', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomerFeedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Questions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=100)),
                ('question_type', models.CharField(choices=[('Text', 'Text'), ('BigText', 'BigText'), ('Radio', 'Radio'), ('Checkbox', 'Checkbox')], default='Text', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Options',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('option_name', models.CharField(max_length=100)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='options', to='practise_app1.questions')),
            ],
        ),
        migrations.CreateModel(
            name='CustomerResponse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('response_text', models.TimeField(blank=True, null=True)),
                ('feedback', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='practise_app1.customerfeedback')),
                ('selected_options', models.ManyToManyField(blank=True, to='practise_app1.options')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='practise_app1.questions')),
            ],
        ),
        migrations.AddField(
            model_name='customerfeedback',
            name='question',
            field=models.ManyToManyField(to='practise_app1.questions'),
        ),
        migrations.DeleteModel(
            name='OTP',
        ),
    ]
