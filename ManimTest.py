#Use cd Manim
#manim -pqm ManimTest.py main
#-----------------------------------------------
from manim import *

class main(Scene):
    
    def construct(self):
        self.camera.background_color = BLUE
        text=Text("Sai Vignesh").to_corner(UL)
        im=SVGMobject("carsymbol3.svg",color=WHITE).scale(0.5).to_edge(LEFT)
        
        tree1=SVGMobject("Tree-003.svg").scale(3).to_edge(RIGHT+DOWN)
        tree2=SVGMobject("dead-tree1.svg").scale(3).to_edge(DOWN)
        rect=Rectangle(height=1,width=20,color=BLACK,fill_opacity=0.8)
        pol=RegularPolygon(8,color=YELLOW,fill_opacity=0.8).scale(0.7).to_edge(UR)
        
        self.add(rect,pol)
        self.play(Write(text),run_time=5)
        self.play(FadeIn(im,run_time=0.02))
        self.play(FadeIn(tree1,run_time=0.02))
        
        self.play((im.animate.to_edge(RIGHT)),(tree1.animate.to_edge(LEFT)),run_time=8,rate_func=linear)
        
        self.play(FadeOut(tree1,run_time=0.01))
        self.camera.background_color = RED
        self.play((im.animate.to_edge(LEFT)),run_time=0.01)
        self.play((im.animate.to_edge(RIGHT)),(tree2.animate.to_edge(LEFT)),run_time=5,rate_func=linear)

        self.wait()

