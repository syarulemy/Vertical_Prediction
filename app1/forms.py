from django import forms
from .models import Record

class RecordForm(forms.Form):
    No_KP = forms.CharField(
        max_length=12, 
        label="Nombor Kad Pengenalan", 
        widget=forms.TextInput(attrs={'pattern': '[0-9]{12}', 'required': True})
    )
    Nama = forms.CharField(max_length=255, label="Nama", required=True)
    No_Tel = forms.CharField(
        max_length=11, 
        label="Nombor Telefon", 
        widget=forms.TextInput(attrs={'pattern': '[0-9]{10,11}', 'required': True})
    )
    Nm_Syarikat = forms.CharField(max_length=255, label="Nama Syarikat", required=True)
    
    Ind_Perniagaan = forms.ChoiceField(
        choices=[(item, item) for item in Record.objects.values_list('Ind_Perniagaan', flat=True).distinct()],
        label="Industri perniagaan anda",
        required=True
    )
    Julat_HasilJualan = forms.ChoiceField(
        choices=[(item, item) for item in Record.objects.values_list('Julat_HasilJualan', flat=True).distinct()],
        label="Hasil Jualan bulanan",
        required=True
    )
    Julat_Keuntungan = forms.ChoiceField(
        choices=[(item, item) for item in Record.objects.values_list('Julat_Keuntungan', flat=True).distinct()],
        label="Jumlah Keuntungan bulanan",
        required=True
    )
    Julat_Pbelanja = forms.ChoiceField(
        choices=[(item, item) for item in Record.objects.values_list('Julat_Pbelanja', flat=True).distinct()],
        label="Jumlah Perbelanjaan bulanan",
        required=True
    )
    Julat_PurataHargaProduk = forms.ChoiceField(
        choices=[(item, item) for item in Record.objects.values_list('Julat_PurataHargaProduk', flat=True).distinct()],
        label="Purata Harga produk",
        required=True
    )
    Lokasi_Sasaran_Audiens = forms.ChoiceField(
        choices=[(item, item) for item in Record.objects.values_list('Lokasi_Sasaran_Audiens', flat=True).distinct()],
        label="Lokasi sasaran audiens",
        required=True
    )
    Bil_Staf = forms.ChoiceField(
        choices=[(item, item) for item in Record.objects.values_list('Bil_Staf', flat=True).distinct()],
        label="Bilangan staff bisnes",
        required=True
    )
    Bis_Mmpu_bthn = forms.ChoiceField(
        choices=[(item, item) for item in Record.objects.values_list('Bis_Mmpu_bthn', flat=True).distinct()],
        label="Mampu bertahan dengan keuntungan semasa?",
        required=True
    )
    Cara_Beli = forms.ChoiceField(
        choices=[(item, item) for item in Record.objects.values_list('Cara_Beli', flat=True).distinct()],
        label="Bagaimanakah pelanggan anda membeli produk/ menggunakan perkhidmatan anda?",
        required=True
    )
    Slrn_Phbngn = forms.ChoiceField(
        choices=[(item, item) for item in Record.objects.values_list('Slrn_Phbngn', flat=True).distinct()],
        label="Saluran mudah alih yang digunakan pelanggan",
        required=True
    )
    K_Pghntrn = forms.ChoiceField(
        choices=[(item, item) for item in Record.objects.values_list('K_Pghntrn', flat=True).distinct()],
        label="Kaedah penghantaran produk",
        required=True
    )
    Plt_Talian = forms.ChoiceField(
        choices=[(item, item) for item in Record.objects.values_list('Plt_Talian', flat=True).distinct()],
        label="Platform atas talian yang digunakan",
        required=True
    )
    Trmnl_Byrn = forms.ChoiceField(
        choices=[(item, item) for item in Record.objects.values_list('Trmnl_Byrn', flat=True).distinct()],
        label="Adakah anda mempunyai terminal pembayaran?",
        required=True
    )
    Cr_Byrn = forms.ChoiceField(
        choices=[(item, item) for item in Record.objects.values_list('Cr_Byrn', flat=True).distinct()],
        label="Bagaimanakah pelanggan anda membuat pembayaran?",
        required=True
    )
    Slrn_Fzkl = forms.ChoiceField(
        choices=[(item, item) for item in Record.objects.values_list('Slrn_Fzkl', flat=True).distinct()],
        label="Adakah anda mempunyai saluran fizikal?",
        required=True
    )
    Mjrt_Kaum = forms.ChoiceField(
        choices=[(item, item) for item in Record.objects.values_list('Mjrt_Kaum', flat=True).distinct()],
        label="Pengguna majoriti produk/perkhidmatan",
        required=True
    )
    Sjl_Halal = forms.ChoiceField(
        choices=[(item, item) for item in Record.objects.values_list('Sjl_Halal', flat=True).distinct()],
        label="Adakah produk anda mempunyai sijil Halal?",
        required=True
    )
    Cap_dgngn = forms.ChoiceField(
        choices=[(item, item) for item in Record.objects.values_list('Cap_dgngn', flat=True).distinct()],
        label="Adakah perniagaan anda mempunyai cap dagangan?",
        required=True
    )
    Akt_Pmsrn = forms.ChoiceField(
        choices=[(item, item) for item in Record.objects.values_list('Akt_Pmsrn', flat=True).distinct()],
        label="Bagaimana anda menjalankan aktiviti pemasaran?",
        required=True
    )
    Kpst_Tgkt_Digital = forms.ChoiceField(
        choices=[(item, item) for item in Record.objects.values_list('Kpst_Tgkt_Digital', flat=True).distinct()],
        label="Adakah anda mempunyai kapasiti untuk meningkatkan pendigitalan?",
        required=True
    )
    Btn_kew_bank = forms.ChoiceField(
        choices=[(item, item) for item in Record.objects.values_list('Btn_kew_bank', flat=True).distinct()],
        label="Adakah anda memerlukan bantuan Kewangan/Perbankan?",
        required=True
    )
    Btn_Pmsrn_Dgtl = forms.ChoiceField(
        choices=[(item, item) for item in Record.objects.values_list('Btn_Pmsrn_Dgtl', flat=True).distinct()],
        label="Adakah anda memerlukan bantuan Pemasaran Digital/Pendigitalan?",
        required=True
    )
    Btn_Sjl = forms.ChoiceField(
        choices=[(item, item) for item in Record.objects.values_list('Btn_Sjl', flat=True).distinct()],
        label="Adakah anda memerlukan bantuan Pensijilan?",
        required=True
    )
    Btn_Prnct_Fzkl = forms.ChoiceField(
        choices=[(item, item) for item in Record.objects.values_list('Btn_Prnct_Fzkl', flat=True).distinct()],
        label="Adakah anda memerlukan bantuan Peruncitan/Kedai Fizikal?",
        required=True
    )
    Btn_Lgstk_Pghtrn = forms.ChoiceField(
        choices=[(item, item) for item in Record.objects.values_list('Btn_Lgstk_Pghtrn', flat=True).distinct()],
        label="Adakah anda memerlukan bantuan Logistik/Penghantaran?",
        required=True
    )
    Jns_Btn_Kew = forms.ChoiceField(
        choices=[(item, item) for item in Record.objects.values_list('Jns_Btn_Kew', flat=True).distinct()],
        label="Apakah jenis bantuan kewangan yang anda perlukan?",
        required=True
    )
