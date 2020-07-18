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
class Comutativa(Scene):
    def construct(self):
        titulo = TexMobject('\\text{Equivalências lógicas}')
        titulo.scale(3)
        titulo.set_color(papoula)

        tit_comutativa = TexMobject('\\text{Comutativa}')
        tit_comutativa.scale(1)
        tit_comutativa.to_edge(UP)
        tit_comutativa.set_color(papoula)

        comutativa_ou = TexMobject(
            'p \\vee q',
            '\\equiv',
            'q \\vee p',
        )

        comutativa_e = TexMobject(
            'p \\wedge q',
            '\\equiv',
            'q \\wedge p',
        )

        # Animações
        self.wait(1.5)
        self.play(
            FadeIn(titulo),
        )
        self.wait(2)

        self.play(
            Transform(titulo, tit_comutativa)
        )
        self.wait(1.5)

        # Comutativa OU
        self.play(
            Write(comutativa_ou[0])
        )
        self.wait(1)
        self.play(
            ReplacementTransform(comutativa_ou[0].copy(), comutativa_ou[2])
        )
        self.wait(1)
        self.play(
            Write(comutativa_ou[1]),
        )
        self.wait(1.5)

        # Comutativa E
        self.play(
            comutativa_ou.shift, 0.5 * UP,
            FadeIn(comutativa_e),
            comutativa_e.shift, 0.5 * DOWN
        )
        self.wait(5)
        
        self.play(
            FadeOut(titulo),
            FadeOut(comutativa_ou),
            FadeOut(comutativa_e),
        )


class Associativa(Scene):
    def construct(self):
        titulo = TexMobject('\\text{Associativa}')
        titulo.scale(1)
        titulo.to_edge(UP)
        titulo.set_color(papoula)

        associativa_ou = TexMobject(
            '(',            #0
            'p \\vee q',    #1
            ')',            #2
            '\\vee r',      #3

            '\\equiv',      #4

            'p \\vee',      #5
            '(',            #6
            'q \\vee r',    #7
            ')',            #8
        )

        associativa_e = TexMobject(
            '(p \\wedge q) \\wedge r \\equiv p \\wedge (q \\wedge r)'
        )

        # Animações
        self.play(
            FadeIn(titulo),
        )
        self.wait(1.5)

        # Associativa OU
        self.play(
            Write(associativa_ou[1]),
            Write(associativa_ou[3]),
        )
        self.wait(1)
        self.play(
            Write(associativa_ou[0]),
            Write(associativa_ou[2]),
        )
        self.wait(1.5)

        self.play(
            Write(associativa_ou[5]),
            Write(associativa_ou[7]),
        )
        self.wait(1)
        # Transforma parênteses
        self.play(
            ReplacementTransform(associativa_ou[0].copy(), associativa_ou[6]),
            ReplacementTransform(associativa_ou[2].copy(), associativa_ou[8]),
            Write(associativa_ou[4]),
        )
        self.wait(1.5)

        # Associativa E
        self.play(
            associativa_ou.shift, 0.5 * UP,
            FadeIn(associativa_e),
            associativa_e.shift, 0.5 * DOWN
        )
        self.wait(5)
        
        self.play(
            FadeOut(titulo),
            FadeOut(associativa_ou),
            FadeOut(associativa_e),
        )


