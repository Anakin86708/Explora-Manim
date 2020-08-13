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

        titulo = TexMobject("\\text{Número de ouro:}\\\\ \\text{razão áurea}")
        titulo.scale(3.5)
        titulo.set_color("#dc6a40")

        self.play(FadeIn(explora))
        self.wait(1)
        self.play(Transform(explora, titulo))
        self.wait(1.5)

############################################
# Cena intermediárias
############################################
class Algebra(Scene):      
    def construct(self):
        # Exibindo título e movendo para o topo
        titulo = TexMobject("\\text{Número de ouro:}\\\\ \\text{razão áurea}")
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
            1.0:TexMobject(
                'a ',
                '=',
                'b',
                '\\phi',
            ),
            1.1:TexMobject(
                'b\\phi',
                ' + b',
            ),
            2.0:TexMobject(
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
            3.0:TexMobject(
                'b',
                '(\\phi + 1)',
            ),
            4.0:TexMobject(
                '\\phi + 1',
            ),
            4.1:TexMobject(
                '\\phi',
            ),
            5.0:TexMobject(
                '{\\phi}^2',
                '= ',
                '\\phi',
                ' + ',
                '1 ',
            ),
            6.0:TexMobject(
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
        self.wait(2)

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
        ## ALINHAMENTO NÃO ESTÁ CORRETO
        self.play(
            eq_inferior[8].next_to, eq_inferior[0], LEFT,
            Transform(eq_inferior[:8], eq_passos[5][1:].move_to(eq_inferior[:8])),
        )
        self.wait(1.5)
        grupo = VGroup(eq_inferior[6:], eq_inferior[0])
        self.play(
            Transform(eq_inferior[:7], eq_passos[5][1:].next_to(eq_inferior[0], RIGHT)),
            Transform(grupo, eq_passos[5][0].move_to(eq_inferior[0])),
        )
        ## ALINHAMENTO NÃO ESTÁ CORRETO
        self.wait(3)
        """

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
        """

        self.wait(5)
        # Limpar Scene
        self.play(
            FadeOutAndShift(titulo, UP),
            FadeOutAndShiftDown(historico),
        )
        self.wait(1)

class Geometria(Scene):   
    def desenhar_fibonacci(self, n, wait_time=0, multiplicador=1, color="#43bfca", align=ORIGIN) -> VGroup:
        try:
            if n < 1:
                raise ValueError

            # Usado para calcular os numeros de Fibonacci    
            fibonacci = lambda x: 1 if x <= 1 else fibonacci(x-1) + fibonacci(x-2)

            quadrados = VGroup()
            lados = {
                0:DOWN,
                1:RIGHT,
                2:UP,
                3:LEFT,
            }

            # Cria o primeiro quadrado
            tamanho = multiplicador
            quadrados.add(Square(side_length = tamanho))
            quadrados[-1].next_to(ORIGIN, DR, buff=0)
            
            # Se necessário, cria o restante
            if n > 1:
                for i in range(1,n):
                    tamanho = fibonacci(i) * multiplicador
                    quadrados.add(Square(side_length = tamanho))
                    quadrados[-1].next_to(quadrados[:i], lados[i%4], buff=0)

            # Deixa a figura centralizada na tela e exibe animação
            quadrados.move_to(align)
            quadrados.set_color(color)
            for i in range(n):
                self.play(
                    ShowCreation(quadrados[i])
                )
                self.wait(wait_time)
            return quadrados

        except ValueError:
            print("Valor inserido é inválido! Tente com um valor maior ou igual a 1")

    def desenhar_arcos(self, quadrados, color = "#F2E33A") -> VGroup:        
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
            ShowCreation(arcos, run_time = 2)
        )
        return arcos

            

    def construct(self):
        # Exibindo título e movendo para o topo
        titulo = TexMobject("\\text{Número de ouro}")
        titulo.set_color(papoula)
        titulo_top = TexMobject("\\text{Abordagem geométrica}")

        titulo.scale(3.5)
        titulo_top.set_color(papoula)
        titulo_top.scale(1)
        titulo_top.to_edge(UP)

        # Animações
        self.play(
            FadeIn(titulo_top),
        )
        # self.wait(2)

        # self.play(
        #     ReplacementTransform(titulo, titulo_top),
        # )
        self.wait(1.5)

        # Desenhando os quadrados e os arcos
        multiplicador = .25
        quadrados = self.desenhar_fibonacci(8, multiplicador=multiplicador)
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
        leg_y.next_to(y,LEFT)
        self.play(
            FadeIn(y),
            Write(leg_y),
            FadeIn(x),
            Write(leg_x),
        )
        self.wait(5)
        

        # Exibe o valor
        formula_str = '\\phi = {{ {} \\over {} }} = {}'.format(val_x, val_y, val_x/val_y)
        formula = TexMobject(
            formula_str
        )

        legendas = VGroup(leg_x,leg_y)
        self.play(
            FadeOut(quadrados),
            FadeOut(x),
            FadeOut(y),
            ReplacementTransform(legendas, formula)
        )

        self.wait(5) 

        # Limpando Scene
        self.play(
            FadeOut(formula),
            FadeOut(arcos),
            FadeOutAndShift(titulo_top, UP),
        )



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
