# template para animacoes dentro do Projeto Explora
# composição cenas 1...n
# 1) Cena de abertura
# 2) cenas intermediárias
# ...
# n) Cena de fechamento

# os objetos, textos, etc devem seguir 
# cores que estejam em harmonia com 
# as cores da sala:
#
# Apatita (verde)   : código Hex "#43bfca"
# Papoula (laranja) : código Hex "#dc6a40"

apatita = "#43bfca"
papoula = "#dc6a40"


from manimlib.imports import *

############################################
# Cena de abertura
############################################
class Abertura(Scene):
    def construct(self):
      explora=TexMobject("\\vec{E}\\hspace{-1mm}\\times\\hspace{-1mm}\\vec{p}\\mathcal{L}0\\mathbb{R}a")
      explora.scale(4.5)
      explora.set_color("#43bfca")

      titulo=TextMobject("Produtos Notáveis")
      titulo.scale(3.5)
      titulo.set_color("#dc6a40")
         
      self.play(FadeIn(explora))
      self.wait(1)
      self.play(Transform(explora,titulo))
      self.wait(1.5)

############################################
# Cena intermediárias
############################################
class Intermediario(Scene):
    def construct(self):
        # Exibindo título e movendo para o topo
        titulo = TextMobject("Produtos Notáveis")
        titulo.set_color("#dc6a40")
        titulo_top = titulo.copy()

        titulo.scale(3.5)
        titulo_top.scale(1)
        titulo_top.to_edge(UP)

        self.add(titulo)

        self.wait(2)
        self.play(Transform(titulo,titulo_top))     
        self.wait(1)

        # Define os pontos que criam o quadrado A
        pontos_a = [
            np.array([-3,-3,0]),
            np.array([1,-3,0]),
            np.array([1,1,0]),
            np.array([-3,1,0])
        ]

        # Retas para quadrado a e legendas
        reta_a_x = Line(pontos_a[0],pontos_a[1], color=apatita)
        reta_a_y = Line(pontos_a[0],pontos_a[3], color=apatita)
        legenda_a_x = TextMobject("a")
        legenda_a_x.next_to(reta_a_x,DOWN)

        legenda_a_y = legenda_a_x.copy()
        legenda_a_y.next_to(reta_a_y,LEFT)

        # Animação quadrado a
        self.play(
            ShowCreation(reta_a_x),
            Write(legenda_a_x)
        )
        self.wait(0.5)
        self.play(
            ShowCreation(reta_a_y),
            Write(legenda_a_y)
        )
        self.wait(0.7)

        quadrado_a = Polygon(
            pontos_a[0],
            pontos_a[1], 
            pontos_a[2], 
            pontos_a[3], 
            fill_color=apatita, 
            fill_opacity=0.7
        )
        legenda_a = TexMobject("{a}^{2}")
        legenda_a.move_to(quadrado_a.get_center())
        self.play(
            ShowCreation(quadrado_a),
            ShowCreation(legenda_a),
            FadeOut(reta_a_x),
            FadeOut(reta_a_y),
        )        
        self.wait(1)

        # Criando quadrado b
        diferenca = 2
        pontos_b = [
            pontos_a[2],
            pontos_a[2] + diferenca * RIGHT,
            pontos_a[2] + diferenca * UR,
            pontos_a[2] + diferenca * UP
        ]

        # Retas para quadrado b
        reta_b_x = Line(pontos_b[0],pontos_b[1], color=papoula)
        reta_b_y = Line(pontos_b[0],pontos_b[3], color=papoula)
        legenda_b_x = TextMobject("b")
        legenda_b_x.next_to(reta_b_x,DOWN)

        legenda_b_y = legenda_b_x.copy()
        legenda_b_y.next_to(reta_b_y,LEFT)

        # Animação quadrado b
        self.play(
            ShowCreation(reta_b_x),
            Write(legenda_b_x)
        )
        self.wait(0.5)
        self.play(
            ShowCreation(reta_b_y),
            Write(legenda_b_y)
        )
        self.wait(0.7)

        quadrado_b = Polygon(
            pontos_b[0],
            pontos_b[1],
            pontos_b[2],
            pontos_b[3],
            fill_color=papoula,
            fill_opacity=0.7,
            color=papoula
        )
        legenda_b = TexMobject("{b}^{2}")
        legenda_b.move_to(quadrado_b.get_center())
        self.play(
            ShowCreation(quadrado_b),
            ShowCreation(legenda_b),
            FadeOut(reta_b_x),
            FadeOut(reta_b_y),
        )  
        self.wait(0.7)

        # Criando retangulos laterais
        retangulo_d = Polygon(
            pontos_a[1],
            pontos_a[1] + diferenca * RIGHT,
            pontos_b[1],
            pontos_b[0],
            fill_color='#F2E33A',
            fill_opacity=0.7,
            color='#F2E33A'
        )

        retangulo_t = Polygon(
            pontos_a[3],
            pontos_a[2],
            pontos_b[3],
            pontos_a[3] + diferenca * UP,
            fill_color='#F2E33A',
            fill_opacity=0.7,
            color='#F2E33A'
        )

        self.play(
            ShowCreation(retangulo_d),
            ShowCreation(retangulo_t)
        )
        self.wait(1)

############################################
# Cena de fechamento
############################################
class Fechamento(Scene):
    def construct(self):
      explora=TexMobject(
           "\\vec{E}\\hspace{-1mm}\\times\\hspace{-1mm}\\vec{p}\\mathcal{L}0\\mathbb{R}a")
      explora.scale(4.5)
      explora.set_color("#43bfca")
      explora.shift(2.5*UP)

      site=TextMobject("https://wordpress.ft.unicamp.br/explora/")
      site.scale(1.0)
      site.set_color(WHITE)
      site.shift(0.8*UP)

      autor=TextMobject("Animações: Ariel Tadeu da Silva")
      autor.scale(1.2)
      autor.set_color("#dc6a40")
      autor.shift(0.3*DOWN)

      ft = ImageMobject("logo-FT.png")
      ft.scale(1.5)
      ft.shift(2.3*DOWN+3*RIGHT)

      unicamp = ImageMobject("logo-unicamp.jpg")
      unicamp.scale(1.5)
      unicamp.shift(2.3*DOWN+3*LEFT)
      
      self.play(FadeIn(explora),FadeIn(site))
      self.wait(1)
      self.play(FadeIn(unicamp),FadeIn(ft))
      self.wait(1)
      self.play(FadeOut(unicamp),FadeOut(ft))
      self.wait(0.8)
      self.play(FadeIn(autor))
      self.wait(2)
############################################
############################################
