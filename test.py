from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class MyGridLayout(GridLayout):
    def __init__(self,**kwargs):
        super(MyGridLayout, self).__init__(**kwargs)

        self.cols = 1

        self.top_grid = GridLayout()
        self.top_grid.cols = 2

        self.top_grid.add_widget(Label(text = "Name : ", font_size = 20))

        self.top_grid.name = TextInput(multiline=False, font_size = 20)
        self.top_grid.add_widget(self.top_grid.name)

        self.top_grid.add_widget(Label(text="Your Favourite Pizza : ",font_size=20))
        self.top_grid.pizza = TextInput(multiline=False, font_size = 20)
        self.top_grid.add_widget(self.top_grid.pizza)

        self.add_widget(self.top_grid)

        self.submit = Button(text="submit", font_size=15,
                             size_hint_y=None,
                             height = 50)
        self.submit.bind(on_press=self.press)
        self.add_widget(self.submit)

    def press(self,instance):
        name = self.top_grid.name.text
        pizza = self.top_grid.pizza.text
        self.add_widget(Label(text="Hi %s, you like %s pizza"%(name,pizza)))
        self.top_grid.name.text = ""
        self.top_grid.pizza.text = ""




class MyApp(App):
    def build(self):
        # return Label(text = "Hello")
        return MyGridLayout()

if __name__=="__main__":
    MyApp().run()