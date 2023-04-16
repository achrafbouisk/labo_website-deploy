from django.db import models
from PIL import Image
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from django.conf import settings

# Create your models here.


class informations(models.Model):

    class Meta:
        verbose_name_plural = "informations"

    titre = models.CharField(max_length=100)
    adresse = models.CharField(max_length=200)
    email = models.EmailField()
    phone_number = models.CharField(max_length=200)
    linkedin = models.CharField(max_length=255)
    instagram = models.CharField(max_length=255)
    facebook = models.CharField(max_length=255)
    twitter = models.CharField(max_length=255)
    youtube = models.CharField(max_length=255)

    def __str__(self):
        return self.titre


class Accueil(models.Model):

    class Meta:
        verbose_name_plural = "Accueil_Slider"

    titre = models.CharField(max_length=100)
    carousel_image = models.ImageField(upload_to='home/images')

    def __str__(self):
        return self.titre


    def save(self, *args, **kwargs):
        super(Accueil, self).save(*args, **kwargs)
        img = Image.open(self.carousel_image.path)
        if img.width != 1920 or img.height != 1080:
            output_size = (1920, 1080)
            img = img.resize(output_size)
            img.save(self.carousel_image.path)
            

class AccueilInfo(models.Model):
    class Meta:
        verbose_name_plural = "Accueil_informations"

    titre = models.TextField()
    nombre_de_project = models.IntegerField(blank=True, null=True)
    nombre_de_certificat = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.titre


class Qui_Somme_Nous(models.Model):

    class Meta:
        verbose_name_plural = "Qui Somme nous"

    titre = models.CharField(max_length=100)
    banner_image = models.ImageField(upload_to='about/banner')


    def __str__(self):
        return self.titre


class equipe(models.Model):

    class Meta:
        verbose_name_plural = "equipe"

    member_image = models.ImageField(upload_to='about/team')
    nom = models.CharField(max_length=100)
    designation = models.CharField(max_length=150)
    linkedin = models.CharField(max_length=255)
    instagram = models.CharField(max_length=255)
    facebook = models.CharField(max_length=255)
    twitter = models.CharField(max_length=255)

    def __str__(self):
        return self.nom

class actualite(models.Model):
    class Meta:
        verbose_name_plural = "actualite"

    blog_image = models.ImageField(upload_to='blog/images')
    titre = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.titre


class certificat(models.Model):

    class Meta:
        verbose_name_plural = "certificat"

    titre = models.CharField(max_length=255)
    certificat = models.ImageField(upload_to='about/certificat')


    def __str__(self):
        return self.titre


class VisitorCount(models.Model):
    count = models.IntegerField(default=0)


class Contact(models.Model):
    nom = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=150)
    message = models.TextField()
    reponse = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nom




from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

@receiver([post_save, post_delete], sender=certificat)
def update_accueil_info(sender, **kwargs):
    certificat_count = certificat.objects.count()
    accueil_info = AccueilInfo.objects.first()
    accueil_info.nombre_certificat = certificat_count
    accueil_info.save()



@receiver(post_save, sender=Contact)
def send_response_email(sender, instance, created, **kwargs):
    if instance.reponse:
        subject = instance.subject
        message = instance.reponse
        recipient_list = [instance.email]
        send_mail(
            subject,
            message,
            settings.EMAIL_HOST_USER,
            recipient_list,
            fail_silently=False,
        )


@receiver(post_save, sender=certificat)
@receiver(post_delete, sender=certificat)
def update_accueil_certificat_count(sender, **kwargs):
    count = certificat.objects.count()
    accueil_info, created = AccueilInfo.objects.get_or_create(id=1)  # Assuming AccueilInfo has a single record with id=1
    accueil_info.nombre_de_certificat = count
    accueil_info.save()