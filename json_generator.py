import json
import pandas as pd
from tkinter import Tk
from tkinter.filedialog import askopenfilename, asksaveasfilename

# Hide the main Tkinter window
Tk().withdraw()

# Prompt the user to select the XLSX file
file_path = askopenfilename(filetypes=[("Excel files", "*.xlsx")])

if file_path:
    # Read the Excel file
    df = pd.read_excel(file_path)

    # Convert the DataFrame to a list of dictionaries
    json_data = df.to_dict(orient='records')

    # Prompt the user to choose save location
    save_path = asksaveasfilename(defaultextension=".json", filetypes=[("JSON files", "*.json")])

    if save_path:
        with open(save_path, "w") as json_file:
            json.dump(json_data, json_file, indent=4)
        print(f"Data has been converted and saved to {save_path}")
    else:
        print("Save operation cancelled")
else:
    print("File selection cancelled")
