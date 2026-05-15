## 📋 Descrição das Resoluções

### Exercício 1: Identificador de Pares e Ímpares

* **O que faz:** Percorre números de 0 a 100.
* **Lógica:** Utiliza o laço `for` com o operador de módulo `%`. Se o resto da divisão por 2 for zero, o número é classificado como par; caso contrário, ímpar.

### Exercício 2: Comparativo de Magnitude

* **O que faz:** Lê três números e identifica o maior e o menor.
* **Lógica:** Os números são armazenados em uma lista e ordenados com o método `.sort()`. O menor valor é acessado pelo índice `[0]` e o maior pelo último índice `[2]`.

### Exercício 3: Nome em Escada

* **O que faz:** Imprime o nome do usuário de forma progressiva (letra por letra).
* **Lógica:** Cria-se uma variável acumuladora de texto. A cada iteração do `for`, uma nova letra do nome é adicionada e impressa, gerando o efeito visual de escada.

### Exercício 4: Sequência de Fibonacci

* **O que faz:** Gera a sequência de Fibonacci até o n-ésimo termo definido pelo usuário.
* **Lógica:** Utiliza um laço `while` e a técnica de atribuição múltipla do Python (`a, b = b, a + b`) para atualizar os termos da sequência de forma eficiente.

### Exercício 5: Validação de Dados Cadastrais

* **O que faz:** Garante que informações como nome, idade, salário e estado civil sigam regras específicas.
* **Lógica:** Aplica laços `while` individuais para cada campo. O programa "prende" o usuário em um loop de entrada até que os dados inseridos satisfaçam os critérios de validação (ex: `len(nome) > 3`).

### Exercício 6: Verificador de Números Primos

* **O que faz:** Determina se um número é divisível apenas por 1 e por ele mesmo.
* **Lógica:** Um laço `for` conta quantos divisores o número possui no intervalo de 1 até ele mesmo. Se o contador final for igual a 2, o número é confirmado como primo.

### Exercício 7: Cálculo de Fatorial

* **O que faz:** Calcula o produto de todos os números inteiros positivos de 1 até $n$.
* **Lógica:** Utiliza um acumulador multiplicativo (`fatorial = 1`) dentro de um laço `for` que percorre o intervalo do número desejado.

### Exercício 8: Análise de Listas

* **O que faz:** Extrai estatísticas de uma lista numérica pré-definida.
* **Lógica:** Demonstra o poder das funções nativas do Python: `len()` para tamanho, `min()` e `max()` para extremos, `sum()` para somatório e `sorted()` para ordenação crescente e decrescente.

### Exercício 9: Estruturação de Dados (Dicionário)

* **O que faz:** Transpõe dados tabulares para um formato de objeto (dicionário).
* **Lógica:** Utiliza o formato chave-valor para representar um cardápio, facilitando a busca e organização de informações. Foi utilizado o módulo `pprint` para uma visualização mais organizada no console.

### Exercício 10: Controle de Acesso

* **O que faz:** Simula um sistema de login que libera acesso apenas com a senha "676767".
* **Lógica:** Um laço `while` que valida a entrada do usuário contra um valor fixo, repetindo a solicitação em caso de erro.

### Exercício 11: Tabuada Dinâmica

* **O que faz:** Gera a tabuada de 1 a 10 para um número escolhido.
* **Lógica:** Primeiro, valida se o número está entre 1 e 10 com `while`. Em seguida, utiliza um `for` para realizar as dez multiplicações e exibir os resultados formatados.
