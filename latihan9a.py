from PIL import Image
from PIL import ImageFilter
from pathlib import Path
from google import genai
from google.genai import types
from dotenv import load_dotenv
import os

load_dotenv()


# ambil gratis di aistudio.google.com
client = genai.Client(api_key=os.getenv("google_gemini_API_key"))  # dari aistudio.google.com

# original_image='D:\Gdrive\2026\training\Latihan Python\screenshota.jpg'

folder_place_to_read=Path(r"D:\Gdrive\2026\training\Latihan Python\gambar captcha test")

folder_place_to_save=Path(r"D:\Gdrive\2026\training\Latihan Python\gambar captcha save")

folder_place_to_save_captcha=Path(r"D:\Gdrive\2026\training\Latihan Python\gambar captcha dibaca gemini")

def applyMaximumFilter(image):
    return image.filter(ImageFilter.MaxFilter);

filenames = [f.name for f in folder_place_to_read.iterdir() if f.is_file()] # pemanggilan sejumlah nama file dari folder terpisah2


#    # Method to apply the filter
for i in range(len(filenames)):
    file_name_existing=filenames[i]
    imageObject = Image.open(folder_place_to_read/file_name_existing)

    # Apply maximum filter
    filterApplied = imageObject

    for i in range(0, 1):
        # print(i);
        filterApplied = applyMaximumFilter(filterApplied);
        new_dpi = (300, 300)
        filterApplied.save(folder_place_to_save/file_name_existing, dpi=new_dpi);
    print(folder_place_to_save/file_name_existing)

    with open(str(folder_place_to_save/file_name_existing), "rb") as f:
        image_bytes = f.read()

        # Kirim ke Gemini
    response = client.models.generate_content(
    model="gemini-3.1-flash-lite",
    contents=[
            types.Part.from_bytes(
                data=image_bytes,
                mime_type="image/png"
            ),
            types.Part.from_text(
                text="Baca teks CAPTCHA ini. Jawab hanya dengan karakter yang kamu baca, tanpa spasi, tanpa penjelasan, selalu 6 huruf saja, abjad selalu huruf kecil, boleh ada angka jika dinyatakan digambar, dan tanpa simbol."
            ),
        ]
    )

    print(response.text.strip())

    Image.open(str(folder_place_to_save/file_name_existing)).save(str(folder_place_to_save_captcha/response.text.strip())+".jpg",dpi=(300, 300))

    
