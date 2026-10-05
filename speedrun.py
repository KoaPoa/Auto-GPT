from manim import *
import numpy as np

class HistorySpeedrun(Scene):
    def construct(self):
        np.random.seed(42)

        # High Contrast / Bold Motion Graphics Palette
        BG_COLOR = "#090a0f"
        PINK = "#ff003c"
        BLUE = "#00f0ff"
        YELLOW = "#ffe600"
        WHITE = "#ffffff"

        self.camera.background_color = BG_COLOR

        # ---------------------------------------------------------
        # 0.0 - 1.0s: INTRO (1.0s)
        # ---------------------------------------------------------
        title = Text("WORLD HISTORY", font_size=72, weight=BOLD, color=WHITE)
        subtitle = Text("IN 15 SECONDS", font_size=48, weight=BOLD, color=PINK).next_to(title, DOWN)
        intro_group = VGroup(title, subtitle)

        self.play(
            Write(title, run_time=0.5, rate_func=rush_into),
            FadeIn(subtitle, shift=UP, run_time=0.5, rate_func=rush_into),
        )
        self.wait(0.5)

        # ---------------------------------------------------------
        # 1.0 - 3.0s: ANTIQUITY (2.0s)
        # ---------------------------------------------------------
        pyramid = Polygon(
            [-2.5, -1.5, 0], [2.5, -1.5, 0], [0, 2.5, 0],
            color=YELLOW, fill_opacity=1, stroke_width=0
        )
        sun = Circle(radius=1.8, color=PINK, fill_opacity=1, stroke_width=0).move_to(pyramid.get_center() + UP * 0.5)
        sun.set_z_index(-1)
        antiquity_group = VGroup(sun, pyramid)

        self.play(
            ReplacementTransform(intro_group, antiquity_group, run_time=0.8, rate_func=smooth),
        )
        # Give it a slight pulse / scale animation while waiting
        self.play(antiquity_group.animate.scale(1.05), run_time=1.2, rate_func=there_and_back)

        # ---------------------------------------------------------
        # 3.0 - 6.0s: CLASSICAL ERA (3.0s)
        # ---------------------------------------------------------
        pillar_group = VGroup()
        for i in range(5):
            pillar = Rectangle(height=4.5, width=0.6, color=WHITE, fill_opacity=1, stroke_width=0).shift(RIGHT * (i - 2) * 1.8)
            pillar_group.add(pillar)

        roof = Polygon(
            [-5.5, 2.25, 0], [5.5, 2.25, 0], [0, 4.5, 0],
            color=BLUE, fill_opacity=1, stroke_width=0
        )
        base = Rectangle(height=0.8, width=11, color=BLUE, fill_opacity=1, stroke_width=0).shift(DOWN * 2.65)
        classical_group = VGroup(base, pillar_group, roof)

        self.play(
            ReplacementTransform(antiquity_group, classical_group, run_time=1.0, rate_func=smooth),
        )
        # Subtle camera-like push in
        self.play(classical_group.animate.scale(1.1), run_time=2.0, rate_func=linear)

        # ---------------------------------------------------------
        # 6.0 - 9.0s: ENLIGHTENMENT / SCIENCE (3.0s)
        # ---------------------------------------------------------
        center_sun = Circle(radius=0.6, color=PINK, fill_opacity=1, stroke_width=0)
        orbits = VGroup()
        planets = VGroup()
        for i, angle in enumerate([0, PI/3, 2*PI/3]):
            orbit = Ellipse(width=7.5, height=2.5, color=BLUE, stroke_width=4).rotate(angle)
            orbits.add(orbit)
            planet = Circle(radius=0.3, color=YELLOW, fill_opacity=1, stroke_width=0).move_to(orbit.point_from_proportion(0))
            planets.add(planet)

        enlightenment_group = VGroup(center_sun, orbits, planets)

        self.play(
            ReplacementTransform(classical_group, enlightenment_group, run_time=1.0, rate_func=smooth),
        )
        self.play(
            Rotate(orbits[0], angle=PI, run_time=2.0, rate_func=linear),
            Rotate(orbits[1], angle=PI, run_time=2.0, rate_func=linear),
            Rotate(orbits[2], angle=PI, run_time=2.0, rate_func=linear),
            Rotate(enlightenment_group, angle=PI/2, run_time=2.0, rate_func=smooth)
        )

        # ---------------------------------------------------------
        # 9.0 - 12.0s: INDUSTRIAL & WAR (3.0s)
        # ---------------------------------------------------------
        factory = VGroup()
        chimneys = VGroup()
        for i in range(4):
            chimney = Rectangle(height=2 + i*0.8, width=0.8, color=WHITE, fill_opacity=1, stroke_width=0).shift(RIGHT * (i - 1.5) * 1.8 + UP * (i*0.4))
            chimneys.add(chimney)
        building = Rectangle(height=2.5, width=9, color=PINK, fill_opacity=1, stroke_width=0).shift(DOWN * 1.75)
        industrial_group = VGroup(chimneys, building)

        self.play(
            ReplacementTransform(enlightenment_group, industrial_group, run_time=1.0, rate_func=smooth),
        )

        smokes = VGroup()
        for i in range(4):
            smoke = Circle(radius=0.6, color=BLUE, fill_opacity=0.8, stroke_width=0).move_to(chimneys[i].get_top() + UP * 0.5)
            smokes.add(smoke)

        self.play(FadeIn(smokes, run_time=0.5))
        self.play(smokes.animate.shift(UP * 2.5).scale(2).set_opacity(0), run_time=1.5, rate_func=linear)

        # ---------------------------------------------------------
        # 12.0 - 14.0s: DIGITAL AGE (2.0s)
        # ---------------------------------------------------------
        nodes = VGroup()
        for i in range(30):
            node = Dot(point=[np.random.uniform(-6, 6), np.random.uniform(-3.5, 3.5), 0], color=YELLOW, radius=0.15)
            nodes.add(node)

        lines = VGroup()
        node_list = list(nodes)
        for i in range(40):
            n1 = np.random.choice(len(node_list))
            n2 = np.random.choice(len(node_list))
            line = Line(node_list[n1].get_center(), node_list[n2].get_center(), color=BLUE, stroke_width=2, stroke_opacity=0.6)
            lines.add(line)

        digital_group = VGroup(lines, nodes)

        self.play(
            ReplacementTransform(industrial_group, digital_group, run_time=0.8, rate_func=smooth),
        )
        self.play(
            digital_group.animate.scale(1.2).rotate(PI/6), run_time=1.2, rate_func=linear
        )

        # ---------------------------------------------------------
        # 14.0 - 15.0s: OUTRO (1.0s)
        # ---------------------------------------------------------
        outro_text = Text("NOW", font_size=160, weight=BOLD, color=WHITE)

        self.play(
            ReplacementTransform(digital_group, outro_text, run_time=0.5, rate_func=rush_into),
        )
        self.play(outro_text.animate.scale(1.2), run_time=0.5, rate_func=rush_from)
