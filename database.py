import pandas as pd

dicas = [
    "Para acessar a rede Wi-Fi do campus Campina Grande, acesse o link e siga os procedimentos: wifi.cge.ifpb.edu.br/",
    "Para ter acesso às últimas notícias do campus Campina Grande, acesse: www.ifpb.edu.br/campinagrande",
    "Precisa de transporte público para ir ao campus ou voltar para casa? Fique ligado: os ônibus da rota IFPB são: 022, 660 e 220.",
    "Precisa de transporte público para ir ao campus ou voltar para casa? Confira os horários da rota IFPB:",
    "Para saber mais sobre Assistência Estudantil do Campus, acesse: www.ifpb.edu.br/campinagrande/assistencia-estudantil"
    "Revise regularmente o conteúdo já estudado para fortalecer a memória.",
    "Mantenha uma atitude positiva e persistente em relação aos estudos.",
    "Faça um cronograma de estudos e siga-o.",
    "Estabeleça metas claras e mensuráveis para o seu estudo.",
    "Mantenha uma atitude positiva e persistente em relação aos estudos.",
    "Revise regularmente o conteúdo já estudado para fortalecer a memória.",
    "Faça pausas regulares durante o estudo para descansar a mente.",
    "Utilize técnicas de memorização, como mapas mentais e resumos.",
    "É fundamental aliar o estudo teórico com as atividades práticas.",
    "Não hesite em pedir ajuda em caso de dúvidas!",
    "Conteúdos de excelência também podem ser encontrados em livros e manuais.",
    "Seja curioso! Além de reunir informações de forma mais leve, esse método te dará uma visão ampla sobre o assunto, podendo fazer conexões com outras matérias.",
    "Ensine outra pessoa! Sempre existirão dúvidas diferentes das suas e essas perguntas podem ser muito úteis para você.",
    "Assista a filmes sobre a matéria. O fato de ser um material audiovisual pode ajudar na memorização.",
    "Leia no mínimo 3 vezes o conteúdo para que ele seja realmente fixado.",
    "'Aprender é a única coisa de que a mente nunca se cansa, nunca tem medo e nunca se arrepende' - Leonardo da Vinci.",
    "Não desista de estudar por causa de um dia ruim. Seja persistente!",
    "Não veja estudar como uma tortura; abrace a dádiva de aprender e evoluir."
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
    "qual é o animal favorito dos programadores? O bit-coin!",
    "lembre-se que é fundamental contar com uma estrutura sólida de lógica de programação, já que ela é quem te ajuda a ter uma compreensão mais eficiente da formação do código e desenvolver soluções funcionais.",
    "não decore a sintaxe de uma linguagem de programação, pois ela pode ser consultada a qualquer momento na documentação da linguagem. Invés disso, foque em aprender sobre os fundamentos, isso dará liberdade para implementar soluções em qualquer linguagem.",
    "utilize papel e caneta; antes de codificar, foque nas ideias e conceitos que cercam o processo. Treine sua mente para resolver esses problemas, isso vai ajudar a traçar o melhor caminho e evitar frustrações com soluções falhas.",
    "não copie e cole códigos prontos. Isto impede que você analise os fundamentos por trás da lógica desenvolvida.",
    "antes de codificar, é importante ter diferentes perspectivas sobre o problema. Use ferramentas e técnicas, como fluxogramas, para planejar a estrutura do código antes de escrever e encontrar a solução mais adequada à situação.",
    "teste sempre o seu código! Ao finalizar uma funcionalidade, tire alguns minutos para clarear a mente e retorne à aplicação. Faça testes buscando refletir sobre os diferentes cenários de uso daquele item e verifique a presença de falhas.",
    "revisar o código constantemente. De tempos em tempos, volte ao código já implementado e revise-o. Analise se o trecho ainda é necessário, se está funcionando como esperado e se algo pode ser melhorado.",
    "lembre-se de comentar seu código: reserve um espaço para explicar de forma objetiva a sua linha de raciocínio sobre o que foi construído.",
    "não repita o código muitas vezes; você pode transformar o trecho que se repete em um componente ou uma função global. Desse modo, esses elementos poderão ser utilizados pela aplicação inteira, mas serão escritos apenas uma vez em um único lugar.",
    "pular o básico e já partir para o desenvolvimento de sistemas complexos resultará em frustração. Lembre-se: a pressa é inimiga da perfeição. Avance gradualmente com a complexidade dos projetos criados."
]

students = pd.read_csv('data/alunos.csv')
teachers = pd.read_csv('data/professores.csv')
