import asyncio
import discord
from discord.ext import commands
from database import *
from config import *

intents = discord.Intents.default()
intents.members = True
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

dicas_de_estudo = [
    "Seu código é como uma pizza, é melhor quando está bem 'implementada' e não possui 'bugs'!",
    "Quando estiver programando, lembre-se de que um bom café pode ser o seu 'compilador' secreto!",
    "Assim como o Pikachu evolui para o Raichu, você precisa evoluir suas habilidades de programação para se tornar um mestre!",
    "Não se preocupe se o seu código não funcionar de primeira. Até mesmo os grandes mestres já receberam mensagens de erro!",
    "A paciência é uma virtude na programação. Seu código pode demorar para compilar, mas lembre-se de que a espera valerá a pena!",
    "Aprender a programar é como aprender um novo idioma. Em vez de verbos e substantivos, você terá loops e condicionais!",
    "O segredo para resolver um bug é olhar para o seu código com um olhar 'depurador'!",
    "Não tenha medo de pedir ajuda. Um programador sempre pode contar com seus 'byte-amigos'!",
    "Programar é como construir um castelo de cartas. Certifique-se de ter uma base sólida antes de adicionar mais funcionalidades!",
    "Um programador bem-sucedido sabe que erros são apenas 'features' inesperadas!",
]

@bot.event
async def on_ready():
    print(f'Bot está pronto. Conectado como {bot.user.name}')

@bot.event
async def on_connect():
    await bot.wait_until_ready()
    bot.loop.create_task(send_study_tip())

@bot.event
async def on_member_join(member):

    # Adicionar o papel de Pretendente ao usuário ao entrar no servidor.
    pretendente_entrada = discord.utils.get(member.guild.roles, id=pretendente_id)
    await member.add_roles(pretendente_entrada)

    # Obtendo os canais do servidor a serem usados e enviando mensagem de boas vindas.
    off_topic = bot.get_channel(off_topic_id)
    public_channel = bot.get_channel(public_channel_id)
    await public_channel.send('Bem-vindo jovem padawan, para entrar para o lado nerd da força, digite o seu e-mail.')
    await public_channel.send('Caso o e-mail não conste na base de dados, você será banido e não entrará para o nosso lado da força.')
    await public_channel.send('O tempo limite para o processo é de 5 minutos.')

    # função necessária para poder receber a entrada do usuário no discord.
    def check(message):
        return message.author == member and message.channel == public_channel

    # O bloco try é usado para a verificação de tempo
    try:

        # esse trecho do código é onde o bot vai receber o e-mail e fazer a validação por meio da função authenticate.
        message = await bot.wait_for('message', check=check, timeout=300)
        email = message.content
        name, authenticated = authenticate(email)
        
        # essa condição verifica se o usuário está autenticado, em caso positivo, ele recebe a chave de acesso no seu e-mail.
        if authenticated:

            # Enviar a chave de autenticação para o e-mail do usuário.
            chave = random_key()
            send_email(email, chave)
            await public_channel.send('A chave de autenticação foi enviada para o seu e-mail, insira-a para ter acesso aos canais do servidor')

            # Aguardar a resposta do usuário com a chave de autenticação no primeiro canal de texto.
            try:
                while True:
                    
                    message = await bot.wait_for('message', check=check, timeout=300)

                    if message.content == chave:

                        # Separa os cargos com base no dominio do e-mail digitado.
                        if "@academico.ifpb.edu.br" in email:
                            role = discord.utils.get(member.guild.roles, name='aluno')
                        elif "@ifpb.edu.br" in email:
                            role = discord.utils.get(member.guild.roles, name='professor')

                        # Adicionar o cargo ao usuário autenticado.
                        await member.add_roles(role)

                        # removendo o cargo de pretendente e adicionando o nome que consta na base de dados ao usuário.
                        await member.remove_roles(pretendente_entrada)
                        await member.edit(nick=name)

                        pretendentes = sum(1 for member in member.guild.members if pretendente_entrada in member.roles)

                        if pretendentes == 0:
                            
                            await public_channel.purge()

                        await off_topic.send(f'Chave válida! Você agora tem acesso aos canais do servidor, seja bem-vindo {name}')

                        break
                    
                    else:
                        await public_channel.send('Chave incorreta. Por favor, digite novamente.')

            # As excessões e os blocos "else" a seguir, são referente as condições de banimento.

            # Caso o usuário não digite o código dentro de 5 minutos ele é banido.
            except asyncio.TimeoutError:
                await member.send(f'Você foi banido do servidor\n'
                                  f'Razão: o código não foi digitado dentro do tempo limite de autenticação\n'
                                  f'caso posssua credenciais válidas, entre em contato com o administrador do servidor para realizar o processo de autenticação novamente'
                                  )
                await member.ban(reason='o código não foi digitado dentro do tempo limite de autenticação')
        # Caso o usuário digite o e-mail errado
        else:
                await member.send(f'Você foi banido do servidor\n'
                                  f'Razão: o email digitado não consta na base de dados do servidor\n'
                                  f'caso ache que isso é um erro, entre em contato com o administrador do servidor para realizar o processo de autenticação novamente'
                                  )
                await member.ban(reason='o email digitado não consta na base de dados do servidor')

    # Caso o usuário não realize o processo dentro de 5 minutos ele é banido.
    except asyncio.TimeoutError:
                await member.send(f'Você foi banido do servidor\n'
                                  f'Razão: o código não foi digitado dentro do tempo limite de autenticação\n'
                                  f'caso posssua credenciais válidas, entre em contato com o administrador do servidor para realizar o processo de autenticação novamente'
                                  )
                await member.ban(reason='o código não foi digitado dentro do tempo limite de autenticação')

