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

from manimlib.imports import *
apatita = "#43bfca"
papoula = "#dc6a40"
starship = "#F2E33A"


############################################
# Cena de abertura
############################################

class Abertura(Scene):
    def construct(self):
        explora = TexMobject(
            "\\vec{E}\\hspace{-1mm}\\times\\hspace{-1mm}\\vec{p}\\mathcal{L}0\\mathbb{R}a")
        explora.scale(4.5)
        explora.set_color("#43bfca")

        titulo = TexMobject("\\text{Produtos notáveis}")
        titulo.scale(3.5)
        titulo.set_color("#dc6a40")

        self.play(FadeIn(explora))
        self.wait(1)
        self.play(Transform(explora, titulo))
        self.wait(1.5)

############################################
# Cena intermediárias
############################################

# GRID from theoremofbeethoven
class Grid(VGroup):
    CONFIG = {
        "height": 7.0,
        "width": 7.0,
    }

    def __init__(self, rows, columns, **kwargs):
        digest_config(self, kwargs, locals())
        super().__init__(**kwargs)

        x_step = self.width / self.columns
        y_step = self.height / self.rows

        for x in np.arange(0, self.width + x_step, x_step):
            self.add(Line(
                [x - self.width / 2., -self.height / 2., 0],
                [x - self.width / 2., self.height / 2., 0],
            ))
        for y in np.arange(0, self.height + y_step, y_step):
            self.add(Line(
                [-self.width / 2., y - self.height / 2., 0],
                [self.width / 2., y - self.height / 2., 0]
            ))


class ScreenGrid(VGroup):
    CONFIG = {
        "rows": 8,
        "columns": 14,
        "height": FRAME_Y_RADIUS * 2,
        "width": 14,
        "grid_stroke": 0.5,
        "grid_color": WHITE,
        "axis_color": RED,
        "axis_stroke": 2,
        "labels_scale": 0.25,
        "labels_buff": 0,
        "number_decimals": 2
    }

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        rows = self.rows
        columns = self.columns
        grid = Grid(width=self.width, height=self.height, rows=rows, columns=columns)
        grid.set_stroke(self.grid_color, self.grid_stroke)

        vector_ii = ORIGIN + np.array((- self.width / 2, - self.height / 2, 0))
        vector_si = ORIGIN + np.array((- self.width / 2, self.height / 2, 0))
        vector_sd = ORIGIN + np.array((self.width / 2, self.height / 2, 0))

        axes_x = Line(LEFT * self.width / 2, RIGHT * self.width / 2)
        axes_y = Line(DOWN * self.height / 2, UP * self.height / 2)

        axes = VGroup(axes_x, axes_y).set_stroke(self.axis_color, self.axis_stroke)

        divisions_x = self.width / columns
        divisions_y = self.height / rows

        directions_buff_x = [UP, DOWN]
        directions_buff_y = [RIGHT, LEFT]
        dd_buff = [directions_buff_x, directions_buff_y]
        vectors_init_x = [vector_ii, vector_si]
        vectors_init_y = [vector_si, vector_sd]
        vectors_init = [vectors_init_x, vectors_init_y]
        divisions = [divisions_x, divisions_y]
        orientations = [RIGHT, DOWN]
        labels = VGroup()
        set_changes = zip([columns, rows], divisions, orientations, [0, 1], vectors_init, dd_buff)
        for c_and_r, division, orientation, coord, vi_c, d_buff in set_changes:
            for i in range(1, c_and_r):
                for v_i, directions_buff in zip(vi_c, d_buff):
                    ubication = v_i + orientation * division * i
                    coord_point = round(ubication[coord], self.number_decimals)
                    label = Text(f"{coord_point}",font="Arial",stroke_width=0).scale(self.labels_scale)
                    label.next_to(ubication, directions_buff, buff=self.labels_buff)
                    labels.add(label)

        self.add(grid, axes, labels)


