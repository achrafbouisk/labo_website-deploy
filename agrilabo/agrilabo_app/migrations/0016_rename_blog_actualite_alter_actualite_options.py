# Generated by Django 4.2 on 2023-04-14 01:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('agrilabo_app', '0015_blog_alter_certificat_titre'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='blog',
            new_name='actualite',
        ),
        migrations.AlterModelOptions(
            name='actualite',
            options={'verbose_name_plural': 'actualite'},
        ),
    ]
