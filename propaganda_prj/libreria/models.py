from django.db import models
from django.urls import reverse

# Create your models here.


class Autori(models.Model):
    nome = models.CharField(max_length = 20)
    cognome = models.CharField(max_length = 20)
    nazione = models.CharField(max_length = 20)

    def __str__(self):
        return self.nome + ' ' + self.cognome

    class Meta:
        verbose_name = 'Autore'
        verbose_name_plural = 'Autori'

    def get_absolute_url(self):
        return reverse('autori_detail', kwargs = {'pk': self.pk})


class Editori(models.Model):
    societa = models.CharField(max_length = 30)

    def __str__(self):
        return self.societa
    class Meta:
        verbose_name = 'Editore'
        verbose_name_plural = 'Editori'

    def get_absolute_url(self):
        return reverse('editori_detail', kwargs = {'pk': self.pk})


class Generi(models.Model):
    tipologia = models.CharField(max_length = 100)

    def __str__(self):
        return self.tipologia

    class Meta:
        verbose_name = 'Generi'
        verbose_name_plural = 'Generi'
        
    def get_absolute_url(self):
        return reverse('genere_detail', kwargs = {'pk': self.pk})
class Libri(models.Model):
    titolo = models.CharField(max_length = 100)
    autore = models.ForeignKey(
        Autori, on_delete = models.CASCADE, related_name = 'libri')
    editore = models.ForeignKey(
        Editori, on_delete = models.CASCADE, related_name = 'libri_per_editore', null = True)
    isbn = models.CharField(max_length = 16)
    genere = models.ManyToManyField(Generi, related_name = 'libri_per_genere')
    quantita = models.IntegerField(default = 0)
    prezzo = models.DecimalField(decimal_places = 2, max_digits = 6, default = 0)
    data_caricamento = models.DateField(auto_now_add=True, blank= True)
    disponibile =models.BooleanField(default=True)
    
    def __str__(self):
        return self.titolo

    class Meta:
        verbose_name = 'Libro'
        verbose_name_plural = 'Libri'
        ordering = ("titolo", "autore", 'editore')

    def get_absolute_url(self):
        return reverse('libro_detail', kwargs = {'pk': self.pk})
    
