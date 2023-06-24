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

<h4> | <a href="#contexto">Contexto e objetivo</a> | <a href="#canais">Descrição dos canais</a> | <a href="#arquivos">Descrição dos arquivos</a> | <a href="#ferramentas">Ferramentas</a> | <a href="#funcionalidades">Funcionalidades</a> | <a href="#bot">O Bot</a> | <a href="#creditos">Créditos</a> |</h4>

<a href="https://imgbox.com/3tZuCnVg" target="_blank"><img src="https://images2.imgbox.com/42/88/3tZuCnVg_o.png" alt="image host" height="5px" width="900px"/></a>

<h2 id="contexto"> :brain: CONTEXTO E OBJETIVO</h2>

<p>Intitulado de BOT IFPB, o robô desenvolvido na plataforma Discord é um mecanismo de autenticação para os acadêmicos do curso, incluindo docentes, discentes e alunos egressos. O desenvolvimento do projeto dar-se-á uma proposta de avaliação para a cadeira de Algoritmos e Programação, ministrada pro Henrique Cunha.</p>

<a href="https://imgbox.com/3tZuCnVg" target="_blank"><img src="https://images2.imgbox.com/42/88/3tZuCnVg_o.png" alt="image host" height="5px" width="900px"/></a>

<h2 id="canais"> :clipboard: DESCRIÇÃO DOS CANAIS DO SERVIDOR</h2>

<li>Canal #Autenticação 🖥️:</li> 
<ul>
Neste canal, o Bot é acionado quando um novo membro entra no servidor; este recebe o cargo de 'pretendente_entrada' e é solicitado que digite seu e-mail para autenticação. Caso o e-mail esteja na base de dados, o usuário recebe uma chave de autenticação via endereço eletrônico. Há um tempo limite de 5 minutos para inserção da chave correta e, caso ela seja válida e o e-mail conste na base de dados, o membro recebe o cargo apropriado e é inserido no servidor; caso contrário, é banido.
</ul>

<li>Canal #Boas vindas 🎉:</li> 
<ul>
Neste canal, o usuário recém-autenticado recebe uma mensagem de boas-vindas, seguido da informação de que possui acesso aos canais do servidor.
</ul>

<li>Canal #Avisos da Coordenação ⚠️:</li> 
<ul>
Este é o canal central do servidor, contendo todos os alunos regularmente matriculados no curso de Engenharia de Computação do IFPB - campus Campina Grande. Ele servirá como intermédio de comunicação entre os estudantes e a Coordenação do curso, de modo a alinhar questões gerenciais, acadêmicas e institucionais. 
</ul>

<li>Canal #Oportunidades de Emprego 📊:</li>  
<ul>
Este fórum engloba alunos atuais e egressos do curso de Engenharia de Computação do IFPB - campus Campina Grande. Ele servirá como intermédio de comunicação para que os ex-estudantes possam compartilhar suas experiências na área da tecnologia, divulgar vagas de emprego e/ou receber oportunidades advindas da coordenação do curso.  
</ul>

<li>Canal “Oportunidades Internas 📌:</li>
<ul>
Fórum destinado aos atuais alunos do curso, de modo que estes possam receber mensagens de divulgação referentes aos editais internos do IFPB (como bolsas de monitoria, pesquisa e extensão, auxílios estudantis, etc.). 
</ul>

<li>Canal #Dúvidas 🙋‍♀️:</li>
<ul>
Este é o fórum apropriado para esclarecimento de dúvidas da comunidade acadêmica (alunos, professores e egressos). Por isso, o canal será moderado e deverá conter apenas perguntas pertinentes ao curso ou mercado profissional da área. 
</ul>

<li>Canal #Off-topic 💥:</li> 
<ul>
  Traduzido livremente para o português como "fora do assunto”, este termo está sendo utilizado para indicar que o assunto das mensagens compartilhadas não possui ligação direta com o tema principal do servidor (comunicação sobre a graduação de Engenharia de Computação). Por isso, é um fórum de tema livre, o espaço apropriado para troca de memes, piadas e discussões de qualquer natureza. Deve-se evitar, no entanto, ofensas, conteúdo sexual, ações e expressões que gerem desconforto aos outros participantes. A moderação será mínima, desde que haja respeito. 
</ul>

