import face_recognition


def compare_faces(known_faces_encoded, input_image):
    index = -1
    matches = face_recognition.compare_faces(known_faces_encoded, input_image)
    if True in matches:
        index = matches.index(True)

    return index


# Load the jpg file into a numpy array
lev_image = face_recognition.load_image_file("lev.jpg")
obama_image = face_recognition.load_image_file("obama.jpg")


lev_face_encoding = face_recognition.face_encodings(lev_image)[0]
obama_face_encoding = face_recognition.face_encodings(obama_image)[0]

known_face_encodings = [
   obama_face_encoding,
   lev_face_encoding
]

input_image = face_recognition.load_image_file("lev1.jpg")
input_image_encoding = face_recognition.face_encodings(input_image)[0]

known_face_names = [
   "Barack Obama",
   "Lev Rybak"
]

name_index = compare_faces(known_faces_encoded=known_face_encodings, input_image=input_image_encoding)
if -1 != name_index:
    print(known_face_names[name_index])
else:
    print("Face is not found")



