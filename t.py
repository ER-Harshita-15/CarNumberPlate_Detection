import pytesseract

# Set the correct Tesseract-OCR path
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files (x86)\Tesseract-OCR\tesseract.exe"

# Check if Tesseract is detected
print("Tesseract Version:", pytesseract.get_tesseract_version())
