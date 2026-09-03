import json
import os
import random
import comandos
import falas_pre_definidas
import tkinter as tk


# =========================================================
# CONFIGURAÇÕES
# =========================================================

NOME = "ASTRUM"
ARQUIVO_MEMORIA = "memoria.json"
janela = tk.Tk()
janela.title("Meu Primeiro App")
janela.geometry("500x500")

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
# RESPOSTA
# =========================================================

def falar(texto):

    #print(f"\n{NOME}: {texto}")
    label = tk.Label(janela, text=f"\n{NOME}: {texto}")
    label.pack(pady=1)



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
# RESPOSTAS BÁSICAS
# =========================================================

def resposta_basica(comando):

    respostas = [

        "Interessante.",
        "Entendido.",
        "Certo.",
        "Compreendido.",
        "Estou analisando isso."

    ]
    if falas_pre_definidas.get_phrase(comando):
        falar(falas_pre_definidas.get_phrase(comando))
        return
    falar(
        random.choice(respostas)
    )


    falar(
        "Ainda não possuo um modelo de IA conectado "
        "para responder perguntas complexas."
    )

# =========================================================
# RESPOSTAS COMPLEXAS
# =========================================================





# =========================================================
# INICIALIZAÇÃO
# =========================================================

def iniciar():

    tit1 = tk.Label(janela, text="="*55+"\n                    A S T R U M\n"+"="*55)
    tit1.pack(pady=5)
    #print("=" * 55)
    #print("                    A S T R U M")
    #print("=" * 55)

    falar(
        "Sistemas inicializados."
    )

    if memoria.get("nome_usuario"):

        falar(
            f"Bem-vindo novamente, "
            f"{memoria['nome_usuario']}."
        )

    else:

        falar(
            "Olá. Ainda não sei seu nome."
        )

    falar(
        "Como posso ajudá-lo?"
    )


    funcionando = True


    while funcionando:

        try:

            def capturar_texto():
    # Obtém o conteúdo atual do Entry
                comando = entrada.get()
                print(comando)

                funcionando = comandos.executar_comando(comando)
                
            entrada = tk.Entry(janela)
            entrada.pack(pady=10)

            # 3. Criar um botão para acionar a função
            botao = tk.Button(janela, text="Enviar", command=capturar_texto)
            botao.pack(pady=5)
            
            janela.mainloop()
            
            #if not comando.strip():

            #    continue

            #funcionando = comandos.executar_comando(
            #    comando
            #)

        except KeyboardInterrupt:
            print(2)

            falar(
                "Interrupção detectada. "
                "Encerrando sistemas."
            )

            break

        except Exception as erro:

            falar(
                f"Ocorreu um erro: {erro}"
            )




# =========================================================
# EXECUÇÃO
# =========================================================

if __name__ == "__main__":

    iniciar()
    janela.mainloop()
