import pandas as pd
import numpy as np
import re
file_name_existing='Data_Participant_Tender_LPSE KABUPATEN KUTAI KARTANEGARA 2014.xlsx'
file_excel=pd.read_excel(file_name_existing,sheet_name='Data Tender');

# matrix=file_excel.to_numpy()
pola_rupiah = r'(Rp\.\s*\d{1,3}(?:\.\d{3})*,\d{2})'
file_excel['Harga Bersih']=(
    file_excel.iloc[:, 6]
    .astype(str)
    .str.strip()
    .str.extract(pola_rupiah,flags=re.IGNORECASE)[0]
)

np.set_printoptions(threshold=np.inf, linewidth=1)
# print(file_excel['I'].to_numpy())
data_export=pd.DataFrame(file_excel['Harga Bersih'].to_numpy())
with pd.ExcelWriter(file_name_existing, engine='openpyxl', mode='a', if_sheet_exists='overlay') as writer:
        data_export.to_excel(
        writer, 
        sheet_name='Data Tender', 
        startrow=1,  # Starts writing immediately after existing data
        startcol=8,
        index=False,               # Removes 0, 1, 2... row numbers
        header=False               # Removes top header text row
    )
# print(file_excel.iloc[:,1].to_numpy())
# print(file_excel['B'].to_numpy())


print('export berhasil')