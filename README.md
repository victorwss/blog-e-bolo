# Exercício com Flask e Jinja2

O exercício consiste em definir oito funções com os devidos mapeamentos de rotas para realizar o cadastramento e
pesquisa de receitas de bolo em um site de receitas de bolo ou então de notícias em um blog.

O primeiro passo é escolher qual dos dois você vai preferir fazer e então jogar o outro fora. Os dois têm o mesmo nível
de dificuldade, a mesma estrutura, os mesmos desafios de implementação e até são bastante parecidos. Um deles pode ser
encontrado na pasta `receitas` e o outro na pasta `blog`.

## Arquivos

Alguns arquivos Python já estão disponibilizados:

- Os arquivos `receitas/model/receita_model.py` e `blog/model/blog_model` já contém as classes que são necessárias
para modelar os dados a serem cadastrados, pesquisados e recebidos na aplicação escolhida. Não altere esses arquivos.

- Os arquivos `receitas/model/receita_dao_mem.py` e `blog/model/blog_dao_mem.py` contêm as nossas implementaçôes do
"banco de dados". No momento o nosso banco de dados não é um banco de dados de verdade, e sim apenas um objeto que
encapsula um dicionário contendo todos os dados. Não altere esses arquivos.

- Os arquivos `receitas/model/__init__.py` e `blog/model/__init__.py` são arquivos em branco que servem para marcar as
respectivas pastas `model` como um dos pacotes do respectivo sistema que estará sendo desenvolvido. Não mexa neles.

- Os arquivos `receitas/receita_controller.py` e `blog/blog_controller.py` deverão conter o controlador do código do
sistema, que é responsável por receber requisições HTTP, entender o que essas requisições significam e extrair os dados
de dentro delas. Observe que os que foram dados pelo professor estão praticamente vazios. **Um deles é o arquivo Python
que você DEVE alterar**. Obviamente, se você escolheu o sistema de receitas de bolo, altere o de receitas de bolo e se
escolheu o do blog, altere o do blog. 

## Arquivo `receita_controller.py`

Se você escolheu o sistema de receitas de bolo, você deve alterar o arquivo `receita_controller.py` e nele implementar
com o Flask as seguintes rotas:

1. Com a rota GET `/receita/nova`, exiba a tela que permita a criação de uma nova receita de bolo, contendo um
    formulário HTML. Esse formulário fará um POST para `/receita/nova`.

2. Com a rota GET `/receita/<id>`, exiba a tela que permita a um usuário casual ler uma receita de bolo (use o campo
    `id_receita`) para identificar qual é a receita.

    Se a receita não existir, redirecione para a rota `/receita` e coloque uma mensagem de erro
    *"A receita {id_receita} não foi encontrada."*

3. Com a rota GET `/receita/<id>/editar`, exiba a tela que permita a edição de uma receita de bolo existente, contendo
    o mesmo formulário HTML utilizado na criação, porém com os dados já preenchidos. Esse formulário fará um POST para
    `/receita/<id>/editar`.

    Se a receita não existir, redirecione para a rota `/receita` e coloque uma mensagem de erro
    *"A receita {id_receita} não foi encontrada."*

4. Com as rotas GET `/receita` e GET `/`, liste as receitas. Mas preste atenção nos campos da query string.

    O campo `msg` na query  string corresponde a uma mensagem a ser exibida na tela. Se esse campo não existir ou
    estiver em branco, nenhuma mensagem deve ser mostrada.

    O campo `msg_tipo` na query string corresponde ao tipo da mensagem a ser exibida na tela. Seu valor pode ser `erro`
    ou `ok`. Se esse campo não existir, estiver em branco ou tiver algum conteúdo que não seja um desses dois, nenhuma
    mensagem deve ser mostrada.

    O campo `q` corresponde a um critério de busca, e pode aparecer múltiplas vezes na query string. Se esse campo não
    existir ou estiver em branco, todas as receitas devem ser listadas.

5. Com a rota POST `/receita/nova`, leia os dados da receita enviados a partir do formulário HTML e monte um objeto do
    tipo `ReceitaSemId`. Salve o objeto no "banco de dados" (o que irá criar um ID para ele) e em seguida, redirecione
    para `/receita` e coloque nesta tela a mensagem *"A receita {id_receita} foi criada com sucesso."*

