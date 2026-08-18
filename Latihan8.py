
from PIL import Image
from PIL import ImageFilter
# import pytesseract

# original_image='D:\\Gdrive\\2026\\training\\Latihan Python\\screenshota.jpg'

folder_place='D:\\Gdrive\\2026\\training\\Latihan Python\\'

# pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
#     # Method to apply the filter
    
def applyMaximumFilter(image):
    return image.filter(ImageFilter.MaxFilter);

imageObject = Image.open(folder_place+"screenshota.jpg")

# Apply maximum filter
filterApplied = imageObject

for i in range(0, 1):
    # print(i);
    filterApplied = applyMaximumFilter(filterApplied);
    new_dpi = (300, 300)
    filterApplied.save(folder_place+"captcha_filter.jpg", dpi=new_dpi);