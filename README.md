# Bot para Discord - Engenharia de Computação/IFPB
Criação de um servidor com mecanismo de autenticação de usuários, na plataforma Discord, para o curso de Engenharia de Computação - IFPB.

<p align="center"> 
<a href="" target="_blank"><img src="https://github.com/ligianogueira1/Bot_Discord_IFPB/assets/109001008/7e3c3093-8c87-499b-9921-0c735ce681f8"/></a>
</p>
<h1 align="center"> BOT IFPB </h1>
<h4 align="center"> Bot para Discord - Engenharia de Computação/<a href="https://www.ifpb.edu.br/">IFPB</a>(Inverno 2023) </h4>

<br>
</br>
<p align="center"> 
<a href="https://image.jimcdn.com/app/cms/image/transf/dimension=970x10000:format=gif/path/sa16dc2497d80e05e/image/icd162bb94ffa0064/version/1551588419/image.gif" target="_blank"><img src="https://image.jimcdn.com/app/cms/image/transf/dimension=970x10000:format=gif/path/sa16dc2497d80e05e/image/icd162bb94ffa0064/version/1551588419/image.gif" alt="image host" height="142px"/></a>
</p>

<h4> | <a href="#contexto">Contexto e objetivo</a> | <a href="#detalhamento">Descrição dos canais</a> | <a href="#arquivos">Descrição dos arquivos</a> | <a href="#ferramentas">Ferramentas</a> | <a href="#creditos">Créditos</a> |</h4>

<a href="https://imgbox.com/3tZuCnVg" target="_blank"><img src="https://images2.imgbox.com/42/88/3tZuCnVg_o.png" alt="image host" height="5px" width="900px"/></a>

<h2 id="contexto"> :brain: CONTEXTO E OBJETIVO</h2>

<p>Intitulado de BOT IFPB, o robô desenvolvido na plataforma Discord é um mecanismo de autenticação para os acadêmicos do curso, incluindo docentes, discentes e alunos egressos. O desenvolvimento do projeto dar-se-á uma proposta de avaliação para a cadeira de Algoritmos e Programação, ministrada pro Henrique Cunha.</p>

<a href="https://imgbox.com/3tZuCnVg" target="_blank"><img src="https://images2.imgbox.com/42/88/3tZuCnVg_o.png" alt="image host" height="5px" width="900px"/></a>


<h2 id="detalhamento"> :clipboard: DESCRIÇÃO DOS CANAIS DO SERVIDOR</h2>

<li>Canal #Avisos da Coordenação ⚠️:</li> 
Este é o canal central do servidor, contendo todos os alunos regularmente matriculados no curso de Engenharia de Computação do IFPB - campus Campina Grande. Ele servirá como intermédio de comunicação entre os estudantes e a Coordenação do curso, de modo a alinhar questões gerenciais, acadêmicas e institucionais. 

<li>Canal #Oportunidades de Emprego 📊:</li>  
Este fórum engloba alunos atuais e egressos do curso de Engenharia de Computação do IFPB - campus Campina Grande. Ele servirá como intermédio de comunicação para que os ex-estudantes possam compartilhar suas experiências na área da tecnologia, divulgar vagas de emprego e/ou receber oportunidades advindas da coordenação do curso.  

<li>Canal “Oportunidades Internas 📌:</li>
Fórum destinado aos atuais alunos do curso, de modo que estes possam receber mensagens de divulgação referentes aos editais internos do IFPB (como bolsas de monitoria, pesquisa e extensão, auxílios estudantis, etc.). 

<li>Canal #Dúvidas 🙋‍♀️:</li>
Este é o fórum apropriado para esclarecimento de dúvidas da comunidade acadêmica (alunos, professores e egressos). Por isso, o canal será moderado e deverá conter apenas perguntas pertinentes ao curso ou mercado profissional da área. 

