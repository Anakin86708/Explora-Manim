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
        explora = TexMobject("\\vec{E}\\hspace{-1mm}\\times\\hspace{-1mm}\\vec{p}\\mathcal{L}0\\mathbb{R}a")
        explora.scale(4.5)
        explora.set_color("#43bfca")
        
        titulo = TexMobject("\\text{Lógica Matemática}")
        titulo.scale(3)
        titulo.set_color("#dc6a40")

        self.play(FadeIn(explora))
        self.wait(1)
        self.play(Transform(explora, titulo))
        self.wait(1.5)

############################################
# Cena intermediárias
############################################
class Trace(Scene):
    # Usado para formatar os itens exibidos no trace
    def format_objetivo(self, item) -> TexMobject:
        item.add(
            SurroundingRectangle(
                item, 
                color = papoula, 
                opacity = 0.7
            )
        )
        item.scale(0.6)
        return item

    def construct(self):
        titulo = TexMobject('\\text{Prolog}')
        titulo.scale(3)
        titulo.set_color(papoula)

        titulo_top = TexMobject('\\text{Trace}')
        titulo_top.scale(1)
        titulo_top.to_edge(UP)
        titulo_top.set_color(papoula)

        separador = Line(np.array([0, 3, 0]), np.array([0, -3.5, 0]), color = apatita)

        base_dados = [
            TexMobject('pais(eva, bob).'),
            TexMobject('pais(tom, bob).'),            
            TexMobject('pais(tom, liz).'),            
            TexMobject('pais(bob, ana).'),            
            TexMobject('pais(bob, bia).'),            
            TexMobject('pais(bia, leo).'),    
            TexMobject(
                'ancestral(X,Z):-',
                'pais(X,Z).',
            ),
            TexMobject(
                'ancestral(X,Z):-',
                'pais(X,Y), ',
                ' ancestral(Y,Z).'
            ),
        ]
        base_dados = [item.scale(0.6) for item in base_dados]

        # Alinhando todos os items
        base_dados[0].next_to(np.array([-2, 3, 0]), DOWN)
        base_dados[0].to_corner(LEFT)
        for n in range(1, len(base_dados)):
            # item.shift(0.5 * n * DOWN + np.array([-5, 3, 0]))
            base_dados[n].next_to(base_dados[n-1], DOWN, buff = 0.2)
            base_dados[n].to_corner(LEFT)

        grupo = VGroup(
            base_dados[0],
            base_dados[1],
            base_dados[2],
            base_dados[3],
            base_dados[4],
            base_dados[5],
            base_dados[6],
            base_dados[7],
        )
        base = Brace(grupo, LEFT)

        # Linha query
        query = TexMobject(
            '?- ',
            'ancestral(bob, leo).'
        )
        query.next_to(base_dados[-1], 4 * DOWN)
        query.to_corner(LEFT)
        query.scale(0.6)

        # Definindo regras
        regra_busca = TexMobject(
            '\\textbf{Regra da busca:}\\\\ \\text{Percorrer as cláusulas de cima para baixo}'
        )
        regra_computacao = TexMobject(
            '\\textbf{Regra de computação:}\\\\ \\text{Escolher o literal mais a esquerda da } \\\\ \\text{cláusula objetivo}'
        )
        regras = VGroup(regra_busca, regra_computacao)
        regras.scale(0.6)
        regras.move_to(4 * RIGHT)

        # Iniciando trace
        ponto_central = np.array([4, 2.5, 0])
        seta = ArrowTip(start_angle = 0).scale(0.6)

        objetivos = [
            TexMobject('pais(bob,leo)'),
            # TexMobject(''),
        ]
        objetivos = list(map(lambda x: self.format_objetivo(x), objetivos))

        retangulo_inicial = query[1].copy()
        retangulo_inicial.add(
            SurroundingRectangle(
                retangulo_inicial, 
                color = papoula, 
                opacity = 0.7
                )
            )
        retangulo_inicial.move_to(np.array(ponto_central))

        objetivos[0].next_to(retangulo_inicial, 5 * DOWN)
        objetivos[0].shift(1.5 * RIGHT)

        # Setas
        seta_pais_inicial = Arrow(start = objetivos[0].get_top(), end = retangulo_inicial.get_bottom(), color = starship)

        # Valores
        falso = TexMobject('\\text{Falso}', color = papoula)
        falso.scale(0.7)
        verdade = TexMobject('\\text{Verdadeiro}', color = apatita)
        verdade.scale(0.7)


        # Animações
        self.wait(1.5)
        self.play(
            FadeIn(titulo),
        )
        self.wait(2)

        self.play(
            Transform(titulo, titulo_top),
            ShowCreation(separador),
            *[Write(item) for item in base_dados],
            Write(query[0]),
        )
        self.wait(1.5)

        # Escrevendo query
        self.play(
            Write(query[1]),
            ShowCreation(seta.next_to(query, LEFT)),
        )
        self.wait(1.5)

        # Escrevendo regras
        self.play(
            Write(regra_busca),
        )
        self.wait(3)

        self.play(
            ReplacementTransform(regra_busca, regra_computacao)
        )
        self.wait(3)

        # Procurando em BC
        seta.next_to(base_dados[0], LEFT)
        seta.set_color(papoula)
        self.play(
            FadeOutAndShiftDown(regra_computacao),
            GrowFromEdge(seta, LEFT),
        )
        for i in range(6):
            self.wait(0.5)
            self.play(
                seta.next_to, base_dados[i+1], LEFT,
            )
            if i == 5:
                seta.set_color(apatita)
                self.play(
                    ShowCreationThenFadeOut(seta.copy().next_to(query, LEFT))
                )

        self.wait(1)
        self.play(
            FadeIn(retangulo_inicial),
        )
        self.wait(1.5)

        # Resolvendo ancestral
        self.play(
            seta.next_to, base_dados[6][1], LEFT,
        )
        self.wait(1)
        self.play(
            FadeIn(objetivos[0]),
        )
        self.wait(1)
        self.play(
            ShowCreation(seta_pais_inicial),
        )
        self.wait(1.5)

        # Buscando pais
        seta_secundaria = seta.copy()
        seta_secundaria.set_color(papoula)
        seta_secundaria.next_to(base_dados[0], LEFT)
        self.play(
            GrowFromEdge(seta_secundaria, LEFT),
        )
        for i in range(7):
            self.wait(0.5)
            self.play(
                seta_secundaria.next_to, base_dados[i+1], LEFT,
            )

        self.wait(1)
        falso.next_to(objetivos[0], DOWN)
        self.play(
            Write(falso),
        )
            



        

        # self.wait(5)
        # for x in range(-7, 8):
        #     for y in range(-4, 5):
        #         self.add((Dot(np.array([x, y, 0]), color = DARK_GREY if x != 0 and y != 0 else YELLOW)))
        self.wait(1)



#############################################
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

        agradecimento = TexMobject("\\text{Agradecimento: Prof. Dr. João Roberto Bertini Jr.}")
        agradecimento.scale(1.2)
        agradecimento.set_color("#dc6a40")
        agradecimento.shift(1.3*DOWN)

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
        self.wait(0.3)
        self.play(FadeIn(agradecimento))
        self.wait(2)
############################################
############################################