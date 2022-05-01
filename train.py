import cv2
import os
import numpy as np
from skimage import io

dataPath = "C:/Users/Admin/OneDrive/Documentos/2022/Inteligencia_Artificial/Proyectito/Dataset_faces"
dir_list = os.listdir(dataPath)
print("Lista archivos:", dir_list)

labels = []     #Etiquetas para cada imagen
facesData = []
label = 0


for name_dir in dir_list:
     dir_path = dataPath + "/" + name_dir
     
     for file_name in os.listdir(dir_path):
          image_path = dir_path + "/" + file_name
          print(image_path)
          image = cv2.imread(image_path, 0)
          #image = io.imread(image_path)
          #cv2.imshow("Image", image)
          #cv2.waitKey(10)
          facesData.append(image)
          labels.append(label)
     label += 1 

#Mascarrilla etiqueta 0, sin mascarilla 1

print("Etiqueta 0: ", np.count_nonzero(np.array(labels) == 0))
print("Etiqueta 1: ", np.count_nonzero(np.array(labels) == 1))

# LBPH FaceRecognizer
face_mask = cv2.face.LBPHFaceRecognizer_create()

# Entrenamiento
print("Entrenando...")
face_mask.train(facesData, np.array(labels))

# Almacenar modelo
face_mask.write("face_mask_model.xml")
print("Modelo almacenado")