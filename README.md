# Lat/Lon to Address Converter

This Python script simplifies the process of converting geographic coordinates (latitude and longitude) into human-readable addresses using the OpenStreetMap Nominatim API. It provides a user-friendly graphical interface for selecting Excel files containing coordinate data and saves the results back to an Excel file.

**Special thanks to the OpenStreetMap Nominatim API** for being a free, reliable, and efficient geocoding service. It works exceptionally well with Irish latitude and longitude data, making it a great tool for anyone working with geolocation datasets in Ireland or elsewhere.


## Why Use This Script?

Working with geolocation data often requires converting raw latitude and longitude coordinates into meaningful addresses. Manually performing this task for large datasets is tedious and error-prone. This script automates the process and provides:

- **Batch processing**: Handles multiple coordinates from an Excel file.
- **Customizable output**: Save the processed data to a new Excel file.
- **User-friendly GUI**: No need for command-line interaction.

### Who Should Use This?

- **Data Analysts**: Quickly enrich datasets with location information.
- **Researchers**: Automate geocoding for large-scale studies.
- **Non-technical Users**: The simple GUI eliminates the need for programming skills.

---

## How It Works

### Core Functionalities

#### `reverse_geocode(lat, lon)`

This function sends a request to the OpenStreetMap Nominatim API to get the address corresponding to the given latitude and longitude.

- **Parameters**:
  - `lat`: Latitude of the location.
  - `lon`: Longitude of the location.
- **Returns**:
  - A human-readable address (or "Address not found" if unsuccessful).
- **Error Handling**:
  - Catches and logs HTTP request errors.
  - Implements a delay (`time.sleep`) before retrying in case of errors.
- **Custom User-Agent**:
  The function includes a custom User-Agent header to comply with the Nominatim API’s usage policy.

#### Why Use a Custom User-Agent?

- Ensures compliance with OpenStreetMap’s [Nominatim Usage Policy](https://operations.osmfoundation.org/policies/nominatim/).
- Helps OpenStreetMap identify your application and contact you if necessary.
- Prevents your requests from being blocked.

#### `process_file(file_path)`

This function processes the selected Excel file by reading latitude and longitude columns, applying reverse geocoding, and saving the results to a new Excel file.

- **Parameters**:
  - `file_path`: Path to the input Excel file.
- **Functionality**:
  - Reads the Excel file into a DataFrame.
  - Iterates through rows to perform reverse geocoding for each coordinate.
  - Prompts the user to save the results in a new Excel file.

#### `select_file()`

Handles file selection through a graphical file dialog.

- **Functionality**:
  - Opens a dialog for selecting an Excel file (`*.xlsx`).
  - Passes the selected file path to `process_file`.

---

## Using `Tkinter` for a User-Friendly GUI

This script uses the `Tkinter` library to provide a graphical user interface (GUI). This makes the script accessible to users who might not be familiar with the command line interface (CLI).

### Benefits of Using `Tkinter`

1. **Eliminates CLI Complexity**:
   - Users don’t need to manually type file paths or run the script from the command line.
   - Reduces the chance of errors related to incorrect file paths or command syntax.

2. **Interactive File Selection**:
   - Provides a simple **file dialog** for selecting Excel files.
   - Includes an **output dialog** for saving the processed file.

3. **Visual Feedback**:
   - Displays informative **message boxes** for success or error notifications.
   - Users get clear prompts and warnings, improving usability.

### GUI Components

- **Button**: 
  - `Select Excel File`: Opens a dialog to choose an Excel file.
- **Dialogs**:
  - **Open File**: For selecting the input file.
  - **Save File**: For choosing where to save the output.
- **Message Boxes**:
  - **Success**: Confirms when the output file is saved.
  - **Warning**: Alerts when no file is selected.

---

## Sample Data Structure

The script assumes your Excel file contains at least two columns named `X` (latitude) and `Y` (longitude). If your dataset uses different names, you can adjust them within the `process_file()` function.

| X (Latitude) | Y (Longitude) |
|--------------|---------------|
| 37.7749      | -122.4194     |
| 40.7128      | -74.0060      |

The output will include an additional `Address` column:

| Latitude | Longitude | Address                               |
|----------|-----------|---------------------------------------|
| 37.7749  | -122.4194 | San Francisco, CA, USA                |
| 40.7128  | -74.0060  | New York, NY, USA                     |

---

## Setup and Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/Agnideep96/Latitude-Longitude-To-Full-Address-conversion.git
   ```

2. **Install Dependencies**:
   Ensure you have Python 3.x installed. Install the required libraries.

3. **Run the Script**:
   ```bash
   python AddressAutomation.py
   ```

---

## How to Use

1. Run the script.
2. Click the **Select Excel File** button.
3. Choose an Excel file with latitude and longitude columns.
4. Wait for processing to complete.
5. Save the output file to your desired location.

---

## Error Handling

- **Network Errors**: 
  If the Nominatim API request fails, the script retries after a short delay.
- **File Selection**:
  - Alerts if no file is selected for input or output.
  - Warns if the selected file is missing required columns.

---



Let me know if you need further modifications!
