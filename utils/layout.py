from manim import *
from manim_slides import Slide

class ThesisSlide(Slide):

    def slide_title(self, text):

        title = Text(text, font_size=48)

        title.to_edge(UP)

        self.add(title)

        return title