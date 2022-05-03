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
        self.cols = 1

        # create a upper layer of layout
        self.top_grid = GridLayout()
        self.top_grid.cols = 2

        # Add widgets
        self.top_grid.add_widget(Label(text = "Name: ",font_size=20))

        # Add text input box
        self.top_grid.name = TextInput(multiline=False,font_size=20)
        self.top_grid.add_widget(self.top_grid.name)

        # Add widgets
        self.top_grid.add_widget(Label(text = "Favourite Pizza: ",font_size=20))

        # Add text input box
        self.top_grid.pizza = TextInput(multiline=False,font_size=20)
        self.top_grid.add_widget(self.top_grid.pizza)

        # Add widget
        self.top_grid.add_widget(Label(text = "Favourite Color: ",font_size=20))

        # Add text input box
        self.top_grid.Color = TextInput(multiline=False,font_size=20)
        self.top_grid.add_widget(self.top_grid.Color)

        self.add_widget(self.top_grid)

        # Create a submit button
        self.submit = Button(text="Submit",
                             font_size = 15,
                             size_hint_y = None,
                             height=50,
                             size_hint_x = None,
                             width = 100)
        self.submit.bind(on_press=self.press)
        self.add_widget(self.submit)

    def press(self,instance):
        name = self.top_grid.name.text
        pizza = self.top_grid.pizza.text
        color = self.top_grid.Color.text
        # print to the terminal
        # print("Hello %s, you like %s and your favourite color is %s"%(name,pizza,color))
        # print to the screen
        self.add_widget(Label(text="Hello %s, you like %s and your favourite color is %s"%(name,pizza,color),font_size=20))
        # clear the input boxes
        self.top_grid.name.text = ""
        self.top_grid.pizza.text = ""
        self.top_grid.Color.text = ""


class MyApp(App):
    def build(self):
        return MyGridLayout()

if __name__ == "__main__":
    MyApp().run()