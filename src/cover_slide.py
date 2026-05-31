from manim import *

from utils.layout import ThesisSlide

config.background_color = WHITE

Text.set_default(color=BLACK)
Tex.set_default(color=BLACK)
MathTex.set_default(color=BLACK)

Line.set_default(color=BLACK)
Arrow.set_default(color=BLACK)
Circle.set_default(color=ORANGE)
Square.set_default(color=BLACK)
RoundedRectangle.set_default(color=BLACK)


class CoverSlide(ThesisSlide):

    def construct(self):
        # --- Cabecera institucional ---
        institution = Tex(
            r"Facultad de Matemática y Computación \\ Universidad de La Habana",
            font_size=30,
        ).to_edge(UP, buff=0.5)

        top_rule = Line(LEFT * 5.5, RIGHT * 5.5, stroke_width=1).next_to(
            institution, DOWN, buff=0.3
        )

        # --- Título principal ---
        title = (
            VGroup(
                Tex("El problema de la satisfacibilidad booleana", font_size=42),
                Tex(
                    "y el vacío de la intersección con lenguajes regulares",
                    font_size=42,
                ),
            )
            .arrange(DOWN, buff=0.3)
            .move_to(ORIGIN)
            .shift(UP * 0.2)
        )

        # --- Autor y tutores ---
        author = Tex("Autor: Jossué Arteche Muñoz", font_size=34)

        tutors = Tex(
            r"""
            \begin{tabular}{rl}
                Tutores: & MSc. Fernando Raul Rodriguez Flores \\
                         & Lic. Raudel Alejandro Gómez Molina
            \end{tabular}
            """,
            font_size=30,
        )

        people = (
            VGroup(author, tutors).arrange(DOWN, buff=0.45).next_to(title, DOWN, buff=1)
        )

        # --- Pie ---
        bottom_rule = Line(LEFT * 5.5, RIGHT * 5.5, stroke_width=1).to_edge(
            DOWN, buff=0.7
        )

        date = Tex("La Habana, 2026", font_size=26).to_edge(DOWN, buff=0.3)

        self.add(
            institution,
            top_rule,
            title,
            people,
            bottom_rule,
            date,
        )

        self.wait()
