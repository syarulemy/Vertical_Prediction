import os
import sys
import django
import pandas as pd

# Add the project directory to the Python path
project_path = r'C:\Users\User\trial3'
sys.path.append(project_path)

# Set up Django environment
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "trial3.settings")
django.setup()

# Now you can import your models
from app1.models import Record

def import_excel():
    # Replace this with your Excel file path
    excel_file_path = r'C:/Users/User/Downloads/pendigitalan_with_analysis_redo.xlsx'

    # Read the Excel file
    df = pd.read_excel(excel_file_path)

    # Print out the column names to debug
    print("Detected Excel Columns:", df.columns.tolist())

    # Iterate over the rows in the dataframe
    for _, row in df.iterrows():
        Record.objects.create(
            No_KP=row["No_KP"],
            Nama=row["Nama"],
            No_Tel=row["No_Tel"],
            Nm_Syarikat=row["Nm_Syarikat"],
            Ind_Perniagaan=row["Ind_Perniagaan"],
            Julat_HasilJualan=row["Julat_HasilJualan"],
            Julat_Keuntungan=row["Julat_Keuntungan"],
            Julat_Pbelanja=row["Julat_Pbelanja"],
            Julat_PurataHargaProduk=row["Julat_PurataHargaProduk"],
            Lokasi_Sasaran_Audiens=row["Lokasi_Sasaran_Audiens"],
            Bil_Staf=int(row["Bil_Staf"]),
            Bis_Mmpu_bthn=row["Bis_Mmpu_bthn"],
            Cara_Beli=row["Cara_Beli"],
            Slrn_Phbngn=row["Slrn_Phbngn"],
            K_Pghntrn=row["K_Pghntrn"],
            Plt_Talian=row["Plt_Talian"],
            Trmnl_Byrn=row["Trmnl_Byrn"],
            Cr_Byrn=row["Cr_Byrn"],
            Slrn_Fzkl=row["Slrn_Fzkl"],
            Mjrt_Kaum=row["Mjrt_Kaum"],
            Sjl_Halal=row["Sjl_Halal"],
            Cap_dgngn=row["Cap_dgngn"],
            Akt_Pmsrn=row["Akt_Pmsrn"],
            Kpst_Tgkt_Digital=row["Kpst_Tgkt_Digital"],
            Btn_kew_bank=row["Btn_kew_bank"],
            Btn_Pmsrn_Dgtl=row["Btn_Pmsrn_Dgtl"],
            Btn_Sjl=row["Btn_Sjl"],
            Btn_Prnct_Fzkl=row["Btn_Prnct_Fzkl"],
            Btn_Lgstk_Pghtrn=row["Btn_Lgstk_Pghtrn"],
            Jns_Btn_Kew=row["Jns_Btn_Kew"],
            SuggestedVerticals=row["SuggestedVerticals"]
        )

    print(f'Successfully imported the Excel file from {excel_file_path}')

if __name__ == "__main__":
    import_excel()