6. Com a rota POST `/receita/<id>/editar`, leia os dados da receita enviados a partir do formulário HTML e monte um
    objeto do tipo `Receita` (desta vez com o ID). Atualize o objeto no "banco de dados" e em seguida, redirecione para
    `/receita` e coloque nesta tela a mensagem *"A receita {id_receita} foi atualizada com sucesso."*

    Se a receita não existir, redirecione para a rota `/receita` e coloque uma mensagem de erro
    *"A receita {id_receita} não foi encontrada."*

7. Com a rota POST `/receita/<id>/excluir`, exclua a receita com o ID correspondente do "banco de dados" e redirecione
    para `/receita`. Coloque a mensagem *"A receita {id_receita} foi excluída com sucesso."* ou então
    *"A receita {id_receita} nem mesmo existia."*, conforme for o caso. Note que ambas as mensagens são consideradas
    como sucessos.

Importante: Note que **todos** os IDs são sempre números inteiros.

## Arquivo `blog_controller.py`

Se você escolheu o sistema de blog, você deve alterar o arquivo `blog_controller.py` e nele implementar com o Flask as
seguintes rotas:

1. Com a rota GET `/materia/nova`, exiba a tela que permita a criação de uma nova matéria do blog, contendo um
    formulário HTML. Esse formulário fará um POST para `/materia/nova`.

2. Com a rota GET `/materia/<id>`, exiba a tela que permita a um usuário casual ler uma matéria do blog (use o campo
    `id_noticia`) para identificar qual é a matéria.

    Se a matéria não existir, redirecione para a rota `/materia` e coloque uma mensagem de erro
    *"A matéria {id_materia} não foi encontrada."*

3. Com a rota GET `/materia/<id>/editar`, exiba a tela que permita a edição de uma matéria existente do blog, contendo
    o mesmo formulário HTML utilizado na criação, porém com os dados já preenchidos. Esse formulário fará um POST para
    `/materia/<id>/editar`.

    Se a matéria não existir, redirecione para a rota `/materia` e coloque uma mensagem de erro
    *"A matéria {id_materia} não foi encontrada."*

4. Com as rotas GET `/materia` e GET `/`, liste as matérias. Mas preste atenção nos campos da query string.

    O campo `msg` na query  string corresponde a uma mensagem a ser exibida na tela. Se esse campo não existir ou
    estiver em branco, nenhuma mensagem deve ser mostrada.

    O campo `msg_tipo` na query string corresponde ao tipo da mensagem a ser exibida na tela. Seu valor pode ser `erro`
    ou `ok`. Se esse campo não existir, estiver em branco ou tiver algum conteúdo que não seja um desses dois, nenhuma
    mensagem deve ser mostrada.

    O campo `q` corresponde a um critério de busca, e pode aparecer múltiplas vezes na query string. Se esse campo não
    existir ou estiver em branco, todas as matérias devem ser listadas.

5. Com a rota POST `/materia/nova`, leia os dados da matéria enviados a partir do formulário HTML e monte um objeto do
    tipo `MateriaSemId`. Salve o objeto no "banco de dados" (o que irá criar um ID para ele) e em seguida, redirecione
    para `/materia` e coloque nesta tela a mensagem *"A matéria {id_materia} foi criada com sucesso."*

6. Com a rota POST `/materia/<id>/editar`, leia os dados da matéria enviados a partir do formulário HTML e monte um
    objeto do tipo `Materia` (desta vez com o ID). Atualize o objeto no "banco de dados" e em seguida, redirecione para
    `/materia` e coloque nesta tela a mensagem *"A matéria {id_materia} foi atualizada com sucesso."*

    Se a matéria não existir, redirecione para a rota `/materia` e coloque uma mensagem de erro
    *"A matéria {id_materia} não foi encontrada."*

7. Com a rota POST `/materia/<id>/excluir`, exclua a matéria com o ID correspondente do "banco de dados" e redirecione
    para `/materia`. Coloque a mensagem *"A matéria {id_materia} foi excluída com sucesso."* ou então
    *"A matéria {id_materia} nem mesmo existia."*, conforme for o caso. Note que ambas as mensagens são consideradas
    como sucessos.

