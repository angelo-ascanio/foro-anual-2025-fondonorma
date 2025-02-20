import json
import pandas as pd
from tkinter import Tk
from tkinter.filedialog import askopenfilename, asksaveasfilename
from cryptography.fernet import Fernet

# Hide the main Tkinter window
Tk().withdraw()

# Generate a key and save it to a file (optional)
key = Fernet.generate_key()
with open("encryption_key.key", "wb") as key_file:
    key_file.write(key)

# Load the key
with open("encryption_key.key", "rb") as key_file:
    key = key_file.read()

# Initialize the Fernet cipher
cipher_suite = Fernet(key)

# Prompt the user to select the XLSX file
file_path = askopenfilename(filetypes=[("Excel files", "*.xlsx")])

if file_path:
    # Read the Excel file
    df = pd.read_excel(file_path)

    # Convert the DataFrame to a list of dictionaries
    json_data = df.to_dict(orient='records')

    # Convert the data to a JSON string
    json_str = json.dumps(json_data, indent=4).encode()

    # Encrypt the JSON data
    encrypted_data = cipher_suite.encrypt(json_str)

    # Prompt the user to choose save location
    save_path = asksaveasfilename(defaultextension=".json", filetypes=[("JSON files", "*.json")])

    if save_path:
        with open(save_path, "wb") as json_file:
            json_file.write(encrypted_data)
        print(f"Encrypted data has been saved to {save_path}")
    else:
        print("Save operation cancelled")
else:
    print("File selection cancelled")
