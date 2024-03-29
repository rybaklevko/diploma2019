import face_recognition


class FaceRecognizer:
    def __init__(self):
        self.images = []
        self.encoded_images = []
        self.user_image1 = None
        self.user_image2 = None
        self.user_image3 = None

    # Load the jpg file into a numpy array
    def load_images(self, user):
        base_path = "C:\\Users\\Lev\\PycharmProjects\\face_recognition_lock_server\\server\\DB\\images\\";
        self.user_image1 = face_recognition.load_image_file(base_path + user['imagesList'][0])
        self.user_image2 = face_recognition.load_image_file(base_path + user['imagesList'][1])
        self.user_image3 = face_recognition.load_image_file(base_path + user['imagesList'][2])

    def encode_image(self):
        self.user_face_encoding1 = face_recognition.face_encodings(self.user_image1)[0]
        self.user_face_encoding2 = face_recognition.face_encodings(self.user_image2)[0]
        self.user_face_encoding3 = face_recognition.face_encodings(self.user_image3)[0]

        self.encoded_images = [
            self.user_face_encoding1,
            self.user_face_encoding2,
            self.user_face_encoding3
        ]

    def compare_faces(self, input_image):
        index = -1
        matches = face_recognition.compare_faces(self.encoded_images, input_image)
        if True in matches:
            index = matches.index(True)

        return index


def face_recognizer_base_function(users_list, input_image_path):
    found_user = {}

    face_recognizer = FaceRecognizer()
    for user in users_list:#users_list_models
        face_recognizer.load_images(user)
        face_recognizer.encode_image()

        input_image = face_recognition.load_image_file(input_image_path)
        input_image_encoding = face_recognition.face_encodings(input_image)[0]

        name_index = face_recognizer.compare_faces(input_image=input_image_encoding)
        if -1 != name_index:
            print(user['firstName'] + ' ' + user['secondName'])
            found_user['firstName'] = user['firstName']
            found_user['secondName'] = user['secondName']

            break
        else:
            print("Face is not found")

    return found_user
