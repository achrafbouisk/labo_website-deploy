# Generated by Django 4.2 on 2023-04-14 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agrilabo_app', '0019_rename_response_contact_reponse'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='accueilinfo',
            name='nombre_certificat',
        ),
        migrations.AddField(
            model_name='accueilinfo',
            name='nombre_de_certificat',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]