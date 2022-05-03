from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button


class MyGridLayout(GridLayout):
    def __init__(self,**kwargs):
        super(MyGridLayout, self).__init__(**kwargs)
        self.cols = 2

        self.add_widget(Label(text = "Name",font_size=20))
        self.name = TextInput(multiline=False,font_size=20)
        self.add_widget(self.name)

        self.add_widget(Label(text="Favourite Pizza",font_size=20))
        self.pizza = TextInput(multiline=False,font_size=20)
        self.add_widget(self.pizza)

        self.add_widget(Label(text="Favourite Color",font_size=20))
        self.color = TextInput(multiline=False,font_size=20)
        self.add_widget(self.color)

        self.submit = Button(text="submit",font_size=20)
        self.add_widget(self.submit)





class MyApp(App):
    def build(self):
        return MyGridLayout()

if __name__ == "__main__":
    MyApp().run()