class Algebra(Scene):      
    def construct(self):
        # Exibindo título e movendo para o topo
        titulo = TexMobject("\\text{Número de ouro}")
        titulo.set_color(papoula)
        titulo_top = TexMobject("\\text{Abordagem algébrica}")

        titulo.scale(3.5)
        titulo_top.set_color(papoula)
        titulo_top.scale(1)
        titulo_top.to_edge(UP)

        # Texto inicial
        texto_inicial = TexMobject(
            "\\text{Dois valores positivos estão em razão áurea se sua }\\\\ \
                \\text{razão é igual à razão da sua soma pela maior das quantidades}"
        )
        # Equação inicial
        eq_inicial = TexMobject(
            '{{a+b}',       # 0
            '\\over',       # 1
            '{a}}',         # 2   
            ' = ',          # 3
            '{{a}',         # 4
            '\\over',       # 5
            '{b}}',         # 6
            ' = ',          # 7
            '\\phi',        # 8
        )

        eq_passos = [
            TexMobject('a = b\\phi'),
            TexMobject('b\\phi + b'),
            TexMobject('b\\phi'),
            TexMobject('\\phi + 1'),
            TexMobject('\\phi'),
            TexMobject('\\phi + 1 = {\\phi}^2'),
            TexMobject('{\\phi}^2 - \\phi - 1 = 0'),
        ]


        # Animações

        self.play(
            FadeIn(titulo),
        )
        self.wait(2)

        self.play(
            ReplacementTransform(titulo, titulo_top),
        )
        self.wait(1.5)

        # Escreve eq inicial
        historico = VGroup()
        self.play(
            Write(eq_inicial),
        )
        historico.add(eq_inicial)
        self.wait(1.5)

        # Coloca texto
        texto_inicial.next_to(eq_inicial, DOWN)
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
        eq_superior = eq_inicial[4:].copy()
        eq_superior.next_to(eq_inicial, DOWN)


        # Mostra a/b = phi
        self.play(
            ReplacementTransform(eq_inicial[4:].copy(), eq_superior)
        )
        self.wait(1.5)
        historico.add(eq_superior)

        eq_inferior = eq_inicial[:7].copy()
        self.play(
            eq_inferior.next_to, eq_superior, DOWN,
        )
        self.wait(1)
        historico.add(eq_inferior)

        # Remove equação inicial
        self.play(
            historico.shift, UP,
            # FadeOutAndShift(eq_inicial, UP),
        )
        self.wait(1)


        # Isolando a
        self.play(
            Transform(eq_superior,eq_passos[0].move_to(eq_superior)),
        )
        self.wait(2)

        # Subitituindo a       
        self.play(
            Transform(eq_inferior[0], eq_passos[1].move_to(eq_inferior[0])),
            Transform(eq_inferior[2], eq_passos[2].move_to(eq_inferior[2]).copy()),
            Transform(eq_inferior[4], eq_passos[2].move_to(eq_inferior[4]).copy()),
        )
        self.wait(2)

        # Cancelando b
        self.play(
            Transform(eq_inferior[0], eq_passos[3].move_to(eq_inferior[0])),
            Transform(eq_inferior[2], eq_passos[4].move_to(eq_inferior[2]).copy()),
            Transform(eq_inferior[4:], eq_passos[4].move_to(eq_inferior[4]).copy()),
        )
        self.wait(3)

        # Multiplicando por phi
        self.play(
            Transform(eq_inferior, eq_passos[5].move_to(eq_inferior)),
        )
        self.wait(3)

        # Muda termos
        self.play(
            Transform(eq_inferior, eq_passos[6].move_to(eq_inferior)),
        )
        self.wait(3)

        # Solucionar equação
        eq_solucao = TexMobject(
            '\\phi = {{1 + \\sqrt{5}} \\over {2}}',
            '\\approx 1,61803398875',
        )
        eq_solucao.next_to(eq_inferior, DOWN)
        self.play(
            Write(eq_solucao),
        )
        self.wait(1)
        self.play(
            # Write(eq_solucao[1]),
            FadeToColor(eq_solucao[1], starship),
        )
        historico.add(eq_solucao)
        

        self.wait(5)
        # Limpar Scene
        self.play(
            FadeOutAndShift(titulo_top, UP),
            FadeOutAndShiftDown(historico),
        )
        self.wait(1)

class Geometria(Scene):      
    def construct(self):
        # Exibindo título e movendo para o topo
        titulo = TexMobject("\\text{Número de ouro}")
        titulo.set_color(papoula)
        titulo_top = TexMobject("\\text{Abordagem geométrica}")

        titulo.scale(3.5)
        titulo_top.set_color(papoula)
        titulo_top.scale(1)
        titulo_top.to_edge(UP)

        grid=ScreenGrid()
        self.add(grid)

        # Animações
        self.play(
            FadeIn(titulo),
        )
        self.wait(2)

        self.play(
            ReplacementTransform(titulo, titulo_top),
        )
        self.wait(1.5)



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
