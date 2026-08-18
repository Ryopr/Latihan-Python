import pandas as pd
import numpy as np
import re
file_name_existing='Data_Participant_Tender_LPSE KABUPATEN KUTAI KARTANEGARA 2014.xlsx'
file_excel=pd.read_excel(file_name_existing,sheet_name='Data Tender');
# 1. Pastikan tipenya string dan ambil bagian sebelum koma (menghilangkan ,00)
file_excel['Harga_Terkoreksi'] = file_excel['Harga_Terkoreksi'].astype(str).str.split(',').str[0]

# 2. Hilangkan text "Rp." dan tanda titik "." sebagai pemisah ribuan
file_excel['Harga_Terkoreksi'] = file_excel['Harga_Terkoreksi'].str.replace('Rp.', '', regex=False)
file_excel['Harga_Terkoreksi'] = file_excel['Harga_Terkoreksi'].str.replace('.', '', regex=False).str.strip()

# 3. Ubah kolom menjadi numeric/integer. 
# errors='coerce' akan mengubah data yang tidak valid atau nan menjadi NaN, lalu kita isi dengan 0 (.fillna(0))
file_excel['Harga_Terkoreksi'] = pd.to_numeric(file_excel['Harga_Terkoreksi'], errors='coerce').fillna(0).astype(int)

matrix=file_excel.to_numpy()
np.set_printoptions(threshold=np.inf, linewidth=1)
print(matrix[:,6])
# pola_rupiah = r'(Rp\.\s*\d{1,3}(?:\.\d{3})*,\d{2})'
# file_excel['Harga Bersih']=(
#     file_excel.iloc[:, 6]
#     .astype(str)
#     .str.strip()
#     .str.extract(pola_rupiah,flags=re.IGNORECASE)[0]
# )
# np.set_printoptions(threshold=np.inf, linewidth=1)
# print(file_excel['I'].to_numpy())
data_export=pd.DataFrame(file_excel['Harga_Terkoreksi'].to_numpy())


with pd.ExcelWriter(file_name_existing, engine='openpyxl', mode='a', if_sheet_exists='overlay') as writer:
        data_export.to_excel(
        writer, 
        sheet_name='Data Tender', 
        startrow=1,  # Starts writing immediately after existing data
        startcol=6, # meng-cleaning data dari sebelumnya yang gak jelas ke kolom G
        index=False,               # Removes 0, 1, 2... row numbers
        header=False               # Removes top header text row
    )
        
# print(file_excel.iloc[:,1].to_numpy())
# print(file_excel['B'].to_numpy())


print('export berhasil')

# parsing data dari "Rp. 310.390.000,00" menjadi Integer


# file_excel['Harga Bersih']=(
#     file_excel.iloc[:, 6]
#     .astype(str)
#     .str.strip()
#     .str.extract(pola_rupiah,flags=re.IGNORECASE)[0]
# )
# print('pembersihan berhasil')