from manim import *
import numpy as np

class CosineSurface3D(ThreeDScene):
    def construct(self):
        self.camera.background_color = "#000000"  # Set background color to black

        # Define resolution and color gradient
        resolution = 32
        def color_function(u, v):
            z = np.cos(u) * np.cos(v)
            # Map z to a color gradient: blue for negative, green for zero, yellow for positive
            alpha = (z + 1) / 2 # Map from [-1, 1] to [0, 1]
            if alpha < 0.5: # Negative z
                return interpolate_color(BLUE, GREEN, alpha * 2)
            else: # Positive z
                return interpolate_color(GREEN, YELLOW, (alpha - 0.5) * 2)

        # Create the 3D cosine surface
        surface = Surface(
            lambda u, v: np.array([u, v, np.cos(u) * np.cos(v)]),
            u_range=[-PI, PI],
            v_range=[-PI, PI],
            color_function=color_function,
            resolution=resolution,
            checkerboard_colors=[BLACK, BLACK] # Turn off checkerboard pattern
        )

        # Create axes for visual reference
        axes = ThreeDAxes(
            x_range=[-PI, PI, 1],
            y_range=[-PI, PI, 1],
            z_range=[-1.5, 1.5, 1],
            x_length=6,
            y_length=6,
            z_length=3,
            axis_config={"include_numbers": True}
        )

        # Set the initial camera position
        self.set_camera_orientation(phi=75 * DEGREES, theta=30 * DEGREES)

        # Add the objects to the scene
        self.add(axes, surface)

        # Play rotation animation
        self.play(surface.animate.rotate(angle=2 * PI, axis=OUT), run_time=5, rate_func=linear) # Rotates surface relative to its center

        # Alternatively, rotate the whole scene including axes and surface
        # self.play(axes.animate.rotate(angle=2 * PI, axis=OUT), surface.animate.rotate(angle=2 * PI, axis=OUT), run_time=5, rate_func=linear)

        # To keep the final state displayed for a bit
        self.wait()