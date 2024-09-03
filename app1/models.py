from django.db import models

# Create your models here.


from django.db import models

class Record(models.Model):
    No_KP = models.CharField(max_length=50,unique=True,default="No records")
    Nama = models.CharField(max_length=255)
    No_Tel = models.CharField(max_length=20)
    Nm_Syarikat = models.CharField(max_length=255)
    Ind_Perniagaan = models.CharField(max_length=255)
    Julat_HasilJualan = models.CharField(max_length=100)
    Julat_Keuntungan = models.CharField(max_length=100)
    Julat_Pbelanja = models.CharField(max_length=100)
    Julat_PurataHargaProduk = models.CharField(max_length=100)
    Lokasi_Sasaran_Audiens = models.CharField(max_length=255)
    Bil_Staf = models.IntegerField()
    Bis_Mmpu_bthn = models.CharField(max_length=255)
    Cara_Beli = models.CharField(max_length=255)
    Slrn_Phbngn = models.CharField(max_length=255)
    K_Pghntrn = models.CharField(max_length=255)
    Plt_Talian = models.CharField(max_length=255)
    Trmnl_Byrn = models.CharField(max_length=255)
    Cr_Byrn = models.CharField(max_length=255)
    Slrn_Fzkl = models.CharField(max_length=255)
    Mjrt_Kaum = models.CharField(max_length=255)
    Sjl_Halal = models.CharField(max_length=50)
    Cap_dgngn = models.CharField(max_length=50)
    Akt_Pmsrn = models.CharField(max_length=255)
    Kpst_Tgkt_Digital = models.CharField(max_length=255)
    Btn_kew_bank = models.CharField(max_length=255)
    Btn_Pmsrn_Dgtl = models.CharField(max_length=255)
    Btn_Sjl = models.CharField(max_length=255)
    Btn_Prnct_Fzkl = models.CharField(max_length=255)
    Btn_Lgstk_Pghtrn = models.CharField(max_length=255)
    Jns_Btn_Kew = models.CharField(max_length=255)
    SuggestedVerticals = models.CharField(max_length=255)

    def __str__(self):
        return self.Nama
