from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.widget import Widget


class MyGridLayout(Widget):
    def press(self, instance):
        name = self.top_grid.name.text
        pizza = self.top_grid.pizza.text
        color = self.top_grid.Color.text
        # print to the terminal
        # print("Hello %s, you like %s and your favourite color is %s"%(name,pizza,color))
        # print to the screen
        # self.add_widget(Label(text="Hello %s, you like %s and your favourite color is %s" % (name, pizza, color),
        #                       font_size = 20))
        # # clear the input boxes
        # self.top_grid.name.text = ""
        # self.top_grid.pizza.text = ""
        # self.top_grid.Color.text = ""


class MyApp(App):
    def build(self):
        return MyGridLayout()

if __name__ == "__main__":
    MyApp().run()