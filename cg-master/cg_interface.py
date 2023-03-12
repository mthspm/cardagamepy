import tkinter as tk
import pygame
from client import Client
from PIL import Image, ImageTk
import threading
import json

LOGSIGIN_PATH = "imgs/logsigin.png"
SIGIN_PATH = "imgs/sigin.png"
LOGIN_PATH = "imgs/login.png"
BG_SOUND_PATH = "sounds/background_sound.mp3"

audio = None
mainWindow = None

# Class audio que controla o audio
class Audio:
    def __init__(self) -> None:
        pygame.mixer.init()
        
    def set_volume(self,volume):
        pygame.mixer.music.set_volume(volume)

    def play_sound(self,music):
        pygame.mixer.music.load(music)
        pygame.mixer.music.play()

    def stop_music(self):
        pygame.mixer.music.stop()

    def is_playing(self):
        return pygame.mixer.music.get_busy()

# Carregando uma thread que vai gerenciar o client
class ClientThread(threading.Thread):
    def __init__(self):
        super().__init__()
        self.client = Client()
        self.stop_event = threading.Event()

    def run(self):
        while not self.stop_event.is_set():
            self.client.connect()
            self.stop_event.wait(1)

    def stop(self):
        self.stop_event.set()

# Carregando as funcoes principais da main window
class SharedWindow():
    def __init__(self) -> None:
        self.client_thread = None
        pass

    def start_thread(self):
            self.client_thread = ClientThread()
            self.client_thread.start()
            return self.client_thread

    def set_title(self,title):
        self.title(title)
        return title

    def load_background(self, image):
        self.img_background = ImageTk.PhotoImage(file=image)
        fundo_label = tk.Label(self, image=self.img_background)
        fundo_label.place(x=0, y=0, relwidth=1, relheight=1)
        #define como atributo de window img_background para que nao se perca
    
    def load_resolution(self,width,height):
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x = int((screen_width - width) / 2)
        y = int((screen_height - height) / 2)
        self.geometry(f"{width}x{height}+{x}+{y}")

    def create_button(self,text,command,pady,rx,ry):
        button = tk.Button(self, text=text, font=("Arial",20), command=command)
        button.pack(pady=pady)
        button.place(relx=rx, rely=ry, anchor="center")
        return button

    def create_label(self,text,pady,rx,ry):
        label = tk.Label(self, text=text)
        label.pack(pady=pady)
        label.place(relx=rx, rely=ry, anchor="center")
        return label

    def create_entry(self,pady,rx,ry):
        entry = tk.Entry(self)
        entry.pack(pady=pady)
        entry.place(relx=rx, rely=ry, anchor="center")
        return entry

    def clear_entry(self,entrys):
        for entry in entrys:
            entry.delete(0, tk.END)

    def create_label_checknet(self):
        label = tk.Label(self, text='Sem conexao com o servidor! Verifique os logs')
        label.pack(pady=5)
        label.place(relx=0.5, rely=0.015, anchor="center")
        return label

class MainWindow(tk.Tk, SharedWindow):

    #START
    def __init__(self, audio: Audio, *args, **kwargs):
        self.audio = audio
        super().__init__(*args, **kwargs)
        self.client_thread = self.start_thread()
        self.checknet = None
        self.initialize_interface()
        #self.check_song()
        self.loginInstancia = LoginWindow(self.client_thread)
        self.signinInstancia = SigninWindow(self.client_thread)

        #INTERFACE SETUP
    def initialize_interface(self):
        self.set_title("Login & Sign-IN for CG")
        self.load_resolution(1024, 1020)
        self.load_background(LOGSIGIN_PATH)
        self.create_button('Login', self.show_login_window, 0, 0.5, 0.52)
        self.create_button('Sign In', self.show_signin_window, 0, 0.5, 0.62)
        self.create_button('Refresh', self.refresh,0,0.5,0.72)
        if self.client_thread.client.check_connection() is not True:
            self.checknet = self.create_label_checknet()

    def check_song(self):
        if self.audio.is_playing():
            pass
        else:
            self.audio.play_sound(BG_SOUND_PATH)

    def refresh(self):
        if not self.client_thread.client.check_connection():
            if not self.checknet or not self.checknet.winfo_exists():
                self.checknet = self.create_label_checknet()
        else:
            if self.checknet and self.checknet.winfo_exists():
                self.checknet.destroy()

    def show_login_window(self):

        self.withdraw()
        self.loginInstancia.deiconify()
    
    def show_signin_window(self):
        self.withdraw()
        self.signinInstancia.deiconify()

    def close(self):
        self.client_thread.stop()


class LoginWindow(tk.Toplevel, SharedWindow):

    #START
    def __init__(self, client_thread, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.initialize_interface()
        self.client_thread = client_thread
        self.withdraw()
        
    def initialize_interface(self):
        #SETUP
        self.set_title("Login for CG")
        self.load_resolution(1024, 1020)
        self.load_background(LOGIN_PATH)
        #BUTTONS
        self.create_label('Username', 5, 0.5, 0.50)
        self.username = self.create_entry(5, 0.5, 0.525)
        self.create_label('Password', 5, 0.5, 0.55)
        self.password = self.create_entry(5, 0.5, 0.575)
        self.create_button('Login', self.send_data_login, 10,0.5,0.625)
        self.create_button('Don`t have account? Back to start!', self.back_to_start, 10, 0.5, 0.95)

    def send_data_login(self):
        user,pw = self.username.get(),self.password.get()
        data = {'user':user, 'password':pw}
        self.client_thread.client.send_data('login', data)

        return user,pw

    def back_to_start(self):
        self.clear_entry([self.username,self.password])
        self.withdraw()
        global mainWindow
        mainWindow.deiconify()

class SigninWindow(tk.Toplevel, SharedWindow):

    def __init__(self, client_thread, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.initializeInterface()
        self.client_thread = client_thread
        self.withdraw()

    def initializeInterface(self):

        self.set_title("SignIn for CG")
        self.load_resolution(1024,1020)
        self.load_background(SIGIN_PATH)
        self.create_label('Username',5,0.5,0.505)
        self.username = self.create_entry(5,0.5,0.53)
        self.create_label("Password",5,0.5,0.555)
        self.password = self.create_entry(5,0.5,0.58)
        self.create_label("Confirm Password",5,0.5,0.61)
        self.password_validate = self.create_entry(5,0.5,0.64)
        self.create_button("Register",self.send_data_signin,10,0.5,0.69)
        self.create_button("Already have an account? Back to start here!",self.back_to_start,10,0.5,0.95)

    def send_data_signin(self):
        user,pw,pwConfirm = self.username.get(),self.password.get(),self.password_validate.get()
        data = {'user':user, 'password':pw, 'passwordconfirm':pwConfirm}
        self.client_thread.client.send_data('signin', data)
        return user,pw,pwConfirm

    def back_to_start(self):
        self.clear_entry([self.username,self.password,self.password_validate])
        self.withdraw()
        global mainWindow
        mainWindow.deiconify()

def main():
    global audio, mainWindow
    audio = Audio()
    mainWindow = MainWindow(audio)
    

    mainWindow.mainloop()

main()