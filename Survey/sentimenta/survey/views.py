from django.shortcuts import render,redirect
from .forms import KomentarForm
from .models import *
from .classifier import sentimenAnalisis
import numpy as np
# Create your views here.
def index(request):
    if request.method == 'POST':
        form = KomentarForm(request.POST)

        if form.is_valid():
            kalimat = form.cleaned_data['kalimat']

            wisata = Wisata.objects.get(nama = form.cleaned_data['wisata'])
            sentimen, proba = sentimenAnalisis(kalimat)
            proba *= 100
            proba = proba[0]
            rdproba = np.round_(proba)
            print(", ".join( repr(e) for e in rdproba ))
            komentar = Komentar(wisata = wisata,kalimat = kalimat, sentimen = sentimen)
            komentar.save()
            context = {'halaman':'sentimen','komentar':komentar, 'proba':rdproba}
            return render(request,'survey/sentimen.html',context)
    form = KomentarForm()
    context = {'halaman':'index','form':form}
    return render(request,'survey/index.html',context)

def wisata(request):
    wisata = Wisata.objects.all()
    sentimen = []
    for x in wisata:
        positif = x.komentar_set.filter(sentimen=True).count()
        negatif = x.komentar_set.filter(sentimen=False).count()

        sentimen.append({
            'nama': x.nama,
            'alamat': x.alamat,
            'positif':positif,
            'negatif':negatif
        })
        #totalsentimen = sentimen.count()

    context = {'halaman':'wisata', 'sentimen': sentimen}
    return render(request,'survey/wisata.html',context)
