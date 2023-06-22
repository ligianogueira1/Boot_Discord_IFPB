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
    channel = bot.get_channel(1121156083583549601)  # Substitua pelo ID do canal desejado
    message = 'Bem-vindo jovem padawan, para entrar para o lado nerd da força, digite o seu e-mail.'
    await channel.send(message)

    # Adicionar o papel de Pretendente ao usuário ao entrar no servidor
    role_id = 1121156684694421645  
    role = discord.utils.get(member.guild.roles, id=role_id)
    await member.add_roles(role)

    # Obter o objeto do canal usando o ID
    public_channel_id = 1121156083583549601  # Substitua pelo ID do canal desejado
    public_channel = bot.get_channel(public_channel_id)

# ***************************** O erro está nesse trecho de código *********************************************************************

    def check(message):
        return message.author == member and message.channel == public_channel

    # Aguardar a resposta do usuário no primeiro canal de texto e armazenar o e-mail fornecido
    try:
        message = await bot.wait_for('message', check=check, timeout=300)
        email = message.content
        await member.send('A chave de autenticação foi enviada para o seu e-mail.')
        name, authenticated = authenticate(email)
        
# ************************ ele sempre entra como false em if authenticated: e vai pra o else "culpado 2" *******************************************

        if authenticated:
            # Enviar a chave de autenticação para o e-mail do usuário
            chave = random_key()
            send_email(email, chave)
            await member.send('A chave de autenticação foi enviada para o seu e-mail.')

            # Aguardar a resposta do usuário com a chave de autenticação no primeiro canal de texto
            try:
                message = await bot.wait_for('message', check=check, timeout=300)

                if message.content == chave:
                    authenticated_users[member.id] = True

                    # Obter o objeto Role correspondente ao papel desejado (Aluno ou Professor)
                    if "@academico.ifpb.edu.br" in email:
                        role = discord.utils.get(member.guild.roles, name='Aluno')
                    elif "@ifpb.edu.br" in email:
                        role = discord.utils.get(member.guild.roles, name='Professor')

                    # Adicionar o papel ao usuário autenticado
                    await member.add_roles(role)

                    await public_channel.send('Chave válida! Você agora tem acesso aos canais do servidor.')

                else:
                    await public_channel.send('Chave incorreta. Por favor, digite novamente.')

            except asyncio.TimeoutError:
                await public_channel.send('Culpado 1')

        else:
            await public_channel.send('Culpado 2')

    except asyncio.TimeoutError:
        await public_channel.send('Culpado 3')


bot.run(token)
