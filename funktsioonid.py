def Loe_failist(fail:str)->list:
    """
    Me loeme info failist
    """
    f=open(fail, "r", encoding="utf-8-sig")
    jarjend=[]
    for rida in f:
        jarjend.append(rida.strip())
    f.close()
    return jarjend

def sal_failisse(fail:str, jarjend:list):
    """
    Me salvestame info failisse
    """
    f=open(fail, "w", encoding="utf-8-sig")
    for line in jarjend:
        f.write(line+"\n")
    f.close()

from gtts import gTTS
import os


def Heli(text:str, keel:str):
    """
    Helime failis
    """
    obj=gTTS(text=text, lang=keel, slow=False).save("heli.mp3")
    os.system("heli.mp3")