import hashlib
import time

def encontrar_nonce(dados_para_hash: bytes, bits_para_zero: int):
    nonce = 0
    tempo_inicio = time.time()
    while True:
        # Combinar o nonce com os dados de entrada      
        bytes_nonce = nonce.to_bytes(4, byteorder='little')
        combinado = bytes_nonce + dados_para_hash
              
        resultado_hash = hashlib.sha256(combinado).digest()  # Calcular o hash SHA256
               
        bits_hash = ''.join(f'{byte:08b}' for byte in resultado_hash)  # Converter o hash para uma sequência de bits       
        
        if bits_hash.startswith('0' * bits_para_zero):  # Verifica se os primeiros bits são zeros
            tempo_fim = time.time()
            tempo_decorrido = tempo_fim - tempo_inicio
            return nonce, tempo_decorrido      
        
        nonce += 1  # Incrementação do nonce
