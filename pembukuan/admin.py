from django.contrib import admin
from .models import Buku


@admin.register(Buku)
class BukuAdmin(admin.ModelAdmin):
    list_filter = ("tanggal",)
    list_display = (
        "id",
        "tanggal",
        "user",
        "nominal",
        "keterangan",
    )
