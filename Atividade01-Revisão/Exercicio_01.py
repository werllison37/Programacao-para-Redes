import json
import os
from tabulate import tabulate

def main():
    try:
        ip = input("Digite o endereço IP: ")
        ip = validar_ip(ip)
        
        mascara_inicial = int(input("Digite a máscara de rede inicial (0-32): "))
        mascara_inicial = validar_mascara(mascara_inicial)
        
        mascara_final = int(input("Digite a máscara de rede final (0-32): "))
        mascara_final = validar_mascara(mascara_final)
        
        if mascara_inicial > mascara_final:
            raise ValueError("A máscara de rede inicial deve ser menor ou igual à final.")
        
        resultado = calcular_intervalo_subredes(ip, mascara_inicial, mascara_final)
        
        nome_arquivo = input("Digite o nome do arquivo JSON para salvar (sem extensão): ") + ".json"
        salvar_resultado_json(resultado, nome_arquivo)
        print(f"Resultados salvos com sucesso em {nome_arquivo}.")
        
        # Exibe a tabela formatada
        exibir_tabela(resultado)
    
    except ValueError as e:
        print(f"Erro de valor: {e}")
    except FileExistsError as e:
        print(e)
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")

def validar_ip(ip):
    """Valida o endereço IP fornecido pelo usuário"""
    partes = ip.split(".")
    if len(partes) != 4:
        raise ValueError("Endereço IP inválido.")
    for parte in partes:
        if not parte.isdigit() or not (0 <= int(parte) <= 255):
            raise ValueError("Endereço IP inválido.")
    return ip

def validar_mascara(mascara): #Verificação e validação da máscara de rede
    if not (0 <= mascara <= 32):
        raise ValueError("Máscara de rede inválida. Deve estar entre 0 e 32.")
    return mascara

def ip_para_binario(ip): #Converter IP em binário
    partes = map(int, ip.split("."))
    return ''.join(f"{parte:08b}" for parte in partes)

def binario_para_ip(binario): #Retornar o binário para endereço IP
    partes = [str(int(binario[i:i+8], 2)) for i in range(0, 32, 8)]
    return ".".join(partes)

def calcular_subrede(ip, mascara): #Calcular informações da sub-rede
    ip_bin = ip_para_binario(ip)
    net_bin = ip_bin[:mascara] + "0" * (32 - mascara)
    broadcast_bin = ip_bin[:mascara] + "1" * (32 - mascara)
    
    rede = binario_para_ip(net_bin)
    broadcast = binario_para_ip(broadcast_bin)
    
    primeiro_host = binario_para_ip(net_bin[:-1] + "1")
    ultimo_host = binario_para_ip(broadcast_bin[:-1] + "0")
    
    num_hosts_validos = (2 ** (32 - mascara)) - 2
    
    mascara_bin = "1" * mascara + "0" * (32 - mascara)
    mascara_decimal = binario_para_ip(mascara_bin)
    
    return {
        "CIDR": f"/{mascara}",
        "Endereço de Rede": rede,
        "Primeiro Host": primeiro_host,
        "Último Host": ultimo_host,
        "Endereço de Broadcast": broadcast,
        "Máscara de Sub-Rede": mascara_decimal,
        "Máscara de Sub-Rede (Binário)": mascara_bin,
        "Hosts Válidos": num_hosts_validos
    }

def salvar_resultado_json(resultado, nome_arquivo): #Salvar resultado sem sobrescrever arquivos existentes
    if os.path.exists(nome_arquivo):
        raise FileExistsError(f"O arquivo '{nome_arquivo}' já existe.")
    
    with open(nome_arquivo, 'w', encoding='utf-8') as f:
        json.dump(resultado, f, indent=4, ensure_ascii=False)

def calcular_intervalo_subredes(ip, mascara_inicial, mascara_final): #Calcular sub-redes para as máscaras no intervalo especificado
    resultado = []
    for mascara in range(mascara_inicial, mascara_final + 1):
        resultado.append(calcular_subrede(ip, mascara))
    return resultado

def exibir_tabela(resultados): #Resultados formatados utilizando tabulate
    tabela = []
    for info in resultados:
        tabela.append([
            info["CIDR"],
            info["Endereço de Rede"],
            info["Primeiro Host"],
            info["Último Host"],
            info["Endereço de Broadcast"],
            info["Máscara de Sub-Rede"],
            info["Máscara de Sub-Rede (Binário)"],
            info["Hosts Válidos"]
        ])
    
    colunas = ["CIDR", "Endereço de Rede", "Primeiro Host", "Último Host", "Endereço de Broadcast", 
               "Máscara de Sub-Rede", "Máscara de Sub-Rede (Binário)", "Hosts Válidos"]
    
    print(tabulate(tabela, headers=colunas, tablefmt="grid"))

if __name__ == "__main__":
    main()