from manim import *

class TestLabel(Scene):
    def construct(self):
        t1 = Text("TEXT OK", font_size=60)
        self.play(Write(t1))
        self.wait(2)