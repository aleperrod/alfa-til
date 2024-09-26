from manim import *
# from manim_voiceover import VoiceoverScene
# from manim_voiceover.services.gtts import GTTSService
# from manim_voiceover.services.recorder import RecorderService

class MovingFrameBox(Scene):
    def construct(self):
        text1=MathTex(
            "\frac{1}{7}",
            "=",
            "0",
            ",",
            "142857",
            "142857..."
        )

        text2=MathTex(
            "\\frac{n}{d}",
            "=",
            
            "f_1f_2\\cdots f_{\\widetilde{\\alpha}}",
            "v_1v_2\cdots v_{\\alpha}"
        )