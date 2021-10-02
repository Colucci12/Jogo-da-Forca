from random import choice

tupla = ({'palavra': 'Abelha', 'dica': 'Te pica e morre'}, {'palavra': 'Porco', 'dica': 'Vive na lama'},
         {'palavra': 'Quadro', 'dica': 'Pendura na parede'}, {'palavra': 'Parede', 'dica': 'Feito de tijolo'},
         {'palavra': 'Adesivo', 'dica': 'Colamos em tudo'}, {'palavra': 'Luz', 'dica': 'Ilumina'},
         {'palavra': 'Musica', 'dica': 'Emoções sonoras'}, {'palavra': 'Celular', 'dica': 'Todo mundo tem'},
         {'palavra': 'Janela', 'dica': 'Abre pra luz entrar'}, {'palavra': 'Piscina', 'dica': 'Benção no calor'})

ndica = True
npalpite = True
tentativas = 0
progresso = []
palavra = []
dica = ''

#========== SETUP ==========
def setup():
    escolha = choice(tupla)
    global dica
    dica = escolha['dica']
    for x in escolha['palavra'].upper():
        palavra.append(x)
    global tentativas
    tentativas = len(palavra)
    for x in range(0, tentativas):
        progresso.append('_')
    opcoes()

#========== OPÇÕES ==========
def opcoes():
    if tentativas == 0 or npalpite == False:
        print('''
        =============
        Você perdeu !
        =============
        ''')
        return
    dados()
    escolha = input('''
    +=============================+
    |[1] - Para usar uma tentativa|
    |[2] - Para usar um palpite   |
    |[3] - Para usar uma dica     |
    ==============================+
    
    ''')
    if escolha == '1':
        tentativa()
    elif escolha == '2':
        palpite()
    elif escolha == '3':
        dicar()
    else:
        print('''
        ========================
        Digite um valor válido !
        ========================
        ''')
        opcoes()

#========== TENTATIVA ==========
def tentativa():
    letra = input('Insira APENAS uma letra !\n').strip().upper()
    if len(letra) == 1:
        for x in range(0, len(palavra)):
            if letra == palavra[x]:
                progresso[x] = letra
        global tentativas
        tentativas -= 1
        if progresso == palavra:
            print('''
                =======================
                Parabéns, você ganhou !
                =======================
                        ''')
            return
        opcoes()
    else:
        tentativa()

#========== PALPITE ==========
def palpite():
    word = input('Insira a PALAVRA que você acha que é !').strip().upper()
    if len(word) == len(palavra):
        for x in range(0, len(palavra)):
            progresso[x] = word[x]
        if progresso == palavra:
            print('''
            =======================
            Parabéns, você ganhou !
            =======================
            ''')
        else:
            global npalpite
            npalpite = False
            opcoes()
    else:
        npalpite = False
        opcoes()


#========== DICA ==========
def dicar():
    global ndica
    if ndica == True:
        ndica = False
        global dica
        print(f'''
    ================= DICA ===================
    {dica}
    ==========================================
    ''')
        ndica = False
        global tentativas
        tentativas -= 1
        opcoes()

    else:
        print('''
        =====================
        Você já usou a dica !
        =====================
        ''')
        opcoes()

#========== MOSTRAR DADOS ==========
def dados():
    print(f'Você ainda tem {tentativas} tentativa(s)!')
    if ndica == True:
        print('Você ainda pode pedir sua dica !')
    print('Você também pode dar um Palpite !')
    print(progresso)


resp = input('''
============================= REGRAS =============================
O número de tentativas é igual a quantidade de letras na palavra !
O jogo te dará apenas uma dica por palavra !
Você perde uma tentativa quando pede a dica !
Você pode dar um palpite ! Se errar o palpite perde !
==================================================================

Pronto para começar ? (S/N)
''').upper()

if resp == 'S':
    setup()