<li>Canal #️Professores 📚:</li>
<ul>
Canal destinado apenas para intermédio de comunicação entre os docentes do curso. Neste, os professores podem discutir desde questões as quais julguem relevantes para o andamento do curso a temáticas livres. 
</ul>

<a href="https://imgbox.com/3tZuCnVg" target="_blank"><img src="https://images2.imgbox.com/42/88/3tZuCnVg_o.png" alt="image host" height="5px" width="900px"/></a>

<h2 id="funcionalidades">✍️ FUNCIONALIDADES ADICIONAIS</h2>

<li>Comando “!artigo” 🔍:</li> 
<ul>
Este comando pode ser utilizado dentro do servidor, em qualquer canal, para busca de artigos científicos (no idioma inglês) localizados através da palavra-chave informada. O Bot retornará 5 artigos classificados por ordem de relevância na arvix, constando: título, autor e link para download em pdf. É importante frisar que outros membros podem ter acesso à pesquisa, com exceção do chat privado com o Bot IFPB (para acessá-lo, basca clicar sobre o nome ou ícone do mascote e digitar o comando no campo “Conversar com @IFPB”).
</ul>

<li>Integração com o Stack Overflow 🗣️:</li>  
<ul>
Pertencente à Rede Stack Exchange, o Stack Overflow é um dos maiores sitee de perguntas e respostas para profissionais e entusiastas na área de programação de computadores. Por isso, a funcionalidade é pertinente ao solicitar a pergunta ao usuário do servidor e respondê-lo com as 5 soluções mais relevantes encontradas no site e seus respectivos links.
</ul>

<li>Envio de dicas acadêmicas 🎓:</li>
<ul>
Em um intervalo de 60 minutos, o servidor encaminha mensagens para suporte acadêmico aos discentes, dentre elas: dicas sobre o Campus (como se conectar ao Wi-Fi e horário dos transportes públicos, por exemplo), dicas acadêmicas/de estudo (por exemplo, revisar regularmente o conteúdo já estudado para fortalecer a memória) e dicas profissionais/da área (a exemplo desta: "Quando estiver programando, lembre-se de que um bom café pode ser o seu 'compilador' secreto!"). Algumas das orações podem conter tom humorístico, também sendo uma característica pertinente ao BOT. 
</ul>

<a href="https://imgbox.com/3tZuCnVg" target="_blank"><img src="https://images2.imgbox.com/42/88/3tZuCnVg_o.png" alt="image host" height="5px" width="900px"/></a>

<h2 id="arquivos"> :floppy_disk: DESCRIÇÃO DOS ARQUIVOS DO PROJETO</h2>

<p>Este projeto inclui arquivos executáveis e de destino, além de acesso ao diretório fonte (repositório), como a seguir:</p>
<h4>➔ Arquivos executáveis:</h4>
<ul>
  <li><a href="https://github.com/ligianogueira1/Bot_Discord_IFPB/blob/main/main.py"><b>main.py</b></a> - Contém o código-fonte responsável pela integração entre o Bot e o servidor do Discord. Para isso, foram utilizados procedimentos de autenticação, em que o BOT envia os comandos de solicitação de e-mail e atribui o usuário ao respectivo cargo quando a condição é cumprida. </li>
   <li><a href="https://github.com/ligianogueira1/Bot_Discord_IFPB/blob/main/database.py"><b>database.py</b></a> - Contém docstrings com dicas a serem enviadas, em um intervalo de 60 minutos, para o usuário autenticado no servidor. </li>
    <li><a href="https://github.com/ligianogueira1/Bot_Discord_IFPB/blob/main/bot_functions.py"><b>bot_functions.py</b></a> - Contém o código-fonte com as intruções para que o BOT encaminhe a chave de verificação para o e-mail informado pelo usuário. </li>
   <li><a href="https://github.com/ligianogueira1/Bot_Discord_IFPB/blob/main/.gitignore"><b>.gitignore</b></a> - Contém um arquivo config.py não rastreável, sendo responsável pela informação dos dados de e-mail e senha do servidor para que o processo de autenticação possa ocorrer (envio do código de verificação e, posteriormente, atribuição de cargos). Trata-se de uma informação confidencial. </li>
</ul>

