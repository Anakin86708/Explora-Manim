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
from math import e
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
class Serie(Scene):
    def construct(self):
        # Exibindo título e movendo para o topo
        titulo_top = TexMobject("\\text{Expansão de série}")
        titulo_top.set_color(PAPOULA)
        titulo_top.scale(1)
        titulo_top.to_edge(UP)

        texto_inicial = TexMobject(
            '\\text{Uma constante irracional, ou seja,} \\\\'
            '\\text{não pode ser escrito como uma simples fração.}'
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
        self.play(
            Write(titulo_top),
        )
        self.wait(1.5)

        self.play(
            Write(texto_inicial),
        )
        self.wait(8)
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

    def calcular_euler(self, x):
        try:
            return (1*(1/x))**x
        except ZeroDivisionError:
            pass

    def config(self):
        self.historia_do_banco = [
            TextMobject(
                """
                Suponhamos um banco com uma aplicação\n
                financeira que forneça 100\% de retorno ao final de um ano\n
                """
            ).to_edge(UP),
            TextMobject(
                """
                Se o banco tiver um de retorno de 50\%\n
                a cada semestre
                """
            ).to_edge(UP),
            TextMobject(
                """
                Se o banco tiver um de retorno de 33,3\%\n
                a cada quadrimestre
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
            TexMobject("R\$1,00").move_to(5.25*LEFT),
            TexMobject("R\$2,00").move_to(5.25*RIGHT),

            TexMobject("R\$1,00").move_to(5.25*LEFT),
            TexMobject("R\$1,50").move_to(ORIGIN),
            TexMobject("R\$2,25").move_to(5.25*RIGHT),

            TexMobject("R\$1,00").move_to(5.25*LEFT),
            TexMobject("R\$1,33").move_to(1.75*LEFT),
            TexMobject("R\$1,76").move_to(1.75*RIGHT),
            TexMobject("R\$2,35").move_to(5.25*RIGHT),
        ]

        valores = [item.scale(tamanho_valores) for item in valores]

        taxas = [
            TextMobject("100\%").move_to(retas[0]),

            TextMobject("50\%").move_to(retas[1]),
            TextMobject("50\%").move_to(retas[2]),

            TextMobject("33\%").move_to(retas[3]),
            TextMobject("33\%").move_to(retas[4]),
            TextMobject("33\%").move_to(retas[5])
        ]

        taxas = [item.scale(tamanho_valores).shift(0.5*DOWN) for item in taxas]

        meses = [
            TextMobject("12 meses").move_to(retas[0]),

            TextMobject("6 meses").move_to(retas[1]),
            TextMobject("6 meses").move_to(retas[2]),

            TextMobject("4 meses").move_to(retas[3]),
            TextMobject("4 meses").move_to(retas[4]),
            TextMobject("4 meses").move_to(retas[5]),
        ]

        meses = [item.scale(tamanho_valores).shift(0.5*UP) for item in meses]

        formulas = [
            TexMobject('2 = \\left (1 + {{1} \\over {1}} \\right )^1'),
            TexMobject('2,25 = \\left (1 + {{1} \\over {2}} \\right )^2'),
            TexMobject('2,37 = \\left (1 + {{1} \\over {3}} \\right )^3'),
        ]

        formulas = [item.shift(1.5*DOWN) for item in formulas]

        self.grupos = [
            VGroup(
                valores[0],
                valores[1],
                retas[0],
                meses[0],
                taxas[0],
                formulas[0],
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
                taxas[2],
                formulas[1],
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
                taxas[5],
                formulas[2],
            )
        ]

    def introducao(self):
         # Exibindo título e movendo para o topo
        titulo = TexMobject("\\text{Número de Euler}")
        titulo.set_color(PAPOULA)
        titulo_top = TexMobject("\\text{Problema dos juros}")

        titulo.scale(2.5)
        titulo_top.set_color(PAPOULA)
        titulo_top.scale(1)
        titulo_top.to_edge(UP)
        
        introducao = TextMobject("""
            Imagine que você tem R\$ 1,00 e deseja investir \n
            esse dinheiro durante um ano.
            """)

        # Animações
        self.add(titulo)
        self.wait(1)

        self.play(
            Transform(titulo, titulo_top),
        )
        self.wait(1.5)

       
        self.play(
            Write(introducao),
            run_time=3
            )
        self.wait(3)
        self.play(
            FadeOut(introducao),
            FadeOut(titulo),
        )
        self.wait()

    def aplicacao_juros(self):
        for i in range(3):
            self.play(Write(self.historia_do_banco[i]), run_time=2)
            self.wait(4)
            self.play(FadeIn(self.grupos[i]), run_time=2)
            self.wait(4)
            self.play(FadeOut(self.historia_do_banco[i]), FadeOut(self.grupos[i]))


class Grafico(GraphScene):
    CONFIG = {
        "x_min": 0,
        "x_max": 10,
        "y_min": 0,
        "y_max": 3,
        "y_axis_height": 5,
        "x_axis_width": 10,
        "x_tick_frequency": 1,
        "y_tick_frequency": 1,
        "y_labeled_nums": range(4),
        "x_labeled_nums": range(11),
        "exclude_zero_label": False,
        "graph_origin": 3 * DOWN + 5 * LEFT,
        "function_color": PAPOULA,
        "axes_color": APATITA,
    }

    def conclusao(self):
        conclusao = TextMobject(
            """
            Percebemos que o valor do investimento se aproxima\n 
            de um número. Essa é a constante de Euler e tem valor\n
            $e=2.71...$
            """
        )

        self.play(
            Write(conclusao),
            run_time=3
        )
        self.wait(5)
        self.play(
            FadeOut(conclusao)
        )
        self.wait()

    def func_graph(self, x):
        return (1 + (1 / x)) ** x

    def e_graph(self, x):
        return e

    def construct(self):
        textos = VGroup(
            TexMobject(
                '\\text{Podemos escrever o problema anterior}\\\\'
                '\\text{da seguinte forma}'
            ),
            TexMobject(
                '\\text{Onde } x \\text{ representa a} \\\\'
                '\\text{quantidade de juros aplicados}'
            )
        )
        legenda_limite = TexMobject(
            '\\lim_{x \\to \\infty}',
            '{\\left(1 + {{1} \\over {x}}\\right)} ^ x',
            '= e'
            )
        legenda_limite[1].move_to(ORIGIN)
        textos.next_to(legenda_limite, UP)

        # Animações
        self.play(
            Write(textos[0]),
            ShowCreation(legenda_limite[1]),
        )
        self.wait(5)
        self.play(
            ReplacementTransform(textos[0], textos[1]),
        )
        self.wait(5)
        self.play(
            FadeOut(textos[1]),
        )

        # Criando o gráfico
        self.setup_axes(animate=True)

        graph_limite = self.get_graph(
            self.func_graph,
            self.function_color,
            x_min=0,
            x_max=10
        )
        graph_e = self.get_graph(
            self.e_graph,
            STARSHIP,
            x_min=0,
            x_max=10,
        )

        # legenda_limite.next_to(graph_limite, 0.05 * DOWN)

        legenda_e = TexMobject('e')
        legenda_e.next_to(graph_e, UP)

        self.play(
            ShowCreation(graph_limite),
            ShowCreation(graph_e),
            Write(legenda_e),
            # Write(legenda_limite),
        )
        self.wait(5)

        legenda_limite[0].next_to(legenda_limite[1], LEFT)
        legenda_limite[2].next_to(legenda_limite[1], RIGHT)
        self.play(
            Write(legenda_limite[0]),
            ReplacementTransform(legenda_e.copy(), legenda_limite[2]),
        )
        self.wait(5)

        # Limpando Scene
        self.play(
            FadeOut(legenda_limite),
            FadeOut(legenda_e),
            FadeOut(graph_limite),
            FadeOut(graph_e),
            FadeOut(self.axes),
        )
        # Apresentando conclusão
        self.conclusao()


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

        autor = TexMobject(
            "\\text{Animações: Ariel Tadeu da Silva}\\\\"
            "\\text{Eric Satoshi Suzuki Kishimoto} \\\\"
            )
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

# TODO
# Colocar gráfico antes
# Terminar outros ajustes [2, 4, 6]