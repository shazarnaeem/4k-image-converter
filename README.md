4K Image Converter

A web application built with Flask that allows users to upload an image, convert it to 4K resolution, and download it in various formats (JPEG, PNG, WEBP, TIFF, BMP, GIF, etc.). This app includes an intuitive interface for uploading images, selecting the desired output format, and viewing both the original and converted images.

Features

    Upload Images: Users can upload images of different formats.
    4K Conversion: Converts uploaded images to 4K resolution (3840 x 2160 pixels) using the high-quality LANCZOS filter.
    Multiple Output Formats: Offers a choice of output formats, including JPEG, PNG, WEBP, TIFF, BMP, GIF, and JPG.
    Download Option: Users can download the converted 4K image.
    Side-by-Side Comparison: Displays both the original and converted images for easy comparison.
    Responsive Design: The interface is fully responsive, providing an optimal user experience on both desktop and mobile.

Technologies Used

    Python (Flask): Backend server for handling image uploads, processing, and file management.
    HTML/CSS: Frontend structure and styling.
    JavaScript: For handling dynamic elements and client-side functionality.
    Pillow: Python Imaging Library (PIL) for image processing.
    Git: Version control for managing project updates.

Installation

Prerequisites

    Python 3.7+ should be installed on your system.
    Install Flask and Pillow by running:

     pip install flask pillow

Steps

  1) Clone the Repository:

        git clone https://github.com/your-username/4k-image-converter.git

  2) Navigate to Project Directory:

        cd 4k-image-converter

  3) Run the Application:

        python app.py

  4) Open the Web App:
        Go to http://127.0.0.1:5000 in your browser.

Usage

    Upload an Image: Click "Choose File" to upload an image.
    Select Output Format: Choose the desired output format from the dropdown.
    Convert: Click "Upload and Convert" to start the 4K conversion.
    Download: View both the original and converted images, and click "Download" to save the 4K version.



Contributing

Feel free to fork this repository, make enhancements, and submit pull requests. All contributions are welcome!
License

This project is open-source and available under the MIT License.
