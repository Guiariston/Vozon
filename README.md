# Vozon

Uma breve descrição: Vozon é um projeto em Python desenvolvido para explorar comandos de voz e interação com assistentes virtuais. O objetivo é permitir que o usuário se comunique por voz com o sistema, que processa o áudio e retorna respostas em tempo real.
O sistema utiliza bibliotecas de reconhecimento de fala e síntese de voz, podendo ser expandido para integração com APIs externas (como OpenAI, Google Speech-to-Text, entre outras). É um estudo prático em interfaces baseadas em voz, automação e acessibilidade.

##  Funcionalidades

- Descreva as principais funcionalidades que o script realiza. Exemplo:
  - Captura de áudio do microfone e conversão para texto.
  - Geração de resposta via biblioteca de TTS (Text-to-Speech).
  - Integração com serviços externos (como OpenAI, Google Speech-to-Text, etc.).
  - Controles de fluxo (comandos personalizados, netrada por voz).

##  Pré-requisitos

- Python 3.x  
- Bibliotecas usadas (liste por exemplo):
  - `pyaudio`
  - `speech_recognition`
  - `gTTS`
  - `requests`

##  Instalação e uso

```bash
# Clone o repositório
git clone https://github.com/Guiariston/Vozon.git
cd Vozon

# Instalando dependências
pip install -r requirements.txt

# Executando o script
python VozON.py
