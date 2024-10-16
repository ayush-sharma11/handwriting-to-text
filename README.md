# Handwriting to Text Converter using Flask and EasyOCR

This is a simple Flask-based web-app that allows users to upload images of handwritten text and convert them into digital text using the EasyOCR library.

## Features

-   Upload images in `.png`, `.jpg`, or `.jpeg` formats.
-   Extract text from uploaded images using EasyOCR.
-   Display the extracted text on the web interface.
-   Supports English language OCR (can be extended to other languages supported by EasyOCR).
-   (WORKS BETTER WITH UPPERCASE LETTERS AND ONES WITHOUT NOISE)

Also, I have added extensive comments for you to follow along properly.

## Prerequisites

Before you begin, ensure you have the following installed:

-   Python 3.x
-   pip (Python package installer)
-   Git (optional, to clone the repository)

## How to run it

```
git clone https://github.com/ayush-sharma11/handwriting-to-text.git
cd handwriting-to-text
pip install -r requirements.txt
python app.py
```
