import speech_recognition as sr
mic = sr.Microphone()
r = sr.Recognizer()

from turkishnlp import detector
obj=detector.TurkishNLP()
#obj.download()
obj.create_word_set()

def recog (r):
    ses = r.listen(mic,timeout=5,phrase_time_limit=5)
    yazi = r.recognize_google(ses, language="tr-tr")
    return yazi

def corr (yazi, obj):
    lwords = obj.list_words(yazi)
    corr_list=obj.auto_correct(lwords)
    corr_phrase=' '.join([str(item) for item in corr_list])
    return corr_phrase

if __name__ == '__main__':
    with mic as source:
        r.adjust_for_ambient_noise(source)
        print("Arka plan gürültüsü:" + str(r.energy_threshold))
        try:
            print("dinliyorum...")
            yazi=recog(r)
            result=corr(yazi,obj)
            print(result)
        except sr.WaitTimeoutError:
           print("Dinleme zaman aşımına uğradı")

        except sr.UnknownValueError:
           print("Ne dediğini anlayamadım")

        except sr.RequestError:
           print("İnternete bağlanamıyorum")