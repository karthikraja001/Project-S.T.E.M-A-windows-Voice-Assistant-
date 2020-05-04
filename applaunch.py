import os
import subprocess

apps=['notepad','vscode','chrome','movies','wordpad','word','excel','powerpoint','study files','utorrent','whatsapp','workstation','arduino','nox']

def openapp(app):
    for app in apps:
        if  apps==app:
            launch(app)

def launch(app):
    if app=="notepad":
        subprocess.Popen('C:\\Windows\\System32\\notepad.exe')
    elif app=='vscode':
        subprocess.Popen("C:\\Users\\31220\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe")
    elif app=='chrome':
        subprocess.Popen("C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe")
    elif app=='movies':
        os.startfile('D:\\ENTERTAINMENT DRIVE')
    elif apps=='study files':
        os.startfile('D:\\COLLEGE DRIVE')
    elif apps=='utorrent':
        subprocess.Popen('C:\\Users\\31220\\Desktop\\uTorrent.exe')
    elif apps=='whatsapp':
        subprocess.Popen('C:\\Users\\31220\\AppData\\Local\\WhatsApp\\WhatsApp.exe')
    elif apps=='workstation':
        subprocess.Popen("C:\\Program Files (x86)\\VMware\\VMware Workstation\\vmware.exe")
    elif apps=='arduino':
        subprocess.Popen("C:\\Program Files (x86)\\Arduino\\arduino.exe")
    elif apps=='nox':
        subprocess.Popen("D:\\Program Files\\Nox\\bin\\Nox.exe")
    elif apps=='wordpad':
        subprocess.Popen("C:\\Program Files\\Windows NT\\Accessories\\wordpad.exe")
    elif apps=='word':
        subprocess.Popen("C:\\Program Files\\Microsoft Office\\root\\Office16\\WINWORD.EXE")
    elif apps=='excel':
        subprocess.Popen("C:\\Program Files\\Microsoft Office\\root\\Office16\\EXCEL.EXE")
    elif apps=='powerpoint':
        subprocess.Popen("C:\\Program Files\\Microsoft Office\\root\\Office16\\POWERPNT.EXE")    