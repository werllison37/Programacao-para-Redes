import os
import sys

def main(): #Verificação de argumentos
    if len(sys.argv) != 4:
        print("Uso: python programa.py <arquivo_origem> <palavra_passe> <arquivo_destino>")
        return

    #Parâmetros da linha de comando
    arquivo_origem = sys.argv[1]
    palavra_passe = sys.argv[2]
    arquivo_destino = sys.argv[3]
    
    xor_encrypt(arquivo_origem, palavra_passe, arquivo_destino) #Chamar a função de criptografia

def xor_encrypt(input_file, password, output_file):
    """
    Função para criptografar os bytes de um arquivo usando a operação XOR com base em uma palavra-passe.

    :param input_file: Nome do arquivo de origem.
    :param password: Palavra-passe para a operação XOR.
    :param output_file: Nome do arquivo de destino.
    """
    
    if not os.path.isfile(input_file): # Verifica a existência do arquivo de origem
        print(f"Erro: O arquivo de origem '{input_file}' não existe.")
        return
    
    if os.path.isfile(output_file): #Verifica se o arquivo de destino já existe para evitar sobrescrita
        print(f"Erro: O arquivo de destino '{output_file}' já existe. Escolha outro nome para evitar sobrescrita.")
        return
 
    if not password: # Verifica se a palavra-passe não está vazia
        print("Erro: A palavra-passe não pode estar vazia.")
        return

    try:
        with open(input_file, 'rb') as f_in: #Abrir o arquivo de origem para leitura em modo binário
            data = f_in.read()
           
        encrypted_data = bytearray() #Prepara a lista para armazenar os bytes criptografados
        
        password_length = len(password) #Criptografar os bytes usando XOR e a palavra-passe
        for i, byte in enumerate(data):      
            encrypted_byte = byte ^ ord(password[i % password_length]) #Realiza a operação XOR entre o byte atual e o byte correspondente da palavra-passe
            encrypted_data.append(encrypted_byte) #Adiciona o byte criptografado à lista
             
        with open(output_file, 'wb') as f_out: #Salva os dados criptografados no arquivo de destino
            f_out.write(encrypted_data)

        print(f"Criptografia concluída com sucesso! O arquivo foi salvo como '{output_file}'.")
    
    except Exception as e:
        print(f"Erro durante a criptografia: {e}")

if __name__ == "__main__":
    main()
