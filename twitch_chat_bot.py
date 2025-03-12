import requests
import socket
import time
import random
import threading

# Informações de autenticação
client_id = ''  # Seu Client ID
client_secret = ''  # Seu Client Secret
category_id = '509511'  # ID da categoria (Twitch ID para jogos/categorias)
nickname = ''  # Seu nome de usuário
token = ''  # Seu token de autenticação para IRC
server = 'irc.chat.twitch.tv'
port = 6667
tempominimo = 120
tempomaximo = 150

# Função para obter o Access Token usando Client ID e Client Secret
def get_access_token(client_id, client_secret):
    url = 'https://id.twitch.tv/oauth2/token'
    params = {
        'client_id': client_id,
        'client_secret': client_secret,
        'grant_type': 'client_credentials'
    }
    response = requests.post(url, params=params)
    if response.status_code == 200:
        access_token = response.json()['access_token']
        print("✅ Access Token obtido com sucesso.")
        return access_token
    else:
        print(f"❌ Erro ao obter Access Token: {response.status_code}")
        return None

# Função para pegar os streamers da categoria
def get_streamers_from_category(client_id, access_token, category_id):
    url = f'https://api.twitch.tv/helix/streams?game_id={category_id}'
    headers = {
        'Client-ID': client_id,
        'Authorization': f'Bearer {access_token}'
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        streams = response.json()['data']
        print(f"✅ Encontrados {len(streams)} streamers na categoria {category_id}.")
        return [stream['user_name'] for stream in streams]
    else:
        print(f"❌ Erro ao pegar streamers: {response.status_code}")
        return []

# Função para enviar a mensagem !play
def send_message(channel, mensagem, irc):
    irc.send(f"PRIVMSG {channel} :{mensagem}\n".encode('utf-8'))

# Função para conectar ao chat da Twitch e enviar mensagens
def connect_and_send():
    print("🔄 Obtendo o Access Token...")
    access_token = get_access_token(client_id, client_secret)
    if not access_token:
        return  # Se não obteve o token, interrompe o script

    print("🔄 Obtendo os streamers da categoria...")
    streamers = get_streamers_from_category(client_id, access_token, category_id)
    
    if not streamers:
        print("❌ Nenhum streamer encontrado na categoria.")
        return

    # Função para enviar a mensagem !play para um único canal e manter o envio em loop
    def send_for_channel(channel):
        print(f"🎮 Conectando ao canal {channel}...")
        
        # Loop infinito para enviar mensagens de forma repetida com intervalo
        while True:
            irc = socket.socket()
            irc.connect((server, port))
            irc.send(f"PASS {token}\n".encode('utf-8'))
            irc.send(f"NICK {nickname}\n".encode('utf-8'))
            irc.send(f"JOIN {channel}\n".encode('utf-8'))
            
            send_message(channel, "!play", irc)
            print(f"✅ Mensagem '!play' enviada para {channel}")                     
            
            # Desconecta após enviar a mensagem
            irc.send("PART {}\n".encode('utf-8'))
            irc.close()
            print(f"❌ Desconectado de {channel}. Aguardando o próximo intervalo...")

    # Função para enviar a mensagem para outros canais a cada 5 segundos
    def send_for_other_channel(channel):
        irc = socket.socket()
        irc.connect((server, port))
        irc.send(f"PASS {token}\n".encode('utf-8'))
        irc.send(f"NICK {nickname}\n".encode('utf-8'))
        irc.send(f"JOIN {channel}\n".encode('utf-8'))
        
        send_message(channel, "!play", irc)
        print(f"✅ Mensagem '!play' enviada para {channel}")
        
        # Desconectar após enviar a mensagem
        irc.send("PART {}\n".encode('utf-8'))
        irc.close()
        print(f"❌ Desconectado de {channel}. Aguardando 5 segundos para o próximo canal...")

        # Intervalo de 5 segundos antes de ir para o próximo canal
        time.sleep(5)

    # Enviar mensagens para todos os streamers
    for i, streamer in enumerate(streamers):
        # Ignora o streamer 'gripsed'
        if streamer.lower() == 'gripsed':
            print(f"❌ Ignorando o streamer {streamer}...")
            continue  # Pula para o próximo streamer
        
        channel = f"#{streamer}"

        # Criar uma thread para o primeiro canal que ficará em loop
        if i == 0:  # Para o primeiro canal, mantemos o envio em loop
            threading.Thread(target=send_for_channel, args=(channel,)).start()
        else:
            threading.Thread(target=send_for_other_channel, args=(channel,)).start()
        
        print(f"🕐 Enviado para {channel}, aguardando 7 segundos para o próximo...")

        # Intervalo de 7 segundos antes de ir para o próximo canal
        time.sleep(7)
    
    print("✅ Script em execução. Continuando o loop...")

# Adiciona um loop para continuar rodando o script indefinidamente
while True:
    connect_and_send()
    print("🔄 Reiniciando o processo...")
    time.sleep(random.randint(tempominimo, tempomaximo))  # Intervalo para a próxima mensagem  # Espera 60 segundos antes de reiniciar, você pode ajustar o tempo conforme necessário
