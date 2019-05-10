import pyttsx3
import webbrowser
import smtplib
import random
import speech_recognition as sr
import wikipedia
import datetime
import wolframalpha
import os
import sys

engine = pyttsx3.init('sapi5')
en_voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"
engine.setProperty('voice', en_voice_id)
engine.say('')
#de_voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_DE-DE_HEDDA_11.0"

# Use female Deutchland voice
#engine.setProperty('voice', de_voice_id)
#engine.say('')
client = wolframalpha.Client('7GVLY3-E89JYA3TQ7')

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[len(voices)-1].id)

def speak(audio):
    print('Bilgisayar: ' + audio)
    engine.say(audio)
    engine.runAndWait()
def myCommand():
    r = sr.Recognizer()                                                                                   
    with sr.Microphone() as source:                                                                       
        print("Dinliyor ...")
        r.pause_threshold =  1
        audio = r.listen(source)
    try:
        query = r.recognize_google(audio, language='tr')
        print(' Kullanıcı: ' + query + '\n')
        
    except sr.UnknownValueError:
        speak('Üzgünüm efendim! Ben yapamadım,komutu yazmayı deneyin!')
        query = str(input('Komut:'))

    return query

def greetMe():
    currentH = int(datetime.datetime.now().hour)
    if currentH >= 0 and currentH < 12:
        speak('Günaydın!')

    if currentH >= 12 and currentH < 18:
        speak('İyi Öğlenler! ')

    if currentH >= 18 and currentH !=0:
        speak('İyi Akşamlar!')

greetMe()

speak('Merhaba efendim, ben dijital asistanınız SİM !')
speak('Size nasıl yardımcı olabilirim? ')


if __name__ == '__main__':

    while True:
    
        query = myCommand();
        query = query.lower()
        
        if 'hava nasıl' in query:
            speak('tamam')
            webbrowser.open('https://www.google.com.tr/search?q=elazığ+hava+durumu&rlz=')
        if 'aç youtube' in query:
            speak('tamam')
            webbrowser.open('www.youtube.com')

        elif 'aç google' in query:
            speak('tamam')
            webbrowser.open('www.google.co.in')

        elif 'aç gmail' in query:
            speak('tamam')
            webbrowser.open('www.gmail.com')

        elif "naber" in query or 'nasılsın' in query:
            stMsgs = [' Sadece işimi yapıyorum! ' , ' Ben iyiyim! ' , ' Güzel! ' , ' Ben iyiyim ve enerji doluyum ']
            speak(random.choice(stMsgs))




        elif 'mail' in query:
            speak('alıcı kim? ')
            recipient = myCommand()

            if 'bana' in recipient:
                try:
                    speak(' Ne demeliyim? ')
                    content = myCommand()
        
                    server = smtplib.SMTP('smtp.gmail.com', 587)
                    server.ehlo()
                    server.starttls()
                    server.login("kullanıcı adınız", 'şifreniz')
                    server.sendmail('kullanıcı adınız', "alıcının kullanıcı adı", content)
                    server.close()
                    speak('Email gönderildi!')

                except:
                    speak('Üzgünüm efendim! Şu anda mesajınızı gönderemiyorum!')


        elif ' hiçbir şey' in query or 'iptal' in query or 'dur' in query:
            speak('tamam')
            speak('Hoşçakalın efendim, iyi günler.')
            sys.exit()
           
        elif 'merhaba' in query:
            speak('Merhaba efendim')

        elif 'hoşçakal' in query:
            speak('Hoşçakalın efendim, iyi günler.')
            sys.exit()
                  

                  
        elif 'aç müzik' in query:
            music_folder = os.system('‪C:/Users/LENOVO/Desktop/')
            music = ['a.mp3','1.mp3']
            random_music = music_folder
            os.system(random_music)
                  
            speak('Tamam, işte müziğin! eğlenceli')
            

        else:
            query = query
            speak('Aranıyor ...')
            try:
                try:
                    res = client.query(query)
                    results = next(res.results).text
                    speak('WOLFRAM-ALPHA diyor - ')
                    speak('Anladım.')
                    speak(results)
                    
                except:
                    results = wikipedia.summary(query, sentences=2)
                    
                    speak(' Anladım.')
                    speak('WIKIPEDIA diyor - ')
                    speak(results)
        
            except:
                webbrowser.open('www.google.com')
        
        speak('Sonraki Komut! Efendim!!')
        