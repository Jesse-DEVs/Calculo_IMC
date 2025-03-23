import telebot

chave_api = "8129721165:AAFnlwfcuv4Cl6rm4jBpbHl8gsddE-ivttE"
bot = telebot.TeleBot(chave_api)

produto_camisa = {
    'nome': 'Camisa',
    'valor': '1$'
}

produto_caneca = {
    'nome': 'Caneca',
    'valor': '2$'}

produto_bolsa = {
    'nome': 'bolsa',
    'valor': '3$'
}

Email = 'Teste.bot@blablabla.com'

@bot.message_handler(commands=['opcao1'])
def opcao1(mensagem):
    pass
    pedido = f"""
    Qual sera seu pedido ??
     /camisa Camisa {produto_camisa["valor"]}
     /caneca Caneca {produto_caneca["valor"]}
     /bolsa Bolsa {produto_bolsa["valor"]}
    Responder qualquer outra coisa nao vai funcionar, Clique em uma das opcao
    """
    bot.reply_to(mensagem, pedido)
    
@bot.message_handler(commands=['camisa'])
def camisa(mensagem):
    pass
    camisa = """
    Qual tamanho da Camisa ?
     /tamanho1 Tamanho P
     /tamanho2 Tamanho M
     /tamanho3 Tamanho G
    Responder qualquer outra coisa nao vai funcionar, Clique em uma das opcao
    """
    bot.reply_to(mensagem, camisa)
    
@bot.message_handler(commands=['tamanho1', 'tamanho2','tamanho3'])
def tamanho1(mensagem):    
    pass
    Pagamento = f"""
    {produto_camisa['nome']} R$: {produto_camisa['valor']}
    Só aceitamos pagamentos no PIX: 123234589023
    Assim que o pagamento for confirmado ja vamos Preparar seu pedido!!
    """
    bot.send_message(mensagem.chat.id, Pagamento)
    
@bot.message_handler(commands=['caneca'])
def caneca(mensagem):
    pass
    caneca = f"""
    {produto_caneca['nome']} R$: {produto_caneca['valor']} 
    Só aceitamos pagamentos no PIX: 123234589023
    Assim que o pagamento for confirmado ja vamos Preparar seu pedido!!
    """
    bot.send_message(mensagem.chat.id, caneca)
      
@bot.message_handler(commands=['bolsa'])
def bolsa(mensagem):
    pass
    bolsa = f"""
    {produto_bolsa['nome']} R$: {produto_bolsa['valor']}  
    Só aceitamos pagamentos no PIX: 123234589023
    Assim que o pagamento for confirmado ja vamos Preparar seu pedido!!
    """
    bot.reply_to(mensagem, bolsa)
    
@bot.message_handler(commands=['opcao2'])
def opcao2(mensagem):
    pass
    reclamar = """
    Qual sua reclamação ?
     /atendimento Reclamação sobre o atendimento
     /produto Reclamação sobre os produtos
     /entrega Reclamação sobre a entrega
    Responder qualquer outra coisa nao vai funcionar, Clique em uma das opcao
     """
    bot.reply_to(mensagem, reclamar)

@bot.message_handler(commands=['atendimento'])
def atendimento(mensagem):    
    pass
    reclamação = f"""
    Se tiver qualquer tipo de reclamação mande para nosso email: {Email}
    Agradecemos pelo seu feedback!
    """
    bot.send_message(mensagem.chat.id, reclamação)

@bot.message_handler(commands=['produto'])
def produto(mensagem):    
    pass
    reclamação = f"""
    Se tiver qualquer tipo de reclamação mande para nosso email: {Email}
    Agradecemos pelo seu feedback!
    """
    bot.send_message(mensagem.chat.id, reclamação)

@bot.message_handler(commands=['entrega'])
def entrega(mensagem):    
    pass
    reclamação = f"""
    Se tiver qualquer tipo de reclamação mande para nosso email: {Email}
    Agradecemos pelo seu feedback!
    """
    bot.send_message(mensagem.chat.id, reclamação)


@bot.message_handler(commands=['opcao3'])
def opcao3(mensagem):
    pass
    atendente = """
   Olá Sou O BOT do jessé, Desculpa não consigo te ajudar no momento
   entre em contato com um dos nossos assitentes!
   
   JESSÉ MIGUEL RAMOS 
   tel: (16)9971234567
    """
    bot.send_message(mensagem.chat.id, atendente)

def verificar(mensagem):
    return True 


@bot.message_handler(func=verificar)
def responder(mensagem):
    texto = """
    Escolha uma opção para continuar (Clique no item):
     /opcao1 Fazer um Pedido
     /opcao2 Fazer uma Reclamação
     /opcao3 Nenhuma dessas opções
    Responder qualquer outra coisa nao vai funcionar, Clique em uma das opcao"""
    bot.reply_to(mensagem, texto)

bot.polling() 