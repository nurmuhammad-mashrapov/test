# Generated by Django 4.2.4 on 2023-08-19 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('neauralnetwork', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='neuralnetwork',
            options={'ordering': ['-order'], 'verbose_name': 'Нейронная сеть', 'verbose_name_plural': 'Нейронные сети'},
        ),
        migrations.AddField(
            model_name='neuralnetwork',
            name='order',
            field=models.IntegerField(default=1, verbose_name='Порядок'),
            preserve_default=False,
        ),
    ]
