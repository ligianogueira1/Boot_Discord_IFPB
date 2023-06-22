import asyncio
import discord
from discord.ext import commands
from database import authenticate, random_key, send_email
from config import *

intents = discord.Intents.default()
intents.members = True
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Bot está pronto. Conectado como {bot.user.name}')

@bot.event
async def on_member_join(member):

    # Obtendo os canais do servidor a serem usados e enviando mensagem de boas vindas.
    public_channel = bot.get_channel(public_channel_id)
    off_topic = bot.get_channel(off_topic_id)
    message = 'Bem-vindo jovem padawan, para entrar para o lado nerd da força, digite o seu e-mail.'
    await public_channel.send(message)

    # Adicionar o papel de Pretendente ao usuário ao entrar no servidor.
    pretendente_entrada = discord.utils.get(member.guild.roles, id=pretendente_id)
    await member.add_roles(pretendente_entrada)

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
            await public_channel.send('A chave de autenticação foi enviada para o seu e-mail.')

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
                await public_channel.send('Culpado 1')
        # Caso o usuário digite o e-mail errado
        else:
            await public_channel.send('Culpado 2')

    # Caso o usuário não digite o código dentro de 5 minutos ele é banido.
    except asyncio.TimeoutError:
        await public_channel.send('Culpado 3')


bot.run(token)