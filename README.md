# Automatic License Plate Recognition (ALPR)

This project implements an end-to-end pipeline for **Automatic License Plate Recognition (ALPR)** using **YOLOv8** for license plate detection and **OCR (Optical Character Recognition)** for character recognition. The solution is designed for applications such as traffic management, law enforcement, and automated toll collection.

---

## 📂 Project Structure

---

## 🚀 Features

- **License Plate Detection**: YOLOv8 is used to detect and localize license plates in images.
- **Character Recognition**: OCR models extract alphanumeric characters from detected license plates.
- **Data Preprocessing**: Includes bounding box conversion to YOLO format and dataset splitting for training and validation.
- **Model Training**: YOLOv8 is trained on custom datasets for robust detection.
- **Inference Pipeline**: Detects license plates and recognizes characters in test images.
- **Submission File Generation**: Outputs results in the required format for evaluation.

---

## 📋 Requirements

- Python 3.8+
- Required Libraries:
  - `ultralytics`
  - `opencv-python`
  - `pandas`
  - `matplotlib`
  - `easyocr`
  - `scikit-learn`
  - `numpy`

Install dependencies using:

```bash
pip install -r requirements.txt
```

📂 Notebooks
1)Final_submission.ipynb: Contains the complete pipeline for license plate detection, character recognition, and submission file generation.
2)License_Plate_Recognition.ipynb: Explores the workflow for ALPR, including data preprocessing, YOLOv8 training, and OCR-based recognition.


🛠️ Usage
1. Set Up Tesseract: Update the Tesseract-OCR path in t.py:

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files (x86)\Tesseract-OCR\tesseract.exe"

2. Prepare Dataset:

->Place training images in license_plates_detection_train/ and license_plates_recognition_train/.
->Ensure bounding box annotations are in Licplatesdetection_train.csv and Licplatesrecognition_train.csv.

3. Train YOLOv8: Run the YOLOv8 training script in the 

notebook:model.train(data="data.yaml", epochs=50, imgsz=640, batch=16, device="cpu")

4. Run Inference: Use the trained model to detect license plates and recognize characters.

5. Generate Submission: Execute the submission generation code to create Final_submission.csv.

📊 Results
>>Detection Accuracy: Achieved robust detection of license plates using YOLOv8.
>>Recognition Accuracy: OCR successfully extracted alphanumeric characters with high precision.

📈 Future Improvements
>>Fine-tune OCR models for better recognition of Arabic characters.
>>Enhance preprocessing techniques for noisy images.
>>Increase dataset diversity for improved generalization.

🤝 Acknowledgments
>>YOLOv8 for object detection.
>>EasyOCR for character recognition.
>>Open-source datasets for training and evaluation.