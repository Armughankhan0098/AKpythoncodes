import time
String='subscribe to Akpython'
wordcount=len(String.split())
print(String)
while True:
    t0=time.time()
    inputtext=str(input('Enter the Sentence:'))
    t1=time.time()
    accuracy = len(set(inputtext.split())&set(String.split())) / wordcount
    timetaken=t1-t0
    wpm=wordcount/timetaken
    print("WPM",wpm,"Accuracy",accuracy,"Timetaken",timetaken)