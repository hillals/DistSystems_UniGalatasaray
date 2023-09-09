import speech_recognition as sr
mic = sr.Microphone()
r = sr.Recognizer()

from multiprocessing import Process

from turkishnlp import detector
obj = detector.TurkishNLP()
obj.download()
obj.create_word_set()

def recog(r,source, yazi):
    ses = r.listen(source, timeout=2, phrase_time_limit=5)
    yazi=r.recognize_google(ses, language='tr-tr')
    print(yazi)

def corr(yazi):
    lwords = obj.list_words(yazi)
    print(obj.auto_correct(lwords))

with sr.Microphone() as source:
    r.adjust_for_ambient_noise(source)
    print("Arka plan gürültüsü:" + str(r.energy_threshold))

    try:
        if __name__ == "__main__":
            yazi=''
            p1=Process(target=recog,args=(r,source,yazi,))
            p2=Process(target=corr,args=(yazi,))
            p1.start()
            p2.start()
            p1.join()
            p2.join()
            p1.kill()
            p2.kill()

    except sr.WaitTimeoutError:
        print("Dinleme zaman aşımına uğradı")

    except sr.UnknownValueError:
        print("Ne dediğini anlayamadım")

    except sr.RequestError:
        print("İnternete bağlanamıyorum")