<h4>➔ Bibliotecas utilizadas:</h4> 
<ul>
  » No arquivo <a href="https://github.com/ligianogueira1/Bot_Discord_IFPB/blob/main/main.py"><b>main.py</b>:</a>
  <li>asyncio: sendo uma biblioteca para escrever código simultâneo, utilizamos as sintaxes async/await. Com o seu conjunto de APIs, conseguimos efetuar funções Python simultaneamente e ter domínio sobre sua execução, além de controlar subprocessos, distribuir tarefas por meio de filas e sincronizar código simultâneo. Apesar de o parâmetro ctx ser uma convenção para boa parte dos comandos, "member" atendeu melhor aos objetivos desta função específica.</li>
  <li>discord: esta biblioteca tem como princípio o conceito de eventos, possibilitando que as mensagens possam ser enviadas, lidas e respondidas com base em pré-definições.</li>
</ul>
<ul>
  » No arquivo <a href="https://github.com/ligianogueira1/Bot_Discord_IFPB/blob/main/database.py"><b>database.py</b>:</a>
  <li>pandas: utilizamos esta biblioteca para a incorporação dos arquivos .csv, que contém as relações de alunos e professores que poderão ser vinculados ao servidor. Pandas é responsável por incorporar e verificar estes Dataframes no processo de autenticação. </li>
 </ul> 
 <ul>
  » No arquivo <a href="https://github.com/ligianogueira1/Bot_Discord_IFPB/blob/main/bot_functions.py"><b>bot_functions.py</b>:</a>
  <li>email.message: sendo uma biblioteca de gerenciamento, seu componente central é um “modelo de objeto” que representa mensagens de e-mail. As aplicações do código interagem com o pacote principalmente através da interface do modelo de objeto definida no submódulo "message".</li>
  <li>random: aqui, são implementados geradores de números pseudoaleatórios para várias distribuições. A biblioteca é utilizada, no código, para gerar a chave de segurança que será enviada para o endereço eletrônico do usuário no processo de autenticação. </li>
  <li>requests: esta é uma biblioteca necessária de utilização devido às funcionalidades de exibir artigos acadêmicos solicitados e integração com o Stack Overflow. No código, para ambas as funções, fizemos uso do método "get" para recuperar os dados do endpoint definido. Entretanto, para a primeira, foram utilizados métodos de busca específicos; para a segunda, por sua vez, definimos o URL da API para varredura dos dados e utilizamos o response.json() para exibir as respostas obtidas. </li>
  <li>smtplib: familiar ao protocolo HTTP, o SMTP (Simple Mail Transfrer Protocol) é utilizado para envio de e-mail; ele dita como este será formatado, criptografado e transmitido.</li>
  <li>xml.etree.ElementTree: XML se refere a "Extensible Markup Language" e possui similaridades com o HTML, sendo que sua proposta principal é guardar e transportar dados. Trata-se de uma linguagem auto-descritiva. Esta biblioteca implementa uma API simples e eficiente para analisar e criar dados XML, funcionando como uma estrutura de árvore que suporta hierarquia. Juntamente aos métodos findall() e find(), o Bot consegue fazer uma busca e retornar o resultado solicitado com base nas variáveis pré-definidas. </li>
</ul>

<h4>➔ Módulos internos:</h4> 
<ul>
  » No arquivo <a href="https://github.com/ligianogueira1/Bot_Discord_IFPB/blob/main/main.py"><b>main.py</b>:</a> </li>
  <li>from discord.ext import commands: correspondendo ao próprio nome do módulo, aqui, estendemos a biblioteca do Discord e adicionamos uma extensão de comando para auxiliar no processo de autenticação.</li>
  <li>from config import *: ao buscar os dados confidenciais do config.py e importá-los no servidor, conseguimos prosseguir com os comandos necessários para o processo de autenticação do usuário. </li>
  <li>from bot_functions import *: o arquivo bot_functions é o responsável pelo processo de envio de e-mail, geração e validação da chave de autenticação, comando "!artigos" e comando !stackoverflow. Por isso, fora imprescindível importá-lo neste arquivo vinculado ao Discord. </li>
  <li>from database import *: neste arquivo, encontramos docstrings com dicas a serem enviadas, em um intervalo de 60 minutos, para o usuário autenticado no servidor. "From" e "import" são comandos utilizados para integrá-lo ao servidor através do main.py. </li>
