from typing import Iterable, Optional
from django.db import models
from django.contrib.auth.models import User
from django.db.models import Sum, F, Window, Case, When
from django.db.models.functions import RowNumber
from django.utils.translation import gettext_lazy as _

from datetime import datetime


class Buku(models.Model):
    class Jenis(models.IntegerChoices):
        masuk = 1, _("Pemasukan")
        keluar = -1, _("Pengeluaran")

    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    nominal = models.FloatField(null=False, verbose_name="nominal", default=0)
    saldo = models.FloatField(null=False, verbose_name="saldo", default=0)
    jenis = models.SmallIntegerField(choices=Jenis.choices, default=Jenis.masuk)
    keterangan = models.TextField(verbose_name="Keterangan", null=False)
    tanggal = models.DateTimeField(
        verbose_name="tanggal input", auto_now_add=True
    )

    def __str__(self) -> str:
        return f"{self.get_jenis_display()}: {self.keterangan[:25]}"

    def get_saldo():
        buku = Buku.objects.all()
        saldo = 0
        for book in buku:
            saldo += book.nominal * book.jenis
        return {"saldo": saldo, "tanggal": datetime.now()}

    def save(self, *args, **kwargs) -> None:
        prev_saldo = Buku.get_saldo()["saldo"]
        jenis_value = (
            self.jenis
        )  # Extract the integer value from the enumeration
        self.saldo = prev_saldo + (self.nominal * jenis_value)
        return super().save(*args, **kwargs)

    @staticmethod
    def get_all_record():
        bukus = (
            Buku.objects.all()
            .defer("jenis")
            .annotate(
                row_number=Window(
                    expression=RowNumber(),
                ),
                jenis_enum=Case(
                    When(
                        jenis=Buku.Jenis.masuk, then=models.Value("Pemasukan")
                    ),
                    When(
                        jenis=Buku.Jenis.keluar,
                        then=models.Value("Pengeluaran"),
                    ),
                    output_field=models.CharField(),
                ),
            )
        )
        return bukus
