# Generated by Django 4.2 on 2023-04-14 03:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agrilabo_app', '0016_rename_blog_actualite_alter_actualite_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('subject', models.CharField(max_length=150)),
                ('message', models.TextField()),
            ],
        ),
        migrations.AlterField(
            model_name='accueilinfo',
            name='nombre_certificat',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='accueilinfo',
            name='nombre_de_project',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='accueilinfo',
            name='titre',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='actualite',
            name='description',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='actualite',
            name='titre',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='certificat',
            name='titre',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='informations',
            name='email',
            field=models.EmailField(max_length=254),
        ),
    ]
