from google import genai
from google.genai import types

import base64
from dotenv import load_dotenv
import os
# Memuat file .env (secara default mencari file .env di direktori yang sama)
load_dotenv()

# ambil gratis di aistudio.google.com
client = genai.Client(api_key=os.getenv("google_gemini_API_key"))  # dari aistudio.google.com

# for model in client.models.list():
#     print(model.name)
# cek jenis model AI
# Baca file gambar
with open("D:/Gdrive/2026/training/Latihan Python/gambar captcha test/2026-08-07 042555.jpg", "rb") as f:
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