Importante: Note que **todos** os IDs são sempre números inteiros.

## Outros requisitos do controller

Qualquer que tenha sido o sistema que você escolheu implementar, há ainda uma oitava rota a ser implementada:

8. Com a rota GET `/nomes`, retorne uma página com lista dos nomes dos alunos que fizeram este trabalho. Mas não é pra
    dar apenas uma lista nua e crua com os nomes e nada mais. Faça uma página bonita, capriche no CSS e no HTML, mostre
    algo interessante, diferente e único. Sejam criativos aqui.

    No entanto, há alguns limites para a criatividade. Assim como você não deve pecar pela falta, não peque pelo
    excesso também. Lembre-se que o objetivo é apenas mostrar a lista dos alunos que fizeram o AC e mostrar que você
    sabe fazer uma página legalzinha sem viajar maionese. Nada de querer fazer um sistema novo inteiro só para essa
    rota ou de fazer algo super complexo. Esta rota também deve se restringir a apenas uma única página, não coloque
    duas, três ou um milhão de páginas só para fazer isso. Também não vale redirecionar a página para algum domínio
    qualquer na internet fora do `http://localhost`. Brincadeiras de mau gosto ou com conteúdo ofensivo também estão
    fora de questão. 

    Além disso, essa rota também não deve de forma alguma interferir com o funcionamento do resto do sistema. Se
    precisar de regras de CSS específicas para serem usadas aqui, crie um CSS só para ser usado aqui ao invés de
    alterar o CSS utilizado pelas demais rotas.

Observação: TODAS as funções a serem definidas no controller devem ser um tanto "burrinhas". **Nenhuma** delas deve ter
lógica complexa (se tiver, você provavelmente está fazendo algo errado). No gabarito, a mais longa delas tem apenas
oito linhas de código, contando com a linha do def e com a linha da definição da rota. Então lembre-se que a solução é
algo simples, não é pra ficar batendo a cabeça com coisa complicada.

**Todas** as funções a serem desenvolvidas no controller se resumem **no máximo** a essas quatro atividades **apenas e
nada mais além do que isso**:

1. Ler os dados recebidos no formulário, URL ou query string.
2. Chamar algum método no objeto `db` e atribuir o resultado do método a alguma variável.
3. Retornar com o `render_template` no caso de métodos GET ou o com o `redirect` no caso de métodos POST.
4. Se o passo 2 resultar em alguma exceção, retornar com o `redirect` para uma página que exiba o erro.

## Templates do Jinja2

Você também precisará editar as templates do Jinja2. Para o sistema de receitas, são essas:

1. `editar_receita.html` - Tela de edição de receita.
2. `receita.html` - Tela de visualização de receitas.
3. `listar_receitas.html` - Tela de listagem e pesquisa de receitas.
4. `base_receitas.html` - Serve de modelo para os três arquivos acima.
5. Alguma template para a rota `/nomes`.

Para o blog, as templates são essas:

1. `editar_materia.html` - Tela de edição de matéria.
2. `materia.html` - Tela de visualização de matérias.
3. `listar_materias.html` - Tela de listagem e pesquisa de matérias.
4. `base_blog.html` - Serve de modelo para os três arquivos acima.
5. Alguma template para a rota `/nomes`.

No entanto, as templates não estão na pasta `templates` do respectivo sistema. Os arquivos estáticos também não estão
na pasta `static`. Ao invés disso, tanto os arquivos estáticos quanto as templates estão misturados na pasta
`prototipos`.

Aliás, só para sacanear e ser maldoso, o professor não só misturou os templates e estáticos na mesma pasta, como também
usou a mesma pasta para misturar os arquivos dos dois sistemas diferentes! Você terá que separá-los corretamente antes
de prosseguir e jogar fora os arquivos do sistema que não te interessa.

Além disso, a forma como as templates encontram os arquivos estáticos vai acabar sendo impactada quando você separá-los
nas pastas `static` e `templates`. Lidar com isso é parte do que você tem que fazer neste AC.

Os HTMLs dados na pasta de protótipos, são, como o nome sugere, apenas protótipos sem funcionamento real. Eles estão
sem o Jinja2, e portanto não funcionarão de pronto se você os colocar na sua aplicação sem antes fazer algumas
alterações. As alterações a serem realizadas estão descritas em cada um dos HTMLs, e a quase totalidade delas consiste
em usar o Jinja2.

