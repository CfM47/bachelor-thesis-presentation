from manim import *  # or: from manimlib import *

from manim_slides import Slide

config.background_color = WHITE

Text.set_default(color=BLACK)
Tex.set_default(color=BLACK)
MathTex.set_default(color=BLACK)
Dot.set_default(color=BLACK)

class BasicExample(Slide):
    def construct(self):
        circle = Circle(radius=3, color=BLUE)
        dot = Dot()

        self.play(GrowFromCenter(circle))
        text = Text("This is a circle").next_to(circle, UP)
        self.play(Write(text))
        self.next_slide()  # Waits user to press continue to go to the next slide

        self.next_slide(loop=True)  # Start loop
        self.play(MoveAlongPath(dot, circle), run_time=2, rate_func=linear)
        self.next_slide()  # This will start a new non-looping slide

        self.play(dot.animate.move_to(ORIGIN))