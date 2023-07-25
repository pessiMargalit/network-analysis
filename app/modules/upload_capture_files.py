import tkinter as tk
from tkinter import filedialog
import requests


def choose_file():
    file_path = filedialog.askopenfilename(initialdir="/", title="Select a File",
                                           filetypes=(("Capture Files", "*.pcap"), ("All Files", "*.*")))
    if file_path:
        upload_file(file_path)


def upload_file(file_path):
    try:
        # Your upload logic goes here
        # Replace 'https://example.com/upload' with the URL of your server for file upload
        response = requests.post('https://example.com/upload', files={'file': open(file_path, 'rb')})

        # Check the response to verify the upload was successful
        if response.status_code == 200:
            print("File uploaded successfully.")
        else:
            print("Failed to upload the file. Response status code:", response.status_code)

    except Exception as e:
        print("Error occurred while uploading the file:", e)

choose_file()
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