Você não precisa alterar os arquivos estáticos (incluindo CSS). Mas se quiser fazê-lo, fique a vontade.

# Dicas

## 1. MyPy

O Python é uma linguagem que normalmente tem tipagem dinâmica. Embora a tipagem dinâmica deixe o código mais enxuto,
legível e flexível, ela também pode retirar do programador muitas das possibilidades de se obter uma melhor verificação
automatizada de código quanto a possíveis erros de programação, coisa que a tipagem estática é capaz de proporcionar.

Por exemplo, no Python (e também em outras linguagens de programação com tipagem dinâmica), se você tentar chamar uma
função com um parâmetro a mais, com um parâmetro a menos, com um parâmetro do tipo string ao invés de inteiro, tentar
usar uma variável com um erro de digitação no nome, entre vários outros possíveis erros comuns, o erro só se
manifestará em tempo de execução. Isso acaba resultando em bugs, erros, aborrecimentos e perda de tempo que de outra
forma poderiam ser evitados. Pior ainda que por vezes esses problemas vão aparecer em tempo de execução em lugares bem
distantes do ponto onde eles se originaram ou apenas em casos especiais e incomuns.

Não existe verificação de erros em tempo de compilação 100% eficiente. No entanto, a tipagem estática é uma solução
parcial capaz de capturar uma grande quantidade de erros típicos e comuns, alertando para problemas no código em tempo
de compilação. Para incorporar este conceito ao Python, o [MyPy](http://mypy-lang.org/) foi concebido. O código aqui
disponibilizado contém anotações de tipo (por exemplo, `dict[str, int]`, `Sequence[str]`) a serem verificadas pelo
MyPy.

No entanto, aprender a usar o MyPy também não é algo fácil, simples ou rápido. Assim sendo, nenhuma pontuação na nota
será adicionada ou subtraída por conta disso. Fica aqui apenas a recomendação para quem quiser experimentá-lo. Caso
queira usar o MyPy, execute o comando `python -m mypy .\` na pasta raiz do seu código e ele já verificará todo o código
Python aqui presente. Se não quiser utilizar, apenas ignore este arquivo e codifique o seu código Python como
normalmente faria.

Caso decida utilizar o MyPy, o tipo de retorno correto para todos os métodos declarados como rotas na controller é
`Response | str`.

## 2. De repente, todos os dados que eu cadastrei sumiram!

O Flask está iniciando com o parâmetro `debug = True`. Isso permite com que quando você realizar qualquer mudança em um
arquivo Python, o Flask reinicie o servidor automaticamente. Se houver algum erro de sintaxe ou outra coisa que impeça
o controller de rodar, o servidor vai cair. Se tudo correr bem, ele vai recarregar novamente.

No entanto, como todos os dados são salvos em memória dentro de um dicionário, quando o servidor reiniciar, todos os
dados que tinham salvos serão perdidos, e é por isso que os dados que você cadastrou sumiram. No terceiro semestre
veremos como usar um banco de dados de verdade para que nada seja perdido quando o servidor cair.

Editar as templates ou os arquivos estáticos é mais seguro, e funciona sem que o Flask tenha que ser reinicializado.

# Como executar a aplicação?


1. Se estiver usando o MyPy, execute `python -m mypy .\`

2. Execute `python xxxx_controller.py`, onde `xxxx` pode ser `receitas` ou `blog`.

3. Abra no navegador o link `http://localhost:5001` se o seu sistema for o blog ou `http://localhost:5002` se for o
   livro de receitas.

# Como testar a aplicação?

1. Abra a tela principal de listagem de receitas ou matérias.

2. Clique no botão de criar uma receita ou matéria, preencha os campos e salve. Veja se a receita ou matéria criada
   apareceu corretamente na tela de listagem.
   
3. Tente criar mais outras receitas ou matérias.

4. Na tela de listagem, clique numa receita ou matéria para visualizá-la.

5. Na tela de visualização de receita ou visualização de matéria, clique no botão de editar, edite os dados e
   certifique-se de que a edição funcionou.
   
6. Na tela de edição de receita ou de edição de matéria, clique no botão de exclusão e certifique-se de que ela se foi.

7. Tente criar uma receita ou uma matéria deixando alguns dos campos obrigatórios em branco ou preenchidos apenas com
   espaços.
   
8. Tente criar uma receita ou uma matéria com o link de uma imagem inválida.

9. Tente alterar uma receita ou uma matéria colocando campos em branco ou imagem inválida.

10. Teste todos os botões "Voltar".

11. Pesquise por uma receita ou matéria e certifique-se de que todos os resultados desejados apareceram e nada mais
    além do que deles.
    
12. Pesquise por algum texto que não exista em nenhuma receita ou matéria.

13. Tente acessar a URL de visualização de receita ou matéria usando um código inexistente. Teste tanto códigos
    numéricos quanto não numéricos.
    
14. Tente acessar a URL de edição de receita ou matéria usando um código inexistente. Teste tanto códigos numéricos
    quanto não numéricos.
    
15. Na tela de edição de receita ou matéria, manipule a URL dos formulários com um código inexiste e tente salvar ou
    excluir a receita ou matéria.
    
16. Tente fazer POST onde só pode GET ou GET onde só pode POST.

17. Abra a tela de edição de uma receita ou matéria em duas abas diferentes do navegador e edite-as de formas
    divergentes.
    
18. Abra a tela de edição de uma receita ou matéria em duas abas diferentes do navegador, exclua na primeira aba e
    salve na segunda.
    
19. Tente bolar outros testes bisonhos que podem acontecer quando você abrir a mesma receita ou matéria em duas abas
    diferentes do navegador.
    
20. Certifique-se de que o seu HTML e o seu CSS nunca têm erros.

21. Não se esqueça de testar a rota `/nomes`.

22. Você verificou se o título da página e o ícone estão corretos em todos os casos?

23. Você verificou se as mensagens de sucesso aparecem na tela de listagem quando você cria ou edita uma receita ou
    matéria?
    
24. Quando você provoca um erro (provavelmente código inexistente), você viu se a mensagem de erro apareceu na tela de
    listagem?
    
25. Você observou o Flask mostrando alguma tela de erro inesperada?

26. Se você criar um formulário para POST para alguma de suas rota e enviar os dados com algum campo a mais ou a menos,
    como o seu código da controller reage?

O ideal seria que houvesse uma forma automatizada de testar tudo isso, mas no entanto, **ainda** não há. Para quebrar o
galho, o script `teste_basico.py` na pasta `teste-basico` pode ser usado para agilizar o processo, que embora ainda vá
continuar a ser manual, será bem mais fácil e rápido de ser executado.

# Como fica a nota?

Há oito rotas especificadas no controller. As sete primeiras valem 0,7 pontos cada. E nisso conta definir a rota
corretamente, definir a função corretamente e implementá-la corretamente de acordo com o especificado para cada uma
delas.

A template de listagem, de visualização e de cadastro, valem 1,2 pontos cada. Incorporar a template de base nelas
corretamente também vale como parte destes pontos. Obviamente que a correta transformação do protótipo em uma template
é o que mais conta na pontuação daqui.

A rota `/nomes` e a template correspondente a ela vale 1,0 ponto.

0,5 pontos são atribuídos para quem fizer a entrega corretamente.

Totalizando:

```python
assert 7 * 0.7 + 3 * 1.2 + 1 + 0.5 == 10
```

Pontos podem ser descontados por quebrar coisas que estavam funcionando, mexer onde não precisava ser mexido, bagunçar
a estrutura de diretórios do projeto, acrescentar arquivos desnecessários no entregável ou misturar arquivos dos dois
sistemas numa coisa só.

# Como realizar a entrega?

Na pasta do sistema que você escolheu implementar (receitas ou blog), crie um arquivo ZIP e coloque dentro dele a pasta
`templates`, a pasta `static`, a pasta `model` e o arquivo da controller.

Não inclua a pasta `prototipos`. Também tome cuidado para não misturar arquivos de um sistema no outro. Não inclua
também este enunciado e nem nada da pasta `teste-basico`.

Também não inclua as pastas `__pycache__` ou `.mypy_cache`, ou o arquivo `mypy.ini`.

Lembre-se que ZIP não é RAR e que RAR não é ZIP.