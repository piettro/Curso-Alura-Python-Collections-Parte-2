from collections import Counter

text_1 = '''
Para começar a fazer vendas online, uma empresa que fabrica adesivos criou uma página para pré cadastro de cartão de crédito que contém campos como nome, idade, endereço, CPF entre outros.
O problema é que alguns cadastros não possuem um formato de CPF válido, isso porque o campo não possui nenhuma validação. Ou seja, o campo está aceitando não só números como letras e outros tipos de caractere.
O que vamos fazer é encontrar uma maneira de ajudar o usuário de forma mais clara possível a preencher o cadastro e garantir a validação no front-end antes que os dados sejam enviados para o back-end.
Fazendo verificação do campo com a ajuda do patter
Atualmente nós temos o seguinte HTML para o preenchimento do CPF:
Como podemos notar não temos nenhuma validação, então fica confuso se devemos ou não colocar ponto ou traço no CPF e pode acontecer do usuário colocar outros caracteres no campo sem querer.
Para isso evitar que isso ocorra vamos usar o atributo pattern do HTML5 que nos permite fazer uso das famosas expressões regulares que nada mais são que padrões utilizados para selecionar caracteres em uma string.
Na nossa verificação vamos usar a lista [0-9], esse padrão indica que queremos os números de 0 até 9 e o intervalo {11}, indicando que temos que ter um número de 11 dígitos no nosso campo.
Com a adição do pattern nosso campo de CPF ficou da seguinte maneira:
Com a ajuda do pattern e das expressões regulares conseguimos resolver uma parte da tarefa, agora o que precisamos fazer encontrar uma maneira de formatar o CPF no padrão que precisamos enviar ao back-end.
Banner promocional da Alura, com um design futurista em tons de azul, apresentando o texto 
Mais um pouco de Regex
Para começar vamos criar uma função que vai ser responsável por formatar o CPF. Dentro dessa função vamos ter as variáveis :
elementoAlvo: responsável pelo parâmetro que vai ser passado na função
cpfAtual: responsável por capturar os números do CPF digitados
cpfAtualizado: responsável por receber o CPF formatado.
Vamos usar os seguintes recursos das expressões regulares para formatar o CPF:
O repetidor { n } seu papel é repetir um item quantas vezes que forem preciso.
O Grupo ( ) seu papel é agrupar itens.
\d que representa o match com todos os números de 0 - 9.
Baseado no padrão normalmente usado para o CPF, nossa expressão ficou assim /(\d{3})(\d{3})(\d{3})(\d{2})/, ou seja, três grupos que recebem três números cada e um grupo que recebe dois números.
Como já o que já temos nossa expressão, o que vamos fazer agora é utilizar o método replace que vai receber dois parâmetros.
O primeiro vai retornar uma nova string no padrão da nossa expressão regular e o segundo recebe uma função que vai concatenar os pontos e o traço com os essa string. Por fim a variável elementoAlvo recebe o CPF formatado. 
Por fim adicionamos o evento blur no nosso input para quando o campo de CPF perder o foco, a função formataCPF ser ativada.
Já temos nossa verificação e padronização, agora vamos pensar um pouco no usuário. Seria interessante o usuário receber um aviso de erro customizado caso digite o número errado no campo.
Ajudando o usuário a ser mais feliz =)
A API do JavaScript nos fornece algumas propriedades para trabalhar com validação, para o nosso caso vamos usar:
validity: responsável por retornar um valor verdadeiro ou falso.
patternMismatch: responsável por verificar o pattern.
setCustomValidity: responsável por personalizar a resposta para o usuário.
Vamos usar o eventListener para que toda vez que clicarmos no botão de enviar aconteça uma verificação.
Caso patterMismatch não corresponda ao padrão que definimos no pattern no input, vamos mandar uma resposta customizada para o usuário e desabilitar o botão de envio para que ele saiba que algo de errado aconteceu, caso contrário o número é enviado sem problemas.
Não vamos abordar nesse post a maneira de fazer o cálculo para saber se o CPF é válido ou não, felizmente o próprio ministério da fazenda nos disponibiliza o algoritmo para lidar com essa situação.
Se ficou interessado em como funciona regex, e quais os casos onde podemos utilizá-las melhor, aqui na Alura temos um curso de expressões regulares. Nele, você verá como expressões regulares, dentre outras muitas coisas.

'''

