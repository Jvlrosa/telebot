import telebot

CHAVE_API = '7399173933:AAE9Ay_-Xe9ILOpZnb4NebmHv3aEoMogz0s'
bot = telebot.TeleBot(CHAVE_API)

# Armazena o estado dos pedidos dos usuários
user_order_state = {}

@bot.message_handler(commands=["start"])
def send_welcome(message):
    bot.reply_to(message, "Olá! Bem-vindo ao nosso serviço de pedidos! Por favor, digite seu nome:")

@bot.message_handler(func=lambda message: message.text and message.chat.id not in user_order_state)
def get_name(message):
    user_id = message.chat.id
    name = message.text
    user_order_state[user_id] = {'name': name, 'items': []}
    bot.reply_to(message, f"Obrigado, {name}! O que você deseja pedir?\nDigite /menu para ver as opções.")

@bot.message_handler(commands=["menu"])
def menu_options(mensagem):
    texto = """MENU DISPONÍVEL (CLIQUE EM UMA OPÇÃO):
/pizza - PIZZA
/hamburguer - HAMBÚRGUERES
/sucos - SUCOS
/finalizar - FINALIZAR PEDIDO"""
    bot.send_message(mensagem.chat.id, texto)

@bot.message_handler(commands=["pizza"])
def pizza_options(mensagem):
    texto = """SABORES DA CASA (CLIQUE EM UMA OPÇÃO):
/opcaopizza1 - PIZZA DE FRANGO
/opcaopizza2 - PIZZA DE CALABRESA
/opcaopizza3 - PIZZA DE LOMBO
/opcaopizza4 - PIZZA DE BRÓCOLIS
/opcaopizza5 - PIZZA DE PORTUGUESA
/opcaopizza6 - PIZZA DE CARNE SECA
/opcaopizza7 - PIZZA DE 4 QUEIJOS"""
    bot.send_message(mensagem.chat.id, texto)

@bot.message_handler(commands=[
    "opcaopizza1", "opcaopizza2", "opcaopizza3", "opcaopizza4", "opcaopizza5", "opcaopizza6", "opcaopizza7"
])
def opcoes_pizzas(mensagem):
    pizzas = {
        "opcaopizza1": "PIZZA DE FRANGO",
        "opcaopizza2": "PIZZA DE CALABRESA",
        "opcaopizza3": "PIZZA DE LOMBO",
        "opcaopizza4": "PIZZA DE BRÓCOLIS",
        "opcaopizza5": "PIZZA DE PORTUGUESA",
        "opcaopizza6": "PIZZA DE CARNE SECA",
        "opcaopizza7": "PIZZA DE 4 QUEIJOS"
    }
    opcao = mensagem.text.strip("/")
    pedido = pizzas[opcao]
    user_id = mensagem.chat.id
    user_order_state[user_id]['items'].append(pedido)
    bot.send_message(user_id, f"{pedido} adicionado ao seu carrinho. Deseja adicionar mais alguma coisa? /menu para opções ou /finalizar para completar o pedido.")

@bot.message_handler(commands=["hamburguer"])
def hamburguer_options(mensagem):
    texto = """HAMBÚRGUERES DISPONÍVEIS (CLIQUE EM UMA OPÇÃO):
/opcaohamb1 - HAMBÚRGUER SIMPLES
/opcaohamb2 - HAMBÚRGUER DUPLO
/opcaohamb3 - HAMBÚRGUER BACON
/opcaohamb4 - HAMBÚRGUER VEGETARIANO
/opcaohamb5 - HAMBÚRGUER CHEDDAR
/opcaohamb6 - HAMBÚRGUER FRANGO
/opcaohamb7 - HAMBÚRGUER CHURRASCO"""
    bot.send_message(mensagem.chat.id, texto)

