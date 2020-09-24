# Generated by Django 3.1.1 on 2020-09-22 21:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0005_auto_20200922_2046'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='product_image',
            field=models.ImageField(default='DEFAULT VALUE', upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='productcategory',
            name='icon',
            field=models.ImageField(upload_to=''),
        ),
        migrations.DeleteModel(
            name='ProductImage',
        ),
    ]
