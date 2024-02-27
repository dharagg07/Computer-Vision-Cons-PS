from ultralytics import FastSAM
from ultralytics.models.fastsam import FastSAMPrompt
import matplotlib.pyplot as plt
import cv2

# Define an inference source
source = '/content/drive/MyDrive/Computer_Vision/page10.jpg'  # Adjust to your image path

# Create a FastSAM model
# Ensure the model path is correct and points to a valid FastSAM model file
model = FastSAM('/content/FastSAM-x.pt')  # Adjust model path and device as needed

# Run inference on an image
# Adjust parameters as needed for your specific case
everything_results = model(source, device='cuda',retina_masks=True, imgsz=1024, conf=0.6, iou=0.9,save=True, show =True)
