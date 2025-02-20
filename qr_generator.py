import pandas as pd
import qrcode
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.moduledrawers import RoundedModuleDrawer
from qrcode.image.styles.colormasks import SolidFillColorMask
from PIL import Image, ImageDraw, ImageFont
from tkinter import Tk, filedialog
import os

# Create a Tkinter root window
root = Tk()
root.withdraw()  # Hide the main window

# Open a file dialog to select the Excel file
file_path = filedialog.askopenfilename(title="Select Excel File", filetypes=[("Excel files", "*.xlsx *.xls")])

# Check if a file was selected
if not file_path:
    raise ValueError("No file selected. Please select an Excel file.")

# Read the Excel file
df = pd.read_excel(file_path)

# Check if the 'hash' and 'ID' columns exist
if 'hash' not in df.columns or 'ID' not in df.columns:
    raise ValueError("The Excel file must contain columns named 'hash' and 'ID'.")

# Ask for the directory to save the QR codes
save_dir = filedialog.askdirectory(title="Select Directory to Save QR Codes")

# Check if a directory was selected
if not save_dir:
    raise ValueError("No directory selected. Please select a directory.")

# Base URL for redirection
base_url = "https://angelo-ascanio.github.io/foro-anual-2025-fondonorma/"

# Path to the logo image
logo_path = os.path.join(os.path.dirname(__file__), "QR_logo.png")

# Check if the logo file exists
if not os.path.exists(logo_path):
    raise ValueError("Logo image not found. Please ensure 'QR_logo.png' is in the same directory as the script.")

boder_size = 20
# Loop through the records and generate QR codes
for index, row in df.iterrows():
    hash_value = row['hash']
    id_value = row['ID']
    url = f"{base_url}?id={hash_value}"
    
    # Generate QR code
    qr = qrcode.QRCode(
        version=1,  # Lower version to reduce the number of points
        error_correction=qrcode.constants.ERROR_CORRECT_H,  # High error correction to allow for logo placement
        box_size=30,  # Increase box size to make the QR code simpler
        border=boder_size,
    )
    qr.add_data(url)
    qr.make(fit=True)
    
    img = qr.make_image(image_factory=StyledPilImage, module_drawer=RoundedModuleDrawer(), color_mask=SolidFillColorMask(back_color=(255, 255, 255), front_color=(83, 83, 83)))
    
    # Open the logo image
    logo = Image.open(logo_path)
    
    # Resize the logo while maintaining aspect ratio
    logo.thumbnail((img.size[0] // 4, img.size[1] // 4), Image.LANCZOS)
    logo_position = ((img.size[0] - logo.size[0]) // 2, (img.size[1] - logo.size[1]) // 2)
    
    # Paste the logo onto the QR code
    img.paste(logo, logo_position)
    
    # Add a message below the QR code
    message = f"@FONDONORMA"
    draw = ImageDraw.Draw(img)
    
    # Use a larger font
    font_size = 150  # Adjusted font size
    font = ImageFont.truetype("arial.ttf", font_size)  # Make sure the font file is available
    
    # Calculate text position to center below the QR code
    text_bbox = draw.textbbox((0, 0), message, font=font)
    text_width, text_height = text_bbox[2] - text_bbox[0], text_bbox[3] - text_bbox[1]
    text_position = ((img.size[0] - text_width) // 2, img.size[1] - 30*boder_size/2 - text_height/2)
    
    # Draw the text with the specified color
    draw.text(text_position, message, font=font, fill=(83, 83, 83))
    
    # Save the QR code image
    img.save(os.path.join(save_dir, f"{id_value}.png"))

print("QR codes generated successfully.")
