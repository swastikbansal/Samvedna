import cv2

def capture_and_save_image():
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
    file_name = "captured_image.jpg"
    cv2.imwrite(file_name, frame)
    print(f"Image saved as {file_name}")
    
    # Release the camera
    cap.release()

capture_and_save_image()


import requests

API_URL = "https://api-inference.huggingface.co/models/dima806/facial_emotions_image_detection"
headers = {"Authorization": "Bearer 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"}

def query(filename):
    with open(filename, "rb") as f:
        data = f.read()
    response = requests.post(API_URL, headers=headers, data=data)
    return response.json()

output = query("C:\\Users\\vidit shrama\\codeCult\\captured_image.jpg")

print(output[0])