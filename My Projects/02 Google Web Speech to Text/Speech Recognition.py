import speech_recognition as sr
r = sr.Recognizer()
mic = sr.Microphone()
mic = sr.Microphone(device_index=1)
with mic as source:
    audio = r.listen(source)

#print('Microsoft Bing Speech: ',r.recognize_bing(audio))
#print('')
print('Google Web Speech API: ',r.recognize_google(audio))
#print('')
#print('Google Cloud Speech: ',r.recognize_google_cloud(audio))
print('')
#print('Houndify by SoundHound: ',r.recognize_houndify(audio))
#print('')
#print('IBM Speech to Text: ',r.recognize_ibm(audio))
#print('')
#print('CMU Sphinx: ',recognize_sphinx(audio))
#print('')
#print('Wit.ai: ',r.recognize_wit(audio))
