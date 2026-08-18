#----- Python example program for applying a maximum filter to a digital image -----
from PIL import Image
from PIL import ImageFilter
import pytesseract
import sys
import datetime

try:
    arg1 = sys.argv[1]
    # nama_gambar='D:/P/Database, Misc, dan Downloadan Untuk node_SPSE_Integrated_Script/screenshota.jpg';
    pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
    # Method to apply the filter
    def applyMaximumFilter(image):
        return image.filter(ImageFilter.MaxFilter);

    # Load the image
    # folder_save="D:\\P\\node\\Captcha Image\\"
    imageObject = Image.open(arg1);
    # menyimpan setiap captcha yang dibuka terpisah
    x = datetime.datetime.now()
    y= x.strftime("%Y-%m-%d %H%M%S")

    # menyimpan setiap captcha yang dibuka terpisah, untuk keperluan debugging jika hasil OCR tidak sesuai dengan yang diharapkan
    folder_save1="D:\\P\\Database, Misc, dan Downloadan Untuk node_SPSE_Integrated_Script\\Gambar Captcha\\"
    imageObject.save(folder_save1+y+'.jpg');

    # Apply maximum filter
    filterApplied = imageObject;
    for i in range(0, 1):
        # print(i);
        filterApplied = applyMaximumFilter(filterApplied);
    new_dpi = (300, 300)
    folder_save="D:\\P\\Database, Misc, dan Downloadan Untuk node_SPSE_Integrated_Script\\Captcha Image\\"
    filterApplied.save(folder_save+"captcha_filter.jpg", dpi=new_dpi);
    # Display images
    # imageObject.show();
    # filterApplied.show();
    # print(pytesseract.image_to_osd('tmp30iqqu7c.jpg'))
    hasil_ocr=pytesseract.image_to_string(folder_save+"captcha_filter.jpg", config='--oem 1 --psm 6 -c tessedit_char_whitelist=abcdefghijklmnopqrstuvwxyz0123456789')
    print(hasil_ocr.replace(" ", ""))
    # print(hasil_ocr)
except IndexError:
    print("❌ Error: Tidak ada argument path gambar yang diberikan")
except FileNotFoundError as e:
    print(f"❌ Error: File tidak ditemukan — {e}")
except Exception as e:
    print(f"❌ Error tidak terduga: {e}")