import cv2
import numpy as np
from pdf2image import convert_from_path
import tkinter as tk
from tkinter import filedialog

def select_pdf_files():
    root = tk.Tk()
    root.withdraw()  # Hide the main window.
    file_paths = filedialog.askopenfilenames(title='Select two PDF files', filetypes=[("PDF files", "*.pdf")])
    return file_paths

def pdf2img(pdf_path, output_prefix):
    images = convert_from_path(pdf_path)
    for i, image in enumerate(images):
        # Save pages as images in the PDF
        image.save(f'{output_prefix}_page{i}.jpg', 'JPEG')

# Select PDF files
selected_files = select_pdf_files()
if len(selected_files) != 2:
    print("Please select exactly two PDF files.")
else:
    # Convert selected PDFs to images
    pdf2img(selected_files[0], "first")
    pdf2img(selected_files[1], "second")

    # Assume the user wants to compare specific pages, e.g., the first page of each PDF
    image1 = cv2.imread('first_page0.jpg')
    image2 = cv2.imread('second_page0.jpg')

    # Compute difference
    difference = cv2.subtract(image1, image2)


    # Color the mask red
    Conv_hsv_Gray = cv2.cvtColor(difference, cv2.COLOR_BGR2GRAY)
    ret, mask = cv2.threshold(Conv_hsv_Gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
    difference[mask == 255] = [0, 0, 255]

    # Add the red mask to the images to make the differences obvious
    image1[mask == 255] = [0, 0, 255]
    image2[mask == 255] = [0, 0, 255]

    # Store images
    cv2.imwrite('diffOverImage1.png', image1)
    cv2.imwrite('diffOverImage2.png', image2)
