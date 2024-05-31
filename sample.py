from PIL import Image
from pytesseract import pytesseract
import re
from tabulate import tabulate


def extract_text_from_jpg():
    # Defining paths to tesseract.exe
    # and the image we would be using
    path_to_tesseract = "C:/Program Files/Tesseract-OCR/tesseract.exe"
    image_path = "D:/pycharm_dir/sample/Combine 2023 paper &ans key_7.jpg"

    # Opening the image & storing it in an image object
    img = Image.open(image_path)

    # Providing the tesseract executable
    # location to pytesseract library
    pytesseract.tesseract_cmd = path_to_tesseract

    # Passing the image object to image_to_string() function
    # This function will extract the text from the image
    text = pytesseract.image_to_string(img, lang='devanagari')

    text_content = text[:-1]
    # print(type(text_content))
    list_content = [line for line in text_content.splitlines() if line]
    print((list_content))
    list_items = list_content[2:-5]
    print(list_items)
    return list_items, image_path


def extract_marathi_text(list_items):
    marathi_option = []
    for line in list_items:
        # print(line)
        if line.startswith("अ."):
            print("line starts with A: ", line)
            marathi_option.append(line)
        if line.startswith("ब."):
            print("line starts with B: ", line)
            marathi_option.append(line)
        if line.startswith("क."):
            print("line starts with C: ", line)
            marathi_option.append(line)
        if line.startswith("ड. "):
            print("line starts with D: ", line)
            marathi_option.append(line)
    print(marathi_option)


def extract_english_text(list_items):
    english_option = []
    for line in list_items:
        if line.startswith("a."):
            print("line starts with A: ", line)
            english_option.append(line)
        if line.startswith("b."):
            print("line starts with B: ",line)
            english_option.append(line)
        if line.startswith("c."):
            print("line starts with C: ",line)
            english_option.append(line)
        if line.startswith("d. "):
            print("line starts with D: ",line)
            english_option.append(line)
    print(english_option)


def write_text_file(list_items, image_path):

    # get name for the text file
    file_name = image_path.split("/")[-1].split(".")[0]
    # print(file_name)

    file_name = file_name + ".txt"

    file = open(file_name, "w", encoding="utf-8")

    for line in list_items:
        file.write(line + "\n")
    print(f"{file_name} Created")


def main():
    list_items, image_path = extract_text_from_jpg()
    # extract_marathi_text(list_items)
    # extract_english_text(list_items)
    write_text_file(list_items, image_path)

if __name__ == "__main__":
    main()