class Distributiva(Scene):
    def construct(self):
        titulo = TexMobject('\\text{Distributiva}')
        titulo.scale(1)
        titulo.to_edge(UP)
        titulo.set_color(papoula)

        distributiva_ou = TexMobject(
            '(',            # 0
            'p',            # 1
            '\\vee',        # 2
            'q',            # 3
            ')',            # 4
            '\\wedge',      # 5
            'r',            # 6

            '\\equiv',      # 7

            '(',            # 8
            'p',            # 9
            '\\wedge',      # 10
            'r',            # 11
            ')',            # 12
            '\\vee',        # 13
            '(',            # 14
            'q',            # 15
            '\\wedge',      # 16
            'r',            # 17
            ')',            # 18
        )

        distributiva_e = TexMobject(
            '(p',           # 0
            '\\wedge',      # 1
            'q)',           # 2
            '\\vee',        # 3
            'r \\equiv (p', # 4
            '\\vee',        # 5
            'r)',           # 6
            '\\wedge',      # 7
            '(q',           # 8
            '\\vee',        # 9
            'r)'            # 10
        )

        # Animações
        self.play(
            FadeIn(titulo),
        )
        self.wait(1.5)

        # Distributiva OU dentro E fora
        self.play(
            Write(distributiva_ou[0:7]),
        )
        self.wait(1)
        self.play(
            Indicate(distributiva_ou[2]),
            Indicate(distributiva_ou[5]),
        )
        self.wait(1.5)

        # Exibindo (p and r)
        self.play(
            Write(distributiva_ou[8]),
            ReplacementTransform(distributiva_ou[1].copy(), distributiva_ou[9]),
        )
        self.wait(0.5)
        self.play(
            ReplacementTransform(distributiva_ou[5].copy(), distributiva_ou[10]),
        )      
        self.wait(0.5)
        self.play(
            ReplacementTransform(distributiva_ou[6].copy(), distributiva_ou[11]),
            Write(distributiva_ou[12]),
        )
        self.wait(1)
        # Exibe or
        self.play(
            ReplacementTransform(distributiva_ou[2].copy(), distributiva_ou[13]),
        )
        self.wait(1)

        # Exibe (q and r)
        self.play(
            Write(distributiva_ou[14]),
            ReplacementTransform(distributiva_ou[3].copy(), distributiva_ou[15]),
        )
        self.wait(0.5)
        self.play(
            ReplacementTransform(distributiva_ou[5].copy(), distributiva_ou[16]),
        )      
        self.wait(0.5)
        self.play(
            ReplacementTransform(distributiva_ou[6].copy(), distributiva_ou[17]),
            Write(distributiva_ou[18]),
        )
        self.wait(1.5)

        self.play(
            Write(distributiva_ou[7]),
        )
        self.wait(1.5)

        # Destaca operadores
        self.play(
            Indicate(distributiva_ou[2]),
            Indicate(distributiva_ou[13]),
        )
        self.wait(1)
        self.play(
            Indicate(distributiva_ou[5]),
            Indicate(distributiva_ou[10]),
            Indicate(distributiva_ou[16]),
        )
        self.wait(3)

        # Distributiva E dentro OU fora
        self.play(
            distributiva_ou.shift, 0.5 * UP,
            FadeIn(distributiva_e),
            distributiva_e.shift, 0.5 * DOWN,
        )
        self.wait(1.5)

        # Destaca operadores
        self.play(
            Indicate(distributiva_e[1]),
            Indicate(distributiva_e[7]),
        )
        self.wait(1)
        self.play(
            Indicate(distributiva_e[3]),
            Indicate(distributiva_e[5]),
            Indicate(distributiva_e[9]),
        )
        self.wait(5)

        self.play(
            FadeOut(titulo),
            FadeOut(distributiva_ou),
            FadeOut(distributiva_e),
        )


class Identidade(Scene):
    def construct(self):
        titulo = TexMobject('\\text{Identidade}')
        titulo.scale(1)
        titulo.to_edge(UP)
        titulo.set_color(papoula)

        identidade_ou = TexMobject(
            'p',
            '\\vee',
            '\\textbf{c}',
            '\\equiv',
            'p'
        )

        identidade_e = TexMobject(
            'p',
            '\\wedge',
            '\\textbf{t}',
            '\\equiv',
            'p',
        )

        # Animações
        self.play(
            FadeIn(titulo),
        )
        self.wait(1.5)

        self.play(
            Write(identidade_ou[0:3]),
        )
        self.wait(1.5)

        self.play(
            Write(identidade_ou[4])
        )
        self.wait(1)
        self.play(
            Write(identidade_ou[3])
        )
        self.wait(1.5)

        self.play(
            identidade_ou.shift, 0.5 * UP,
            FadeIn(identidade_e),
            identidade_e.shift, 0.5 * DOWN,
        )
        self.wait(5)

        self.play(
            FadeOut(titulo),
            FadeOut(identidade_ou),
            FadeOut(identidade_e),
        )


class Negacao(Scene):
    def construct(self):
        titulo = TexMobject('\\text{Negação}')
        titulo.scale(1)
        titulo.to_edge(UP)
        titulo.set_color(papoula)

        negacao_ou = TexMobject(
            'p',            # 0
            '\\vee',        # 1
            '\\neg',        # 2
            'p',            # 3
            '\\equiv',      # 4
            '\\textbf{t}'   # 5
        )

        negacao_e = TexMobject(
            'p',            # 0
            '\\wedge',      # 1
            '\\neg',        # 2
            'p',            # 3
            '\\equiv',      # 4
            '\\textbf{c}',  # 5
        )

        # Animações
        self.play(
            FadeIn(titulo),
        )
        self.wait(1.5)

        self.play(
            Write(negacao_ou[0]),
            Write(negacao_ou[1]),
        )
        self.wait(0.5)
        self.play(
            Write(negacao_ou[2]),
            ReplacementTransform(negacao_ou[0].copy(), negacao_ou[3]),
        )
        self.wait(1.5)

        self.play(
            Write(negacao_ou[5]),
        )
        self.wait(1)
        self.play(
            Write(negacao_ou[4]),
        )
        self.wait(1.5)

        self.play(
            negacao_ou.shift, 0.5 * UP,
            FadeIn(negacao_e),
            negacao_e.shift, 0.5 * DOWN,
        )
        self.wait(5)

        self.play(
            FadeOut(titulo),
            FadeOut(negacao_ou),
            FadeOut(negacao_e),
        )


