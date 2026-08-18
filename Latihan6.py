import pandas as pd
import numpy as np
file_name_existing='Data_Participant_Tender_LPSE KABUPATEN KUTAI KARTANEGARA 2015B.xlsx'
file_excel=pd.read_excel(file_name_existing,sheet_name='Data Tender');
matrix=file_excel.to_numpy()

print(matrix[1,1])

from prisma import Prisma
db=Prisma()
db.connect()

db.Data_Participant.create(
        data={
            'kode_paket':matrix[1,0],
            'nama_paket':matrix[1,1],
            'LPSE':matrix[1,2],
            'Nama_Peserta':matrix[1,3],
            'Alasan':matrix[1,4],
            'Skor_Teknis':matrix[1,5],
            'Harga_Terkoreksi':matrix[1,6],
            'Skor_Akhir':matrix[1,7]
        }
)

db.disconnect()
# with open()


# print(file_excel.columns.tolist())
# print(file_excel.dtypes)
# print(file_excel.head())