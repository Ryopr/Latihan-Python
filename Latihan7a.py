import pandas as pd
import numpy as np
import re
from prisma import Prisma
from pathlib import Path
import asyncio
from prisma.models import Data_Participant

folder_path = Path(r"D:\Gdrive\2026\training\Latihan Python\Data test all cleansing to import postgresql")# nama alamat folder excel yang terpisah2

filenames = [f.name for f in folder_path.iterdir() if f.is_file()] # pemanggilan sejumlah nama file dari folder terpisah2
async def main(nama_file_excel_import):
    file_name_existing=nama_file_excel_import
    file_excel=pd.read_excel(file_name_existing,sheet_name='Data Tender');
    kolom_target = file_excel.iloc[:, 6]

    if not pd.api.types.is_numeric_dtype(kolom_target):
    # Regex untuk mengekstrak pola Rupiah
        pola_rupiah = r'(Rp\.\s*\d{1,3}(?:\.\d{3})*,\d{2})'
        
        # Ekstrak string Rupiah
        bersih = (
            kolom_target.astype(str)
            .str.strip()
            .str.extract(pola_rupiah, flags=re.IGNORECASE)[0]
        )
        
        # Ambil bagian sebelum koma (menghilangkan desimal ",00")
        bersih = bersih.str.split(',').str[0]
        
        # Hapus "Rp." dan titik pemisah ribuan
        bersih = bersih.str.replace('Rp.', '', regex=False)
        bersih = bersih.str.replace('.', '', regex=False).str.strip()
        
        # Ubah ke numeric integer
        file_excel['Harga_Terkoreksi'] = pd.to_numeric(bersih, errors='coerce').fillna(0).astype(int)
        print('cleansing dan parsing ' + str(file_name_existing) + '  berhasil')
    else:
        # Jika data sudah berupa angka, tinggal pastikan tipenya integer dan isi NaN jika ada
        file_excel['Harga_Terkoreksi'] = kolom_target.fillna(0).astype(int)

    # 3. Export ke Excel
    data_export = pd.DataFrame(file_excel['Harga_Terkoreksi'].to_numpy())

    with pd.ExcelWriter(file_name_existing, engine='openpyxl', mode='a', if_sheet_exists='overlay') as writer:
        data_export.to_excel(
            writer, 
            sheet_name='Data Tender', 
            startrow=1, 
            startcol=6,
            index=False, 
            header=False 
        )
    
    # baca data excel lagi untuk kemudian dapat di import ke db
    file_excel=pd.read_excel(file_name_existing,sheet_name='Data Tender');
    matrix=file_excel.to_numpy()

    db=Prisma()
    await db.connect()

    data=[]
    for i in range(len(matrix[1:])):
                # print("data ke " +str(i)+ "  berhasil diimport!")
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
    print('export ' + str(file_name_existing) + ' ke postgresql  berhasil')

for i in range(len(filenames)):
    # print('proses copy dan append file '+filenames[i]+' ke postgresql');
    print("=================")
    file_name_existing=filenames[i]
    asyncio.run(main(folder_path/file_name_existing))