class Dupla_negacao(Scene):
    def construct(self):
        titulo = TexMobject('\\text{Dupla negação}')
        titulo.scale(1)
        titulo.to_edge(UP)
        titulo.set_color(papoula)

        dupla_negacao = TexMobject(
            '\\neg',
            '(',
            '\\neg',
            'p',
            ')',
            '\\equiv',
            'p'
        )

        # Animações
        self.play(
            FadeIn(titulo),
        )
        self.wait(1.5)

        self.play(
            Write(dupla_negacao[0:5]),
        )
        self.wait(1.5)

        self.play(
            Indicate(dupla_negacao[0]),
            Indicate(dupla_negacao[2]),
        )
        self.wait(1)
        self.play(
            ReplacementTransform(dupla_negacao[3].copy(), dupla_negacao[6]),
            Write(dupla_negacao[5]),
        )

        self.wait(5)
        
        self.play(
            FadeOut(titulo),
            FadeOut(dupla_negacao),
        )


class Indepotente(Scene):
    def construct(self):
        titulo = TexMobject('\\text{Indepotente}')
        titulo.scale(1)
        titulo.to_edge(UP)
        titulo.set_color(papoula)

        indepotente_ou = TexMobject(
            'p',
            '\\vee',
            'p',
            '\\equiv',
            'p',
        )

        indepotente_e = TexMobject(
            'p',
            '\\wedge',
            'p',
            '\\equiv',
            'p',
        )

        # Animações
        self.play(
            FadeIn(titulo),
        )
        self.wait(1.5)

        self.play(
            Write(indepotente_ou[0:3]),
        )
        self.wait(1.5)

        ps = VGroup(indepotente_ou[0], indepotente_ou[2])
        self.play(
            ReplacementTransform(ps.copy(), indepotente_ou[4]),
            Write(indepotente_ou[3]),
        )
        self.wait(1.5)

        self.play(
            indepotente_ou.shift, 0.5 * UP,
            FadeIn(indepotente_e),
            indepotente_e.shift, 0.5 * DOWN,
        )
        self.wait(5)

        self.play(
            FadeOut(titulo),
            FadeOut(indepotente_ou),
            FadeOut(indepotente_e),
        )


class Universal(Scene):
    def construct(self):
        titulo = TexMobject('\\text{Universal}')
        titulo.scale(1)
        titulo.to_edge(UP)
        titulo.set_color(papoula)

        universal_ou = TexMobject(
            'p',
            '\\vee',
            '\\textbf{t}',
            '\\equiv',
            '\\textbf{t}',
        )

        universal_e = TexMobject(
            'p',
            '\\wedge',
            '\\textbf{c}',
            '\\equiv',
            '\\textbf{c}',
        )

        # Animações
        self.play(
            FadeIn(titulo),
        )
        self.wait(1.5)

        self.play(
            Write(universal_ou[0:3]),
        )
        self.wait(1.5)

        self.play(
            Write(universal_ou[4])
        )
        self.wait(1)
        self.play(
            Write(universal_ou[3])
        )
        self.wait(1.5)

        self.play(
            universal_ou.shift, 0.5 * UP,
            FadeIn(universal_e),
            universal_e.shift, 0.5 * DOWN,
        )
        self.wait(5)

        self.play(
            FadeOut(titulo),
            FadeOut(universal_ou),
            FadeOut(universal_e),
        )


