# Generated by Django 4.2 on 2023-04-13 00:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('agrilabo_app', '0007_topbar_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='certificat',
            name='accueil',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='certificats', to='agrilabo_app.accueil'),
            preserve_default=False,
        ),
    ]
