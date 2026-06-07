from manim import *

class Tugaspertemuan15(ThreeDScene):
    def construct(self):

        self.set_camera_orientation(
            phi=70 * DEGREES,
            theta=-45 * DEGREES,
            zoom=0.9
        )

        axes = ThreeDAxes(
            x_range=[-10, 10, 2],
            y_range=[-10, 10, 2],
            z_range=[-5, 5, 1],
            x_length=10,
            y_length=10,
            z_length=5
        )

        self.play(Create(axes))

        title = Text(
            "Muhammad Zidni Alkausar_25109004",
            font_size=32
        )

        self.add_fixed_in_frame_mobjects(title)
        title.to_edge(UP)

        self.play(Write(title))

        formula1 = MathTex(
            r"f(x)=x^3"
        ).set_color(BLUE)

        formula2 = MathTex(
            r"f^{-1}(x)=\sqrt[3]{x}"
        ).set_color(RED)

        formula1.to_corner(UL)
        formula2.next_to(
            formula1,
            DOWN,
            aligned_edge=LEFT
        )

        self.add_fixed_in_frame_mobjects(
            formula1,
            formula2
        )

        self.play(Write(formula1))

        # fungsi utama

        graph1 = ParametricFunction(
            lambda t: axes.c2p(
                t,
                t**3,
                0
            ),
            t_range=[-2, 2],
            color=BLUE,
            stroke_width=6
        )

        self.play(Create(graph1))

        # bidang refleksi

        plane = Surface(
            lambda u, v: axes.c2p(
                u,
                u,
                v
            ),
            u_range=[-10, 10],
            v_range=[-2, 2],
            resolution=(20, 10),
            fill_opacity=0.25,
            checkerboard_colors=[
                TEAL_D,
                TEAL_E
            ]
        )

        self.play(Create(plane))

        # garis y=x

        diagonal = Line3D(
            start=axes.c2p(-10, -10, 0),
            end=axes.c2p(10, 10, 0),
            color=YELLOW,
            thickness=0.05
        )

        self.play(Create(diagonal))

        # titik contoh

        point_a = Dot3D(
            axes.c2p(2, 8, 0),
            color=GREEN
        )

        label_a = MathTex(
            "(2,8)"
        ).scale(0.7)

        label_a.move_to(
            axes.c2p(2, 8, 0) + UP
        )

        self.add_fixed_orientation_mobjects(
            label_a
        )

        self.play(
            FadeIn(point_a),
            Write(label_a)
        )

        self.wait(1)

        # titik hasil refleksi

        point_b = Dot3D(
            axes.c2p(8, 2, 0),
            color=ORANGE
        )

        label_b = MathTex(
            "(8,2)"
        ).scale(0.7)

        label_b.move_to(
            axes.c2p(8, 2, 0) + UP
        )

        self.add_fixed_orientation_mobjects(
            label_b
        )

        self.play(
            Transform(
                point_a.copy(),
                point_b
            )
        )

        self.play(
            Write(label_b)
        )

        # fungsi invers

        graph2 = ParametricFunction(
            lambda t: axes.c2p(
                t**3,
                t,
                0
            ),
            t_range=[-2, 2],
            color=RED,
            stroke_width=6
        )

        self.play(Create(graph2))
        self.play(Write(formula2))

        self.begin_ambient_camera_rotation(
            rate=0.12
        )

        self.wait(10)

        self.stop_ambient_camera_rotation()

        self.wait(2)