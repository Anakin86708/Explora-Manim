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
    def desenhar_fibonacci(self, n, wait_time = 0, multiplicador = 1, color = "#43bfca") -> VGroup:
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
            quadrados.move_to(ORIGIN)
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
            FadeIn(titulo),
        )
        self.wait(2)

        self.play(
            ReplacementTransform(titulo, titulo_top),
        )
        self.wait(1.5)

        # Desenhando os quadrados e os arcos
        quadrados = self.desenhar_fibonacci(8, multiplicador=.25)
        self.desenhar_arcos(quadrados)
        self.wait(3)

        # Exibindo tamanho
        x = Brace(quadrados, DOWN)
        y = Brace(quadrados, LEFT)
        self.play(
            FadeIn(y),
            FadeIn(x),
        )
        

        # Exibe o valor
        # formula - TexMobject(
        #     '\\phi = ',
        # )

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
