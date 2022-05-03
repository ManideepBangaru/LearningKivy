from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class MyGridLayout(GridLayout):
    # Initialize infinite keywords
    def __init__(self,**kwargs):
        # Call grid layout constructor
        super(MyGridLayout,self).__init__(**kwargs)

        # set columns
        self.cols = 2

        # Add widgets
        self.add_widget(Label(text = "Name: ",font_size=20))

        # Add text input box
        self.name = TextInput(multiline=False,font_size=20)
        self.add_widget(self.name)

        # Add widgets
        self.add_widget(Label(text = "Favourite Pizza: ",font_size=20))

        # Add text input box
        self.pizza = TextInput(multiline=False,font_size=20)
        self.add_widget(self.pizza)

        # Add widgets
        self.add_widget(Label(text = "Favourite Color: ",font_size=20))

        # Add text input box
        self.Color = TextInput(multiline=False,font_size=20)
        self.add_widget(self.Color)

        # Create a submit button
        self.submit = Button(text="Submit",font_size = 30)
        self.submit.bind(on_press=self.press)
        self.add_widget(self.submit)

    def press(self,instance):
        name = self.name.text
        pizza = self.pizza.text
        color = self.Color.text
        # print to the terminal
        # print("Hello %s, you like %s and your favourite color is %s"%(name,pizza,color))
        # print to the screen
        self.add_widget(Label(text="Hello %s, you like %s and your favourite color is %s"%(name,pizza,color),font_size=20))
        # clear the input boxes
        self.name.text = ""
        self.pizza.text = ""
        self.Color.text = ""


class MyApp(App):
    def build(self):
        return MyGridLayout()

if __name__ == "__main__":
    MyApp().run()