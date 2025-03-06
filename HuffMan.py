from manim import *

class HuffMan(Scene):
    def construct(self):

        # Text:
        intro = Text(
            "Huffman coding", font="Bahnschrift", weight=BOLD
        ).scale(2)
        question = Text(
            "What is Huffman coding?", font="Bahnschrift", weight=BOLD
        ).to_edge(UP).scale(2)

        explain = Text(
            "♦ Huffman coding is a lossless compression method \n"
            "that assigns shorter codes to frequent characters, \n"
            "reducing storage efficiently.",
            font="Bahnschrift", line_spacing=1.5
        ).scale(0.8)

        question2 = Text(
            "How it works?", font="Bahnschrift", weight=BOLD
        ).scale(2)

        explain2 = Text(
            "Assume that we have a 5×5 image that looks like this",
            font="Bahnschrift"
        ).scale(0.6).shift(UP * 1.8)

        e1 = MathTex(
            r"\text{Since we are using grayscale, the total number of bits is }"
            r"(5 \times 5 \times \log_2(256) = 200)",
            font_size=45
        ).scale(0.6).shift(UP * 2.5)

        explain2v1 = Text(
            "We will convert it to grayscale",
            font="Bahnschrift"
        ).scale(0.6).shift(UP * 1.8)

        legend = Text(
            "45 -> Dark Red\n"
            "80 -> Medium Red\n"
            "200 -> Light Red",
            font="Bahnschrift",
        ).to_edge(UL, buff=0).scale(0.5)

        explain2v2 = Text(
            "Count the frequency of each number",
            font="Bahnschrift",
        ).scale(0.6).shift(UP * 1.8, RIGHT * 2)

        explain2v3 = Text(
            "Now let's make the Huffman tree",
            font="Bahnschrift",
        ).scale(1).shift(ORIGIN)

        explain2v4 = Text(
            "We will begin by sorting the frequency numbers in ascending order",
            font="Bahnschrift",
        ).shift(UP * 2).scale(0.6)

        explain2v5 = Text(
            "Then, we will start by adding the two smallest numbers first",
            font="Bahnschrift",
        ).shift(UP * 2).scale(0.6)

        explain2v6 = Text(
            "Then, we will add the next two smallest numbers",
            font="Bahnschrift",
        ).shift(UP * 2).scale(0.6)

        explain2v7 = Text(
            "Finally, we will assign 0 to the left lines\n             and 1 to the right lines",
            font="Bahnschrift",
        ).shift(UP * 2 + RIGHT * 2).scale(0.7)

        legend2 = Text(
            "Left Lines -> Yellow\n"
            "Right Lines -> Red\n"
            "7 -> (45)\n"
            "8 -> (80)\n"
            "10 -> (200)",
            font="Bahnschrift",
        ).to_edge(UL, buff=0).scale(0.5).shift(LEFT)

        explain2v8 = Text(
            "We will now start assigning each frequency\n           to its bits using the tree",
            font="Bahnschrift",
        ).shift(UP * 2 + RIGHT * 2).scale(0.6)

        newC1 = Text(
            "7 ---> 1  0",
            font="Bahnschrift",
        ).shift(LEFT * 4).scale(0.6)

        newC2 = Text(
            "8 ---> 1  1",
            font="Bahnschrift",
        ).shift(LEFT * 4 + DOWN * 1.5).scale(0.6)

        newC3 = Text(
            "10 ---> 0",
            font="Bahnschrift",
        ).shift(LEFT * 4 + DOWN * 3).scale(0.6)

        Dig1 = Text(
            "45 ---> 1  0",
            font="Bahnschrift",
        ).shift(LEFT * 4).scale(0.6)

        Dig2 = Text(
            "80 ---> 1  1",
            font="Bahnschrift",
        ).shift(LEFT * 4 + DOWN * 1.5).scale(0.6)

        Dig3 = Text(
            "200 ---> 0",
            font="Bahnschrift",
        ).shift(LEFT * 4 + DOWN * 3).scale(0.6)

        explain2v9 = Text(
            "The total number of bits after compression is 40",
            font="Bahnschrift",
        ).shift(UP * 2).scale(0.9)

        calc = Text(
            "(7 x 2[two bits]) + (8 x 2[two bits]) + (10 x 1[one bit]) = 40",
            font="Bahnschrift",
        ).shift(DOWN).scale(0.7)

        F1 = Text(
            "Now, let's compare before and after compression",
            font="Bahnschrift",
        ).shift(UP).scale(0.9)

        before = Text(
            "Total number\n  of bits [before] = 200",
            font="Bahnschrift",
        ).shift(DOWN, LEFT * 3).scale(0.7)

        after = Text(
            "Total number\n  of bits [after] = 40",
            font="Bahnschrift",
        ).shift(DOWN, RIGHT * 3).scale(0.7)

        end = Text(
            "Thank you for watching!", font="Bahnschrift", weight=BOLD
        ).scale(1.8)






        # Image:
        values = [
            [45, 80, 200, 200, 80],
            [80, 45, 200, 200, 45],
            [200, 200, 80, 200, 45],
            [45, 80, 200, 45, 80],
            [80, 45, 80, 200, 200]
        ]

        color_map = {
            45: "#8B0000",    # Dark Red
            80: "#B22222",    # Medium Red
            200: "#FF6347",   # Light Red
        }

        # Create the matrix as squares
        matrix_group = VGroup()

        for row_idx, row in enumerate(values):

            for col_idx, val in enumerate(row):
                square = Square(
                    side_length=1, fill_color=color_map[val], fill_opacity=1
                )
                square.move_to(np.array([col_idx, -row_idx, 0]))
                matrix_group.add(square)

        matrix_group.move_to(ORIGIN).shift(DOWN).scale(0.9)

        # Transform to numbers
        new_matrix_group = VGroup()

        for row_idx, row in enumerate(values):

            for col_idx, val in enumerate(row):
                number = Text(str(val), font="Bahnschrift", font_size=24, color=color_map[val])
                number_square = Square(
                    side_length=1, stroke_color=WHITE, stroke_width=2, fill_opacity=0
                )
                number.move_to(number_square.get_center())
                new_matrix_group.add(VGroup(number_square, number))
                number_square.move_to(np.array([col_idx, -row_idx, 0]))
                number.move_to(np.array([col_idx, -row_idx, 0]))

        new_matrix_group.move_to(ORIGIN).shift(DOWN).scale(0.9)








        self.play(Write(intro))
        self.wait()

        intro.generate_target()
        intro.target.become(question)
        intro.target.to_edge(UP).scale(0.5)

        self.play(MoveToTarget(intro))
        self.wait(0.5)

        self.play(Write(explain))
        self.wait(5)

        self.play(FadeOut(intro, explain))
        self.play(Write(question2))
        self.wait()

        self.play(FadeOut(question2))
        self.play(Write(explain2), Write(matrix_group))
        self.play(Write(e1))
        self.wait(2)

        self.play(
            FadeOut(explain2, e1), FadeIn(explain2v1)
        )
        self.wait(2)

        self.play(
            ReplacementTransform(matrix_group, new_matrix_group), Write(legend)
        )
        self.wait(1)

        self.play(
            new_matrix_group.animate.to_corner(LEFT + DOWN).scale(0.9),
            legend.animate.to_corner(LEFT + UP * -10).scale(0.8),
            ReplacementTransform(explain2v1, explain2v2)
            )
        self.wait(2)



        # Create blue square matrix
        target_numbers = [45, 80, 200]
        all_blue_squares = []
        freq = []
        all_explanation_texts = []

        for idx, target_number in enumerate(target_numbers):
            blue_squares = []

            for number_square_group in new_matrix_group:
                number = number_square_group[1]

                if int(number.text) == target_number:
                    blue_square = Square(
                        side_length=0.6, stroke_color=BLUE, stroke_width=4, fill_opacity=0
                    )
                    blue_square.move_to(number.get_center())
                    blue_squares.append(blue_square)
            all_blue_squares.extend(blue_squares)
            freq.append(len(blue_squares))

            if blue_squares:
                self.play(*[Write(blue_square) for blue_square in blue_squares])

            explanation_text = Text(
                f"{len(blue_squares)} occurrences of the number {target_number}", font="Bahnschrift", font_size=24
            ).scale(1)

            if idx == 0:
                explanation_text.shift(UP * 1.8, RIGHT * 2 + DOWN * 2)
            elif idx == 1:
                explanation_text.shift(UP * 1.8, RIGHT * 2 + DOWN * 3)
            else:
                explanation_text.shift(UP * 1.8, RIGHT * 2 + DOWN * 4)

            all_explanation_texts.append(explanation_text)

            self.play(Write(explanation_text))
            self.wait(1)

        self.wait(2)

        blue_squares_group = VGroup(*all_blue_squares)
        first = Text(str(freq[0]), font_size=24, font="Bahnschrift").scale(2).move_to(LEFT * 2)
        second = Text(str(freq[1]), font_size=24, font="Bahnschrift").scale(2).move_to(ORIGIN)
        third = Text(str(freq[2]), font_size=24, font="Bahnschrift").scale(2).move_to(RIGHT * 2)


        self.play(
            FadeOut(new_matrix_group),
            FadeOut(legend),
            FadeOut(blue_squares_group),
            ReplacementTransform(explain2v2, explain2v3),
            FadeOut(*all_explanation_texts),
        )
        self.wait(2)

        self.play(ReplacementTransform(explain2v3, explain2v4)) 
        self.play(
            Write(first), Write(second), Write(third)
        )
        self.wait(3)

        self.play(
            ReplacementTransform(explain2v4, explain2v5)
        )
        self.wait(1)

        self.play(
            first.animate.move_to(DOWN * 3 + LEFT * 1),
            second.animate.move_to(DOWN * 3 + RIGHT * 1),
        )

        # Draw arrows from 2 nums to the merged values
        merged_value = Text(f"{freq[0] + freq[1]}", font_size=24, font="Bahnschrift").scale(2)
        merged_value.move_to(DOWN * 1.5)

        merged_sum = int(merged_value.text) + freq[2]
        merged_value2 = Text(f"{merged_sum}", font_size=24, font="Bahnschrift").scale(2)
        merged_value2.move_to(DOWN * -0.5 + LEFT * 1.3)

        arrow1 = Line(start=first.get_top(), end=merged_value.get_bottom(), buff=0.2).set_stroke(width=4)
        arrow2 = Line(start=second.get_top(), end=merged_value.get_bottom(), buff=0.2).set_stroke(width=4)

        self.play(
            Create(arrow1), Create(arrow2), Write(merged_value)
        )
        self.wait(2)

        self.play(
            ReplacementTransform(explain2v5, explain2v6),
            third.animate.next_to(merged_value, LEFT * 8),
        )

        arrow3 = Line(start=merged_value.get_top(), end=merged_value2.get_bottom(), buff=0.2).set_stroke(width=4)
        arrow4 = Line(start=third.get_top(), end=merged_value2.get_bottom(), buff=0.2).set_stroke(width=4)

        self.play(
            Create(arrow3), Create(arrow4), Write(merged_value2)
        )
        self.wait(2)





        bit0v0 = Text(
            "0",
            font="Bahnschrift",
        ).next_to(arrow1, LEFT * 0.2 + UP * 0.01).scale(0.7)

        bit0v1 = Text(
            "0",
            font="Bahnschrift",
        ).next_to(arrow4, LEFT * 0.2 + UP * 0.01).scale(0.7)

        bit1v0= Text(
            "1",
            font="Bahnschrift",
        ).next_to(arrow2, RIGHT * 0.2 + UP * 0.01).scale(0.7)

        bit1v1 = Text(
            "1",
            font="Bahnschrift",
        ).next_to(arrow3, RIGHT * 0.2 + UP * 0.01).scale(0.7)
        tree_group = VGroup(bit0v0, bit0v1, bit1v0, bit1v1, merged_value, merged_value2, first, second, third, arrow1, arrow2, arrow3, arrow4)





        self.play(
            ReplacementTransform(explain2v6, explain2v7),
            Write(legend2),
        )
        self.wait(1)

        self.play(
            arrow1.animate.set_color(YELLOW),
            arrow4.animate.set_color(YELLOW),
            Write(bit0v0),
            Write(bit0v1),
        )

        self.play(
            arrow2.animate.set_color(RED),
            arrow3.animate.set_color(RED),
            Write(bit1v0),
            Write(bit1v1),
        )
        self.wait(2)

        self.play(
            ReplacementTransform(explain2v7, explain2v8),
            tree_group.animate.shift(RIGHT * 4),
        )
        self.wait(1)

        self.play(
            Write(newC1),
            arrow1.animate.set_stroke(WHITE, width=15),
            arrow3.animate.set_stroke(WHITE, width=15),
        )
        self.wait(2)
        self.play(
            arrow1.animate.set_stroke(YELLOW, width=4),
            arrow3.animate.set_stroke(RED, width=4),
        )

        self.play(
            Write(newC2),
            
            arrow2.animate.set_stroke(WHITE, width=15),
            arrow3.animate.set_stroke(WHITE, width=15),
        )
        self.wait(2)
        self.play(
            arrow2.animate.set_stroke(RED, width=4),
            arrow3.animate.set_stroke(RED, width=4),
        )

        self.play(
            Write(newC3),
            arrow4.animate.set_stroke(WHITE, width=15),
        )
        self.wait(2)
        self.play(
            arrow4.animate.set_stroke(YELLOW, width=4),
        )
        self.wait(2)

        self.play(
            ReplacementTransform(newC1, Dig1),
            ReplacementTransform(newC2, Dig2),
            ReplacementTransform(newC3, Dig3),
        )

        self.play(
            FadeOut(legend2),
            FadeOut(tree_group),
            ReplacementTransform(explain2v8, explain2v9),
            Dig1.animate.next_to(ORIGIN ,LEFT * 13),
            Dig2.animate.move_to(ORIGIN).shift(LEFT * 0.5),
            Dig3.animate.next_to(ORIGIN, RIGHT * 10),
            Write(calc)
        )
        self.wait(3)

        self.play(
            ReplacementTransform(explain2v9, F1),
            FadeOut(calc),
            FadeOut(Dig1, Dig2, Dig3)
        )

        self.play(
            Write(before),
            Write(after)
        )
        self.wait(2)

        self.play(
            FadeOut(before),
            FadeOut(after),
            ReplacementTransform(F1, end),
        )
        self.wait(3)