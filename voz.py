from gtts import gTTS
from playsound import playsound

audio = "audio.mp3"
language ="en"

sp = gTTS(
    text="hi, my name is jhon, and i fucked your mother aftermoon",
    lang=language
)

sp.save(audio)
playsound(audio)