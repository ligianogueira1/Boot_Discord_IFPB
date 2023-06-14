import asyncio
import discord
from discord.ext import commands
from database import authenticate, random_key, send_email
from config import token

intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix='=', intents=intents)

authenticated_users = {}

@bot.event
async def on_ready():
    print(f'Bot está pronto. Conectado como {bot.user.name}')

@bot.event
async def on_member_join(member):
    # Obter o objeto Role correspondente ao papel de Pretendente
    role = discord.utils.get(member.guild.roles, name='Pretendente')

    # Adicionar o papel de Pretendente ao usuário ao entrar no servidor
    await member.add_roles(role)

    # Obter o canal "Canal de autenticação"
    channel = discord.utils.get(member.guild.channels, name='Canal de autenticação')

    # Enviar uma mensagem de boas-vindas e solicitar o e-mail de autenticação no canal "Canal de autenticação"
    await channel.send(f'Bem-vindo, jovem padawan! Digite o seu e-mail para realizar a autenticação e entrar para o lado nerd da força')

    def check(message):
        return message.author == member and message.channel == channel

    # Aguardar a resposta do usuário no canal "Canal de autenticação" e armazenar o e-mail fornecido
    message = await bot.wait_for('message', check=check)
    email = message.content

    name, authenticated = authenticate(email)

    if authenticated:
        # Enviar a chave de autenticação para o e-mail do usuário
        chave = random_key()
        send_email(email, chave)
        await member.send('A chave de autenticação foi enviada para o seu e-mail.')

        def check(message):
            return message.author == member and message.channel == channel

        # Aguardar a resposta do usuário com a chave de autenticação no canal "Canal de autenticação"
        message = await bot.wait_for('message', check=check)

        if message.content == chave:
            authenticated_users[member.id] = True

            # Obter o objeto Role correspondente ao papel desejado (Aluno ou Professor)
            if "@academico.ifpb.edu.br" in email:
                role = discord.utils.get(member.guild.roles, name='Aluno')
            elif "@ifpb.edu.br" in email:
                role = discord.utils.get(member.guild.roles, name='Professor')

            # Adicionar o papel ao usuário autenticado
            await member.add_roles(role)

            # Conceder acesso aos canais do servidor (exceto "Canal de autenticação")
            for guild_channel in member.guild.channels:
                if guild_channel != channel:
                    await member.add_roles(guild_channel)

            await channel.send('Chave válida! Você agora tem acesso aos canais do servidor.')
        else:
            await channel.send('Sinto muito, a chave digitada não é válida. Verifique novamente seu e-mail e procure pela chave correta.')
    else:
        await channel.send('E-mail não encontrado na base de dados.')
        await member.ban(reason='E-mail não encontrado na base de dados')

bot.run(token)
