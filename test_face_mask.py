from cgi import print_arguments
from time import sleep
import cv2  #Algoritmos de reconocimiento facial
import os
import mediapipe as mp
import numpy as np
from pygame import mixer
import pygame
from splash_screen_gui import *


mp_face_detection = mp.solutions.face_detection

LABELS = ["Con_mascarilla", "Sin_mascarilla"]   #Etiquetas

# Leer el modelo
face_mask = cv2.face.LBPHFaceRecognizer_create()
face_mask.read("face_mask_model.xml")

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)    #VIDEO STREAM

#   A partir del with se crea el VIDEO-STREAM con sus diferentes configuraciones
with mp_face_detection.FaceDetection(
        min_detection_confidence=0.5) as face_detection:  # Valor minimo de confianza, se descartan las menores a 0.5

    while True:
        ret, frame = cap.read()
        if ret == False:
            break
        frame = cv2.flip(frame, 1)  # QUE EL VIDEO SE VEA EN MODO ESPEJO

        height, width, _ = frame.shape
        # Frame para el video
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = face_detection.process(frame_rgb)

        # Los 2 frames, el de la camara y donde los emojis
        #nFrame = cv2.hconcat([frame, np.zeros((480, 300, 3), dtype=np.uint8)])

        # Deteccion del rostro usando mediapipe
        if results.detections is not None:
            for detection in results.detections:
                xmin = int(
                    detection.location_data.relative_bounding_box.xmin * width)
                ymin = int(
                    detection.location_data.relative_bounding_box.ymin * height)
                w = int(detection.location_data.relative_bounding_box.width * width)
                h = int(
                    detection.location_data.relative_bounding_box.height * height)
                if xmin < 0 or ymin < 0 or h < 0 or w < 0:  # ERROR AL SALIR DEL BORDE ESTABLECIDOk. Si alguien mas entra al video
                    continue
                #cv2.rectangle(frame, (xmin, ymin), (xmin + w, ymin + h), (0, 255, 0), 5)

                # Aplicamos el rostro en escala de grises y lo redimensionamos (Lo ocultamos tambien)
                face_image = frame[ymin: ymin + h, xmin: xmin + w]
                face_image = cv2.cvtColor(face_image, cv2.COLOR_BGR2GRAY)
                face_image = cv2.resize(
                    face_image, (72, 72), interpolation=cv2.INTER_CUBIC)

                # Valor de confianza y el label que usaremos mas adelante
                result = face_mask.predict(face_image)
                # cv2.putText(frame, "{}".format(result), (xmin, ymin - 5),
                #           1, 1.3, (210, 124, 176), 1, cv2.LINE_AA)

                # Validar si detecta la mascarilla (Si esta en el rango es verde si no rojo)
                if result[1] < 150:
                    color = (0, 255, 0) if LABELS[result[0]] == "Con_mascarilla" else (0, 0, 255)  # Lo dejamos en color rojo

                    if LABELS[result[0]] == "Con_mascarilla":
                        print("Lleva mascarilla")
                    else:
                        print("No lleva xd")
                        mixer.init()
                        soundObj = pygame.mixer.Sound('Beep.mp3')
                        soundObj.play()
                        #mixer.music.load('stranger_in_paradise.mpeg')   #Grande ray coniff
                        #mixer.music.play()

                    cv2.putText(frame, "{}".format(LABELS[result[0]]), (xmin, ymin - 15), 2, 1, color, 1, cv2.LINE_AA)
                    cv2.rectangle(frame, (xmin, ymin),(xmin + w, ymin + h), color, 2)

        cv2.imshow("Detector de mascarilla", frame)
        k = cv2.waitKey(1)
        if k == 27:  # SALIMOS CON "ESC"
            break

    
cap.release()
cv2.destroyAllWindows()
