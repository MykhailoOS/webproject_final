# Generated by Django 3.2.23 on 2023-12-23 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AboutUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=300)),
                ('is_visible', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name_plural': 'AboutUs',
            },
        ),
        migrations.CreateModel(
            name='BlogPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=100)),
                ('description', models.TextField(blank=True, max_length=400)),
                ('body', models.TextField(blank=True, max_length=500)),
                ('photo', models.ImageField(blank=True, upload_to='blog_images/')),
                ('is_visible', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Home',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=55)),
                ('description', models.TextField(blank=True, max_length=300)),
                ('chair_name', models.CharField(max_length=55)),
                ('chair_price', models.DecimalField(blank=True, decimal_places=2, max_digits=10)),
                ('is_visible', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name_plural': 'Home',
            },
        ),
        migrations.CreateModel(
            name='OurTeam',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50)),
                ('description', models.TextField(max_length=200)),
                ('is_visible', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chair_name', models.CharField(blank=True, max_length=55)),
                ('chair_price', models.DecimalField(blank=True, decimal_places=2, max_digits=10)),
                ('chair_photo', models.ImageField(blank=True, upload_to='images/')),
                ('is_visible', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Testimonials',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(blank=True, max_length=500)),
                ('is_visible', models.BooleanField(default=True)),
            ],
        ),
    ]
