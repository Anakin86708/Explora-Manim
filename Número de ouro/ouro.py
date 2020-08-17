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

        titulo = TexMobject("\\text{Número de ouro:}\\\\ \\text{razão áurea}")
        titulo.scale(2.5)
        titulo.set_color("#dc6a40")

        self.play(FadeIn(explora))
        self.wait(1)
        self.play(Transform(explora, titulo))
        self.wait(1.5)

############################################
# Cena intermediárias
############################################
class Algebra(GraphScene):   
    CONFIG = {
        "x_min": -5,
        "x_max": 5,
        "y_min": -5,
        "y_max": 5,
        "y_axis_height": 5,
        "x_axis_width": 5,
        "graph_origin": ORIGIN,
        "function_color": PAPOULA,
        "axes_color": APATITA,
    }   

    def func_to_graph(self, x):
        return x**2 - x - 1

    def construct(self):
        # Exibindo título e movendo para o topo
        titulo = TexMobject("\\text{Número de ouro:}\\\\ \\text{razão áurea}")
        titulo.set_color(PAPOULA)
        titulo_top = TexMobject("\\text{Abordagem algébrica}")

        titulo.scale(2.5)
        titulo_top.set_color(PAPOULA)
        titulo_top.scale(1)
        titulo_top.to_edge(UP)

        # Texto inicial
        texto_inicial = TexMobject(
            "\\text{Dois valores positivos estão em razão áurea se sua }\\\\ \
            \\text{razão é igual à razão da sua soma pela maior das quantidades}"
        )

        # Condições
        condicao = TexMobject(
            "\\text{Considere dois valores } a \\text{ e } b \\text{, onde } a > 0 \\text{ e } b > 0"
        )
        # Equação inicial
        eq_inicial = TexMobject(
            '{{a}',         # 0
            '\\over',       # 1
            '{b}}',         # 2
            ' = ',          # 3
            '{{a',          # 4
            '+',            # 5
            'b}',           # 6
            '\\over',       # 7
            '{a}}',         # 8
            ' = ',          # 9
            '\\phi',        # 10
        )

        eq_superior = TexMobject(
            '{{a}',         # 0
            '\\over',       # 1
            '{b}}',         # 2
            ' = ',          # 3
            '\\phi'         # 4
        )

        eq_inferior = TexMobject(
            '{{a}',         # 0
            '\\over',       # 1
            '{b}}',         # 2
            ' = ',          # 3
            '{{a',          # 4   
            '+',            # 5
            'b}',           # 6
            '\\over',       # 7
            '{a}}',         # 8
        )

        eq_passos = {
            1.0: TexMobject(
                'a ',
                '=',
                'b',
                '\\phi',
            ),
            1.1: TexMobject(
                'b\\phi',
                ' + b',
            ),
            2.0: TexMobject(
                '{{b',          # 0
                '\\phi}'        # 1
                '\\over',       # 2
                '{b}}',         # 3
                ' = ',          # 4
                '{{b',          # 5
                '\\phi}'        # 6   
                '+',            # 7
                'b',            # 8
                '\\over',       # 9
                '{b',           # 10
                '\\phi}}'       # 11
            ),
            3.0: TexMobject(
                'b',
                '(\\phi + 1)',
            ),
            4.0: TexMobject(
                '\\phi + 1',
            ),
            4.1: TexMobject(
                '\\phi',
            ),
            5.0: TexMobject(
                '{\\phi}^2',
                '= ',
                '\\phi',
                ' + ',
                '1 ',
            ),
            6.0: TexMobject(
                '{\\phi}^2',
                ' - \\phi ',
                '- 1',
                '= 0',
            ),
        }

        # Animações
        self.add(titulo)
        self.wait(1)

        self.play(
            Transform(titulo, titulo_top),
        )
        self.wait(1.5)

        # Coloca condição
        condicao.next_to(eq_inicial, 1.5 * DOWN)
        self.play(
            Write(condicao),
        )
        self.wait(7)

        # Escreve eq inicial
        historico = VGroup()
        self.play(
            FadeOutAndShiftDown(condicao),
            Write(eq_inicial),
        )
        historico.add(eq_inicial)
        self.wait(2)

        # Coloca texto
        texto_inicial.next_to(eq_inicial, 1.5 * DOWN)
        self.play(
            Write(texto_inicial),
        )
        self.wait(10)        
        self.play(
            FadeOutAndShiftDown(texto_inicial),
        )
        self.wait(2)

        # Separa equação inicial
        self.play(
            eq_inicial.shift, UP
        )
        self.wait(1)

        # Mostra a/b = phi
        grupo = VGroup(eq_inicial[:4],eq_inicial[10])
        eq_superior.next_to(eq_inicial, DOWN)
        self.play(
            ReplacementTransform(grupo.copy(), eq_superior)
        )
        self.wait(2)
        historico.add(eq_superior)

        # Mostra a/b = (a+b)/a
        grupo = VGroup(eq_inicial[:9])
        eq_inferior.next_to(eq_superior, DOWN)
        self.play(
            ReplacementTransform(grupo.copy(), eq_inferior)
        )
        self.wait(2)
        historico.add(eq_inferior)

        # Isolando a
        eq_passos[1].move_to(eq_superior)
        self.play(
            Transform(eq_superior[:2], eq_passos[1][0]),
            Transform(eq_superior[2], eq_passos[1][2]),
            Transform(eq_superior[3], eq_passos[1][1]),
            Transform(eq_superior[4], eq_passos[1][3]),
        )
        self.wait(2)

        # Subitituindo a       
        sub = [eq_passos[1][2:].copy(),eq_passos[1][2:].copy(),eq_passos[1][2:].copy()]
        eq_passos[1.1].move_to(eq_inferior[4:7])
        self.play(
            FadeOut(eq_inferior[0]),
            FadeOut(eq_inferior[8]),
            Transform(eq_inferior[4:7], eq_passos[1.1]),
            sub[0].move_to, eq_inferior[0],
            sub[1].move_to, eq_passos[1.1][0],
            sub[2].move_to, eq_inferior[8],
        )
        self.wait(2)

        # Colocando b em evidência
        eq_passos[3].move_to(eq_inferior[4:7])
        self.play(
            FadeOut(sub[1]),
            Transform(eq_inferior[4:7], eq_passos[3])
        )
        self.wait(3.5)

        # Cancelando b
        self.play(
            FadeOut(sub[0]),
            FadeOut(sub[2]),
            Transform(eq_inferior[0:3], eq_passos[4.1].move_to(eq_inferior[0:3]).copy()),
            Transform(eq_inferior[4:7], eq_passos[4].move_to(eq_inferior[4:7])),
            Transform(eq_inferior[8], eq_passos[4.1].move_to(eq_inferior[8]).copy()),
        )
        self.wait(3)

        # Multiplicando por phi
        self.play(
            eq_inferior[8].next_to, eq_inferior[0], LEFT,
            Transform(eq_inferior[1:8], eq_passos[5][1:].next_to(eq_inferior[0], RIGHT)),
        )
        self.wait(1.5)
        grupo = VGroup(eq_inferior[8], eq_inferior[0])
        self.play(
            Transform(grupo, eq_passos[5][0].move_to(eq_inferior[0])),
        )
        self.wait(3)

        # Muda termos
        eq_passos[6].move_to(eq_inferior)
        self.play(
            FadeOut(eq_passos[5][4]),
            Transform(eq_inferior[1], eq_passos[6][3]),
            Transform(eq_inferior[2], eq_passos[6][1]),
            Transform(eq_inferior[3:8], eq_passos[6][2]),
            Transform(grupo, eq_passos[6][0]),
        )
        self.wait(3)

        # Colocando gráfico da equação
        self.play(
            FadeOutAndShiftDown(historico[:-1]),
            eq_inferior.shift, 1.3 * DOWN,
        )
        self.setup_axes(animate=True),

        # Desenhando gráfico
        func_graph = self.get_graph(
            self.func_to_graph, 
            self.function_color,
            x_min=-2,
            x_max=3,
        )
        self.play(
            ShowCreation(func_graph),
        )
        self.wait(3)

        # Determinando raizes
        x = self.coords_to_point(1, self.func_to_graph(0))
        y = self.coords_to_point(0, self.func_to_graph(0))
        raiz_1 = Dot(self.coords_to_point((1-math.sqrt(5))/2, 0))
        raiz_2 = Dot(self.coords_to_point((1+math.sqrt(5))/2, 0))
        raiz_2.set_color(STARSHIP)
        self.play(
            ShowCreation(raiz_1),
            ShowCreation(raiz_2),
        )

        # Solucionar equação
        eq_solucao = TexMobject(
            '\\phi = {{1 + \\sqrt{5}} \\over {2}}',
            '\\approx 1,61803398875',
        )
        eq_solucao.next_to(self.axes, DOWN)
        self.play(
            FadeOut(eq_inferior),
            Write(eq_solucao[0]),
        )
        self.wait(1)
        eq_solucao[1].set_color(STARSHIP)
        self.play(
            Write(eq_solucao[1]),
        )
        historico.add(eq_solucao)

        self.wait(5)
        # Limpar Scene
        grupo = VGroup(self.axes, func_graph, raiz_1, raiz_2)
        self.play(
            FadeOut(grupo),
            FadeOutAndShift(titulo, UP),
            FadeOutAndShiftDown(historico[-1]),
        )
        self.wait(1)


