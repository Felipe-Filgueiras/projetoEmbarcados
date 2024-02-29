# Detecção de Rosto Utilizando Feed de Webcam

Este script em Python utiliza o OpenCV para realizar a detecção de rostos em tempo real usando um feed de webcam. Ele detecta rostos no fluxo de vídeo e desenha retângulos ao redor deles para destacar os rostos detectados.

## Pré-requisitos

- Python 3.x
- OpenCV (biblioteca `cv2`)
- Webcam ou câmera IP com URL de streaming acessível

## Instalação

Certifique-se de ter o Python instalado em seu sistema. Você pode instalar o OpenCV usando pip:

```bash
pip install opencv-python-headless
```

## Uso

1. Clone ou baixe o repositório.
2. Navegue até o diretório que contém o script.
3. Certifique-se de ter uma webcam conectada ao seu sistema ou forneça a URL de streaming da câmera IP apropriada.
4. Execute o script usando o seguinte comando:

```bash
python face_detection.py
```

5. Pressione 'q' para sair do programa.

## Descrição

- O script utiliza o classificador de cascata de Haar, uma abordagem baseada em aprendizado de máquina, para detecção de rostos.
- Ele carrega o arquivo XML de cascata de rosto pré-treinado (`face.xml`) para detectar rostos.
- O script captura frames de vídeo do feed da webcam ou da câmera IP e os converte em escala de cinza para uma detecção de rosto eficiente.
- Os rostos detectados são contornados com retângulos verdes no quadro original.
- O programa exibe o feed de vídeo em uma janela intitulada "Feed de Vídeo".
- Pressione 'q' para sair do programa.

## Arquivos

- `face.xml`: Arquivo XML de cascata de Haar pré-treinado para detecção de rostos.
- `reconhecimentoFacial.py`: Script Python para detecção de rosto em tempo real a partir de um feed de webcam ou câmera IP.

## Dependências

- `cv2`: Biblioteca OpenCV para tarefas de visão computacional.

## Contribuição

Autores:  
Data:
