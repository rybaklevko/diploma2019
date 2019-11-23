# importing the requests library
import requests

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
        else:
                print("Face not found - door still closed")

