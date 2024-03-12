import cv2
import pytesseract
from langdetect import detect

# Set Tesseract executable path
pytesseract.pytesseract.tesseract_cmd = r'C:/Program Files/Tesseract-OCR/tesseract.exe'

def recognize_handwritten_text(image_path, output_path):
    # Load the image
    image = cv2.imread(image_path)

    # Check if the image is successfully loaded
    if image is None:
        print("Error: Unable to load the image.")
        return

    # Convert the image to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply Gaussian blur
    blurred_image = cv2.GaussianBlur(gray_image, (5, 5), 0)

    # Thresholding
    _, threshold_image = cv2.threshold(blurred_image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    # Language detection
    language = detect(pytesseract.image_to_string(threshold_image))

    # Set Tesseract language based on detected language
    lang = 'vie' if language == 'vi' else 'eng'

    # Perform OCR
    text = pytesseract.image_to_string(threshold_image, lang=lang)

    # Write the recognized text to the output file
    with open(output_path, 'w', encoding='utf-8') as output_file:
    # with open(output_path, 'a', encoding='utf-8') as output_file:
    # output_file.write("\nRecognized Text:\n")
        output_file.write(text)


    print("Recognized Text:")
    print(text)

    cv2.imshow('Original Image', image)
    cv2.imshow('Processed Image', threshold_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Example usage
image_path = 'viet.png'
output_path = 'output.txt'
recognize_handwritten_text(image_path, output_path)
