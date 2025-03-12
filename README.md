# Marbles-On-Stream-Bot

Este projeto é um bot para o chat da Twitch que envia mensagens automaticamente para múltiplos canais. Ele se conecta ao chat de cada canal, envia mensagens programadas e se desconecta quando necessário.

## **Pré-requisitos**

Antes de rodar o script, você precisa obter algumas credenciais da Twitch:

1. **Client ID**: Usado para autenticar a aplicação com a Twitch.
2. **Client Secret**: Usado para gerar o Access Token.
3. **Access Token**: Usado para autenticar o bot no chat da Twitch.

Aqui está o passo a passo para obter cada uma dessas credenciais.

---

## **Como Obter o Client ID, Client Secret e Access Token**

### 1. **Criar uma Conta na Twitch**

Se você ainda não tem uma conta na Twitch, crie uma em [https://www.twitch.tv/](https://www.twitch.tv/).

### 2. **Acessar o Console de Desenvolvedor da Twitch**

- Vá para [Twitch Developer Console](https://dev.twitch.tv/console/apps).
- Faça login com sua conta da Twitch.

### 3. **Registrar uma Nova Aplicação**

- No painel do desenvolvedor, clique em **"Register Your Application"**.
- Preencha os seguintes campos:
  - **Name**: Escolha um nome para a sua aplicação (exemplo: `TwitchBot`).
  - **OAuth Redirect URL**: Use `http://localhost`.
  - **Category**: Selecione uma categoria (exemplo: **Chat Bot**).
- Clique em **Create**.

### 4. **Obter o Client ID e o Client Secret**

- Após criar a aplicação, na página da aplicação, você verá o **Client ID** e o **Client Secret**.
- Copie esses valores. O **Client Secret** será mostrado apenas uma vez, então guarde-o com segurança.

### 5. **Obter o Access Token via Twitch Token Generator**

- Acesse o site [Twitch Token Generator](https://twitchtokengenerator.com/).
- **Selecione a opção** `Twitch Chat Bot`.
- **Faça login** com sua conta da Twitch.
- **Escolha os escopos** necessários para o seu bot:
  - Selecione as permissões **chat:read**, **chat:edit** e **user:write:chat**.
  - **`chat:read`**: Permite que o bot leia o chat.
  - **`chat:edit`**: Permite que o bot envie mensagens no chat.
  - **`user:write:chat`**: Permite que o bot envie mensagens em nome do usuário.
- O site irá gerar o **Access Token** automaticamente após você autorizar o acesso.
- Copie o **Access Token** gerado. Ele será utilizado para autenticar o bot no chat da Twitch.

Agora você tem todas as credenciais necessárias para rodar o script!

---

## **Instalação**

### 1. **Instalar Dependências**

Este script utiliza a biblioteca `requests` para interagir com a API da Twitch. Para instalar as dependências, execute:

```pip install -r requirements.txt```

---

## **Configuração**

Abra o arquivo `twitch_chat_bot.py` e insira as credenciais diretamente no script:

```
client_id = '<seu_client_id>'
client_secret = '<seu_client_secret>'
access_token = '<seu_access_token>'
```

Substitua os valores com as credenciais correspondentes que você obteve no passo anterior.

---

## **Uso**

1. **Configure o Script**
    
    Abra o arquivo `twitch_chat_bot.py` e edite os parâmetros se necessário, como o nome de usuário e canais.

2. **Execute o Script**
    
    Execute o script no terminal:
    
```
python twitch_chat_bot.py
```
    
O bot se conectará aos canais da Twitch e começará a enviar mensagens no intervalo configurado.

---

## **Estrutura do Projeto**

O repositório possui a seguinte estrutura:

```
twitch_chat_bot/
│
├── twitch_chat_bot.py        # Script principal do bot
├── requirements.txt          # Arquivo de dependências
└── README.md                 # Este arquivo
```

---

## **Considerações Finais**

- **Segurança**: Nunca compartilhe seu `client_secret` ou `access_token` publicamente. Se você acredita que suas credenciais foram comprometidas, gere novas credenciais no [Twitch Developer Console](https://dev.twitch.tv/console/apps).
- **Limitações de Rate Limit**: A Twitch pode impor limites de taxa em sua API. Certifique-se de não violar esses limites ao enviar muitas mensagens em um curto espaço de tempo.

Se você tiver dúvidas ou sugestões de melhorias, sinta-se à vontade para abrir um **Issue** ou enviar um **Pull Request**!