text_2 = '''
Vamos imaginar uma empresa como o Nubank, seu nome é ByteBank. A primeira vista ela vende cartões de crédito e possui uma estratégia de marketing de conteúdo para seus clientes (Business to Consumer, B2C).
Agora ela está lançando um novo cartão focado em empresas e quer criar uma estratégia de marketing de conteúdo para outras empresas (business to business, B2B).
Como eles podem criar essa estratégia? É possível utilizar ideias e ferramentas do marketing de conteúdo B2C para o B2B?
Banner da Escola de Inovação e Gestão: Matricula-se na escola de Inovação e Gestão. Junte-se a uma comunidade de mais de 500 mil estudantes. Na Alura você tem acesso a todos os cursos em uma única assinatura; tem novos lançamentos a cada semana; desafios práticos. Clique e saiba mais!
No marketing de conteúdo criado para B2C da ByteBank é muito enfatizado que as principais vantagens da empresa são:
saber o limite na hora;
não pagar qualquer tarifa e
não ter que lidar com burocracia na hora de fazer o cartão.
Então, todo o plano é focado em criar conteúdos sobre questões relacionadas ao mundo financeiro, para mostrar que a empresa é especialista no assunto, transmitindo uma confiança aos clientes.
A equipe de marketing escreveu um texto no qual foram explicadas todas as taxas do cartão de crédito. Depois de explicar com detalhes o que é cada taxa, foi mostrado o porquê do cartão dessa empresa não cobrar nenhuma delas.
Para mostrar na prática o quanto o consumidor economizaria, eles deram como um exemplo que mostram o que pode ser comprado com o dinheiro economizado em tarifas do cartão. Veja como ficou o texto:
Se a tarifa é de 30 reais por mês, depois de um ano: 30 (tarifa) * 12 (meses) = 360, você gasta R$ 360,00 só em tarifas! Não seria muito melhor comprar um Kindle ou dois jogos para Playstation 4 ou, até mesmo, ir uma vez por mês ao cinema (e pagando inteira) com esse dinheiro em vez de pagá-lo em tarifas?
Será que se pode fazer a mesma coisa para o B2B, já que não existem tarifas para empresas também?
As empresas que querem comprar um produto precisam avaliar muito bem toda a compra, sempre se perguntando se aquele produto realmente compensa para ela, principalmente a longo prazo.
Então, e se fosse dito coisas que a empresa poderia fazer com o dinheiro que também vão trazer um retorno financeiro, ao contrário das taxas dos bancos? Como fazer pesquisas com usuários, desenvolver novos produtos, treinar pessoas para marketing, entre outras coisas?
Pensando nessas diferenças, utilizamos o mesmo exemplo: quanto seria economizado por ano pela empresa cliente. Porém, no texto inteiro, queremos também mostrar dicas de como ela pode poupar, de diversas maneiras, mesmo usando um cartão de crédito. Então, o exemplo de economia no texto ficou assim:
Pensando que a tarifa para empresas é mais barata que para pessoas físicas, ou seja, de 30 reais, passa a ser 10 reais por cartão para cada colaborador, e dez cartões serão feitos, cada um pertencendo a colaborador, depois de um ano, serão pagos: 10 (de tarifa) * 10 (quantidade de cartões) * 12 (meses do ano) = 1200.
Assim, a organização gastaria R$ 1.200,00 para manter os cartões durante esse período. Agora, se os cartões não possuem tarifa nenhuma, em vez de pagar esse valor, a empresa economizará R$1.200,00.
Agora, com essa economia, você poderia investir em treinamentos ou eventos, que, após um tempo, poderiam aumentar ainda mais o retorno da empresa.
Foi usada uma linguagem mais formal do que a B2C porque quando estamos lidando com empresas temos que ser mais práticos e mostrar exatamente o que a empresa ganha, e, no caso, até como poderia ganhar mais depois.
Além dessa mudança na linguagem, tivemos ideias diferentes de conteúdo. No B2C foram apresentados conhecimentos a respeito de cada taxa, para que a pessoa entenda o que está pagando e confie em empresas que não cobra as taxas.
Agora para B2B foram apresentadas formas para economizar no cartão, pois, muitas vezes, os empresários sabem o que é cada taxa do cartão e tem que utilizá-lo mesmo assim. Então, mostramos como ele pode economizar e, uma dessas formas, é usar o cartão da ByteBank.
Nesse mesmo texto para B2B também acrescentamos o conteúdo de outra vantagem do cartão: poder determinar um limite de gastos para cada categoria nos cartões dos funcionários da empresa.
Dessa forma, os funcionários não podem gastar mais do que o determinado e, assim, a empresa consegue economizar e planejar os gastos e não extrapolar com compras dos funcionários.
O foco da comunicação B2B que utilizamos foi dar dicas para não cometer erros e economizar mais, para que a empresa perceba que utilizar o cartão é vantagem.
E caso a sua empresa seja diferente da ByteBank, seja só B2B e não tenha nenhum plano de comunicação focado para B2C para se basear?
Existem diversas empresas B2
as que vendem tanto para B2B quanto para B2C, como a ByteBank;
as que vendem para ambos os consumidores, mas possuem um foco maior no B2B, como a Marmotex, que tem como serviço entrega de marmitas e entregam tanto para consumidores quanto empresas, mas possuem um foco maior em organizações e catering  para eventos, ou seja, B2B
as empresas somente B2B, como as de agências de publicidade
Cada uma das empresas que são B2B possui um produto e um serviço para mostrar.
Então, caso você trabalhe em uma empresa que não possui um plano de marketing de conteúdo para B2C para se basear, é só seguir a ideia do marketing de conteúdo, de passar informações relacionados a sua empresa, tornando-a uma autoridade no assunto. E, além disso, mostrar maneiras que o seu produto e/ou serviço pode ajudar a empresa em determinado tema.
No B2B, como no marketing de conteúdo focado no B2C, é importante frisar a importância e a relevância do produto e/ou serviço para o cliente. E, melhor, a longo prazo.
A empresa cliente precisa entender e saber que a vantagem trazida pelo produto será duradoura. Pois o processo de compra B2B é mais longo justamente porque há muito em jogo e muitas pessoas envolvidas.
Mudar de produto ou serviço é trabalhoso e pode causar prejuízo para a empresa, assim, eles buscam e precisam de garantias de que a solução funcionará por muito tempo.
Assim, como no marketing B2C, os tipos de conteúdo devem se atentar aos clientes em cada fase do funil de marketing de conteúdo para trazer o conteúdo certo para a empresa em cada momento da obtenção do cartão.
Para isso, a Bytebank utilizou dados, números, infográficos e mostrou com exemplos práticos maneiras de ajudar a contratante. Também escreveu conteúdos com histórias de empresas - os chamados cases de sucesso - que obtiveram lucro ou sucesso com o produto/serviço.
Além disso, apresentou novidades e dicas tanto da sua empresa, que passou a fornecer uma conta para pessoas físicas e jurídicas, quanto do segmento dela, com informações que podem ser úteis ao cliente do setor financeiro.
Como vimos, as principais diferenças entre os conteúdos B2C para o B2B são a linguagem, que deve ser mais formal se for B2B e apelar para o emocional se for B2C.
No B2B você estará lidando com pessoas que tomam decisões nas empresas, então deverá mostrar como o produto pode ajudar a empresa, de preferência a longo prazo.
Fora isso, o tipo de conteúdo pode ser o mesmo do marketing de conteúdo B2C. Passando desde textos sobre novidades, inovações e dicas na área, até infográficos com dados de pesquisas, vídeos, áudios de podcast, imagens e publicações nas redes sociais.
Também, para conteúdo B2B, é muito comum encontrar whitepapers, grupos de usuários, meetups, cases de sucesso, trial gratuito, e até mesmo vídeos ou campanhas e posts de marketing com influenciadores.
Agora, se você quiser saber mais sobre marketing de conteúdo, pode fazer nosso curso de Marketing de Conteúdo e, também, conferir mais informações no livro da Casa do Código, Marketing de Conteúdo: Estratégias para entregar o que seu público quer consumir.
'''

text_1_counter = Counter(text_1.lower())
text_2_counter = Counter(text_2.lower())

print(text_1_counter)
print(text_2_counter)

total_char_text_1 = sum(text_1_counter.values())
total_char_text_2 = sum(text_2_counter.values())

print(total_char_text_1)
print(total_char_text_2)

def analyse_frequency_letters(texto):
  appers = Counter(texto.lower())
  total_char = sum(appers.values())

  prop = [(letra, frequencia / total_char) for letra, frequencia in appers.items()]
  prop = Counter(dict(prop))
  most_common = prop.most_common(10)
  for char, prop in most_common:
    print("{} => {:.2f}%".format(char, prop * 100))

analyse_frequency_letters(text_1)