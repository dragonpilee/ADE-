# Automated Data Entry System

This Python script automates data entry into forms using **PyAutoGUI**. It reads data from an Excel file and simulates keyboard inputs to enter data into an application or web form.

## Features
- Reads data from an Excel file
- Automates form filling using keyboard inputs
- Simulates tab navigation and pressing enter
- Delays execution for better accuracy

## Requirements
Make sure you have the required dependencies installed:
```bash
pip install pyautogui pandas openpyxl
```

## Usage
1. Prepare an **Excel file (`data.xlsx`)** with columns: `Name`, `Email`, `Phone`, `Address`.
2. Open the application or form where data needs to be entered.
3. Run the script:
   ```bash
   python automated_data_entry.py
   ```
4. Switch to the target application within 5 seconds.
5. The script will automatically fill in the data.

## Notes
- Ensure the target form follows the expected tab order.
- Modify the script if additional fields are needed.

## License
This project is licensed under the MIT License.

