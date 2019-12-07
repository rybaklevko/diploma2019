# importing the requests library
import requests
import ctypes
import json

# defining the api-endpoint
API_ENDPOINT = "http://127.0.0.1:5000/web_camera_image"


def send_image(path):
        # data to be sent to api
        data = {'file_path': path}

        # sending post request and saving response as response object
        r = requests.post(url=API_ENDPOINT, data=data)

        # extracting response text
        #print(r.json())
        #response_native = json.loads(r.text)
        #print(response_native)
        #print(response_native['first_name'])
        print(r.text)
        #print(r.json()['first_name'])



        if r.ok:
                print("Opening doors")
                ctypes.windll.user32.MessageBoxW(0, "Find user : %s. Opening door...", "Face has been found!", 0 )

                return True
        else:
                print("Face not found - door still closed")
                ctypes.windll.user32.MessageBoxW(0, "Face not found - door still closed", "Face hasn't been found!", 0)

                return False
        return False

