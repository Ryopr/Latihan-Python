
from PIL import Image
from PIL import ImageFilter
import pytesseract
from pathlib import Path
# original_image='D:\Gdrive\2026\training\Latihan Python\screenshota.jpg'

folder_place_to_read=Path(r"D:\Gdrive\2026\training\Latihan Python\gambar captcha test")

folder_place_to_save=Path(r"D:\Gdrive\2026\training\Latihan Python\gambar captcha save")

folder_place_to_save_captcha=Path(r"D:\Gdrive\2026\training\Latihan Python\gambar captcha dibaca tesseract")

def applyMaximumFilter(image):
    return image.filter(ImageFilter.MaxFilter);

filenames = [f.name for f in folder_place_to_read.iterdir() if f.is_file()] # pemanggilan sejumlah nama file dari folder terpisah2

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
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

    hasil_ocr=pytesseract.image_to_string(str(folder_place_to_save/file_name_existing), config='--oem 1 --psm 6 -c tessedit_char_whitelist=abcdefghijklmnopqrstuvwxyz0123456789').strip()

    print(hasil_ocr)

    Image.open(str(folder_place_to_save/file_name_existing)).save(str(folder_place_to_save_captcha/hasil_ocr)+".jpg",dpi=(300, 300))

    
