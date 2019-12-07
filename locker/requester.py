# importing the requests library
import requests
import tkinter
from tkinter import messagebox


# defining the api-endpoint
API_ENDPOINT = "http://127.0.0.1:5000/web_camera_image"


def send_image(path):
        # data to be sent to api
        data = {'file_path': path}

        # sending post request and saving response as response object
        r = requests.post(url=API_ENDPOINT, data=data)

        # extracting response text
        print(r.text)

        if r.ok:
                print("Opening doors")
                root = tkinter.Tk()
                root.withdraw()
                messagebox.showinfo("Face has been found!", "Find user : %s. Opening door...")
                return True
        else:
                print("Face not found - door still closed")
                messagebox.showerror("Face hasn't been found!", "Face not found - door still closed")
                return False
        return False