class Geometria(Scene):
    def desenhar_fibonacci(self, n, wait_time=0, multiplicador=1, color="#43bfca", align=ORIGIN, labels_inside=False):
        try:
            if n < 1:
                raise ValueError

            # Usado para calcular os numeros de Fibonacci
            fibonacci = lambda x: 1 if x <= 1 else fibonacci(x-1) + fibonacci(x - 2)

            quadrados = VGroup()
            legendas = VGroup()
            lados = {
                0: DOWN,
                1: RIGHT,
                2: UP,
                3: LEFT,
            }

            # Cria o primeiro quadrado
            quadrados.add(Square(side_length=multiplicador))
            quadrados[-1].next_to(ORIGIN, DR, buff=0)

            # Se necessário, cria o restante
            if n > 1:
                for i in range(1, n):
                    tamanho = fibonacci(i)
                    quadrados.add(Square(side_length=tamanho * multiplicador))
                    quadrados[-1].next_to(quadrados[:i], lados[i % 4], buff=0)

            if labels_inside:
                for i in range(n):
                    valor = fibonacci(i)
                    legendas.add(TexMobject(valor))
                    legendas[-1].scale(multiplicador * math.sqrt(valor))

            # Deixa a figura centralizada na tela e exibe animação
            quadrados.move_to(align)
            quadrados.set_color(color)
            for i in range(n):
                self.play(
                    ShowCreation(quadrados[i]),
                )
                if labels_inside:
                    legendas[i].move_to(quadrados[i].get_center())
                    self.play(FadeIn(legendas[i])) 
                self.wait(wait_time)
            if labels_inside:
                return quadrados, legendas
            else:
                return quadrados

        except ValueError:
            print("Valor inserido é inválido! Tente com um valor maior ou igual a 1")

    def desenhar_arcos(self, quadrados, color="#F2E33A") -> VGroup:
        arcos = VGroup()
        i = 0
        for quadrado in quadrados:
            pontos = quadrado.get_vertices()
            # Necessário para fazer a animação do arco no sentido correto
            if i % 2:
                arco = ArcBetweenPoints(pontos[(i+2) % 4], pontos[i % 4])
            else:
                arco = ArcBetweenPoints(pontos[i % 4], pontos[(i+2) % 4])
            arcos.add(arco)
            i += 1

        arcos.set_color(color)
        self.play(
            ShowCreation(arcos, run_time=2)
        )
        return arcos

    def construct(self):
        # Exibindo título e movendo para o topo
        titulo = TexMobject("\\text{Número de ouro}")
        titulo.set_color(PAPOULA)
        titulo_top = TexMobject("\\text{Abordagem geométrica}")

        titulo.scale(3.5)
        titulo_top.set_color(PAPOULA)
        titulo_top.scale(1)
        titulo_top.to_edge(UP)

        # Animações
        self.play(
            FadeIn(titulo_top),
        )
        self.wait(1.5)

        # Desenhando os quadrados e os arcos
        n = 8
        multiplicador = .25
        quadrados, legendas_quad = self.desenhar_fibonacci(
            n, multiplicador=multiplicador, labels_inside=True
        )
        arcos = self.desenhar_arcos(quadrados)
        self.wait(3)

        # Exibindo tamanho
        x = Brace(quadrados, DOWN)
        y = Brace(quadrados, LEFT)
        val_x = quadrados[-2].get_width() / multiplicador + quadrados[-1].get_width() / multiplicador
        val_y = quadrados[-1].get_width() / multiplicador
        leg_x = TexMobject(f'{val_x}')
        leg_y = TexMobject(f'{val_y}')
        leg_x.next_to(x, DOWN)
        leg_y.next_to(y, LEFT)
        self.play(
            FadeIn(y),
            Write(leg_y),
            FadeIn(x),
            Write(leg_x),
        )
        self.wait(5)

        # Exibe o valor
        num = f'{val_x}'
        den = f'{val_y}'
        val = '{}'.format(val_x/val_y)
        # formula_str = '\\phi = {{ {} \\over {} }} = '.format(num, val_y)
        formula = TexMobject(
            '\\phi = {{ ',  # 0
            num,            # 1
            '\\over',       # 2
            den,            # 3
            '}} = ',        # 4
            val,            # 5
        )

        legendas = VGroup(leg_x, leg_y)
        self.play(
            FadeOut(quadrados),
            FadeOut(legendas_quad),
            FadeOut(x),
            FadeOut(y),
            ReplacementTransform(legendas, formula[:4]),
        )
        self.wait(2)
        self.play(
            FadeIn(formula[4:]),
        )
        self.wait(3)

        # Continuar na sequencia de Fibonacci
        fibonacci = lambda x: 1 if x <= 1 else fibonacci(x-1) + fibonacci(x-2)
        valores = VGroup(*[TexMobject(fibonacci(i)) for i in range(n, n+14)])
        for i in range(13):
            time = -1.5/14*i + 1.5
            self.play(
                Transform(formula[3], valores[i].move_to(formula[3]), run_time=time),
                Transform(formula[1], valores[i+1].move_to(formula[1]), run_time=time),
                Transform(
                    formula[5],
                    TexMobject(
                        f'{fibonacci(n + i + 1)/fibonacci(n + i)}'
                    ).move_to(formula[5]), run_time=time),
            )
            self.wait(time)

        limite = TexMobject(
            '\\lim_{n \\to \\infty} {F_{n+1} \\over F_{n}}',
            '= 1.6180339887498948',
        )
        limite.next_to(formula[0], RIGHT)
        self.play(
            ReplacementTransform(formula[1:4], limite[0]),
            ReplacementTransform(formula[4:], limite[1]),
        )
        self.play(
            FadeToColor(limite[1], STARSHIP),
        )

        self.wait(5)

        # Limpando Scene
        self.play(
            FadeOut(limite),
            FadeOut(formula[0]),
            FadeOut(arcos),
            FadeOutAndShift(titulo_top, UP),
        )
        self.wait(1)


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
