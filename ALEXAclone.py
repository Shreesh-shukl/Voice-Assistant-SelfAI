#from ast import excepthandler
import speech_recognition as sr
import pyttsx3
import pywhatkit as pw
import time
import datetime
import wikipedia
import pyjokes


listener=sr.Recognizer()
try:
    with sr.Microphone() as source:
        print('listening...')
        voice=listener.listen(source)
        command=listener.recognize_google(voice)
        command=command.lower()
        if 'alexa' in command:
            print(command)
        # print(command)
except:
    pass
time.sleep(1)

engine=pyttsx3.init()
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
#print(voices[0].id)
engine.setProperty('rate',160)
if command=='alexa what is your name' or command=='alexa tell me your name':
    engine.say("hello, my name is alexa.")
elif 'play' in command:
    command=command.replace('alexa','')
    
    pw.playonyt(command)
elif 'time' in command:
    times=datetime.datetime.now().strftime('%H:%M %p')
    print(times)
    engine.say(times)
elif 'wikipedia' in command:
    person=command.replace('wikipedia','')
    info=wikipedia.summary(person,2)
    engine.say(info)
elif 'who is' in command:
    person=command.replace('who is','')
    info=wikipedia.summary(person,1)
    engine.say(info)
elif 'tell' and 'joke' in command:
    rop=pyjokes.get_joke()
    print(rop)
    engine.say(rop)
    
elif command=='alexa':
    engine.say("What mr. Shreesh...")
elif 'tell me about' in command:
    per=command.replace('tell me about','')
    engine.say("Telling You shreesh...")
    pw.info(per, Lines=3)

    
elif 'your name' in command or command=='alexa can i ask your name' or command=='alexa can i know your name':
    engine.say("oh, why not. my name is alexa, a servent of Shreesh.")
elif 'your owner' in command or command=='alexa who is your owner' or command=='alexa who made you' or command=='alexa who coded you' or command=='alexa tell name of your owner.':
    
    engine.say("Well, both of my owner and coder is Shreesh Shukla. in addition to it, I respect him alot.")
elif command=='alexa what are you doing' or command=='alexa what work are you engaged in now':
    
    engine.say("I am simpy an artificial intelligence project, and now i am talking to you my lord.")
elif 'search' in command:
    cosearch=command.replace('alexa search','')
    engine.say(f"Searching... {cosearch}, there are some results for that")
    pw.search(cosearch)
elif command=='alexa do you love me' or command=='alexa do you like me' or command=='alexa do have some feelings for me':
    
    engine.say("why not, i love you as much as vapours love the cloud, as much as massful objects love the earth and also living beings love food.")
elif 'roshan' in command:
    
    engine.say("well, he is from m.a.i.m.s., a friend of shreesh living in the fourth room to that of shreesh. he loves cricket.")
elif 'whatsapp a message' or 'send a message' in command:
    engine.say("Please tell me whom you want to message")
    engine.runAndWait()
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice=listener.listen(source)
            nom=listener.recognize_google(voice)
            nom=nom.lower()
            if 'alexa' in nom:
                print(nom)
            # print(command)
    except:
        pass
    lenom=len(nom)
    if lenom>=10:
        lestr=str(lenom)
        roomlen='+91'+lestr
        print(roomlen)
    else:
        pass
    time.sleep(1)
    roomle=(f'{roomlen}')
    
    engine.say("Please tell me what message you want to send")
    engine.runAndWait()
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice=listener.listen(source)
            com=listener.recognize_google(voice)
            com=com.lower()
            if 'alexa' in com:
                print(com)
            # print(command)
    except:
        pass
    
    time.sleep(1)
    engine.say("Please tell me at what time, you want to send the message")
    engine.runAndWait()
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice=listener.listen(source)
            co=listener.recognize_google(voice)
            co=co.lower()
            if 'alexa' in co:
                print(co)
            # print(command)
    except:
        pass
    sr=co
    n=len(sr)
    
    if n==3:
        mr=str(sr)
        j='0'+sr
        sr=j
    else:
        j=sr
    l1=sr[0]
    l2=sr[1]
    l3=sr[2]
    l4=sr[3]
    mine=sr[2]+sr[3]
    hre=sr[0]+sr[1]
    hr=int(mine)
    min=int(hre)
    pw.sendwhatmsg('+91',f'{com}', hr, min)
        
        



else:
    engine.say("hmm, i cannot recognise that, can you please repeat")
    
    

    
time.sleep(1)
engine.runAndWait()

