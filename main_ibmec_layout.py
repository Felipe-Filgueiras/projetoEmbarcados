import mediapipe as mp
import cv2 as cv
from scipy.spatial import distance as dis
import threading
import pyttsx3
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

# Configurações e constantes
STATIC_IMAGE = False
MAX_NO_FACES = 1
DETECTION_CONFIDENCE = 0.5
TRACKING_CONFIDENCE = 0.5

# Coordenadas de Landmarks
LIPS = [61, 146, 91, 181, 84, 17, 314, 405, 321, 375, 291, 308, 324, 318, 402, 317, 14, 87, 178, 88, 95, 185, 40, 39, 37, 0, 
        267, 269, 270, 409, 415, 310, 311, 312, 13, 82, 81, 42, 183, 78]
RIGHT_EYE = [33, 7, 163, 144, 145, 153, 154, 155, 133, 173, 157, 158, 159, 160, 161, 246]
LEFT_EYE = [362, 382, 381, 380, 374, 373, 390, 249, 263, 466, 388, 387, 386, 385, 384, 398]
LEFT_EYE_TOP_BOTTOM = [386, 374, 385, 263, 388, 466]
LEFT_EYE_LEFT_RIGHT = [263, 362, 249, 466, 385, 384]
RIGHT_EYE_TOP_BOTTOM = [159, 145, 158, 33, 157, 246]
RIGHT_EYE_LEFT_RIGHT = [133, 33, 246, 158, 157, 154]
UPPER_LOWER_LIPS = [13, 14, 39, 27, 35, 183]
LEFT_RIGHT_LIPS = [78, 308, 79, 80, 81, 82]
FACE = [10, 338, 297, 332, 284, 251, 389, 356, 454, 323, 361, 288, 397, 365, 379, 378, 400,
        377, 152, 148, 176, 149, 150, 136, 172, 58, 132, 93, 234, 127, 162, 21, 54, 103, 67, 109]

# Configurações de cor
COLOR_RED = (0, 0, 255)
COLOR_BLUE = (255, 0, 0)
COLOR_GREEN = (0, 255, 0)
COLOR_WHITE = (224, 224, 224)

# Configurações do MediaPipe
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_face_mesh = mp.solutions.face_mesh

# Variáveis globais para controle de exibição e thread
show_eyes = None
show_lips = None
show_tesselation = None
stop_thread = False

# Funções Auxiliares
def run_speech(speech_message):
    """Executa o alerta de áudio em uma thread separada."""
    def speech_task():
        speech = pyttsx3.init()
        speech.say(speech_message)
        speech.runAndWait()

    speech_thread = threading.Thread(target=speech_task)
    speech_thread.start()

def euclidean_distance(image, top, bottom):
    """Calcula a distância euclidiana entre dois pontos."""
    height, width = image.shape[0:2]
    point1 = int(top.x * width), int(top.y * height)
    point2 = int(bottom.x * width), int(bottom.y * height)
    return dis.euclidean(point1, point2)

def get_aspect_ratio(image, outputs, top_bottom, left_right):
    """Calcula a razão de aspecto para os olhos ou lábios."""
    if outputs and outputs.multi_face_landmarks:
        landmark = outputs.multi_face_landmarks[0]
        top = landmark.landmark[top_bottom[0]]
        bottom = landmark.landmark[top_bottom[1]]
        top_bottom_dis = euclidean_distance(image, top, bottom)
        left = landmark.landmark[left_right[0]]
        right = landmark.landmark[left_right[1]]
        left_right_dis = euclidean_distance(image, left, right)
        return left_right_dis / top_bottom_dis
    return 0

# Funções de Desenho
def draw_landmarks(image, outputs, landmarks_list, color):
    """Desenha os landmarks especificados na imagem."""
    if outputs.multi_face_landmarks:
        for face_landmarks in outputs.multi_face_landmarks:
            for idx, landmark in enumerate(face_landmarks.landmark):
                if idx in landmarks_list:
                    x, y = int(landmark.x * image.shape[1]), int
                    y = int(landmark.y * image.shape[0])
                    cv.circle(image, (x, y), 1, color, -1)
                    
