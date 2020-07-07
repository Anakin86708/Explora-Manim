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
starship = "#F2E33A"


from manimlib.imports import *

############################################
# Cena de abertura
############################################
class Abertura(Scene):
    def construct(self):
      explora=TexMobject("\\vec{E}\\hspace{-1mm}\\times\\hspace{-1mm}\\vec{p}\\mathcal{L}0\\mathbb{R}a")
      explora.scale(4.5)
      explora.set_color("#43bfca")

      titulo = TexMobject("\\text{Produtos notáveis}")
      titulo.scale(3.5)
      titulo.set_color("#dc6a40")
         
      self.play(FadeIn(explora))
      self.wait(1)
      self.play(Transform(explora,titulo))
      self.wait(1.5)

############################################
# Cena intermediárias
############################################
class Intermediario_soma(Scene):
    CONFIG = {
        "x_min": -20.0,
        "x_max": 20.0,
        "y_min": -20.0,
        "y_max": 20.0,
        "graph_origin": ORIGIN,
        "function_color": RED,
        "axes_color": WHITE,
        "x_labeled_nums": range(-10, 12, 2)
    }

    def construct(self):
        # Exibindo título e movendo para o topo
        titulo = TexMobject("\\text{Produtos notáveis}")
        titulo.set_color("#dc6a40")
        titulo_top = titulo.copy()

        titulo.scale(3.5)
        titulo_top.scale(1)
        titulo_top.to_edge(UP)

        self.add(titulo)

        self.wait(2)
        self.play(Transform(titulo, titulo_top))     
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
        legenda_a_x = TexMobject("a")
        legenda_a_x.next_to(reta_a_x, DOWN)

        legenda_a_y = legenda_a_x.copy()
        legenda_a_y.next_to(reta_a_y, LEFT)

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
        reta_b_x = Line(pontos_b[0], pontos_b[1], color=papoula)
        reta_b_y = Line(pontos_b[0], pontos_b[3], color=papoula)
        legenda_b_x = TexMobject("b")
        legenda_b_x.next_to(reta_b_x, DOWN)

        legenda_b_y = legenda_b_x.copy()
        legenda_b_y.next_to(reta_b_y, LEFT)

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

