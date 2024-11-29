import random

def main(): #Ler o arquivo
    
    arquivo_palavras = r"exercicio03.txt"  #Nome do arquivo
    palavras = ler_palavras(arquivo_palavras)
    
    if not palavras:
        print("Nenhuma palavra válida encontrada no arquivo.")
        return
        
    palavra_sorteada = sortear_palavra(palavras) # Sorteio da palavra
    jogar(palavra_sorteada) #Iniciar

def ler_palavras(arquivo): #Ler o conteúdo do arquivo e retorna
    with open(arquivo, 'r') as file:
        palavras = [linha.strip() for linha in file if 5 <= len(linha.strip()) <= 8] #Retornar uma lista com palavras de 5 a 8 letras
    return palavras

def sortear_palavra(palavras): #Função para o sorteio das palavras
    palavra_sorteada = random.choice(palavras)
    print(f"A palavra sorteada tem {len(palavra_sorteada)} letras.")
    return palavra_sorteada

def fornecer_feedback(palavra_sorteada, tentativa): #Resultado das tentativas do jogador
    resultado = []
    for i, letra in enumerate(tentativa):
        if letra == palavra_sorteada[i]:
            resultado.append(f"\033[92m{letra}\033[0m")  # Verde
        elif letra in palavra_sorteada:
            resultado.append(f"\033[93m{letra}\033[0m")  # Amarelo
        else:
            resultado.append(f"\033[90m{letra}\033[0m")  # Cinza
    return " ".join(resultado)

def jogar(palavra_sorteada): 
    tentativas_restantes = 6
    while tentativas_restantes > 0:
        tentativa = input(f"Tentativa ({tentativas_restantes} restantes): ").strip().lower()
        
        if len(tentativa) != len(palavra_sorteada):
            print(f"A palavra deve ter {len(palavra_sorteada)} letras.")
            continue
        
        if tentativa == palavra_sorteada:
            print(f"Parabéns! Você acertou a palavra '{palavra_sorteada}' em {6 - tentativas_restantes + 1} tentativas.")
            return
               
        print(f"Resultado: {fornecer_feedback(palavra_sorteada, tentativa)}")
        
        tentativas_restantes -= 1
    
    print(f"Você perdeu! A palavra era '{palavra_sorteada}'.")

if __name__ == "__main__":
    main()