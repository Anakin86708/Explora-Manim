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
# APATITA (verde)   : código Hex "#43bfca"
# PAPOULA (laranja) : código Hex "#dc6a40"

from manimlib.imports import *
APATITA = "#43bfca"
PAPOULA = "#dc6a40"
STARSHIP = "#F2E33A"


############################################
# Cena de abertura
############################################

class Abertura(Scene):
    def construct(self):
        explora = TexMobject(
            "\\vec{E}\\hspace{-1mm}\\times\\hspace{-1mm}\\vec{p}\\mathcal{L}0\\mathbb{R}a")
        explora.scale(4.5)
        explora.set_color("#43bfca")

        titulo = TexMobject("\\text{Número de Euler}")
        titulo.scale(2.5)
        titulo.set_color("#dc6a40")

        self.play(FadeIn(explora))
        self.wait(1)
        self.play(Transform(explora, titulo))
        self.wait(1.5)


############################################
# Cena intermediárias
############################################
class Euler(Scene):
    def construct(self):
        # Exibindo título e movendo para o topo
        titulo = TexMobject("\\text{Número de Euler}")
        titulo.set_color(PAPOULA)
        titulo_top = TexMobject("\\text{Expansão de série}")

        titulo.scale(2.5)
        titulo_top.set_color(PAPOULA)
        titulo_top.scale(1)
        titulo_top.to_edge(UP)

        texto_inicial = TexMobject(
            '\\text{Uma constante irracional e transcendental, ou seja,} \\\\'
            '\\text{não pode ser escrito como uma simples fração e}\\\\'
            '\\text{nem pode ser a solução para qualquer equação algébrica}'
        )
        texto_inicial.scale(.9)

        serie = TexMobject(
            'e',
            '\\approx 1',
            '+ {{1} \\over {1}}',
            '+ {{1} \\over {2 \\times 1}}',
            '+ {{1} \\over {3 \\times 2 \\times 1}}',
            '+ {{1} \\over {4 \\times 3 \\times 2 \\times 1}} + ...',
            '\\approx 2.7083',
        )

        serie_fatorial = TexMobject(
            'e',
            '\\approx 1',
            '+ {{1} \\over {1!}}',
            '+ {{1} \\over {2!}}',
            '+ {{1} \\over {3!}}',
            '+ {{1} \\over {4!}} + ...',
            '\\approx 2.7083',
        )

        # Animações
        self.add(titulo)
        self.wait(1)

        self.play(
            Transform(titulo, titulo_top),
        )
        self.wait(1.5)

        self.play(
            Write(texto_inicial),
        )
        self.wait(15)
        self.play(
            FadeOut(texto_inicial),
        )
        self.wait(3)

        # Exibe a série
        self.play(
            Write(serie[0]),
        )
        self.wait(1)
        self.play(
            Write(serie[1:])
        )
        self.wait(5)
        self.play(
            Transform(serie, serie_fatorial),
        )
        self.wait(5)
        

############################################
# Cena de fechamento
############################################
class Fechamento(Scene):
    def construct(self):
        explora = TexMobject(
            "\\vec{E}\\hspace{-1mm}\\times\\hspace{-1mm}\\vec{p}\\mathcal{L}0\\mathbb{R}a")
        explora.scale(4.5)
        explora.set_color("#43bfca")
        explora.shift(2.5*UP)

        site = TexMobject("https://wordpress.ft.unicamp.br/explora/")
        site.scale(1.0)
        site.set_color(WHITE)
        site.shift(0.8*UP)

        autor = TexMobject("\\text{Animações: Ariel Tadeu da Silva}")
        autor.scale(1.2)
        autor.set_color("#dc6a40")
        autor.shift(0.3*DOWN)

        ft = ImageMobject("./logo-FT.jpeg")
        ft.scale(1.5)
        ft.shift(2.3*DOWN+3*RIGHT)

        unicamp = ImageMobject("./logo-unicamp.jpeg")
        unicamp.scale(1.5)
        unicamp.shift(2.3*DOWN+3*LEFT)

        self.play(FadeIn(explora), FadeIn(site))
        self.wait(1)
        self.play(FadeIn(unicamp), FadeIn(ft))
        self.wait(1)
        self.play(FadeOut(unicamp), FadeOut(ft))
        self.wait(0.8)
        self.play(FadeIn(autor))
        self.wait(2)
############################################
############################################
