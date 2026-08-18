import pandas as pd
import numpy as np

from pathlib import Path

folder_path = Path(r"D:\Gdrive\2026\training\Latihan Python\Data untuk di import")# nama alamat folder excel yang terpisah2
filenames = [f.name for f in folder_path.iterdir() if f.is_file()] # pemanggilan sejumlah nama file dari folder terpisah2

import asyncio
from prisma import Prisma
from prisma.models import Data_Participant

async def main(nama_file_excel_import):
    file_name_existing=nama_file_excel_import
    file_excel=pd.read_excel(file_name_existing,sheet_name='Data Tender');
    # data di excel seperti ini
    matrix=file_excel.to_numpy()

    print(len(matrix[1:]))
    # import data
    db=Prisma()
    await db.connect()
    data=[]
    for i in range(len(matrix[1:])):
                print("data ke " +str(i)+ "  berhasil diimport!")
                data.append({
                    'kode_paket':int(matrix[i,0]),
                    'nama_paket':str(matrix[i,1]),
                    'LPSE':str(matrix[i,2]),
                    'Nama_Peserta':str(matrix[i,3]),
                    'Alasan':str(matrix[i,4]) if pd.notna(matrix[i,4]) else None,
                    'Skor_Teknis':str(matrix[i,5]) if pd.notna(matrix[i,5]) else None,
                    'Harga_Terkoreksi':int(matrix[i,6]),
                    'Skor_Akhir':str(matrix[i,7]) if pd.notna(matrix[i,7]) else None
                })
    
        # )
    
    await db.data_participant.create_many(data=data ,skip_duplicates=False)
        # db.product.create_many(data=data, skip_duplicates=True)
    
    await db.disconnect()



for i in range(len(filenames)):
    print('proses copy dan append file '+filenames[i]+' ke postgresql');

    file_name_existing=filenames[i]
    asyncio.run(main(folder_path/file_name_existing))
   
# with open()


# print(file_excel.columns.tolist())
# print(file_excel.dtypes)
# print(file_excel.head())