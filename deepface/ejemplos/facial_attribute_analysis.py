from deepface import DeepFace

obj = DeepFace.analyze( img_path = "/home/raul/EjerciciosIoT/git/apertura_puertas_reconocimiento/deepface/aifaces/imagen_generada_ai_1.jpg", actions = ['age', 'gender', 'race', 'emotion'] )

print ( "--------- Resultado del análisis: " )
print ( obj )

#result = DeepFace.verify(img1_path = "/home/raul/EjerciciosIoT/git/apertura_puertas_reconocimiento/deepface/aifaces/Emilia_clarke_1.jpg", img2_path = "/home/raul/EjerciciosIoT/git/apertura_puertas_reconocimiento/deepface/aifaces/Emilia_clarke_2.jpg" )
#print ( "--------- Resultado del análisis: " )
#print ( result )

