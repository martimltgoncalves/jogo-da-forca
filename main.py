import random  


def escolher_palavra():
    """Escolhe e retorna uma palavra secreta de uma lista"""
    palavras = ["python", "programacao", "jogo", "forca", "desafio"]
    return random.choice(palavras)

def mostrar_estado(letras_descobertas, erros, max_erros):
    """Mostra o estado atual do jogo"""
    print("Palavra:", " ".join(letras_descobertas))
    print("Erros: ", ", ".join(erros)) 
    print(f"Tentativas restantes: {max_erros - len(erros)}")

def verificar_vitoria(letras_descobertas):
    """Retorna True se o jogador descobriu todas as letras"""
    return "_" not in letras_descobertas

def jogar():
    """Executa o loop principal do jogo da forca"""
    palavra_secreta = escolher_palavra()
    letras_descobertas = ["_"] * len(palavra_secreta)
    erros = []
    max_erros = 6
    
    print("Bem-vindo ao Jogo da Forca!")
    print("Adivinhe a palavra secreta:") 

    while True:
        mostrar_estado(letras_descobertas, erros, max_erros)

        letra = input("Digite uma letra: ").lower()
        if letra in letras_descobertas or letra in erros:
            print("Você já tentou essa letra. Tente outra.")
            continue
        if letra in palavra_secreta:
            print(f"Boa! A letra '{letra}' está na palavra.")
            for i, char in enumerate(palavra_secreta):
                if char == letra:
                    letras_descobertas[i] = letra
        else:
            print(f"Ops! A letra '{letra}' não está na palavra.")
            erros.append(letra)

        if verificar_vitoria(letras_descobertas):
            print("Parabéns! Você acertou a palavra!")
            break

        if len(erros) >= max_erros:
            print("Você perdeu! A palavra secreta era:", palavra_secreta)
            break

if __name__ == "__main__":
    jogar()