class Intermediario_produto(Scene):
    def construct(self):
        titulo = TexMobject("\\text{Produto da soma pela diferença}", color = papoula)
        titulo.scale(1)
        titulo.to_edge(UP)

        equacao = TexMobject(
            "(a+b)",    #0
            "(a-b)",    #1
            " = ",      #2
            "{a}^2",    #3
            "-a",       #4
            "b",        #5
            "+a",       #6
            "b",        #7
            "-{b}^2"    #8
        )
        equacao.scale(1)
        equacao.to_edge(UP)

        equacao_final = TexMobject("(a+b)(a-b) = {a}^2-{b}^2")
        equacao_final.scale(1)
        equacao_final.to_edge(UP)

        total = 2.5
        b = 1
        a = total - b
        pontos_quadrado_total = [
            np.array([-total,-total,0]),
            np.array([total,-total,0]),
            np.array([total,total,0]),
            np.array([-total,total,0])
        ]
        quadrado_total = Polygon(
            pontos_quadrado_total[0],
            pontos_quadrado_total[1],
            pontos_quadrado_total[2],
            pontos_quadrado_total[3],
            color = '#000000'
        )

        # Quadrado a
        linha_a_x = Line(pontos_quadrado_total[0], (pontos_quadrado_total[1] - (b * RIGHT)), color = papoula)
        legenda_a_x = TexMobject("a")
        legenda_a_x.next_to(linha_a_x,DOWN)
        
        pontos_quadrado_a = [
            pontos_quadrado_total[0],
            pontos_quadrado_total[1] - (b * RIGHT),
            pontos_quadrado_total[2] - (b * UR),
            pontos_quadrado_total[3] - (b * UP),
        ]
        quadrado_a = Polygon(
            pontos_quadrado_a[0],
            pontos_quadrado_a[1],
            pontos_quadrado_a[2],
            pontos_quadrado_a[3],
            fill_color = papoula,
            fill_opacity = 0.7,
            color = papoula
        )
        legenda_a = TexMobject("{a}^2")
        legenda_a.move_to(quadrado_a.get_center())
        legenda_a_y = TexMobject("a")
        legenda_a_y.next_to(quadrado_a, LEFT)

        # Quadrado b
        pontos_soma_b = [
            pontos_quadrado_a[1],
            pontos_quadrado_a[1] + (b * RIGHT),
            pontos_quadrado_a[2] + (b * RIGHT),
            pontos_quadrado_a[2],
        ]

        pontos_diferenca_b = [
            pontos_quadrado_a[3] - (b * UP),
            pontos_quadrado_a[2] + (b * DOWN),
            pontos_quadrado_a[2],
            pontos_quadrado_a[3],
        ]

        pontos_quadrado_b = [
            pontos_diferenca_b[1],
            pontos_diferenca_b[1] + (b * RIGHT),
            pontos_diferenca_b[2] + (b * RIGHT),
            pontos_diferenca_b[2],
        ]

        linha_soma_b = Line(pontos_soma_b[0], pontos_soma_b[1], color = apatita)
        legenda_b_x = TextMobject("b")
        legenda_b_x.next_to(linha_soma_b, DOWN)

        linha_diferenca_b = Line(pontos_quadrado_a[3], (pontos_quadrado_a[3] - (b * UP)), color = apatita)
        legenda_b_y = TexMobject("b")
        legenda_b_y.next_to(linha_diferenca_b, LEFT)

        retangulo_soma_b = Polygon(
            pontos_soma_b[0],
            pontos_soma_b[1],
            pontos_soma_b[2],
            pontos_soma_b[3],
            fill_color = apatita,
            fill_opacity = 0.7,
            color = apatita
        )

        retangulo_diferenca_b = Polygon(
            pontos_diferenca_b[0],
            pontos_diferenca_b[1],
            pontos_diferenca_b[2],
            pontos_diferenca_b[3],
            fill_color = apatita,
            fill_opacity = 0.7,
            color = apatita
        )

        quadrado_b = Polygon(
            pontos_quadrado_b[0],
            pontos_quadrado_b[1],
            pontos_quadrado_b[2],
            pontos_quadrado_b[3],
            fill_color = apatita,
            fill_opacity = 0.7,
            color = apatita
        )

        legenda_b = TexMobject("{b}^2")
        legenda_b.move_to(quadrado_b.get_center())

        # Regiões com mesma área
        pontos_soma_ab = [
            pontos_quadrado_a[1],
            pontos_soma_b[1],
            pontos_quadrado_b[1],
            pontos_quadrado_b[0],
        ]

        pontos_diferenca_ab = [
            pontos_diferenca_b[0],
            pontos_quadrado_b[0],
            pontos_quadrado_b[3],
            pontos_diferenca_b[3],
        ]

        soma_ab = Polygon(
            pontos_soma_ab[0],
            pontos_soma_ab[1],
            pontos_soma_ab[2],
            pontos_soma_ab[3],
            fill_color = starship,
            fill_opacity = 0.7,
            color = starship
        )

        diferenca_ab = Polygon(
            pontos_diferenca_ab[0],
            pontos_diferenca_ab[1],
            pontos_diferenca_ab[2],
            pontos_diferenca_ab[3],
            fill_color = starship,
            fill_opacity = 0.7,
            color = starship
        )

        # Retângulo final
        pontos_retangulo_final = [
            pontos_quadrado_a[0],
            pontos_soma_b[1],
            pontos_quadrado_b[1],
            pontos_diferenca_b[0],
        ]

        retangulo_final = Polygon(
            pontos_retangulo_final[0],
            pontos_retangulo_final[1],
            pontos_retangulo_final[2],
            pontos_retangulo_final[3],
            fill_color = papoula,
            fill_opacity = 0.7,
            color = papoula            
        )
        legenda_retangulo_final = legenda_a.copy()
        legenda_retangulo_final.move_to(retangulo_final.get_center())

        legenda_x = TexMobject("(a+b)")
        legenda_x.next_to(retangulo_final, DOWN)
        legenda_y = TexMobject("(a-b)")
        legenda_y.next_to(retangulo_final, LEFT)


        ## Animações ##
        self.wait(0.3)
        self.play(
            ShowCreation(titulo),
        )
        self.wait(0.7)

        # Quadrado total
        self.play(
            ShowCreation(quadrado_total),
        )
        self.wait(1)

        # Criando a
        self.play(
            ShowCreation(linha_a_x),
            Write(legenda_a_x),
        )
        self.wait(0.7)

        self.play(
            ShowCreation(quadrado_a),
            Write(legenda_a),
            Write(legenda_a_y),
            FadeOut(linha_a_x),
            FadeOut(titulo),
        )
        self.wait(1)

        # Criando b
        self.play(
            ShowCreation(linha_soma_b),
            Write(legenda_b_x),
        )
        self.wait(0.7)

        self.play(
            ShowCreation(linha_diferenca_b),
            Write(legenda_b_y),
        )

        # Colocando so produtos de ab
        self.play(
            ReplacementTransform(legenda_a_y.copy(), equacao[6]),
        )
        self.wait(0.3)
        self.play(
            ReplacementTransform(legenda_b_x.copy(), equacao[7]),
            ShowCreation(retangulo_soma_b),
            FadeOut(linha_diferenca_b),
        )

        self.play(
            ReplacementTransform(legenda_a_x.copy(), equacao[4]),
        )
        self.wait(0.3)
        self.play(
            ReplacementTransform(legenda_b_y.copy(), equacao[5]),
            ShowCreation(retangulo_diferenca_b),    
            FadeOut(linha_soma_b),
        )
        self.wait(0.7)

        self.play(
            FadeIn(quadrado_b),
            Write(legenda_b),
        )
        self.wait(0.7)
        
        # Preparando para o final
        self.play(
            FadeIn(soma_ab),
            FadeIn(diferenca_ab),
            FadeOut(legenda_a_y),
            FadeOut(legenda_a_x),
            FadeOut(legenda_b_y),
            FadeOut(legenda_b_x),
            FadeOut(retangulo_soma_b),
            FadeOut(retangulo_diferenca_b),
        )
        self.wait(0.7)

        self.play(
            ShowCreation(retangulo_final),
            Write(legenda_x),
            Write(legenda_y),
            ReplacementTransform(legenda_a, legenda_retangulo_final),            
            FadeOut(quadrado_a),
            FadeOut(soma_ab),
            FadeOut(diferenca_ab),
        )
        self.wait(0.7)

        self.play(
            ReplacementTransform(legenda_retangulo_final, equacao[3]),
            ReplacementTransform(legenda_b, equacao[8]),
            FadeOut(quadrado_b),
        )
        self.wait(0.3)
        self.play(
            ReplacementTransform(legenda_x.copy(), equacao[0]),
            ReplacementTransform(legenda_y.copy(), equacao[1]),            
            Write(equacao[2]),            
        )
        self.wait(0.7)

        self.play(
            ReplacementTransform(equacao,equacao_final)
        )
        
        self.wait(2)

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

      site=TexMobject("https://wordpress.ft.unicamp.br/explora/")
      site.scale(1.0)
      site.set_color(WHITE)
      site.shift(0.8*UP)

      autor=TexMobject("\\text{Animações: Ariel Tadeu da Silva}")
      autor.scale(1.2)
      autor.set_color("#dc6a40")
      autor.shift(0.3*DOWN)

      ft = ImageMobject("logo-FT.jpeg")
      ft.scale(1.5)
      ft.shift(2.3*DOWN+3*RIGHT)

      unicamp = ImageMobject("logo-unicamp.jpeg")
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
