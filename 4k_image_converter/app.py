from flask import Flask, request, render_template, send_file, redirect, url_for
from PIL import Image
import os
import re

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/uploads'
app.config['CONVERTED_FOLDER'] = 'static/converted'

# Ensure upload and converted folders exist
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
os.makedirs(app.config['CONVERTED_FOLDER'], exist_ok=True)

def sanitize_filename(filename):
    # Remove special characters and limit filename length
    filename = re.sub(r'[^\w\s-]', '', filename)  # Remove non-alphanumeric characters except for dash and space
    return filename[:50]  # Limit filename length to 50 characters

def convert_to_4k(image_path, output_path, format):
    # Map JPG to JPEG for compatibility with PIL
    if format.upper() == "JPG":
        format = "JPEG"
    
    # Open the uploaded image
    image = Image.open(image_path)
    
    # Resize the image to 4K resolution using LANCZOS filter
    target_size = (3840, 2160)
    resized_image = image.resize(target_size, Image.LANCZOS)
    
    # Save the image in the selected format
    resized_image.save(output_path, format)

@app.route('/', methods=['GET', 'POST'])
def upload_image():
    if request.method == 'POST':
        file = request.files.get('file')
        if not file or file.filename == '':
            return "No file selected"
        
        # Get selected format from the form
        selected_format = request.form.get("format", "JPEG")
        
        # Sanitize filename and save uploaded image
        safe_filename = sanitize_filename(file.filename)
        upload_path = os.path.join(app.config['UPLOAD_FOLDER'], safe_filename)
        file.save(upload_path)
        
        # Set up the path for the converted image
        converted_filename = f"4k_{safe_filename.split('.')[0]}.{selected_format.lower()}"
        converted_path = os.path.join(app.config['CONVERTED_FOLDER'], converted_filename)
        
        # Convert and save the image
        convert_to_4k(upload_path, converted_path, selected_format)
        
        # Redirect to display page with the paths of both images and format
        return redirect(url_for('display_image', 
                                original_image=safe_filename, 
                                converted_image=converted_filename, 
                                format=selected_format))

    return render_template('upload.html')

@app.route('/display')
def display_image():
    original_image = request.args.get('original_image')
    converted_image = request.args.get('converted_image')
    selected_format = request.args.get('format')
    return render_template('display.html', 
                           original_image=original_image, 
                           converted_image=converted_image, 
                           selected_format=selected_format)

@app.route('/download/<filename>')
def download_image(filename):
    return send_file(os.path.join(app.config['CONVERTED_FOLDER'], filename), as_attachment=True)
    
if __name__ == '__main__':
    app.run(debug=True)
