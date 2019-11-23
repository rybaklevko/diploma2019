import face_recognition
from cv2 import *
import keyboard
import os
import requester
import timestamper


def are_faces_found(image_name):
    # Load the jpg file into a numpy array
    image = face_recognition.load_image_file(image_name)

    # Find all the faces in the image using the default HOG-based model.
    # This method is fairly accurate, but not as accurate as the CNN model and not GPU accelerated.
    # See also: find_faces_in_picture_cnn.py
    face_locations = face_recognition.face_locations(image)

    number_of_users = len(face_locations)

    print("I found {} face(s) in this photograph.".format(number_of_users))

    return number_of_users


def take_an_image_from_web(image_name):
    # take an image

    cam = VideoCapture(0)
    s, img = cam.read()
    if s:  # frame captured without any errors
        waitKey(0)
        imwrite(image_name, img)  # save image


def button_pressed():
    keyboard.wait("p")
    print("You pressed p")
    return True


def app_control_process():
    image_name = "image" + str(timestamper.get_timestamp()) + ".jpg"
    print("Starting process...")
    while True:
        if button_pressed():
            take_an_image_from_web(image_name)
            while not are_faces_found(image_name):
                take_an_image_from_web(image_name)
            print("image has been taken!")
            requester.send_image(os.getcwd() + "\\" + image_name)


print("Path at terminal when executing this file")
print(os.getcwd() + "\n")

app_control_process()

