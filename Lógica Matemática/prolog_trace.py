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
            TexMobject('pais(eva, bob).'),      #0
            TexMobject('pais(tom, bob).'),      #1 
            TexMobject('pais(tom, liz).'),      #2    
            TexMobject(                         #3
                'pais(bob,',
                'ana',
                ').',
            ),   
            TexMobject(                         #4
                'pais(bob,',
                'bia',
                ').',
            ),
            TexMobject(                         #5
                'pais(bia,',
                'leo',
                ').',
            ),
            TexMobject(                         #6
                'ancestral(X,Z):-',
                'pais(X,Z).',
            ), 
            TexMobject(                         #7
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
            'ancestral(',
            'bob',
            ',',
            'leo',
            ').',
        )
        query.next_to(base_dados[-1], 4 * DOWN)
        query.to_corner(LEFT)
        query.scale(0.6)

        # Definindo regras
        regra_busca = TexMobject(
            '\\textbf{Regra da busca:}\\\\ \\text{Percorrer as cláusulas de cima para baixo}'
        )
        regra_computacao = TexMobject(
            '\\textbf{Regra de computação:}\\\\ \\text{Escolher o literal mais a esquerda da} \\\\ \\text{ cláusula objetivo}'
        )
        regras = VGroup(regra_busca, regra_computacao)
        regras.scale(0.6)
        regras.move_to(4 * RIGHT)

        # Iniciando trace
        ponto_central = np.array([4, 2.5, 0])
        seta = ArrowTip(start_angle = 0).scale(0.6)

        objetivos = [
            TexMobject('pais(bob,leo)'),    #0
            TexMobject(                     #1
                'pais(bob,',
                'Y',
                ')',
            ),
            TexMobject(                     #2
                'pais(bob,',
                'ana',
                ')',
            ),
            TexMobject(                     #3
                'ancestral(ana,leo)',
            ),
            TexMobject(                     #4
                'pais(bob,',
                'bia',
                ')',
            ),
            TexMobject(                     #5
                'ancestral(bia,leo)'
            ),
            TexMobject(                     #6
                'pais(ana,leo)' 
            ),
            TexMobject(                     #7
                'pais(bia,leo)'
            ),
            TexMobject(                     #8
                'pais(ana,Y)'
            )
        ]
        objetivos = list(map(lambda x: self.format_objetivo(x), objetivos))

        retangulo_inicial = TexMobject(
            'ancestral(',
            'bob',
            ',',
            'leo',
            ')',
        )
        retangulo_inicial.scale(0.6)
        retangulo_inicial.add(
            SurroundingRectangle(
                retangulo_inicial, 
                color = papoula, 
                opacity = 0.7
                )
            )
        # Posicionamento dos retângulos
        retangulo_inicial.move_to(np.array(ponto_central))
        nivel_um = VGroup(objetivos[1], objetivos[2], objetivos[4])
        nivel_dois = VGroup(objetivos[3], objetivos[5])
        nivel_tres = VGroup(objetivos[6], objetivos[7], objetivos[8])

        objetivos[0].next_to(retangulo_inicial, 5 * DOWN)
        objetivos[0].shift(1.5 * RIGHT)

        nivel_um.next_to(retangulo_inicial, 5 * DOWN)
        nivel_um.shift(1.5 * LEFT)

        nivel_dois.next_to(objetivos[2], 5 * DOWN)    

        nivel_tres.next_to(objetivos[3], 5 * DOWN)

        # Setas
        setas = [
            Arrow(start = objetivos[0].get_top(), end = retangulo_inicial.get_bottom(), color = starship),
            Arrow(start = objetivos[1].get_top(), end = retangulo_inicial.get_bottom(), color = starship),
            Arrow(start = objetivos[3].get_top(), end = objetivos[1].get_bottom(), color = starship),
            Arrow(start = objetivos[6].get_top(), end = objetivos[3].get_bottom(), color = starship),
        ]

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
            Write(query[1:]),
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
            ReplacementTransform(query[2].copy(), retangulo_inicial[1]),
            ReplacementTransform(query[4].copy(), retangulo_inicial[3]),
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
            ShowCreation(setas[0]),
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
        self.wait(3)

        self.play(
            FadeOutAndShift(seta_secundaria, LEFT),
            FadeOutAndShiftDown(falso),
        )
        self.wait(1.5)

        # Continua com a execução principal
        self.play(
            seta.next_to, base_dados[6], LEFT,
        )
        seta.set_color(papoula)
        self.wait(1)
        self.play(
            seta.next_to, base_dados[7], LEFT ,
        )
        seta.set_color(apatita)
        self.wait(1)
        self.play(
            Indicate(retangulo_inicial),
        )
        self.wait(1.5)

        # Colocar lado esquerdo do trace
        self.play(
            seta.next_to, base_dados[7][1], LEFT,
        )
        self.wait(1.5)
        
        self.play(
            FadeIn(objetivos[1]),
        )
        self.wait(1)
        self.play(
            ShowCreation(setas[1]),
        )
        self.wait(1.5)

        # Resolvendo pais Y
        seta_secundaria.set_color(papoula)
        seta_secundaria.next_to(base_dados[0], LEFT)
        self.play(
            GrowFromEdge(seta_secundaria, LEFT),
        )
        for i in range(3):
            self.wait(0.5)
            self.play(
                seta_secundaria.next_to, base_dados[i+1], LEFT,
            )
        seta_secundaria.set_color(apatita)
        self.wait(1.5)

        # Encontra ana
        self.play(
            FadeIn(objetivos[2]),
            FadeOut(objetivos[1]),
            ReplacementTransform(base_dados[3][1].copy(), objetivos[2][1]),
        )
        self.wait(3)

        # Coloca Y em ancestral ana, leo
        self.play(
            seta.next_to, base_dados[7][2], LEFT,
        )
        self.wait(1)
        self.play(
            FadeIn(objetivos[3]),
        )
        self.wait(1)
        self.play(
            ShowCreation(setas[2]),
        )   

        # Resolvendo ancestral ana, leo
        seta_tres = seta_secundaria.copy()
        seta_tres.set_color(papoula)
        seta_tres.next_to(base_dados[0], LEFT)
        self.play(
            GrowFromEdge(seta_tres, LEFT)
        )
        for i in range(6):
            self.wait(0.5)
            self.play(
                seta_tres.next_to, base_dados[i+1], LEFT,
            )
        seta_tres.set_color(apatita)
        self.wait(1)
        # Resolvendo pais ana, leo
        self.play(
            seta_tres.next_to, base_dados[6][1], LEFT,
        )
        self.wait(1)
        self.play(
            FadeIn(objetivos[6]),            
        )
        self.wait(1)
        self.play(
            ShowCreation(setas[3]),
        )
        self.wait(3)

        # Procurando pais ana, leo
        seta_quatro = seta_tres.copy()
        seta_quatro.set_color(papoula)
        seta_quatro.next_to(base_dados[0], LEFT)
        self.play(
            GrowFromEdge(seta_quatro, LEFT)
        )
        for i in range(7):
            self.wait(0.5)
            self.play(
                seta_quatro.next_to, base_dados[i+1], LEFT,
            )

        self.wait(1)
        falso.next_to(objetivos[6], DOWN)
        self.play(
            Write(falso),
        )
        self.wait(3)

        ## ARRUMAR O FADE DO FALSO E COLOCAR AGORA COM A BIA

        # Falso para ana
        self.play(
            FadeOutAndShift(seta_quatro, LEFT),
            FadeOutAndShiftDown(falso),
        )
        self.wait(1)
        self.play(
            FadeOut(objetivos[6]),
            FadeOut(setas[3]),
        )
        self.wait(1.5)

        # Retorna a seta para proximo ancestral
        seta_tres.set_color(papoula)
        self.play(
            seta_tres.next_to, base_dados[6], LEFT,
        )
        self.wait(1)
        self.play(
            seta_tres.next_to, base_dados[7], LEFT,
        )
        seta_tres.set_color(apatita)
        self.wait(1.5)

        # Seta em pais ana, Y
        self.play(
            seta_tres.next_to, base_dados[7][1], LEFT,
        )
        self.wait(1.5)

        self.play(
            FadeIn(objetivos[8]),
        )
        self.wait(1)
        self.play(
            FadeIn(setas[3]),
        )
        
        # Resolver pais ana, Y
        seta_quatro.next_to(base_dados[0], LEFT)
        seta_quatro.set_color(papoula)
        self.play(
            GrowFromEdge(seta_quatro, LEFT)
        )
        for i in range(7):
            self.wait(0.5)
            self.play(
                seta_quatro.next_to, base_dados[i+1], LEFT,
            )

        self.wait(1)
        falso.next_to(objetivos[6], DOWN)
        self.play(
            Write(falso),
        )
        self.wait(3)

        self.play(
            FadeOutAndShiftDown(falso),
            FadeOutAndShift(seta_quatro, LEFT),
        )

        # Remover pais ana, Y
        self.wait(1)
        self.play(
            FadeOut(objetivos[8]),
            FadeOut(setas[3]),
            seta_tres.next_to, base_dados[7], LEFT,
        )
        self.wait(1)
        #Remover ancestral ana, leo
        self.play(
            FadeOutAndShift(seta_tres, LEFT),
            FadeOut(objetivos[3]),
            FadeOut(setas[2]),
        )
        self.wait(1.5)

        # Retorna seta para pais
        self.play(
            seta.next_to, base_dados[7][1], LEFT,
        )
        self.wait(1.5)

        # Avançar para pais bob, bia
        seta_secundaria.set_color(papoula)
        self.play(
            seta_secundaria.next_to, base_dados[4], LEFT,
        )
        seta_secundaria.set_color(apatita)
        self.wait(1.5)

        # Subistituir pais bob, bia
        self.play(
            FadeOut(objetivos[2]),
            ReplacementTransform(base_dados[4].copy(), objetivos[4]),
        )
        self.wait(1.5)

        # Avança para ancestral
        self.play(
            seta.next_to, base_dados[7][2], LEFT,
        )
        self.wait(1)
        self.play(
            FadeIn(objetivos[5]),
        )
        self.wait(1)
        self.play(
            ShowCreation(setas[2]),
        )

        # Resolvendo ancestral bia, leo
        seta_tres.next_to(base_dados[0], LEFT)
        seta_tres.set_color(papoula)
        self.play(
            GrowFromEdge(seta_tres, LEFT)
        )
        for i in range(6):
            self.wait(0.5)
            self.play(
                seta_tres.next_to, base_dados[i+1], LEFT,
            )
        seta_tres.set_color(apatita)
        self.wait(1.5)

        self.play(
            seta_tres.next_to, base_dados[6][1], LEFT,
        )
        self.wait(1.5)
        
        # Exibe retângulo pais bia, leo
        self.play(
            FadeIn(objetivos[7]),
        )
        self.wait(1)
        self.play(
            FadeIn(setas[3]),
        )
        self.wait(1.5)

        # Procurando pais bia, leo
        seta_quatro.next_to(base_dados[0], LEFT)
        seta_quatro.set_color(papoula)
        self.play(
            GrowFromEdge(seta_quatro, LEFT)
        )
        for i in range(5):
            self.wait(0.5)
            self.play(
                seta_quatro.next_to, base_dados[i+1], LEFT,
            )
        self.wait(1.5)

        seta_quatro.set_color(apatita)
        self.wait(1.5)
        verdade.next_to(objetivos[7], DOWN)
        self.play(
            FadeIn(verdade),
        )
        self.wait(10)

        # Removendo objetos da scene
        self.play(          
            *[FadeOutAndShift(item, LEFT) for item in base_dados],
            FadeOutAndShift(query, LEFT),
            FadeOutAndShift(seta_quatro, LEFT),
            FadeOutAndShift(seta_tres, LEFT),
            FadeOutAndShift(seta_secundaria, LEFT),
            FadeOutAndShift(seta, LEFT),

            Uncreate(retangulo_inicial),
            Uncreate(objetivos[0]),
            Uncreate(objetivos[4]),
            Uncreate(objetivos[5]),
            Uncreate(objetivos[7]),
            Uncreate(verdade),
            *[Uncreate(item) for item in setas],
            Uncreate(separador),
            Uncreate(titulo),
        )
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