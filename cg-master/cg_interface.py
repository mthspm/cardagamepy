import tkinter as tk
import pygame
import client
from PIL import Image, ImageTk

LOGSIGIN_PATH = "imgs/logsigin.png"
SIGIN_PATH = "imgs/sigin.png"
LOGIN_PATH = "imgs/login.png"
BG_SOUND_PATH = "sounds/background_sound.mp3"

audio = None
mainWindow = None

# Carregando as funcoes principais da main window

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

class SharedWindow():
    def __init__(self) -> None:
        global clientSocket

    def set_title(self,title):
        self.title(title)

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

    def create_label(self,text,pady,rx,ry):
        label = tk.Label(self, text=text)
        label.pack(pady=pady)
        label.place(relx=rx, rely=ry, anchor="center")

    def create_entry(self,pady,rx,ry):
        entry = tk.Entry(self)
        entry.pack(pady=pady)
        entry.place(relx=rx, rely=ry, anchor="center")
        return entry

    def create_label_checknet(self):
        label = tk.Label(self,'NO CONNECTION WITH SERVER',5,0.5,0.2)
        label.pack(5)


class MainWindow(tk.Tk, SharedWindow):

    #START
    def __init__(self, audio: Audio, *args, **kwargs):
        self.audio = audio
        super().__init__(*args, **kwargs)
        self.initialize_interface()
        self.check_song()

        self.loginInstancia = LoginWindow()
        self.signinInstancia = SigninWindow()

        #INTERFACE SETUP
    def initialize_interface(self):
        self.set_title("Login & Sign-IN for CG")
        self.load_resolution(1024, 1020)
        self.load_background(LOGSIGIN_PATH)
        self.create_button('Login', self.show_login_window, 0, 0.5, 0.52)
        self.create_button('Sign In', self.show_signin_window, 0, 0.5, 0.62)

    def check_song(self):
        if self.audio.is_playing():
            pass
        else:
            self.audio.play_sound(BG_SOUND_PATH)

    def show_login_window(self):
        self.withdraw()
        self.loginInstancia.deiconify()
    
    def show_signin_window(self):
        self.withdraw()
        self.loginInstancia.deiconify()

class LoginWindow(tk.Toplevel, SharedWindow):

    #START
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.initialize_interface()
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
        self.create_button('Login', self.receive_data_login, 10,0.5,0.625)
        self.create_button('Don`t have account? Back to start!', self.back_to_start, 10, 0.5, 0.95)

    def receive_data_login(self):
        user,pw = self.username.get(),self.password.get()
        #clientconnection.sendEvent('auth', username, password)
        return user,pw

    def back_to_start(self):
        self.withdraw()
        global mainWindow
        mainWindow.deiconify()

class SigninWindow(tk.Toplevel, SharedWindow):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.initializeInterface()
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
        self.create_button("Register",self.receive_data_signin,10,0.5,0.69)
        self.create_button("Already have an account? Back to start here!",self.back_to_start,10,0.5,0.95)

    def receive_data_signin(self):
        user,pw,pwConfirm = self.username.get(),self.password.get(),self.password_validate.get()
        return user,pw,pwConfirm

    def back_to_start(self):
        self.withdraw()
        global mainWindow
        mainWindow.deiconify()

def main():
    global audio, mainWindow

    audio = Audio()
    mainWindow = MainWindow(audio)
    mainWindow.mainloop()