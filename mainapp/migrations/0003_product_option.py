# Generated by Django 3.0.2 on 2020-02-25 09:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0002_filldb'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product_option',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='имя продукта')),
                ('option', models.CharField(max_length=128, verbose_name='вариант продукта')),
                ('image', models.ImageField(blank=True, upload_to='products_images')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.Product')),
            ],
        ),
    ]
