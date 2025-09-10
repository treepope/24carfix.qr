import qrcode 
from PIL import Image

# URL to be encoded in the QR code
url = "https://app.24carfix.com/"
file_name = "24carfix-webapp.png"

# Create a QR code object
qr = qrcode.QRCode(
    version=1,  # Controls the size of the QR code (1 is the smallest)
    error_correction=qrcode.constants.ERROR_CORRECT_L,  # Error correction level
    box_size=10,  # Size of each box in the QR code grid
    border=2,  # Thickness of the border
)

# Add the URL data to the QR code
qr.add_data(url)
qr.make(fit=True)

# Create an image from the QR code
img = qr.make_image(fill='black', back_color='white')

# Save the image as a PNG file
img.save(file_name)

print(f'QR Code generated and saved as {file_name}')
