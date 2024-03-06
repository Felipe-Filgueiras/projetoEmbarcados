# Bibliotecas
import cv2
import mediapipe as mp

# Configurações e constantes
mp_face_mesh = mp.solutions.face_mesh
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles

# Captura de Imagem - Webcam
# webcam = cv2.VideoCapture(0) # 0 = Índice padrão de webcam

# Captura de Imagem - Streaming
# IP da câmera
camera_ip = "http://172.16.5.91:81/stream"

# Captura de Imagem
webcam = cv2.VideoCapture(camera_ip)

# Loop para demarcações faciais
while webcam.isOpened():
    sucess, img = webcam.read()
    
    # Aplicação de modelo usando mediapipe    
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img = cv2.resize(img,(837,586))
    results = mp_face_mesh.FaceMesh(max_num_faces=2,refine_landmarks = True,min_detection_confidence = 0.7,min_tracking_confidence = 0.6).process(img)
    
    # Função para desenhar os marcos faciais na imagem    
    img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
    if results.multi_face_landmarks:
        for face_landmarks in results.multi_face_landmarks:
            
            #Marcação - Malha Facial 
            mp_drawing.draw_landmarks(
                image = img,
                landmark_list = face_landmarks,
                connections = mp_face_mesh.FACEMESH_TESSELATION ,
                landmark_drawing_spec = None,
                connection_drawing_spec = mp_drawing_styles.get_default_face_mesh_tesselation_style()
                )
            
            #Marcação - Iris
            #mp_drawing.draw_landmarks(
                #image = img,
                #landmark_list = face_landmarks,
                #connections = mp_face_mesh.FACEMESH_IRISES,
                #landmark_drawing_spec = None,
                #connection_drawing_spec = mp_drawing_styles.get_default_face_mesh_iris_connections_style()
                #)
            
            #Marcação - Contorno (Rosto/Olhos/Sobrancelha/Boca)
            mp_drawing.draw_landmarks(
                image = img,
                landmark_list = face_landmarks,
                connections = mp_face_mesh.FACEMESH_CONTOURS,
                landmark_drawing_spec = None,
                connection_drawing_spec = mp_drawing_styles.get_default_face_mesh_contours_style()
                )            
            
    # Exibição de Vídeo
    cv2.imshow("SMARTCAP - Monitoramento de Fadiga 1_0",img)
    if cv2.waitKey(1) & 255 == 27: #Finalizar com ESC
        break

# Liberação de Recursos    
webcam.release()
cv2.destroyAllWindows
