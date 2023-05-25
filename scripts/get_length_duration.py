import os
from mutagen.mp3 import MP3

mp3filename = ""
statinfo = os.stat(mp3filename)
length = str(statinfo.st_size)

audio = MP3(mp3filename)
duration = str(audio.info.length)

print(length, duration)
