
from kivy.app import App
from kivy.uix.button import Button
from functools import partial
class FirstKivy(App):
    #def disable(self,instance, * args):
        #instance.disabled= True
    #def update(self,instance,*args):
        #instance.text="saya dinokaktifkan!"
    def build(self):
        #mybtn=#Button(text="click me to disabled")
        #mybtn.bind(on_press=partial(self.disable,mybtn))
        #mybtn.bind(on_press=partial(self.update,mybtn))
        return Button(text="FILE",pos=(300,350),size_hint=(.18,.11))




FirstKivy().run()