</ul>
<ul>
  » No arquivo <a href="https://github.com/ligianogueira1/Bot_Discord_IFPB/blob/main/bot_functions.py"><b>bot_functions.py</b>:</a>
  <li>from database import *: neste arquivo, encontramos docstrings com dicas a serem enviadas, em um intervalo de 60 minutos, para o usuário autenticado no servidor. "From" e "import" são comandos utilizados para integrá-lo às funções dos Bot. </li>
  <li>from config import *: os dados confidenciais do config.py são necessários para a normalização do funcionamento das funções do Bot. </li>
</ul>  
<h4>➔ Arquivos de destino:</h4> 
<ul>
  <li><a href="https://github.com/ligianogueira1/Bot_Discord_IFPB/blob/main/data/alunos.csv"><b>alunos.csv</b></a> - Contém o arquivo de "alunos.csv" utilizado como banco de dados do projeto. Não é uma informação confidencial, visto que apresenta alunos matriculados em uma Instituição de Ensino Pública.</li>
  <li><a href="https://github.com/ligianogueira1/Bot_Discord_IFPB/blob/main/data/professores.csv"><b>professores.csv</b></a> - Contém o arquivo de "professores.csv" utilizado como banco de dados do projeto. Não é uma informação confidencial, visto que apresenta professores vinculados à uma Instituição de Ensino Pública.</li>
</ul>

<h4>➔ Diretório fonte:</h4>
<ul>
  <li><a href="https://github.com/ligianogueira1/Bot_Discord_IFPB"><b> Bot_Discord_IFPB</b></a> - Inclui todos os arquivos listados acima. </li>
</ul>

<a href="https://imgbox.com/3tZuCnVg" target="_blank"><img src="https://images2.imgbox.com/42/88/3tZuCnVg_o.png" alt="image host" height="5px" width="900px"/></a>

<h2 id="ferramentas"> :books: PRINCIPAIS FERRAMENTAS UTILIZADAS </h2>

<ul>
  <li>Discord</li>
  <p> Utilizamos a plataforma <strong>Discord</strong> como alicerce do Bot, sendo esta, além de uma das principais ferramentas de comunicação dentro da comunidade de TI, detentora de funcionalidades próprias de autenticação e atribuição de cargos. </p>
</ul> 
<ul>
  <li>Python</li>
  <p> Para o desenvolvimento do projeto, utilizados como base a linguagem de programação<strong> Python</strong>, tanto por ser a ferramenta de aprendizado utilizada durante o curso de Algoritmos, quanto por ser uma linguagem de alto nível, orientada a objetos, funcional e de tipagem dinâmica e forte. </p>
</ul>  
<ul>
  <li>Pandas</li>
  <p> Utilizamos, para manipulação dos arquivos .csv, a biblioteca <strong>Pandas</strong>, visto que esta auxilia com uma melhor visualização do Dataframe e possui uma filtragem de dados melhor documentada.</p>
</ul> 
<ul>
  <li>HTML</li>
  <p> Para envio do e-mail contendo o código de verificação do usuário a ser autenticado, fizemos uso da linguagem <strong>HTML</strong> para melhor formatação e agradabilidade estética, visto que é uma linguagem de marcação utilizada na construção de páginas na Web. </p>
</ul>

<a href="https://imgbox.com/3tZuCnVg" target="_blank"><img src="https://images2.imgbox.com/42/88/3tZuCnVg_o.png" alt="image host" height="5px" width="900px"/></a>

<h2 id="bot">🤖 O BOT</h2>

<h4>➔ Confira alguns exemplos do funcionamento do Bot IFPB</h4>

<h4 align="center">Canais:</h4>
<p align="center"> 
<a href="" target="_blank"><img src="https://uploaddeimagens.com.br/images/004/519/173/full/Captura_de_tela_2023-06-24_183525.png?1687643464"/></a>

<h4 align="center">Envio automático de dicas acadêmicas:</h4>
<p align="center"> 
<a href="" target="_blank"><img src="https://uploaddeimagens.com.br/images/004/519/181/full/Captura_de_tela_2023-06-24_151119.png?1687643850"/></a>

<a href="https://imgbox.com/3tZuCnVg" target="_blank"><img src="https://images2.imgbox.com/42/88/3tZuCnVg_o.png" alt="image host" height="5px" width="900px"/></a>

<h2 id="creditos"> :scroll: CRÉDITOS</h2>

<li>Alunos</li>
<p>Anna Lígia Alves Nogueira</p>
<p>Rodrigues Matheus Lima</p></p>

<li>Professor responsável</li>
<p>Henrique Cunha</p>
