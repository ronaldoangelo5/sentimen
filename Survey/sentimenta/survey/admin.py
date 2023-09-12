from django.contrib import admin

from .models import *

class WisataAdmin(admin.ModelAdmin):
    list_display = ['nama','alamat']
    search_fields = ['nama']

admin.site.register(Wisata,WisataAdmin)

class KomentarAdmin(admin.ModelAdmin):
    list_display = ['wisata','kalimat','sentimen']
    list_filter = ['sentimen']

admin.site.register(Komentar,KomentarAdmin)
