import face_recognition
image = face_recognition.load_image_file("4-find-faces.jpeg")

face_locations = face_recognition.face_locations(image)
print(face_locations)

face_landmarks_list = face_recognition.face_landmarks(image)
print(face_landmarks_list)

known_image = face_recognition.load_image_file("4-find-faces-sunli.jpg")
unknown_image = face_recognition.load_image_file("4-find-faces-unknown.jpg")
unknown_image1 = face_recognition.load_image_file("4-find-faces-liutao.jpg")

sunli_encoding = face_recognition.face_encodings(known_image)[0]
unknown_encoding = face_recognition.face_encodings(unknown_image)[0]
unknown_encoding1 = face_recognition.face_encodings(unknown_image1)[0]

results = face_recognition.compare_faces([sunli_encoding], unknown_encoding)
print(results)
results = face_recognition.compare_faces([sunli_encoding], unknown_encoding1)
print(results)