def segment_face(image, outputs):
    """Extrai a região do rosto da imagem."""
    if outputs.multi_face_landmarks:
        face_landmarks = outputs.multi_face_landmarks[0]
        h, w, _ = image.shape
        min_x, min_y = w, h
        max_x = max_y = 0
        for landmark in face_landmarks.landmark:
            x, y = int(landmark.x * w), int(landmark.y * h)
            min_x, min_y = min(x, min_x), min(min_y, y)
            max_x, max_y = max(x, max_x), max(max_y, y)
        min_x, min_y = max(0, min_x), max(0, min_y)
        max_x, max_y = min(w, max_x), min(h, max_y)
        return image[min_y:max_y, min_x:max_x]
    return None

def draw_landmarks_with_lines(image, outputs, landmarks_list, color):
    """Desenha linhas conectando os landmarks especificados na imagem."""
    if outputs.multi_face_landmarks:
        for face_landmarks in outputs.multi_face_landmarks:
            for i in range(len(landmarks_list) - 1):
                point1 = face_landmarks.landmark[landmarks_list[i]]
                x1, y1 = int(point1.x * image.shape[1]), int(point1.y * image.shape[0])
                point2 = face_landmarks.landmark[landmarks_list[i + 1]]
                x2, y2 = int(point2.x * image.shape[1]), int(point2.y * image.shape[0])
                cv.line(image, (x1, y1), (x2, y2), color, 1)

def draw_tesselation(image, outputs, color):
    """Desenha a tesselação (malha facial) na imagem."""
    if outputs.multi_face_landmarks:
        for face_landmarks in outputs.multi_face_landmarks:
            mp_drawing.draw_landmarks(
                image=image,
                landmark_list=face_landmarks,
                connections=mp_face_mesh.FACEMESH_TESSELATION,
                landmark_drawing_spec=None,
                connection_drawing_spec=mp_drawing.DrawingSpec(color=color, thickness=1)
            )
            
# Função principal
def main():
    global stop_thread
    stop_thread = False
    #capture = cv.VideoCapture(1)  # Use 0 para a câmera padrão
    
    # Captura de Imagem - Streaming

# IP da câmera
    camera_ip = "http://192.168.15.6:81/video"

