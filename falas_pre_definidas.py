import random

perg = {
    1: ["oi", 'ola', 'opa'],
    2: ["como tu ta", 'como você tá', 'tudo bem'],
    3: ['quem é você', 'quem e voce', 'quem e tu'],
    4: ['qual seu nome', 'seu nome'],
    5: ["astrum", 'ia']
}

frases = {
            1: ["Oi 😄", "Olá!", "Eii~"],
            2: ["Estou bem sim 😄 E você?", "Tudo ótimo!", "Indo bem!"],
            3: [
                "Sou sua IA 😄",
                "Sou uma assistente que está aprendendo.",
                "Sou sua companheira digital."
            ],
            4: ["Astrum", "É Astrum"],
            5: ["Sim?", "Me chamou?", "O que você deseja?"]
        }

def get_phrase(text):
        text = text.lower()

        for key in perg.items():
            print(key[1])
            if key[1] in text:
                print(2)
                return random.choice(frases[key])

        return ""