class DeMorgan(Scene):
    def construct(self):
        titulo = TexMobject('\\text{DeMorgan}')
        titulo.scale(1)
        titulo.to_edge(UP)
        titulo.set_color(papoula)

        demorgan_ou = TexMobject(
            '\\neg',        # 0
            '(',            # 1
            'p',            # 2
            '\\vee',        # 3
            'q',            # 4
            ')',            # 5
            '\\equiv',      # 6
            '(',            # 7
            '\\neg',        # 8
            'p',            # 9
            '\\wedge',      # 10
            '\\neg',        # 11
            'q',            # 12
            ')',            # 13
        )

        demorgan_e = TexMobject(
            '\\neg (p \\wedge q) \\equiv (\\neg p \\vee \\neg q)'
        )

        # Animações
        self.play(
            FadeIn(titulo),
        )
        self.wait(1.5)

        self.play(
            Write(demorgan_ou[0:6]),
        )
        self.wait(1.5)

        negacoes = VGroup(demorgan_ou[8], demorgan_ou[11])
        self.play(
            ReplacementTransform(demorgan_ou[2].copy(), demorgan_ou[9]),
            ReplacementTransform(demorgan_ou[4].copy(), demorgan_ou[12]),
        )
        self.wait(1)
        self.play(
            ReplacementTransform(demorgan_ou[0].copy(), negacoes),
        )
        self.play(
            ReplacementTransform(demorgan_ou[3].copy(), demorgan_ou[10]),
            Write(demorgan_ou[7]),
            Write(demorgan_ou[13]),
        )
        self.wait(1)
        self.play(
            Write(demorgan_ou[6]),
        )
        self.wait(1.5)

        # Destacar operadores
        self.play(
            Indicate(demorgan_ou[3]),
            Indicate(demorgan_ou[10]),
        )
        self.wait(1.5)

        self.play(
            demorgan_ou.shift, 0.5 * UP,
            FadeIn(demorgan_e),
            demorgan_e.shift, 0.5 * DOWN,
        )
        self.wait(5)

        self.play(
            FadeOut(titulo),
            FadeOut(demorgan_ou),
            FadeOut(demorgan_e),
        )


class Absorcao(Scene):
    def construct(self):
        titulo = TexMobject('\\text{Absorção}')
        titulo.scale(1)
        titulo.to_edge(UP)
        titulo.set_color(papoula)

        absorcao_ou = TexMobject(
            'p',
            '\\vee',
            '(',
            'p',
            '\\wedge',
            'q',
            ')',
            '\\equiv',
            'p',
        )

        absorcao_e = TexMobject(
            'p',
            '\\wedge',
            '(p',
            '\\vee',
            'q)',
            '\\equiv p',
        )

        # Animações
        self.play(
            FadeIn(titulo),
        )
        self.wait(1.5)

        self.play(
            Write(absorcao_ou[0:7])
        )
        self.wait(1.5)

        self.play(
            Indicate(absorcao_ou[0]),
            Indicate(absorcao_ou[3]),
        )
        self.wait(1)
        self.play(
            Indicate(absorcao_ou[1]),
            Indicate(absorcao_ou[4]),
        )
        self.wait(1.5)

        ps = VGroup(absorcao_ou[0], absorcao_ou[3])
        self.play(
            ReplacementTransform(ps.copy(), absorcao_ou[8]),
        )
        self.wait(1)
        self.play(
            Write(absorcao_ou[7]),
        )
        self.wait(1.5)

        self.play(
            absorcao_ou.shift, 0.5 * UP,
            FadeIn(absorcao_e),
            absorcao_e.shift, 0.5 * DOWN,
        )
        self.wait(1.5)
        
        self.play(
            Indicate(absorcao_e[1]),
            Indicate(absorcao_e[3]),
        )
        self.wait(5)

        self.play(
            FadeOut(titulo),
            FadeOut(absorcao_ou),
            FadeOut(absorcao_e),
        )


class Negacao_t_c(Scene):
    def construct(self):
        titulo = TexMobject('\\text{Negação de \\textbf{t} e \\textbf{c}}')
        titulo.scale(1)
        titulo.to_edge(UP)
        titulo.set_color(papoula)

        negacao_t = TexMobject(
            '\\neg \\textbf{t}',
            '\\equiv',
            '\\textbf{c}',
        )

        negacao_c = TexMobject(
            '\\neg \\textbf{c}',
            '\\equiv',
            '\\textbf{t}',
        )

        # Animações
        self.play(
            FadeIn(titulo),
        )
        self.wait(1.5)

        self.play(
            Write(negacao_t[0]),
        )
        self.wait(1)
        self.play(
            Write(negacao_t[2]),
        )
        self.wait(1)
        self.play(
            Write(negacao_t[1]),
        )
        self.wait(1.5)

        self.play(
            negacao_t.shift, 0.5 * UP,
            FadeIn(negacao_c),
            negacao_c.shift, 0.5 * DOWN,
        )
        self.wait(5)

        self.play(
            FadeOut(titulo),
            FadeOut(negacao_t),
            FadeOut(negacao_c),
        )


# ############################################
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