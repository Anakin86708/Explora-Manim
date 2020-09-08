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
        
class Juros(Scene):
    def construct(self):
        self.config()
        self.introducao()
        self.aplicacao_juros()
        self.conclusao()
    
    def calcular_euler(self, x):
        try:
            return (1*(1/x))**x
        except ZeroDivisionError:
            pass

    def config(self):
        self.historia_do_banco = [
            TextMobject(
                """
                Suponhamos um banco com 100\% de taxa de juros ao ano.\n
                Temos o seguinte financiamento:
                """
            ).to_edge(UP),
            TextMobject(
                """
                Se o banco tiver uma taxa de juros 50\% a cada semestre.\n
                Temos o seguinte financiamento
                """
            ).to_edge(UP),
            TextMobject(
                """
                Se o banco tiver uma taxa de juros de 33,3\% a cada\n 
                quadrimestre. Temos o seguinte financiamento
                """
            ).to_edge(UP)
        ]

        tamanho_valores = 0.75

        retas = [
            Line(start=4.5*LEFT, end=4.5*RIGHT),
            
            Line(start=4.5*LEFT, end=0.75*LEFT),
            Line(start=0.75*RIGHT, end=4.5*RIGHT),

            Line(start=4.5*LEFT, end=2.5*LEFT),
            Line(start=1*LEFT, end=1*RIGHT),
            Line(start=2.5*RIGHT, end=4.5*RIGHT),
        ]

        valores = [
            TexMobject("R\$1,00").move_to(5.25*LEFT).scale(tamanho_valores),
            TexMobject("R\$2,00").move_to(5.25*RIGHT).scale(tamanho_valores),

            TexMobject("R\$1,00").move_to(5.25*LEFT).scale(tamanho_valores),
            TexMobject("R\$1,50").move_to(ORIGIN).scale(tamanho_valores),
            TexMobject("R\$2,25").move_to(5.25*RIGHT).scale(tamanho_valores),

            TexMobject("R\$1,00").move_to(5.25*LEFT).scale(tamanho_valores),
            TexMobject("R\$1,33").move_to(1.75*LEFT).scale(tamanho_valores),
            TexMobject("R\$1,76").move_to(1.75*RIGHT).scale(tamanho_valores),
            TexMobject("R\$2,35").move_to(5.25*RIGHT).scale(tamanho_valores),
        ] 

        taxas = [
            TextMobject("100\%").move_to(retas[0]).scale(tamanho_valores).shift(0.5*DOWN),

            TextMobject("50\%").move_to(retas[1]).scale(tamanho_valores).shift(0.5*DOWN),
            TextMobject("50\%").move_to(retas[2]).scale(tamanho_valores).shift(0.5*DOWN),
            
            TextMobject("33\%").move_to(retas[3]).scale(tamanho_valores).shift(0.5*DOWN),
            TextMobject("33\%").move_to(retas[4]).scale(tamanho_valores).shift(0.5*DOWN),
            TextMobject("33\%").move_to(retas[5]).scale(tamanho_valores).shift(0.5*DOWN)
        ]

        meses = [
            TextMobject("12 meses").move_to(retas[0]).scale(tamanho_valores).shift(0.5*UP),

            TextMobject("6 meses").move_to(retas[1]).scale(tamanho_valores).shift(0.5*UP),
            TextMobject("6 meses").move_to(retas[2]).scale(tamanho_valores).shift(0.5*UP),
            
            TextMobject("4 meses").move_to(retas[3]).scale(tamanho_valores).shift(0.5*UP),
            TextMobject("4 meses").move_to(retas[4]).scale(tamanho_valores).shift(0.5*UP),
            TextMobject("4 meses").move_to(retas[5]).scale(tamanho_valores).shift(0.5*UP),
        ]

        self.grupos = [
            VGroup(
                valores[0],
                valores[1],
                retas[0],
                meses[0],
                taxas[0]
            ),
            VGroup(
                valores[2],
                valores[3],
                valores[4],
                retas[1],
                retas[2],
                meses[1],
                meses[2],
                taxas[1],
                taxas[2]
            ),
            VGroup(
                valores[5],
                valores[6],
                valores[7],
                valores[8],
                retas[3],
                retas[4],
                retas[5],
                meses[3],
                meses[4],
                meses[5],
                taxas[3],
                taxas[4],
                taxas[5]
            )
        ]

        
    def introducao(self):
        introducao = TextMobject("""
            Imagine que você tem R\$ 1,00 e deseja investir \n 
            esse dinheiro durante um ano
            """)      

        self.play(Write(introducao), run_time=3)
        self.wait(3)
        self.play(FadeOut(introducao))
        self.wait()

    def aplicacao_juros(self):
        for i in range(3):
            self.play(Write(self.historia_do_banco[i]), run_time=2)
            self.wait(4)
            self.play(FadeIn(self.grupos[i]), run_time=2)
            self.wait(4)
            self.play(FadeOut(self.historia_do_banco[i]), FadeOut(self.grupos[i]))

    def conclusao(self):
        conclusao = TextMobject(
            """
            Percebemos que quanto maior a quantidade de\n 
            empréstimos, mais próximo de um número o empréstimo \n 
            resultará. Esse número é chamado de\n 
            constante de euler e possui valor $e=2.71...$
            """
        ) 

        self.play(Write(conclusao), run_time=3)
        self.wait(3)
        self.play(FadeOut(conclusao))
        self.wait()

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
