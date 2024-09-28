import PyPDF2
import json
import os
import docx
import pytesseract
from PIL import Image
import cv2

#tis is  __main__
def convertToJson(file_name):
    pdf_text = readFile(file_name)
    with open("output.json", 'w', encoding='utf-8') as json_file:
        json.dump(pdf_text, json_file, indent=4, ensure_ascii=False)

def readFile(file_path):
    file_extension = os.path.splitext(file_path)[1].lower()

    if file_extension == '.pdf':
        with open(file_path, 'rb') as pdf_file:
            reader = PyPDF2.PdfReader(pdf_file)
            pdf_text = {}
            for page_number in range(len(reader.pages)):
                page = reader.pages[page_number]
                pdf_text[f"Page_{page_number + 1}"] = page.extract_text().replace('\n',
                                                                                  ' ') if page.extract_text() else ""
            return pdf_text
    elif file_extension == '.docx':
        doc = docx.Document(file_path)
        doc_text = {"Content": "\n".join([para.text for para in doc.paragraphs]).replace('\n', ' ')}
        return doc_text
    elif file_extension == '.doc':
        return {}
    elif file_extension == '.jpg':
        return convertImage(file_path)
    elif file_extension == '.png':
        return convertImage(file_path)
    else:
        raise ValueError(f"Unsupported file format: {file_extension}")


def convertImage(file_path, lang='ron'):
    processed_image = preprocess_image(file_path)
    temp_filename = "result.jpg"
    cv2.imwrite(temp_filename, processed_image)
    pil_image = Image.open(temp_filename)
    custom_config = r'--oem 3 --psm 4'
    extracted_text = pytesseract.image_to_string(pil_image, lang=lang, config=custom_config)
    return extracted_text





def preprocess_image(image_path):
    image = cv2.imread(image_path)
    grayscale_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    scale_factor = 4.0       # Asta influenteaza mult textul schimbarea de la 4 la 5 and more
    new_width = int(grayscale_image.shape[1] * scale_factor)
    new_height = int(grayscale_image.shape[0] * scale_factor)
    resized_image = cv2.resize(grayscale_image, (new_width, new_height), interpolation=cv2.INTER_LINEAR)

    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
    contrast_enhanced_image = clahe.apply(resized_image)

    denoised_image = cv2.medianBlur(contrast_enhanced_image, 3)
    _, binary_image = cv2.threshold(denoised_image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    return binary_image



