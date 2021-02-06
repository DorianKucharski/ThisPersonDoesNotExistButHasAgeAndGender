import cv2
import requests
import time
import os
import sys


def recognize_gender_and_age(filename):
    model_mean_values = (78.4263377603, 87.7689143744, 114.895847746)
    age_list = ['(0-2)', '(4-6)', '(8-12)', '(15-20)', '(25-32)', '(38-43)', '(48-53)', '(60-100)']
    gender_list = ['Male', 'Female']

    age_net = cv2.dnn.readNet("models/age_net.caffemodel", "models/age_deploy.prototxt")
    gender_net = cv2.dnn.readNet("models/gender_net.caffemodel", "models/gender_deploy.prototxt")

    cap = cv2.VideoCapture(filename)

    _, frame = cap.read()

    blob = cv2.dnn.blobFromImage(frame, 1.0, (227, 227), model_mean_values, swapRB=False)
    gender_net.setInput(blob)
    gender_predictions = gender_net.forward()
    gender = gender_list[gender_predictions[0].argmax()]

    age_net.setInput(blob)
    age_predictions = age_net.forward()
    age = age_list[age_predictions[0].argmax()]

    age = age[1:-1].split("-")

    return gender.lower(), int(age[0]), int(age[1])


def download_image():
    url = "https://thispersondoesnotexist.com/image"
    timestamp = int(time.time())
    f = str(timestamp) + '.jpg'
    with open(f, 'wb') as handle:
        response = requests.get(url, stream=True)
        for block in response.iter_content(1024):
            if not block:
                break

            handle.write(block)
    return f


def get_person(r_gender, r_age):
    while True:
        filename = download_image()
        gender, age_min, age_max = recognize_gender_and_age(filename)

        if r_gender == gender and age_min < r_age < age_max:
            new_filename = r_gender + "_" + str(r_age) + "_" + filename
            os.rename(filename, new_filename)
            return new_filename
        else:
            os.remove(filename)


def main():
    usage = "Provide gender and age like this -> python script.py gender age \n" \
            "gender: male or female\n" \
            "age: (0,100)"

    if len(sys.argv) == 3:
        gender = sys.argv[1].lower()
        if gender in ["male", "female"]:
            try:
                age = int(sys.argv[2])
                if 0 <= age <= 100:
                    get_person(gender, age)
                    return
                else:
                    raise ValueError
            except ValueError:
                print("Wrong age")
        else:
            print("Wrong gender")

    print(usage)


if __name__ == "__main__":
    main()


