# from PIL import Image
# from pytesseract import pytesseract
#
# # Defining paths to tesseract.exe
# # and the image we would be using
# path_to_tesseract = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
# image_path = r"D:\pycharm_dir\sample\Combine 2023 paper &ans key_7.jpg"
#
# # Opening the image & storing it in an image object
# img = Image.open(image_path)
#
# # Providing the tesseract executable
# # location to pytesseract library
# pytesseract.tesseract_cmd = path_to_tesseract
#
# # Passing the image object to image_to_string() function
# # This function will extract the text from the image
# text = pytesseract.image_to_string(img, lang='devanagari')
#
# # Displaying the extracted text
# print(text[:-1])
# # print("raw text: ", text)


# importing required classes
from pypdf import PdfReader

# creating a pdf reader object
reader = PdfReader('rahiwashi dakhla.pdf')

# printing number of pages in pdf file
print(len(reader.pages))

# creating a page object
page = reader.pages[0]

# extracting text from page
print(page.extract_text())
