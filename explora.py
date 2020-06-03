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
      titulo.scale(3.5)
      titulo.set_color("#dc6a40")

      titulo_top = TextMobject("Produtos Notáveis")
      titulo_top.scale(1)
      titulo_top.set_color("#dc6a40")
      titulo_top.to_edge(UP)

      self.add(titulo)

      self.wait(2)
      self.play(Transform(titulo,titulo_top))     
      self.wait(1)

      # Criando os quadrados a partir de retas
      tamanho_a = 4
      reta_a = Line(np.array([0,-2,0]), np.array([tamanho_a,-2,0]))

      legenda_a = TextMobject("a")
      legenda_a.next_to(reta_a,DOWN)

      quadrado_a = Square(
        fill_color = apatita,
        fill_opacity = .7,
        color = apatita,
        side_length = tamanho_a)
      quadrado_a.to_edge(
        (reta_a.get_corner(LEFT) + (tamanho_a/2))*LEFT,
         reta_a.get_center()) # escolher uma cordenada que corresponde a linha

      self.play(ShowCreation(reta_a),Write(legenda_a))
      self.wait(0.5)
      self.play(Transform(reta_a,quadrado_a))

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

      autor=TextMobject("Animações: Autor")
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
