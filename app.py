from flask import Flask, render_template, request
import os
import easyocr

app = Flask(__name__)

# Creates uploads directory if it doesn't exist
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Initializes the EasyOCR reader
reader = easyocr.Reader(["en"], gpu=True)

def ocr(image_location):
    text = reader.readtext(image_location, detail=0)
    return " ".join(text)
    # Joins the list into a single string for display

@app.route("/")
def home():
    return render_template("input.html")

@app.route("/", methods=["POST"])
def my_form_post():
    if "image" not in request.files:
        return render_template("output.html", data="No file uploaded.")
    
    file = request.files["image"]
    
    # Checks if the file is valid
    if file.filename == "":
        return render_template("output.html", data="No selected file.")
    
    # Saves the uploaded file temporarily
    file_path = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(file_path)
    
    # Performs OCR on the image
    text = ocr(file_path)
    
    # Removes the file after processing
    os.remove(file_path)

    return render_template("output.html", data=text)

if __name__ == "__main__":
    app.run(debug=True)
