from Exercicio_02_noncedef import encontrar_nonce

def main(): # Função principal
    textos = [
        "Esse é fácil", "Esse é fácil", "Esse é fácil", "Texto maior muda o tempo?", 
        "Texto maior muda o tempo?", "Texto maior muda o tempo?", 
        "É possível calcular esse?", "É possível calcular esse?", "É possível calcular esse?"
    ]
    bits_para_zero_lista = [8, 10, 15, 8, 10, 15, 18, 19, 20]

    resultados = []

    for texto, bits in zip(textos, bits_para_zero_lista):
        dados = texto.encode('utf-8')
        nonce_encontrado, tempo_decorrido = encontrar_nonce(dados, bits)
        resultados.append((texto, bits, nonce_encontrado, tempo_decorrido))

    # Exibição da tabela de resultados
    print(f"{'Texto':<30} {'Bits em zero':<12} {'Nonce':<10} {'Tempo (s)':<10}")
    for resultado in resultados:
        print(f"{resultado[0]:<30} {resultado[1]:<12} {resultado[2]:<10} {resultado[3]:<10.4f}")

if __name__ == "__main__":
    main()