@bot.event
async def send_study_tip():
    off_topic = bot.get_channel(off_topic_id)
    await bot.wait_until_ready()
    while not bot.is_closed():
        
        tip = random.choice(dicas_de_estudo)
        await off_topic.send(f'Dica de Estudo: {tip}')

        await asyncio.sleep(60*60)

# Comando de pesquisar artigos por meio da biblioteca arvix
@bot.command()
async def pesquisar(member):
    await member.send(
        f'Por favor, digite as palavras-chave para a pesquisa:\n'
        f'*apenas termos em inglês são aceitos.*\n'
        f'*o tempo limite de espera é de 60 segundos*'
        )
    
    def check(m):
        return m.author == member.author and m.channel == member.channel
    
    try:
        mensagem = await bot.wait_for("message", check=check, timeout=60)  # Espera por 30 segundos para a entrada do usuário
        palavras_chave = mensagem.content
        
        resultados = pesquisar_artigos_arxiv(palavras_chave, max_resultados=5)

        for resultado in resultados:
            autores = [autor.name for autor in resultado.authors]
            mensagem = (
                f'Título: *{resultado.title}*\n'
                f'Autores: *{", ".join(autores)}*\n'
                f'Link de download: {resultado.pdf_url}\n'
            )
            await member.send(mensagem)

    except asyncio.TimeoutError:
        await member.send("Tempo esgotado. Por favor, tente novamente.")

@bot.command()
async def stackoverflow(member):
    await member.send(f'Digite a sua dúvida ou a mensagem de erro\n'
                      f'Por gentileza, digite em inglês para uma maior chance de eficâcia na pesquisa\n')
    def check(m):
        return m.author == member.author and m.channel == member.channel
    
    try:
        mensagem = await bot.wait_for("message", check=check, timeout=60)  # Espera por 30 segundos para a entrada do usuário
        consulta = mensagem.content
        author_name = member.author.name
        resultados = buscar_solucoes(consulta)

        # Filtrar resultados pelo título desejado
        titulo_desejado = consulta.lower()  # Converter para minúsculas para comparação
        resultados_filtrados = [item for item in resultados["items"] if titulo_desejado in item["title"].lower()]

        # Limitar o número de soluções exibidas
        num_solucoes_exibidas = 5
        resultados_limitados = resultados_filtrados[:num_solucoes_exibidas]

        # Verificar se há resultados válidos na resposta
        if len(resultados_limitados) > 0:
            mensagem = f"{author_name}, aqui estão as 5 soluções mais relevantes para '{consulta}':\n"
            for i, item in enumerate(resultados_limitados, start=1):
                titulo = item["title"]
                link_resposta = item["link"]
                mensagem += f"{i}. {titulo}: {link_resposta}\n"
            await member.send(mensagem)
        else:
            await member.send("Nenhuma solução encontrada.")

    except asyncio.TimeoutError:
        await member.send("Tempo esgotado. Por favor, tente novamente.")

bot.run(token)