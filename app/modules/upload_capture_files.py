import asyncio
import tkinter as tk
from tkinter import filedialog

import requests

# TODO:A local file that will have the BASE_PATH written in it
url = "http://127.0.0.1:8000/network/upload"


async def choose_file():
    # TODO: Add option to upload *cap and *capng files
    capture_file_path = filedialog.askopenfilename(initialdir="/", title="Select a File",
                                                   filetypes=(("Capture Files", "*.pcap", "*.pcapng"), ("All Files", "*.*")))
    # capture_file_path = r'C:/Users/User/Downloads/evidence04.pcap'
    if capture_file_path:
        upload_file(capture_file_path)


def upload_file(capture_file_path):
    try:
        with open(capture_file_path, 'rb') as f:
            files = {'file': (capture_file_path, f, 'application/octet-stream')}
            print(files)
            response = requests.post(url, files=files)
        if response.status_code == 200:
            print("File uploaded successfully.")
            return response.json()
        else:
            print("Failed to upload the file. Response status code:", response.status_code)
    except Exception as e:
        print("Error occurred while uploading the file:", e)

# asyncio.run(choose_file())

# # Create the GUI window
# window = tk.Tk()
# window.title("File Upload")
#
# # Create a button to choose the file
# choose_button = tk.Button(window, text="Choose File", command=choose_file,padx=30, pady=30)
# choose_button.pack(pady=80 ,padx=80)
#
# # Run the GUI event loop
# window.mainloop()
