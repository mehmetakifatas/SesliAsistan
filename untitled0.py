# -*- coding: utf-8 -*-
"""
Created on Wed May  1 12:04:02 2019

@author: Mehmet
"""
from gtts import gTTS 
import os
tts = gTTS(text='Merhaba Dünya', lang='tr')
tts.save("asd.mp3")
os.system("asd.mp3")