<li>Canal #Off-topic 💥:</li> 
Traduzido livremente para o português como "fora do assunto”, este termo está sendo utilizado para indicar que o assunto das mensagens compartilhadas não possui ligação direta com o tema principal do servidor (comunicação sobre a graduação de Engenharia de Computação). Por isso, é um fórum de tema livre, o espaço apropriado para troca de memes, piadas e discussões de qualquer natureza. Deve-se evitar, no entanto, ofensas, conteúdo sexual, ações e expressões que gerem desconforto aos outros participantes. A moderação será mínima, desde que haja respeito. 

<li>Canal #️Professores 📚:</li>  
Canal destinado apenas para intermédio de comunicação entre os docentes do curso. Neste, os professores podem discutir desde questões as quais julguem relevantes para o andamento do curso a temáticas livres. 

<li>Comando “!artigo” 🔍:</li>  

Este comando pode ser utilizado dentro do servidor, em qualquer canal, para busca de artigos científicos (no idioma inglês) localizados através da palavra-chave informada. É importante frisar que outros membros podem ter acesso à sua pesquisa, com exceção do chat privado com o Bot IFPB (para acessá-lo, basca clicar sobre o nome ou ícone do mascote e digitar o comando no campo “Conversar com @IFPB”. 

<a href="https://imgbox.com/3tZuCnVg" target="_blank"><img src="https://images2.imgbox.com/42/88/3tZuCnVg_o.png" alt="image host" height="5px" width="900px"/></a>

<h2 id="arquivos"> :floppy_disk: DESCRIÇÃO DOS ARQUIVOS DO PROJETO</h2>

<p>Este projeto inclui arquivos executáveis e de destino, além de acesso ao nosso diretório fonte (repositório), como a seguir:</p>
<h4>➔ Arquivos executáveis:</h4>
<ul>
  <li><a href="https://github.com/ligianogueira1/Bot_Discord_IFPB/blob/main/main.py"><b>main.py</b></a> - Contém o código-fonte responsável pela integração entre o Bot e o servidor do Discord. Para isso, foram utilizadas as seguintescom os procedimentos de autenticação, em que o BOT envia os comandos de solicitação de e-mail e atribui o usuário ao respectivo cargo quando a condição é cumprida. </li>
   <li><a href="https://github.com/ligianogueira1/Bot_Discord_IFPB/blob/main/database.py"><b>database.py</b></a> - Contém docstrings com dicas a serem enviadas, em um intervalo de 60 minutos, para o usuário autenticado no servidor. </li>
    <li><a href="https://github.com/ligianogueira1/Bot_Discord_IFPB/blob/main/bot_functions.py"><b>bot_functions.py</b></a> - Contém o código-fonte com as intruções para que o BOT encaminhe a chave de verificação para o e-mail informado pelo usuário. </li>
   <li><a href="https://github.com/ligianogueira1/Bot_Discord_IFPB/blob/main/.gitignore"><b>.gitignore</b></a> - Contém um arquivo config.py não rastreável, sendo responsável pela informação dos dados de e-mail e senha do servidor para que o processo de autenticação possa ocorrer (envio do código de verificação e, posteriormente, atribuição de cargos). Trata-se de uma informação confidencial. </li>
</ul>

<h4>➔ Bibliotecas utilizadas:</h4> 
<ul>
  <li>» No arquivo <a href="https://github.com/ligianogueira1/Bot_Discord_IFPB/blob/main/main.py"><b>main.py</b></a> </li>
  <li>asyncio:</li>
  <li>discord:</li>
</ul>
<ul>
  <li>» No arquivo <a href="https://github.com/ligianogueira1/Bot_Discord_IFPB/blob/main/database.py"><b>database.py</b></a> </li>
  <li>pandas:</li>
 </ul> 
 <ul>
  <li>» No arquivo <a href="https://github.com/ligianogueira1/Bot_Discord_IFPB/blob/main/bot_functions.py"><b>bot_functions.py</b></a> </li>
  <li>email.message:</li>
  <li>random:</li>
  <li>requests:</li>
  <li>smtplib:</li>
  <li>xml.etree.ElementTree:</li>
</ul>

<h4>➔ Módulos internos:</h4> 
<ul>
  <li>» No arquivo <a href="https://github.com/ligianogueira1/Bot_Discord_IFPB/blob/main/main.py"><b>main.py:</b></a> </li>
  <li>from discord.ext import commands:</li>
  <li>from config import *:</li>
  <li>from bot_functions import *:</li>
  <li>from database import *:</li>
</ul>
<ul>
  <li>» No arquivo <a href="https://github.com/ligianogueira1/Bot_Discord_IFPB/blob/main/bot_functions.py"><b>bot_functions.py</b></a> </li>
  <li>from database import *:</li>
  <li>from config import *:</li>
</ul>  
<h4>➔ Arquivos de destino:</h4> 
<ul>
  <li><a href="https://github.com/ligianogueira1/Bot_Discord_IFPB/blob/main/data/alunos.csv"><b>alunos.csv</b></a> - Contém o arquivo de "alunos.csv" utilizado como banco de dados do projeto. Não é uma informação confidencial, visto que apresenta alunos matriculados em uma Instituição de Ensino Pública.</li>
  <li><a href="https://github.com/ligianogueira1/Bot_Discord_IFPB/blob/main/data/professores.csv"><b>professores.csv</b></a> - Contém o arquivo de "professores.csv" utilizado como banco de dados do projeto. Não é uma informação confidencial, visto que apresenta professores vinculados à uma Instituição de Ensino Pública</li>
</ul>

<h4>➔ Diretório fonte:</h4>
<ul>
  <li><a href="https://github.com/ligianogueira1/Bot_Discord_IFPB"><b> Bot_Discord_IFPB</b></a> - Inclui todos os arquivos listados acima </li>
</ul>

<a href="https://imgbox.com/3tZuCnVg" target="_blank"><img src="https://images2.imgbox.com/42/88/3tZuCnVg_o.png" alt="image host" height="5px" width="900px"/></a>

<h2 id="ferramentas"> :books: PRINCIPAIS FERRAMENTAS UTILIZADAS </h2>

<ul>
  <li>Discord</li>
  <p> Utilizamos a plataforma <strong>Discord</strong> como alicerce do Bot. A plataforma é um dos principais meios de comunicação dentro da comunidade de TI, além de possuir ferramentas próprias de autenticação e atribuição de cargos. </p>
</ul> 
<ul>
  <li>Python</li>
  <p> Para o desenvolvimento do projeto, utilizados como base a linguagem de programação<strong> Python </strong>, tanto por ser a ferramenta de aprendizado utilizada durante o curso de Algoritmos, quando por ser uma linguagem de alto nível, orientada a objetos, funcional, de tipagem dinâmica e forte.
</ul>  
<ul>
  <li>Pandas</li>
  <p> Utilizados, para manipulação dos Dataframes, a biblioteca <strong>Pandas</strong>, visto que esta auxilia com uma melhor visualização do Dataframe e possuir uma filtragem de dados melhor documentada.</p>
</ul> 
<ul>
  <li>HTML</li>
  <p>Para envio do e-mail contendo o código de verificação do usuário a ser autenticado, fizemos uso da linguagem <strong>HTML</strong> para melhor formatação e agradabilidade estética, visto que é uma linguagem de marcação utilizada na construção de páginas na Web.</p>
</ul>

<a href="https://imgbox.com/3tZuCnVg" target="_blank"><img src="https://images2.imgbox.com/42/88/3tZuCnVg_o.png" alt="image host" height="5px" width="900px"/></a>

<h2 id="creditos"> :scroll: CRÉDITOS</h2>

<li>Alunos</li>
<p>Anna Lígia Alves Nogueira</p>
<p>Rodrigues Matheus Lima</p></p>

<li>Professor responsável</li>
<p>Henrique Cunha</p>
