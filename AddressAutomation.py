# %%
import requests
import time
import pandas as pd
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
import os


# %%
# Function to reverse geocode using OpenStreetMap Nominatim API
def reverse_geocode(lat, lon):
    url = f"https://nominatim.openstreetmap.org/reverse?format=json&lat={lat}&lon={lon}"
    headers = {
        'User-Agent': 'YourAppName/1.0 (your-email@example.com)'  # Custom User-Agent
    }
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Check if the response was successful
        data = response.json()
        return data.get('display_name', 'Address not found')
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        time.sleep(1)  # Pause before retrying
        return None

# %%
# Function to process the selected file and perform reverse geocoding
def process_file(file_path):
    df = pd.read_excel(file_path)

    # Create a list to hold the results
    results = []

    # Assuming columns 'X' and 'Y' are latitude and longitude
    for index, row in df.iterrows():
        lat = row['X']  # Adjust the column name as per your data
        lon = row['Y']  # Adjust the column name as per your data
        address = reverse_geocode(lat, lon)
        
        # Append the results to the list
        results.append({'Latitude': lat, 'Longitude': lon, 'Address': address})

    # Create a DataFrame from the results
    results_df = pd.DataFrame(results)

    # Ask where to save the output file
    output_file_path = filedialog.asksaveasfilename(defaultextension=".xlsx", filetypes=[("Excel files", "*.xlsx")])

    if output_file_path:
        results_df.to_excel(output_file_path, index=False)
        messagebox.showinfo("Success", f"Results saved to {output_file_path}")
    else:
        messagebox.showwarning("Warning", "No output file selected.")

# %%
# Function to handle file selection
def select_file():
    file_path = filedialog.askopenfilename(filetypes=[("Excel files", "*.xlsx")])
    if file_path:
        process_file(file_path)
    else:
        messagebox.showwarning("Warning", "No file selected.")

# %%
# Create a simple GUI
root = tk.Tk()
root.title("Lat/Lon to Address Converter")

# %%
# Add a button to select file
select_file_btn = tk.Button(root, text="Select Excel File", command=select_file,bg="red")
select_file_btn.pack(pady=20)


# %%
# Start the GUI loop
root.geometry("300x200")
root.mainloop()



