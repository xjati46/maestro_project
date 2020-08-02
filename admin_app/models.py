from django.db import models
from django.utils import timezone
from coach_app.models import Coach
from student_app.models import Student

# Create your models here.


class Product(models.Model):
    PILIHAN_KATEGORI = models.TextChoices(
        'Pilih Kategori',
        'Bandung Jakarta Dnurs',
    )

    nama_produk = models.CharField(max_length=10)
    kategori = models.CharField(
        max_length=10,
        choices=PILIHAN_KATEGORI.choices,
    )

    jumlah_siswa = models.IntegerField()
    jumlah_pertemuan = models.IntegerField()
    harga = models.IntegerField()

    class Meta:
        ordering = ['nama_produk']

    def __str__(self):
        return self.nama_produk


class Order(models.Model):
    student = models.ForeignKey(
        Student,
        on_delete=models.SET_NULL,
        null=True,
    )

    coach = models.ForeignKey(Coach, on_delete=models.SET_NULL, null=True)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    diskon = models.FloatField(blank=True, null=True)
    tanggal_transaksi = models.DateField()
    tanggal_expired = models.DateField()
    arsip = models.BooleanField(default=False)
    p1 = models.DateField('Pertemuan 1', null=True, blank=True)
    p1_a = models.BooleanField(null=True, blank=True)
    p1_c = models.BooleanField(null=True, blank=True)
    p2 = models.DateField('Pertemuan 2', null=True, blank=True)
    p2_a = models.BooleanField(null=True, blank=True)
    p2_c = models.BooleanField(null=True, blank=True)
    p3 = models.DateField('Pertemuan 3', null=True, blank=True)
    p3_a = models.BooleanField(null=True, blank=True)
    p3_c = models.BooleanField(null=True, blank=True)
    p4 = models.DateField('Pertemuan 4', null=True, blank=True)
    p4_a = models.BooleanField(null=True, blank=True)
    p4_c = models.BooleanField(null=True, blank=True)
    p5 = models.DateField('Pertemuan 5', null=True, blank=True)
    p5_a = models.BooleanField(null=True, blank=True)
    p5_c = models.BooleanField(null=True, blank=True)
    p6 = models.DateField('Pertemuan 6', null=True, blank=True)
    p6_a = models.BooleanField(null=True, blank=True)
    p6_c = models.BooleanField(null=True, blank=True)
    p7 = models.DateField('Pertemuan 7', null=True, blank=True)
    p7_a = models.BooleanField(null=True, blank=True)
    p7_c = models.BooleanField(null=True, blank=True)
    p8 = models.DateField('Pertemuan 8', null=True, blank=True)
    p8_a = models.BooleanField(null=True, blank=True)
    p8_c = models.BooleanField(null=True, blank=True)

    class Meta:
        ordering = ['student']

    def __str__(self):
        return f'{self.id}/{self.student.nama_panggilan}'

    def is_expired(self):
        if self.tanggal_expired < timezone.now().date():
            return "EXPIRED"
        else:
            return "OK"

    def bill(self):
        x = 0
        if self.diskon:
            x = (1 - self.diskon) * self.product.harga
            return int(x)
        return int(self.product.harga)

    def share_dnurs(self):
        x = self.bill() * 0.2
        return int(x)

    def share_maestro(self):
        x = self.bill() * 0.8
        return int(x)

    def coach_share(self):
        x = self.coach.bagi_hasil * self.bill()
        y = self.product.jumlah_pertemuan
        return int(x/y)

    def coach_share_dnurs(self):
        x = int(self.coach.bagi_hasil * self.share_maestro())
        y = self.product.jumlah_pertemuan
        return int(x/y)

    def p_total(self):
        count = 0
        if self.p1:
            count += 1
        if self.p2:
            count += 1
        if self.p3:
            count += 1
        if self.p4:
            count += 1
        if self.p5:
            count += 1
        if self.p6:
            count += 1
        if self.p7:
            count += 1
        if self.p8:
            count += 1
        return count

    def p_a_total(self):
        count = 0
        if self.p1_a:
            count += 1
        if self.p2_a:
            count += 1
        if self.p3_a:
            count += 1
        if self.p4_a:
            count += 1
        if self.p5_a:
            count += 1
        if self.p6_a:
            count += 1
        if self.p7_a:
            count += 1
        if self.p8_a:
            count += 1
        return count

    def margin_p_a(self):
        x = int(self.p_total())
        y = int(self.p_a_total())
        if x != y:
            return x-y
        else:
            return '---'

    def p_c_total(self):
        count = 0
        if self.p1_c:
            count += 1
        if self.p2_c:
            count += 1
        if self.p3_c:
            count += 1
        if self.p4_c:
            count += 1
        if self.p5_c:
            count += 1
        if self.p6_c:
            count += 1
        if self.p7_c:
            count += 1
        if self.p8_c:
            count += 1
        return count

    def p_status(self):
        if self.p_total() >= self.product.jumlah_pertemuan:
            return "SELESAI"
        else:
            return "OK"

    def income_coach_normal(self):
        return int(self.p_c_total() * self.coach_share())

    def income_coach_dnurs(self):
        return int(self.p_c_total() * self.coach_share_dnurs())

    def potential_income_coach_normal(self):
        return int(
            (self.product.jumlah_pertemuan - self.p_c_total())
            * self.coach_share()
            )

    def potential_income_coach_dnurs(self):
        return int(
            (self.product.jumlah_pertemuan - self.p_c_total())
            * self.coach_share_dnurs()
            )
