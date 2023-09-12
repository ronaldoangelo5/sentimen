from django.db import models

class Wisata(models.Model):
    nama = models.CharField(max_length=200)
    alamat = models.CharField(max_length=500)

    def __str__(self):
        return self.nama

class Komentar(models.Model):
    wisata = models.ForeignKey(Wisata, on_delete=models.CASCADE)
    kalimat = models.TextField()
    sentimen = models.BooleanField()
