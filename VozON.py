import google.generativeai as genai
import speech_recognition as sr
import pyttsx3

# Configura sua API KEY
genai.configure(api_key="AIzaSyD1YGNlcfVx7RIWCME_8NpVX4pGzqrlpAs")

# Carrega o modelo Gemini (use "gemini-1.5-flash" ou "gemini-1.5-pro" se disponível)
model = genai.GenerativeModel('gemini-1.5-flash')

# Inicia um chat com histórico vazio
chat = model.start_chat(history=[])

# Inicializa o motor de síntese de fala
motor_de_sistese_de_fala = pyttsx3.init()
voices = motor_de_sistese_de_fala.getProperty('voices')
motor_de_sistese_de_fala.setProperty('voice', voices[0].id)

# Função para falar uma frase
def falar(frase):
    motor_de_sistese_de_fala.say(frase)
    motor_de_sistese_de_fala.runAndWait()
    motor_de_sistese_de_fala.stop()

# Remove caracteres especiais do texto
def remover_caracteres_especiais(texto):
    texto_sem_asteriscos = ""
    for caractere in texto:
        if caractere not in "*!@$%&''-+.*/=+-_":
            texto_sem_asteriscos += caractere
    return texto_sem_asteriscos

# Função para reconhecer fala do usuário
def reconhecer_fala():
    microfone = sr.Recognizer()
    with sr.Microphone() as source:
        microfone.adjust_for_ambient_noise(source)
        falar('Sobre o que você quer conversar? ')
        audio = microfone.listen(source)

        for _ in range(5):
            try:
                frase_reconhecida = microfone.recognize_google(audio, language='pt')
                falar('Você disse:')
                falar(frase_reconhecida)
                return frase_reconhecida
            except sr.UnknownValueError:
                falar('Não entendi o que você disse, vou encerrar a conversa.')
                break
            except sr.RequestError as e:
                falar(f'Ocorreu um erro ao reconhecer a fala: {e}')
                break
    return None

# Saudação inicial
falar('Seja bem-vindo ao Chatoz')
falar('Para encerrar a conversa diga FIM')

# Loop principal da conversa
def iniciar_conversa():
    prompt = reconhecer_fala()
    while prompt and prompt.lower() != 'fim':
        response = chat.send_message(prompt)
        falar(remover_caracteres_especiais(response.text))
        prompt = reconhecer_fala()
    falar('Você encerrou a conversa.')

iniciar_conversa()