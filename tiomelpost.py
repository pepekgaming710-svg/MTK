from manim import *

class AlgebraInverse3D(ThreeDScene):
    def construct(self):

        # ==========================
        # Kamera
        # ==========================
        self.set_camera_orientation(
            phi=70 * DEGREES,
            theta=-45 * DEGREES,
            zoom=0.9
        )

        # ==========================
        # Sumbu 3D
        # ==========================
        axes = ThreeDAxes(
            x_range=[-3, 3, 1],
            y_range=[-3, 3, 1],
            z_range=[-3, 3, 1],
            x_length=8,
            y_length=8,
            z_length=6,
        )

        self.play(Create(axes))

        # ==========================
        # Label sumbu (stabil)
        # ==========================
        x_label = Tex("x").scale(0.8)
        y_label = Tex("y").scale(0.8)
        z_label = Tex("z").scale(0.8)

        x_label.move_to(axes.x_axis.get_end() + RIGHT * 0.4)
        y_label.move_to(axes.y_axis.get_end() + UP * 0.4)
        z_label.move_to(axes.z_axis.get_end() + OUT * 0.4)

        self.add_fixed_orientation_mobjects(
            x_label,
            y_label,
            z_label
        )

        self.add(
            x_label,
            y_label,
            z_label
        )

        title = Text(
            "Muhammad Zidni Alkausar - 25109004",
            font_size=32
        )

        title.to_edge(UP)

        self.add_fixed_in_frame_mobjects(title)

        self.play(
            Write(title)
        )


        func_formula = MathTex(
            r"f(x)=x^3"
        ).set_color(BLUE)

        inverse_formula = MathTex(
            r"f^{-1}(x)=\sqrt[3]{x}"
        ).set_color(RED)

        func_formula.to_corner(UL)

        inverse_formula.next_to(
            func_formula,
            DOWN,
            aligned_edge=LEFT
        )

        self.add_fixed_in_frame_mobjects(
            func_formula,
            inverse_formula
        )

        self.play(
            Write(func_formula)
        )

        self.play(
            Write(inverse_formula)
        )


        func = ParametricFunction(
            lambda t: axes.c2p(
                t,
                t**3 / 3,
                1
            ),
            t_range=[-1.6, 1.6],
            color=BLUE,
            stroke_width=6
        )

        self.play(
            Create(func)
        )


        plane = Surface(
            lambda u, v: axes.c2p(
                u,
                u,
                v
            ),
            u_range=[-2.5, 2.5],
            v_range=[-2.5, 2.5],
            resolution=(20, 20),
            fill_opacity=0.25,
            checkerboard_colors=[
                TEAL_D,
                TEAL_E
            ]
        )

        self.play(
            Create(plane)
        )

        reflection_line = Line3D(
            start=axes.c2p(
                -2.5,
                -2.5,
                0
            ),
            end=axes.c2p(
                2.5,
                2.5,
                0
            ),
            color=YELLOW,
            thickness=0.05
        )

        self.play(
            Create(reflection_line)
        )

        inverse = ParametricFunction(
            lambda t: axes.c2p(
                t**3 / 3,
                t,
                -1
            ),
            t_range=[-1.6, 1.6],
            color=RED,
            stroke_width=6
        )

        self.play(
            Create(inverse)
        )

        self.begin_ambient_camera_rotation(
            rate=0.15
        )

        self.wait(10)

        self.stop_ambient_camera_rotation()

        self.wait(2)