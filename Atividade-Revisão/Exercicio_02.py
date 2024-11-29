import hashlib
import time

def encontrar_nonce(dados_para_hash: bytes, bits_para_zero: int):
    nonce = 0
    tempo_inicio = time.time()
    while True: # Combine o nonce com os dados de entrada      
        bytes_nonce = nonce.to_bytes(4, byteorder='little')
        combinado = bytes_nonce + dados_para_hash
              
        resultado_hash = hashlib.sha256(combinado).digest() # Calcular o hash SHA256
               
        bits_hash = ''.join(f'{byte:08b}' for byte in resultado_hash) # Converter o hash para uma sequência de bits       
        
        if bits_hash.startswith('0' * bits_para_zero): # Verificar se os primeiros bits são zeros
            tempo_fim = time.time()
            tempo_decorrido = tempo_fim - tempo_inicio
            return nonce, tempo_decorrido      
        
        nonce += 1 # Incrementar o nonce

# Programa principal para preencher a tabela
textos = [
    "Esse é fácil", "Esse é fácil", "Esse é fácil", "Texto maior muda o tempo?", 
    "Texto maior muda o tempo?", "Texto maior muda o tempo?", 
    "É possível calcular esse?", "É possível calcular esse?", "É possível calcular esse?"
]
bits_para_zero_lista = [8, 10, 15, 8, 10, 15, 8, 15, 20]

resultados = []

for texto, bits in zip(textos, bits_para_zero_lista):
    dados = texto.encode('utf-8')
    nonce_encontrado, tempo_decorrido = encontrar_nonce(dados, bits)
    resultados.append((texto, bits, nonce_encontrado, tempo_decorrido))

# Exibir a tabela de resultados
print(f"{'Texto':<30} {'Bits em zero':<12} {'Nonce':<10} {'Tempo (s)':<10}")
for resultado in resultados:
    print(f"{resultado[0]:<30} {resultado[1]:<12} {resultado[2]:<10} {resultado[3]:<10.4f}")
