from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button 
from kivy.uix.image import Image
from kivy.uix.slider import Slider
from kivy.uix.switch import Switch
from kivy.uix.scatter import Scatter 
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout


class TextoApp(App):
  def build(self):
    bl = BoxLayout()
    def tex(instance,value):
      print('Se oprimió el boton')
    slide = Slider(orientation='horizontal',min=-10, max=10, value=5,value_track=True,value_track_color=(1,0,0,1))
    bt = Button(text='Hola')
    bt.bind(state=tex)
    bl.add_widget(slide)
    bl.add_widget(bt)
    return bl


if __name__ == "__main__":
  TextoApp().run()