@bot.message_handler(commands=[
    "opcaohamb1", "opcaohamb2", "opcaohamb3", "opcaohamb4", "opcaohamb5", "opcaohamb6", "opcaohamb7"
])
def opcoes_hamburguers(mensagem):
    hamburguers = {
        "opcaohamb1": "HAMBÚRGUER SIMPLES",
        "opcaohamb2": "HAMBÚRGUER DUPLO",
        "opcaohamb3": "HAMBÚRGUER BACON",
        "opcaohamb4": "HAMBÚRGUER VEGETARIANO",
        "opcaohamb5": "HAMBÚRGUER CHEDDAR",
        "opcaohamb6": "HAMBÚRGUER FRANGO",
        "opcaohamb7": "HAMBÚRGUER CHURRASCO"
    }
    opcao = mensagem.text.strip("/")
    pedido = hamburguers[opcao]
    user_id = mensagem.chat.id
    user_order_state[user_id]['items'].append(pedido)
    bot.send_message(user_id, f"{pedido} adicionado ao seu carrinho. Deseja adicionar mais alguma coisa? /menu para opções ou /finalizar para completar o pedido.")

@bot.message_handler(commands=["sucos"])
def sucos_options(mensagem):
    texto = """SUCOS DISPONÍVEIS (CLIQUE EM UMA OPÇÃO):
/opcaosuco1 - SUCO DE LARANJA
/opcaosuco2 - SUCO DE ABACAXI
/opcaosuco3 - SUCO DE MORANGO
/opcaosuco4 - SUCO DE MARACUJÁ
/opcaosuco5 - SUCO DE MANGA
/opcaosuco6 - SUCO DE LIMÃO"""
    bot.send_message(mensagem.chat.id, texto)

@bot.message_handler(commands=[
    "opcaosuco1", "opcaosuco2", "opcaosuco3", "opcaosuco4", "opcaosuco5", "opcaosuco6"
])
def opcoes_sucos(mensagem):
    sucos = {
        "opcaosuco1": "SUCO DE LARANJA",
        "opcaosuco2": "SUCO DE ABACAXI",
        "opcaosuco3": "SUCO DE MORANGO",
        "opcaosuco4": "SUCO DE MARACUJÁ",
        "opcaosuco5": "SUCO DE MANGA",
        "opcaosuco6": "SUCO DE LIMÃO"
    }
    opcao = mensagem.text.strip("/")
    pedido = sucos[opcao]
    user_id = mensagem.chat.id
    user_order_state[user_id]['items'].append(pedido)
    bot.send_message(user_id, f"{pedido} adicionado ao seu carrinho. Deseja adicionar mais alguma coisa? /menu para opções ou /finalizar para completar o pedido.")

@bot.message_handler(commands=["finalizar"])
def finalizar_pedido(mensagem):
    user_id = mensagem.chat.id
    if user_id in user_order_state:
        nome = user_order_state[user_id]['name']
        pedidos = user_order_state[user_id]['items']
        pedido_texto = f"{nome} - {', '.join(pedidos)}"
        salvar_pedido(pedido_texto)
        bot.send_message(user_id, f"Obrigado, {nome}! Seu pedido foi registrado: {pedido_texto}")
        del user_order_state[user_id]  # Limpa o estado do pedido após finalizar
    else:
        bot.send_message(user_id, "Você não tem nenhum pedido em aberto.")

def salvar_pedido(pedido_texto):
    with open("pedidos.txt", "a") as file:
        file.write(f"{pedido_texto}\n")

@bot.message_handler(commands=["opcao1"])
def opcao1(mensagem):
    texto = """O que você deseja comer (CLIQUE EM UMA OPÇÃO):
/pizza PIZZA
/hamburguer HAMBÚRGUERES
/sucos SUCOS"""
    bot.send_message(mensagem.chat.id, texto)

@bot.message_handler(commands=["opcao2"])
def opcao2(mensagem):
    bot.send_message(mensagem.chat.id, 'Para fazer uma reclamação, mande um e-mail para reclamacao@blablabla.com')

@bot.message_handler(commands=["opcao3"])
def opcao3(mensagem):
    bot.send_message(mensagem.chat.id, "Vlw cxr, tmj")

def verificar(mensagem):
    return True  # Aqui você pode adicionar qualquer lógica de verificação necessária

@bot.message_handler(func=verificar)
def responder(mensagem):
    texto = """CLIQUE em uma das opções:
/opcao1 Fazer pedido
/opcao2 Fazer reclamação
/opcao3 Manda oi"""
    bot.send_message(mensagem.chat.id, texto)

bot.polling()
