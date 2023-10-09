import PyPDF2
from gtts import gTTS
from playsound import playsound
from googletrans import Translator

def extract_text_from_pdf(filename):
    with open(filename, 'rb') as file:
        pdf_reader = PyPDF2.PdfReader(file)
        text = ''
        for page_num in range(len(pdf_reader.pages)):
            page = pdf_reader.pages[page_num]
            text += page.extract_text()
    return text

# Exemplo de uso
pdf_file = input("pdf file: ")
extracted_text = extract_text_from_pdf(pdf_file)

def translate_text(text):
    tradutor = Translator(service_urls=['translate.google.com'])
    traducao = tradutor.translate(text, src='en', dest='pt')
    return traducao.text

# Exemplo de uso
translated_text = translate_text(extracted_text)
print(translated_text)

audio = "Livro.mp3"
language ="pt-br"


sp = gTTS(
    text=extracted_text,
    lang=language
)

#sp.save(audio)
#playsound(audio)