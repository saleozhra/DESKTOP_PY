from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.app import App

from kivy.uix.textinput import TextInput
import time

class HelloSteemitIndonesiaABC(BoxLayout):



    def __init__(self, **kwargs):
        super(HelloSteemitIndonesiaABC, self).__init__(**kwargs)


        tombol1 = Button(text="Nama Dosen:")
        tombol1.bind(on_press=self.hello)
        self.add_widget(tombol1)

        tombol2= Button(text="Mata Kuliah:")
        tombol2.bind(on_press=self.steemit)
        self.add_widget(tombol2)

        tombol3= Button(text="Tugas Kuliah: ")
        tombol3.bind(on_press=self.indonesia)
        self.add_widget(tombol3)

        tombol4 = Button(text="Jadwal kuliah:")
        tombol4.bind(on_press=self.A)
        self.add_widget(tombol4)

        tombol5 = Button(text="Tugas kelompok :")
        tombol5.bind(on_press=self.B)
        self.add_widget(tombol5)

        tombol6 = Button(text="DAFTAR TEMAN: ")
        tombol6.bind(on_press=self.C)
        self.add_widget(tombol6)

        # label display the text on screen


    # creating the object
    # run the window




   # def build(self,obj):
        #return Button(text="FILE", pos=(300, 350), size_hint=(.18, .11))

    def hello(self, obj):
        input("Masukan nama dosen: ")
        print("--> Hello terjadi pada waktu %s" % time.ctime())

    def steemit(self, obj):
        input("Masukan jenis mata kuliah:")
        print("--> Steemit terjadi pada waktu %s" % time.ctime())

    def indonesia(self, obj):
        input("Masuakan tugas:")
        print("--> Indonesia terjadi pada waktu %s" % time.ctime())

    def A(self, obj):
        input("Masukan nama dosen: ")
        print("--> Hello terjadi pada waktu %s" % time.ctime())

    def B(self, obj):
        input("Masukan jenis mata kuliah:")
        print("--> Steemit terjadi pada waktu %s" % time.ctime())

    def C(self, obj):
        input("Masukan daftar teman:")
        print("--> Indonesia terjadi pada waktu %s" % time.ctime())

class HelloSteemitIndonesiaABCApp(App):
    def build(self):
        return HelloSteemitIndonesiaABC(pos=(5, 520), size_hint=(.96, .12) )

if __name__ == "__main__":
    myApp = HelloSteemitIndonesiaABCApp()
    print("Nama Aplikasi Saya adalah %s " %myApp.name)
    myApp.run()
