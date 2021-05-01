#from vidstream import AudioSender, AudioReceiver,ScreenShareClient, CameraClient, StreamingServer
#screenshare data and camera data received by streamingserver and audio data by audioreceiver
from vidstream import *
import tkinter as tk
import socket #to getting your private ip
import threading #because we have many cannections like audio stream send and receive data, camera send and receive data etc.
#import requests #for public ip information

local_ip_address = socket.gethostbyname(socket.gethostname()) #we get our private ip address
#print(local_ip_address)
#myip.is for public ip
#public_ip_address= requests.get('https://ipify.org').text  #'https://ipify.org' is api
#server = StreamingServer('192.168.0.207',9999) #it's private ip, when you host something you need to use private ip and others connect to your public ip

server = StreamingServer(local_ip_address, 7777) #we are going to listen on 7777 instead of 9999
receiver = AudioReceiver(local_ip_address, 6666) #6666 instead of 8888
def start_listening(): 
    t1 = threading.Thread(target=server.start_server)
    t2 = threading.Thread(target=receiver.start_server)
    t1.start()
    t2.start()
    
def start_camera_stream():
    camera_client = CameraClient(text_target_ip.get(1.0,'end-1c'),7777) #get(1.0, 'end-1c') will read untill the end of ip but not gonna have backslash at end
    t3 = threading.Thread(target=camera_client.start_stream) 
    t3.start()

def start_screen_sharing():
    screen_client = ScreenShareClient(text_target_ip.get(1.0,'end-1c'), 9999) #9999 instead of 7777
    t5 = threading.Thread(target=screen_client.start_stream) 
    t5.start()
    
def start_audio_stream():
    audio_sender = AudioSender(text_target_ip.get(1.0,'end-1c'),8888) #video is on one port so audio is on other port on the same ip
    t4 = threading.Thread(target=audio_sender.start_stream) #8888 instead of 6666
    t4.start()    
    
#GUI

window = tk.Tk()
window.title('ZoomClone')
window.geometry('300x200')#for resolution

label_target_ip = tk.Label(window, text='Target IP:')
label_target_ip.pack()

text_target_ip = tk.Text(window, height=1) #textbox of height one word
text_target_ip.pack()

btn_listen = tk.Button(window, text="Start Listening", width=50, command = start_listening) #command will jump to given function
btn_listen.pack(anchor=tk.CENTER, expand=True)

btn_camera = tk.Button(window, text="Start Camera Stream", width=50, command = start_camera_stream)
btn_camera.pack(anchor=tk.CENTER, expand=True)

btn_screen = tk.Button(window, text="Start Screen Sharing", width=50,command = start_screen_sharing)
btn_screen.pack(anchor=tk.CENTER, expand=True)

btn_audio = tk.Button(window, text="Start Audio Stream", width=50, command = start_audio_stream)
btn_audio.pack(anchor=tk.CENTER, expand=True)

window.mainloop()