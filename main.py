import asyncio
import discord
from discord.ext import commands
from config import *
from bot_functions import *
from database import *

intents = discord.Intents.default()
intents.members = True
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

# EVENTOS DO BOT
@bot.event
async def on_ready():
    """
    Evento chamado quando o bot está pronto e conectado ao servidor.
    """
    print(f'Bot está pronto. Conectado como {bot.user.name}')

@bot.event
async def on_connect():
    """
    Evento acionado quando o bot estabelece conexão com o servidor do Discord.

    Aguarda o bot estar pronto para uso e inicia a tarefa assíncrona "send_study_tip()" para enviar dicas de estudo.
    """
    await bot.wait_until_ready()
    bot.loop.create_task(send_study_tip())

@bot.event
async def send_study_tip():
    """
    Tarefa assíncrona para enviar periodicamente dicas de estudo em um canal específico.

    Obtém o canal "off_topic" usando o ID fornecido.
    Aguarda o bot estar pronto para uso.
    Em um loop contínuo, escolhe uma dica de estudo aleatória e a envia no canal "off_topic".
    Espera por 1 hora antes de enviar a próxima dica.
    """
    off_topic = bot.get_channel(off_topic_id)
    await bot.wait_until_ready()
    while not bot.is_closed():
        tip = random.choice(dicas)
        await off_topic.send(f'Fica a dica: {tip}')

        await asyncio.sleep(15*60)

@bot.event
async def on_member_join(member):
    """
    Evento acionado quando um novo membro entra no servidor.

    O membro recebe o cargo de 'pretendente_entrada' e é solicitado que digite seu e-mail para autenticação.
    Caso o e-mail esteja na base de dados, o membro recebe uma chave de autenticação por e-mail.
    O membro tem 5 minutos para inserir a chave correta.
    Se a chave for correta e o e-mail estiver na base de dados, o membro recebe o cargo apropriado e é bem-vindo ao servidor.
    Caso contrário, o membro é banido do servidor.

    As funções foram importadas do modúlo database, assim como o banco de dados do código.
    As informações confidências das variáveis de ID foram importadas do modúlo config, por questões de segurança do bot.
    As excessões neste evento são para evitar bugs e garantir o banimento por inatividade.

    o uso do parâmetro member se dá para diferenciar os eventos dos comandos.
    """
    pretendente_entrada = discord.utils.get(member.guild.roles, id=pretendente_id)
    await member.add_roles(pretendente_entrada)
    welcome_channel = bot.get_channel(welcome_id)
    public_channel = bot.get_channel(public_channel_id)
    await member.send(
    'Bem-vindo ao servidor de Engenharia de computação!\n\n'
    'Eu sou um bot desenvolvido para ajudar nas suas pesquisas e solucionar dúvidas de programação.\n'
    'Aqui estão alguns dos comandos disponíveis:\n\n'
    '!artigos: Pesquisa artigos no arXiv.\n'
    '!stackoverflow: Busca soluções no Stack Overflow.\n\n'
    'Para explorar o servidor, interagir com os membros e utilizar os comandos, realize a autenticação.\n'
    'Se tiver alguma dúvida ou precisar de ajuda, não hesite em mencionar um administrador ou moderador.\n\n'
    'Divirta-se e aproveite a comunidade!'
)
    await public_channel.send('Bem-vindo jovem padawan, para entrar para o lado nerd da força, digite o seu e-mail.')
    await public_channel.send('Caso o e-mail não conste na base de dados, você será banido e não entrará para o nosso lado da força.')
    await public_channel.send('O tempo limite para o processo é de 5 minutos.')

    def check(message):
        return message.author == member and message.channel == public_channel

    try:
        message = await bot.wait_for('message', check=check, timeout=300)
        email = message.content
        name, authenticated = authenticate(email)

        if authenticated:
            chave = random_key()
            send_email(email, chave)
            await public_channel.send('A chave de autenticação foi enviada para o seu e-mail, insira-a para ter acesso aos canais do servidor')

            while True:
                message = await bot.wait_for('message', check=check, timeout=300)

                if message.content == chave:
                    if "@academico.ifpb.edu.br" in email:
                        role = discord.utils.get(member.guild.roles, name='aluno')
                    elif "@ifpb.edu.br" in email:
                        role = discord.utils.get(member.guild.roles, name='professor')

                    await member.add_roles(role)
                    await member.remove_roles(pretendente_entrada)
                    await member.edit(nick=name)

                    pretendentes = sum(1 for member in member.guild.members if pretendente_entrada in member.roles)

                    if pretendentes == 0:
                        await public_channel.purge()

                    await welcome_channel.send(f'Chave válida! Você agora tem acesso aos canais do servidor, seja bem-vindo {name}')

                    break
                else:
                    await public_channel.send('Chave incorreta. Por favor, digite novamente.')

        else:
            await member.send(f'Você foi banido do servidor\n'
                              f'Razão: o email digitado não consta na base de dados do servidor\n'
                              f'caso ache que isso é um erro, entre em contato com o administrador do servidor para realizar o processo de autenticação novamente'
                              )
            await member.ban(reason='o email digitado não consta na base de dados do servidor')
            pretendentes = sum(1 for member in member.guild.members if pretendente_entrada in member.roles)
            if pretendentes == 0:
                await public_channel.purge()

    except asyncio.TimeoutError:
        await member.send(f'Você foi banido do servidor\n'
                          f'Razão: o código não foi digitado dentro do tempo limite de autenticação\n'
                          f'caso posssua credenciais válidas, entre em contato com o administrador do servidor para realizar o processo de autenticação novamente'
                          )
        await member.ban(reason='o código não foi digitado dentro do tempo limite de autenticação')
        pretendentes = sum(1 for member in member.guild.members if pretendente_entrada in member.roles)
        if pretendentes == 0:
            await public_channel.purge()

