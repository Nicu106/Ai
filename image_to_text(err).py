import easyocr

def image_to_text(image_path, language='ro'):
    try:
        # Initialize the EasyOCR Reader for the desired language
        reader = easyocr.Reader([language])

        # Read the image and extract text
        result = reader.readtext(image_path, detail=0)  # detail=0 returns just the text

        # Combine the extracted text into a single string
        extracted_text = "\n".join(result)

        return extracted_text
    except Exception as e:
        return f"Error processing image: {str(e)}"

if __name__ == "__main__":
    image_path = "path_to_your_image.jpg"  # Specify your image path here
    result = image_to_text(image_path)
    print(result)


# Specify the path to your image
image_path = "1.jpg"

# Call the function and get the extracted text
extracted_text = image_to_text(image_path, language='en')

# Print the extracted text
print(extracted_text)