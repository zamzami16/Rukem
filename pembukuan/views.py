from django.shortcuts import render
from .models import Buku


def BukuList(request):
    buku = Buku.get_all_record()
    saldo = Buku.get_saldo()
    return render(
        request, "pembukuan/aruskas/list.html", {"kas": buku, "saldo": saldo}
    )