# Captura de Imagem
    capture = cv.VideoCapture(camera_ip)

    face_model = mp.solutions.face_mesh.FaceMesh(
        static_image_mode=STATIC_IMAGE,
        max_num_faces=MAX_NO_FACES,
        min_detection_confidence=DETECTION_CONFIDENCE,
        min_tracking_confidence=TRACKING_CONFIDENCE
    )

    frame_count = 0
    min_frame = 6
    min_tolerance = 5.0

    while not stop_thread:
        result, image = capture.read()
        if not result:
            print("Erro na captura do vídeo.")
            break

        image_rgb = cv.cvtColor(image, cv.COLOR_BGR2RGB)
        outputs = face_model.process(image_rgb)
        image = cv.resize(image, (800, 600))

        cv.rectangle(image, (20, 500), (780, 20), (255, 255, 255), 1)
        cv.rectangle(image, (20, 566), (780, 510), (255, 255, 255), -1)
        cv.putText(image, 'MONITORAMENTO DE FADIGA', (230, 547), cv.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 0), 1)

        if outputs.multi_face_landmarks:
            for face_landmarks in outputs.multi_face_landmarks:
                if show_eyes.get():
                    draw_landmarks_with_lines(image, outputs, RIGHT_EYE, COLOR_WHITE)
                    draw_landmarks_with_lines(image, outputs, LEFT_EYE, COLOR_WHITE)

                if show_lips.get():
                    draw_landmarks_with_lines(image, outputs, LIPS, COLOR_WHITE)

                if show_tesselation.get():
                    draw_tesselation(image, outputs, COLOR_GREEN)

            ratio_lips = get_aspect_ratio(image, outputs, UPPER_LOWER_LIPS, LEFT_RIGHT_LIPS)
            ratio_left = get_aspect_ratio(image, outputs, LEFT_EYE_TOP_BOTTOM, LEFT_EYE_LEFT_RIGHT)
            ratio_right = get_aspect_ratio(image, outputs, RIGHT_EYE_TOP_BOTTOM, RIGHT_EYE_LEFT_RIGHT)
            ratio_lips = get_aspect_ratio(image, outputs, UPPER_LOWER_LIPS, LEFT_RIGHT_LIPS)
        if ratio_lips < 2:
            #*****  ALERTA INTERMEDIÁRIO *****
            cv.rectangle(image, (20, 100), (780, 20), (255, 0, 0), -1)
            cv.rectangle(image, (20, 500), (780, 20), (255, 0, 0), 2)
            cv.putText(image, '*****  ALERTA  *****', (220, 70), cv.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 1)
            message = 'Alerta de Cansaço, faça uma parada!'
            p = threading.Thread(target=run_speech, args=(message,))
            p.start()

        # Alerta - Olhos Fechados
        draw_landmarks(image, outputs, LEFT_EYE_TOP_BOTTOM, None)
        draw_landmarks(image, outputs, LEFT_EYE_LEFT_RIGHT, None)
        ratio_left = get_aspect_ratio(image, outputs, LEFT_EYE_TOP_BOTTOM, LEFT_EYE_LEFT_RIGHT)

        draw_landmarks(image, outputs, RIGHT_EYE_TOP_BOTTOM, None)
        draw_landmarks(image, outputs, RIGHT_EYE_LEFT_RIGHT, None)
        ratio_right = get_aspect_ratio(image, outputs, RIGHT_EYE_TOP_BOTTOM, RIGHT_EYE_LEFT_RIGHT)

        ratio = (ratio_left + ratio_right) / 2.0

        if ratio > min_tolerance:
            frame_count += 1
        else:
            frame_count = 0

        if frame_count > min_frame:
            #*****  ALERTA MÁXIMO  *****
            cv.rectangle(image, (20, 100), (780, 20), (0, 0, 255), -1)
            cv.rectangle(image, (20, 500), (780, 20), (0, 0, 255), 2)
            cv.putText(image, '*****  ALERTA  *****', (220, 70), cv.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 1)
            message = 'Alerta de sono... pare imediatamente!'
            t = threading.Thread(target=run_speech, args=(message,))
            t.start()

        cv.imshow("SMARTAPP - Monitoramento de Fadiga 1_0", image)
        if cv.waitKey(1) & 0xFF == 27:
            break

    capture.release()
    cv.destroyAllWindows()

# Função para encerrar a thread
def set_stop_thread():
    global stop_thread
    stop_thread = True

# Criação da Interface Gráfica com Tkinter
def create_ui():
    global show_eyes, show_lips, show_tesselation
    window = tk.Tk()
    window.title("Monitoramento de Fadiga")

    show_eyes = tk.BooleanVar(window, value=True)
    show_lips = tk.BooleanVar(window, value=True)
    show_tesselation = tk.BooleanVar(window, value=True)

    start_button = ttk.Button(window, text="Iniciar Monitoramento", command=lambda: threading.Thread(target=main).start())
    start_button.pack()

    stop_button = ttk.Button(window, text="Parar Monitoramento", command=set_stop_thread)
    stop_button.pack()

    check_eyes = ttk.Checkbutton(window, text="OLHOS", variable=show_eyes)
    check_eyes.pack(anchor=tk.W)

    check_lips = ttk.Checkbutton(window, text="LABIOS", variable=show_lips)
    check_lips.pack(anchor=tk.W)

    check_tesselation = ttk.Checkbutton(window, text="MALHA", variable=show_tesselation)
    check_tesselation.pack(anchor=tk.W)

    window.mainloop()

if __name__ == "__main__":
    create_ui()