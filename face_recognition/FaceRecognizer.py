import face_recognition

images = []
user_image1 = None
user_image2 = None
user_image3 = None

encoded_images = []

users_list = [{'firstName': 'Jeff', 'secondName': 'Amazon', 'imagesList':['jeff1.jpg','jeff2.jpg','jeff3.jpg']},
              {'firstName': 'Lev', 'secondName': 'Rybak', 'imagesList': ['lev1.jpg', 'lev2.jpg', 'lev3.jpg']}]


def compare_faces(known_faces_encoded, input_image):
    index = -1
    matches = face_recognition.compare_faces(known_faces_encoded, input_image)
    if True in matches:
        index = matches.index(True)

    return index


# Load the jpg file into a numpy array
def load_images(user):
    global user_image1
    user_image1=face_recognition.load_image_file(user['imagesList'][0])
    global user_image2
    user_image2=face_recognition.load_image_file(user['imagesList'][1])
    global user_image3
    user_image3 = face_recognition.load_image_file(user['imagesList'][2])

def encode_image():
    user_face_encoding1 = face_recognition.face_encodings(user_image1)[0]
    user_face_encoding2 = face_recognition.face_encodings(user_image2)[0]
    user_face_encoding3 = face_recognition.face_encodings(user_image3)[0]
    global encoded_images
    encoded_images = [
        user_face_encoding1,
        user_face_encoding2,
        user_face_encoding3
    ]

    # for image in images:
    #     encoded_images.append(face_recognition.load_image_file(image)[0])

def base_function():
    for user in users_list:
        load_images(user)
        encode_image()
        input_image = face_recognition.load_image_file("lev1.jpg")
        input_image_encoding = face_recognition.face_encodings(input_image)[0]
        name_index = compare_faces(known_faces_encoded=encoded_images, input_image=input_image_encoding)
        if -1 != name_index:
            print(user['firstName'] + ' ' + user['secondName'])
        else:
            print("Face is not found")
