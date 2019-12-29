from gtts import gTTS
import playsound
import os
tts = gTTS(text='এইচআর টেক্সটাইল বাংলাদেশের ভেতরে একাধিক আউটলেটের মাধ্যমে শাড়ি বাচ্চাদের পোশাক মহিলাদের পোশাক এবং অন্যান্য টেক্সটাইল পণ্য উৎপাদন ও বিপণন করে', lang='bn')
tts.save("hello.mp3")
os.system("hello.mp3")
playsound.playsound('hello.mp3', True)