# FUNCIONALIDADES DO BOT

@bot.command()
async def artigos(member):
    """
    Comando para pesquisar artigos por meio da biblioteca arXiv.

    Uso:
        !artigos

    Exemplo:

        O usuário usa: !artigos

        O bot retorna: O usuário será solicitado a digitar as palavras-chave para a pesquisa.
        Somente termos em inglês são aceitos.
        O tempo limite de espera é de 60 segundos.

        O bot retornará 5 artigos classificados por ordem de relevância na arvix,
        constando: titúlo, autor e link para download em pdf.

        Posteriormente, o resumo também poderá ser adicionado, porém, no momento está gerando bugs,
        portanto é uma feature futura do bot.

        O parâmetro ctx é uma convenção para boa parte dos comandos, porém optei por usar member nessa função especifica.
    """
    await member.send(
        'Por favor, digite as palavras-chave para a pesquisa:\n\n'
        '*apenas termos em inglês são aceitos.*\n'
        '*o tempo limite de espera é de 60 segundos*'
    )

    def check(m):
        return m.author == member.author and m.channel == member.channel

    try:
        mensagem = await bot.wait_for("message", check=check, timeout=60)  # Espera por 30 segundos para a entrada do usuário
        palavras_chave = mensagem.content
        
        resultados = pesquisar_artigos_arxiv(palavras_chave, max_resultados=5)

        for resultado in resultados:
            mensagem = (
                f'Título: {resultado["titulo"]}\n'
                f'Autores: {", ".join(resultado["autores"])}\n'
                f'Link de download: {resultado["pdf_url"]}\n'
                f"\n\n"
            )
            await member.send(mensagem)
           
    except asyncio.TimeoutError:
        await member.send('Tempo esgotado. Por favor, tente novamente.')


@bot.command()
async def duvida(ctx):
    """
    Comando para buscar soluções de código no Stack Overflow.

    Uso:

        !duvida

    O usuário será solicitado a digitar sua dúvida ou mensagem de erro.
    Por gentileza, digite em inglês para aumentar a eficácia da pesquisa.
    O tempo limite de espera é de 60 segundos.

    Exemplo:

        O usuário usa: !duvida

        O bot retorna: O usuário será solicitado a digitar as palavras-chave para a pesquisa.
        Somente termos em inglês são aceitos.
        O tempo limite de espera é de 60 segundos.

        O bot retornará o link das soluções mais relevantes do stackoverflow para cada dúvida,
        constando: titúlo e link para o forúm.

        o bot possibilita que você use mais do que 5 soluções, 
        25 se você não estiver usando a chave de API

        O parâmetro ctx é uma convenção para boa parte dos comandos, por essa razão está sendo usado.
    """
    await ctx.send('Digite a sua dúvida ou a mensagem de erro para buscar no stack overflow\n'
                   'Por gentileza, digite em inglês para uma maior chance de eficácia na pesquisa\n')

    def check(message):
        return message.author == ctx.author and message.channel == ctx.channel

    try:
        message = await bot.wait_for('message', check=check, timeout=60)
        consulta = message.content
        author_name = ctx.author.name
        resultados = buscar_solucoes(consulta)

        titulo_desejado = consulta.lower() 
        resultados_filtrados = [item for item in resultados['items'] if titulo_desejado in item['title'].lower()]

        num_solucoes_exibidas = 5
        resultados_limitados = resultados_filtrados[:num_solucoes_exibidas]

        if len(resultados_limitados) > 0:
            mensagem = f"{author_name}, aqui estão a(s) soluções mais relevantes para '{consulta}':\n"
            for i, item in enumerate(resultados_limitados, start=1):
                titulo = item['title']
                link_resposta = item['link']
                mensagem += f"{i}. {titulo}: {link_resposta}\n"
            await ctx.send(mensagem)
        else:
            await ctx.send('Nenhuma solução encontrada.')

    except asyncio.TimeoutError:
        await ctx.send('Tempo esgotado. Por favor, tente novamente.')

    
bot.run(token)