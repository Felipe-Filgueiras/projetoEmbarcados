
# 📺 Monitoramento de Fadiga para Motoristas de Caminhão

Este projeto Android Studio foi desenvolvido em Kotlin e utiliza a biblioteca MediaPipe para detectar pontos faciais de um motorista de caminhão enquanto ele estiver com a câmera do celular apontada para o rosto. O aplicativo monitora sinais de fadiga e envia um alerta ao detectar indícios de cansaço, recomendando que o motorista estacione o caminhão e pare de dirigir para evitar acidentes.

## Funcionalidades

- *Detecção Facial:* Utiliza a biblioteca MediaPipe para detectar pontos faciais.
- *Monitoramento de Fadiga:* Analisa os pontos faciais para identificar sinais de fadiga.
- *Alerta de Fadiga:* Envia uma notificação ao motorista sugerindo que ele pare de dirigir ao detectar sinais de fadiga.

## Tecnologias Utilizadas

- *Kotlin:* Linguagem principal para o desenvolvimento do aplicativo.
- *Android Studio:* IDE utilizada para o desenvolvimento do projeto.
- *MediaPipe:* Biblioteca utilizada para a detecção de pontos faciais.

## Instalação

1. *Clone o repositório:*
   bash
   git clone https://github.com/seu-usuario/nome-do-repositorio.git
   
2. *Abra o projeto no Android Studio:*
   - Selecione "Open an existing Android Studio project".
   - Navegue até o diretório onde você clonou o repositório e selecione-o.

3. *Configure o projeto:*
   - Certifique-se de que todas as dependências estão corretamente instaladas.
   - Sincronize o projeto com o Gradle.

4. *Execute o aplicativo:*
   - Conecte um dispositivo Android ou use um emulador.
   - Clique em "Run" no Android Studio.

## Uso

1. *Inicialização:*
   - Ao abrir o aplicativo, a câmera frontal do dispositivo será ativada.
   - O aplicativo começará a detectar pontos faciais automaticamente.

2. *Monitoramento:*
   - O aplicativo monitora os sinais de fadiga analisando a abertura dos olhos e a posição da cabeça.
   - Se sinais de fadiga forem detectados, uma notificação será enviada.

3. *Alerta:*
   - A notificação irá sugerir que o motorista pare o caminhão em um local seguro e descanse.

## Contribuição

1. *Fork o projeto.*
2. *Crie uma nova branch:*
   bash
   git checkout -b minha-nova-funcionalidade
   
3. *Faça as alterações desejadas e commit:*
   bash
   git commit -m "Adiciona minha nova funcionalidade"
   
4. *Envie para o branch original:*
   bash
   git push origin minha-nova-funcionalidade
   
5. *Crie um Pull Request.*


## Contato

- *Desenvolvedores:* Felipe Tavares, Felipe Filgueiras, Gabriel Rosa, Felipe Seda e Giovanna Amaral.

Sinta-se à vontade para enviar sugestões, reportar bugs ou contribuir com o projeto!

---

Agradecemos por utilizar nosso aplicativo e contribuir para a segurança nas estradas.

# Brainstorming


Ideia 1.


Sistema de som integrado na própria placa, fazendo com que erros humanos independam para o seu funcionamento.

Quando integrado no telefone, há diversas variáveis para interromper o funcionamento do mesmo.
Ex: Perda de telefone, esquecimento do telefone na mochila, telefone sem bateria.

## Instructions
-Etapas Gerais:

  📷 Conectar a Câmera à ESP32:
        Conecte a câmera (por exemplo, OV2640) à ESP32-WROVER-Dev seguindo o esquema de pinos especificado nas documentações.

  Desenvolver o Software:
        Use a IDE Arduino ou PlatformIO para desenvolver o software na ESP32.
        Utilize bibliotecas para capturar imagens da câmera e transmiti-las ao vivo.

  Configurar a Transmissão de Vídeo:
        Configure o ESP32 para transmitir as imagens da câmera por meio de um protocolo de transmissão de vídeo, como RTSP (Real-Time Streaming Protocol) ou MJPEG (Motion JPEG).

  Implementar a Detecção de Fadiga:
        Desenvolva ou integre um algoritmo de detecção de fadiga do motorista. Pode envolver técnicas de processamento de imagem, como detecção de olhos fechados, bocejos, ou análise de movimentos da cabeça.

  Integração e Teste:
        Integre a detecção de fadiga ao fluxo de vídeo.
        Realize testes para garantir que o sistema detecta corretamente a fadiga do motorista.

  Transmissão de Dados:
        Pode ser necessário implementar uma solução para transmitir dados relevantes para um servidor ou outro dispositivo, dependendo dos requisitos do seu projeto.

  Implementar Medidas de Segurança:
        Implemente medidas de segurança para garantir que a transmissão de imagens e dados seja segura e privada.

  Otimização e Melhorias:
        Otimize o código e faça melhorias conforme necessário para garantir um desempenho eficiente e uma detecção confiável.

## Items Used (Hardware)
-ESP32-WROVER-Dev

-Câmera

## Apps and Tools

## opencv
- para inverter a image: img = cv.flip(img, 0)

## How it Streams Video
The ESP32 Wrover, a versatile microcontroller module renowned for its robust Wi-Fi and Bluetooth capabilities, offers the ability to stream video through a concise yet efficient process. Leveraging camera modules like the OV7670 or OV2640, the ESP32 captures video frames, transforming them into pixel data for subsequent processing. These frames undergo essential tasks such as resizing, encoding, or compression, optimizing them for transmission across wireless networks. Harnessing its built-in Wi-Fi or Bluetooth functionalities, the ESP32 establishes seamless connections with receiving devices, facilitating real-time transmission of the processed video frames. Upon reception, these frames are decoded and can be promptly displayed, stored, or further processed as per application requirements. This capability makes the ESP32 Wrover an invaluable tool for diverse applications ranging from remote surveillance to IoT projects necessitating efficient visual data transmission, albeit requiring considerations for bandwidth limitations and processing constraints.

## Documentation
-ESP-WROVER-KIT is a highly integrated ultra-low-power development board, with rich peripheral set, Wi-Fi, and Bluetooth connectivity offered by Espressif's flagship SoC, ESP32. Create Internet cameras, smart displays, or Internet radios by connecting LCDs, microphones, and codecs. ESP32 supports JTAG debugging, while the ESP-WROVER-KIT integrates a USB debugger. This makes debugging and tracing complex applications very easy, without the need for any additional hardware. ESP32 is engineered to be fast, smart, and versatile. The ESP-WROVER-KIT complements these characteristics by offering an on-board high-speed Micro-SD card interface, VGA camera interface, as well as a 3.2 SPI LCD panel and I/O expansion capabilities. Have you been developing your applications around the ESP32-WROOM-32 module? Not only does the ESP-WROVER-KIT support the popular ESP-WROOM-32 module, but it also supports ESP32-WROVER module that has additional SPIRAM for your application's use.

Link(https://docs.espressif.com/projects/esp-idf/en/stable/esp32/hw-reference/esp32/get-started-wrover-kit.html)

## Picture
<img src="images/img1.jpeg" alt="Embedded Video Streaming Project" width="300">
---
