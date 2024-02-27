# PDF Comparison and Difference Highlighting Toolkit
This toolkit consists of three distinct scripts designed to compare PDF documents and highlight differences between them. Each script serves a unique purpose, from detailed pixel-level comparison to focusing on significant changes, and employing advanced image processing techniques for specific region analysis.

## 1. Pixel-Level Difference Highlighting
### Overview
The first script converts PDF pages into images and performs a pixel-by-pixel comparison between two selected PDF files. It highlights every difference in red, making it easy to visualize changes between the documents.

### Key Features
- Converts PDF pages to images.
- Compares two PDFs at the pixel level.
- Highlights all differences in red on the compared images.

### Usage
Ideal for scenarios where you need to identify every single difference, no matter how small, between two PDF documents.

## 2. Contour-Based Difference Highlighting for Significant Changes
### Overview
Building upon the first script, this version adds an advanced feature that identifies and highlights only significant differences. It uses contours to outline large discrepancies, ignoring minor variations that may not be relevant for certain applications.

### Enhancements
- Identifies significant differences by finding contours in the difference image.
- Highlights larger differences with contours, making it easier to spot major changes.
- Allows customization of the minimum area for differences to be considered significant.

### Usage
This script is particularly useful when you're only interested in major differences between documents, such as layout changes or large text modifications, and wish to avoid the noise of minor discrepancies.

## 3. Targeted Difference Detection in Specific Regions
### Overview
The third script diverges from the PDF comparison to demonstrate an advanced image processing technique using the FastSAM model. It's designed for detecting differences or anomalies within specific, closed regions of an image, without manual editing.

### Unique Approach
- Employs the FastSAM model for advanced image analysis.
- Capable of identifying differences or features within targeted regions.
- Offers visualization of the analysis, highlighting detected areas directly on the image.

### Usage
Suited for specialized applications where the focus is on analyzing specific parts of an image for differences or anomalies, such as quality control, surveillance, or research studies requiring detailed examination of visual data.

## Getting Started
To use these scripts, ensure you have the required dependencies installed, including `cv2`, `numpy`, `pdf2image`, and `tkinter` for the first two scripts, and the `ultralytics` package for the third script. Each script is designed with a specific use case in mind, allowing for flexibility in how you approach document and image comparison tasks.
