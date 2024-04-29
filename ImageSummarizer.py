import cv2
import os
import requests

class ImageSummarizer:
    def capture_and_save_image(self):
        # Open the default camera (usually the webcam)
        cap = cv2.VideoCapture(0)

        if not cap.isOpened():
            print("Error: Unable to open camera.")
            return

        # Capture a frame
        ret, frame = cap.read()

        if not ret:
            print("Error: Unable to capture frame.")
            cap.release()
            return

        # Save the captured frame
        file_name = "general_image.jpg"
        cv2.imwrite(file_name, frame)
        print(f"Image saved as {file_name}")

        # Release the camera
        cap.release()

    API_URL = "https://api-inference.huggingface.co/models/Salesforce/blip-image-captioning-large"
    headers = {"Authorization": "Bearer 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"}

    def query(self, filename):
        with open(filename, "rb") as f:
            data = f.read()
        response = requests.post(self.API_URL, headers=self.headers, data=data)
        return response.json()