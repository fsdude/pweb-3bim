# pweb-3bim
Projeto do terceiro bimestre de PWEB para gerenciar provas

# como django atua
No arquivo MODELS.py está escrito o código para criar as tabelas e campos do banco de dados e no FORMS.py está o de criar formulários, que tem campos iguais aos do MODELS.

O conteúdo exibido nas páginas saem do arquivo VIEWS.py, o qual é responsável pelo processamento dos dados recebidos (métodos POST/GET). É nele que é definido com qual template (onde o conteúdo será exibido) a página vai ser renderizada.

As VIEWS são chamadas pelas urls acessadas definidas no URLS.py. Com regex é possível determinar os padrões de acesso as páginas e trabalhar com o dados passados pelas urls também.

# passo-a-passo de um exemplo

url - fsdude.pythonanywhere.com/add (chama view SubmitView)

- SubmitView tem duas funções declaradas: get e get_context_data

- A primeira (executada primariamente também) renderizará os formulários de submissão de dados

- A segunda passará conteúdo (valor dos dados) para o template 'submeter.html'

 O template 'submeter.html' com uso de operações lógicas (html liquid é a linguagem usada que permite isso) vai exibir o conteúdo passado na página.
 Se o usuário inserir dados nos formulários exibidos pelo template, vai ocorrer outra requisição para a view definida no action do formulário, que por sua vez processará o código, retornará o render, dados para o template... e assim por diante.