from manim import *

class TestMath(Scene):
    def construct(self):
        eq = MathTex(r"f(x)=x^3")
        self.play(Write(eq))
        self.wait(2)