import time
import pyautogui
import pandas as pd

# Load data from Excel file
data = pd.read_excel("data.xlsx")

def enter_data(row):
    """Function to enter data into a form."""
    pyautogui.write(str(row["Name"]))  # Example field
    pyautogui.press('tab')
    pyautogui.write(str(row["Email"]))
    pyautogui.press('tab')
    pyautogui.write(str(row["Phone"]))
    pyautogui.press('tab')
    pyautogui.write(str(row["Address"]))
    pyautogui.press('enter')
    time.sleep(1)  # Delay to allow processing

# Give time to switch to the application
print("Switch to the application where data needs to be entered. Starting in 5 seconds...")
time.sleep(5)

# Loop through each row and enter data
for index, row in data.iterrows():
    enter_data(row)

print("Data entry completed successfully!")
