import datetime
import subprocess
import webbrowser
import platform
import json
import os
import astrum

NOME = "ASTRUM"
ARQUIVO_MEMORIA = "memoria.json"

# =========================================================
# MEMÓRIA
# =========================================================

def carregar_memoria():

    if not os.path.exists(ARQUIVO_MEMORIA):
        return {
            "nome_usuario": None,
            "anotacoes": []
        }

    try:
        with open(ARQUIVO_MEMORIA, "r", encoding="utf-8") as arquivo:
            return json.load(arquivo)

    except:
        return {
            "nome_usuario": None,
            "anotacoes": []
        }


def salvar_memoria(memoria):

    with open(
        ARQUIVO_MEMORIA,
        "w",
        encoding="utf-8"
    ) as arquivo:

        json.dump(
            memoria,
            arquivo,
            indent=4,
            ensure_ascii=False
        )


memoria = carregar_memoria()

# =========================================================
# MEMÓRIA DO USUÁRIO
# =========================================================

def definir_nome(nome):

    memoria["nome_usuario"] = nome.strip()

    salvar_memoria(memoria)

    falar(
        f"Prazer em conhecê-lo, {memoria['nome_usuario']}."
    )


def mostrar_nome():

    nome = memoria.get("nome_usuario")

    if nome:

        falar(
            f"Seu nome é {nome}."
        )

    else:

        falar(
            "Ainda não sei seu nome."
        )


def adicionar_anotacao(texto):

    memoria["anotacoes"].append(texto)

    salvar_memoria(memoria)

    falar(
        "Anotação salva na memória."
    )


def mostrar_anotacoes():

    anotacoes = memoria.get("anotacoes", [])

    if not anotacoes:

        falar(
            "Minha memória está vazia."
        )

        return

    falar("Estas são suas anotações:")

    for i, anotacao in enumerate(
        anotacoes,
        start=1
    ):

        print(
            f"  {i}. {anotacao}"
        )

# =========================================================
# INFORMAÇÕES
# =========================================================

def obter_hora():

    agora = datetime.datetime.now()

    return agora.strftime("%H:%M:%S")


def obter_data():

    agora = datetime.datetime.now()

    return agora.strftime("%d/%m/%Y")


def informacoes_sistema():

    sistema = platform.system()
    versao = platform.version()
    arquitetura = platform.machine()

    falar(
        f"Sistema operacional: {sistema}\n"
        f"Versão: {versao}\n"
        f"Arquitetura: {arquitetura}"
    )


# =========================================================
# PROGRAMAS E SITES
# =========================================================

def abrir_google():

    falar("Abrindo o Google.")

    webbrowser.open(
        "https://www.google.com"
    )


def abrir_livro():

    falar("Abrindo seu livro.")

    webbrowser.open(
        "https://docs.google.com/document/d/1erTgP8Of_CkMAJC_nl9bhsfT6_PwwPvxq5Nf70lykz4/edit?tab=t.0#heading=h.qzx6ou1mmin9"
    )


def abrir_youtube():

    falar("Abrindo o YouTube.")

    webbrowser.open(
        "https://www.youtube.com"
    )


def abrir_calculadora():

    sistema = platform.system()

    if sistema == "Windows":

        subprocess.Popen("calc.exe")

        falar("Calculadora aberta.")

    else:

        falar(
            "Ainda não sei abrir a calculadora "
            "automaticamente neste sistema."
        )


# =========================================================
# CALCULADORA
# =========================================================

def calcular(expressao):

    try:

        resultado = eval(
            expressao,
            {"__builtins__": {}},
            {}
        )

        falar(f"O resultado é {resultado}.")

    except:

        falar(
            "Não consegui calcular essa expressão."
        )

# =========================================================
# RESPOSTA
# =========================================================

def falar(texto):

    #astrum.falar(texto)
    print(texto)

# =========================================================
# INTERPRETADOR
# =========================================================

def executar_comando(comando):

    comando = comando.lower().strip()


    # ---------------------------------------------
    # SAIR
    # ---------------------------------------------

    if comando in [
        "sair",
        "desligar",
        "encerrar",
        "fechar"
    ]:

        falar(
            "Encerrando sistemas. Até mais."
        )

        return False


    # ---------------------------------------------
    # HORA
    # ---------------------------------------------

    if "que horas" in comando:

        falar(
            f"São {obter_hora()}."
        )

        return True


    # ---------------------------------------------
    # DATA
    # ---------------------------------------------

    if "qual a data" in comando:

        falar(
            f"Hoje é {obter_data()}."
        )

        return True


    # ---------------------------------------------
    # GOOGLE
    # ---------------------------------------------

    if "abra o google" in comando:

        abrir_google()

        return True

    # ---------------------------------------------
    # LIVRO
    # ---------------------------------------------

    if "vou escrever" in comando:

        abrir_livro()

        return True
    # ---------------------------------------------
    # YOUTUBE
    # ---------------------------------------------

    if "abra o youtube" in comando:

        abrir_youtube()

        return True


    # ---------------------------------------------
    # CALCULADORA
    # ---------------------------------------------

    if "abra a calculadora" in comando:

        abrir_calculadora()

        return True


    # ---------------------------------------------
    # SISTEMA
    # ---------------------------------------------

    if (
        "informações do sistema" in comando
        or "informações do computador" in comando
    ):

        informacoes_sistema()

        return True


    # ---------------------------------------------
    # NOME
    # ---------------------------------------------

    if comando.startswith(
        "meu nome é "
    ):

        nome = comando.replace(
            "meu nome é ",
            "",
            1
        )

        definir_nome(nome)

        return True


    if (
        "qual é meu nome" in comando
        or "você sabe meu nome" in comando
    ):

        mostrar_nome()

        return True


    # ---------------------------------------------
    # ANOTAÇÃO
    # ---------------------------------------------

    if comando.startswith(
        "anote "
    ):

        texto = comando.replace(
            "anote ",
            "",
            1
        )

        adicionar_anotacao(texto)

        return True


    if (
        "minhas anotações" in comando
        or "mostre minhas anotações" in comando
    ):

        mostrar_anotacoes()

        return True


    # ---------------------------------------------
    # CALCULAR
    # ---------------------------------------------

    if comando.startswith(
        "calcule "
    ):

        expressao = comando.replace(
            "calcule ",
            "",
            1
        )

        calcular(expressao)

        return True


    # ---------------------------------------------
    # COMANDO DESCONHECIDO
    # ---------------------------------------------

    astrum.resposta_basica(comando)

    return True
