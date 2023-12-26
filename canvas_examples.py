from kivy.lang import Builder
from kivy.metrics import dp
from kivy.properties import Clock
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.graphics.vertex_instructions import Line, Rectangle, Ellipse

Builder.load_file("canvas_examples.kv")

class CanvasExample1(Widget):
    pass

class CanvasExample2(Widget):
    pass

class CanvasExample3(Widget):
    pass

class CanvasExample4(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        with self.canvas:
            self.rect = Rectangle(pos=(200, 200), size=(150, 100))

    def on_button_a_click(self):
        x, y = self.rect.pos
        w, h = self.rect.size
        inc = dp(10)

        diff = self.width - (x + w)
        if diff < inc:
            inc = diff

        x += inc
        self.rect.pos = (x, y)

class CanvasExample5(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.ball_size = dp(50)
        self.vx = dp(3)
        self.vy = dp(4)
        with self.canvas:
            self.ball = Ellipse(pos=self.center, size=(self.ball_size, self.ball_size))
        Clock.schedule_interval(self.update, 1/60)

    def on_size(self, *args):
        self.ball.pos = (self.center_x-self.ball_size/2, self.center_y-self.ball_size/2)
    
    def update(self, dt):
        x, y = self.ball.pos

        if (x+self.ball_size) >= self.width:
            x = self.width-self.ball_size
            self.vx = -self.vx

        if (y+self.ball_size) >= self.height:
            y = self.height-self.ball_size
            self.vy = -self.vy

        if x < 0:
            x = 0
            self.vx = -self.vx

        if y < 0:
            y = 0
            self.vy = -self.vy

        x += self.vx
        y += self.vy

        self.ball.pos = (x, y)

class CanvasExample6(BoxLayout):
    pass
