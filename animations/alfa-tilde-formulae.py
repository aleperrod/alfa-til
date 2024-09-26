from manim import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.gtts import GTTSService
# from manim_voiceover.services.recorder import RecorderService

class MovingFrameBox(VoiceoverScene):
    def construct(self):
        self.set_speech_service(GTTSService(lang='pt'))
        # self.set_speech_service(RecorderService())

        text=MathTex(
            "\\widetilde{\\alpha}(b,r_0,n)",
            "=",
            "\\begin{cases} 0 & \\text{ se\\ \\  mdc(b,n)=1}\\\\ \\max_c\\left\\lfloor\\frac{e_{n,c}-e_{r_0,c}}{e_{b,c}}\\right\\rfloor& \\text{ caso\\ contrário } \\end{cases}"
        )

        with self.voiceover(text="Esta é a fórmula do número de algarismos no falso período.") as tracker:
            self.play(Write(text))
        
        framebox1 = SurroundingRectangle(text[0], buff = .1)
        framebox2 = SurroundingRectangle(text[1], buff = .1)
        framebox3 = SurroundingRectangle(text[2][1:14], buff = .1)
        framebox4 = SurroundingRectangle(text[2][14:49], buff = .1)

        with self.voiceover(text="Esta é a notação que indica este número de algarismos. Ela começa com a letra grega, alfa, marcada com o acento til.") as tracker:
            self.play(
                Create(framebox1),
            )
            self.wait()
        
        self.play(
            ReplacementTransform(framebox1,framebox2),
        )
        self.wait()

        with self.voiceover(text="Se alfa-tilda é nulo, ou seja, se não houver um falso período, é porque a base e o denominador não tinham fatores em comum.") as tracker:
            self.play(
                ReplacementTransform(framebox2,framebox3),
            )
            self.wait()

        with self.voiceover(text="Mas, ao contrário, se a base e o denominador tiverem fatores primos em comum, alfa-tilda é calculada com esta expressão, que envolve o máximo da função maior inteiro.") as tracker:
            self.play(
                ReplacementTransform(framebox3,framebox4),
            )
            self.wait()
        
        self.remove(framebox4)
        self.wait(1)
        self.remove(text)
        self.wait(1)