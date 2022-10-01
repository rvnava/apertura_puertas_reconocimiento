from deepface import DeepFace

#Buscar rostro
print ( "Buscando rostro" )
        
df = DeepFace.find( img_path = "/home/raul/EjerciciosIoT/git/apertura_puertas_reconocimiento/deepface/aifaces/Charlotte_le_Bon_ini.jpg", db_path = "/home/raul/EjerciciosIoT/git/apertura_puertas_reconocimiento/deepface/my_db" )

print ( "Resultado: " )
print ( df )


print ( "Resultado 2: " )
print ( df[0] )
