# Generated by Django 3.2.9 on 2022-10-13 19:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Visitor', '0010_alter_visitordetails_profile_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='visitordetails',
            name='profile_picture',
            field=models.ImageField(default='images\\Visitors\\default.jpg', upload_to='images\\Visitors'),
        ),
    ]