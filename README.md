# OpenCV Computer Vision Projects

This repository contains four computer vision projects implemented using OpenCV and Python. Each project demonstrates different image processing techniques and real-time applications.

## Project 1: Photo to Pencil Sketch Converter

**File:** `cv project-1.pdf`

### Overview
This project converts regular photographs into pencil sketch-style images using image processing techniques.

### Key Features
- Converts color images to grayscale
- Creates inverted grayscale images
- Applies Gaussian blur for smoothing
- Uses image division to create pencil sketch effect
- Interactive trackbars for real-time adjustment of scale and color parameters

### Techniques Used
- Color space conversion (BGR to Grayscale)
- Image inversion
- Gaussian blur filtering
- Image division operations
- Trackbar controls for parameter tuning

### Process Flow
1. Load and resize input image
2. Convert to grayscale
3. Create inverted grayscale image
4. Apply Gaussian blur to inverted image
5. Invert the blurred image
6. Divide original grayscale by inverted blur to create sketch effect

---

## Project 2: ROI Overlay using Thresholding and Bitwise Operations

**File:** `project roi using thresholding and bitwise operator.pdf`

### Overview
This project demonstrates how to overlay one image onto a specific region of interest (ROI) in another image using thresholding and bitwise operations.

### Key Features
- Region of Interest (ROI) extraction
- Binary thresholding for mask creation
- Bitwise operations for image compositing
- Background removal and foreground extraction
- Image overlay techniques

### Techniques Used
- Image resizing and ROI selection
- Grayscale conversion
- Binary thresholding (`cv2.THRESH_BINARY`)
- Bitwise operations (`bitwise_and`, `bitwise_not`)
- Image addition for final composition

### Process Flow
1. Load main image (thor.jpg) and overlay image (axe.jpg)
2. Define ROI in main image
3. Convert overlay image to grayscale
4. Apply binary thresholding to create mask
5. Create reverse mask using bitwise NOT
6. Extract background and foreground regions
7. Combine regions to create final composite image

---

## Project 3: Object Detection using Color Masking

**File:** `project object detection using masking.pdf`

### Overview
A real-time object detection system that tracks colored objects using HSV color space masking with interactive parameter adjustment.

### Key Features
- Real-time color-based object detection
- HSV color space filtering
- Interactive trackbars for HSV range adjustment
- Dynamic mask creation and application
- Live video processing

### Techniques Used
- Color space conversion (BGR to HSV)
- Range-based color masking (`cv2.inRange`)
- Bitwise operations for filtering
- Trackbar controls for real-time parameter adjustment
- Image masking and filtering

### Process Flow
1. Load input image and resize
2. Create trackbars for HSV parameter control
3. Convert image to HSV color space
4. Get trackbar values for upper and lower HSV bounds
5. Create mask using color range
6. Apply mask to original image using bitwise AND
7. Display original, mask, and filtered results

---

## Project 4: Real-time Finger Counter

**File:** `cv project-2 of finger counter.pdf`

### Overview
An advanced computer vision application that counts fingers in real-time using hand detection, contour analysis, and convexity defects.

### Key Features
- Real-time hand tracking using color detection
- Finger counting using convexity defects
- Live video feed processing
- Interactive parameter adjustment
- Cosine rule for angle calculation

### Techniques Used
- Video capture and processing
- HSV color space filtering
- Morphological operations (dilation)
- Contour detection and analysis
- Convex hull computation
- Convexity defects analysis
- Mathematical angle calculation using cosine rule

### Process Flow
1. Capture video from camera/IP camera
2. Create ROI for hand detection
3. Convert to HSV and apply color-based masking
4. Apply morphological operations to enhance mask
5. Find contours and select largest one (hand)
6. Calculate convex hull and convexity defects
7. Use cosine rule to calculate angles between defects
8. Count valid defects (fingers) based on angle threshold
9. Display finger count on screen

### Mathematical Background
The project uses the cosine rule to calculate angles:
```
a² = b² + c² - 2bc·cos(A)
```
Where angles ≤ 50° are considered valid finger separations.

---

## Dependencies

All projects require the following Python libraries:
- `opencv-python` (cv2)
- `numpy`
- `math` (for finger counter project)

## Installation

```bash
pip install opencv-python numpy
```

## Usage Notes

- Ensure proper lighting conditions for color-based detection projects
- Adjust HSV parameters using trackbars for optimal results
- For finger counter: position hand within the blue rectangle ROI
- Camera permissions may be required for real-time projects

## Applications

These projects demonstrate fundamental computer vision concepts applicable in:
- Image processing and filtering
- Real-time object tracking
- Gesture recognition systems
- Augmented reality applications
- Educational computer vision demonstrations
