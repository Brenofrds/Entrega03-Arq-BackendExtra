# Template Method - Quiz de Preferências

## Participações

| Nome                                 |
|--------------------------------------|
| [Breno Soares Fernandes](https://github.com/brenofrds) |
| [Bruno Ricardo de Menezes](https://github.com/EhOBruno) |

---

## Introdução

O padrão de projeto **Template Method**, pertencente à categoria comportamental dos GoF, define o esqueleto de um algoritmo em uma superclasse, permitindo que subclasses personalizem partes do processo sem alterar sua estrutura geral.

Neste projeto, aplicamos o padrão para estruturar o fluxo do **quiz de preferências do aniversariante**, mantendo a sequência de execução fixa, mas permitindo personalizar como as perguntas são feitas e como as preferências são salvas.

---

## Objetivo

Nosso objetivo foi utilizar o Template Method para padronizar o processo de coleta e salvamento das preferências dos usuários, garantindo consistência no fluxo e flexibilidade para adaptar o comportamento de acordo com o ambiente (terminal, web, etc.).

A superclasse `QuizTemplate` define o esqueleto da execução do quiz. Já a subclasse `QuizPreferenciasTerminal` implementa a lógica concreta para ambientes de terminal, sendo possível no futuro criar subclasses para outros contextos (ex: interface gráfica ou chatbot).

---

## Metodologia

A implementação foi realizada em Python, estruturando o quiz em duas classes principais:

- `QuizTemplate` (abstrata): define o método `executar_quiz()`, que encapsula o fluxo comum:
  1. `boas_vindas()`
  2. `fazer_perguntas()`
  3. `salvar_preferencias()`
  4. `finalizar()`

- `QuizPreferenciasTerminal`: especialização concreta que:
  - Exibe perguntas no terminal com listas de opções.
  - Permite múltiplas seleções por categoria (lugares, comidas, músicas).
  - Salva os dados no dicionário do usuário.

Com isso, o código ficou modular, fácil de extender, e aderente ao princípio do "aberto para extensão, fechado para modificação" (OCP do SOLID).

---

## Diagrama UML (Template Method)

> *(Inserir imagem do diagrama aqui, caso tenha sido feito)*  
> Exemplo:  
> ![Diagrama Template Method](./assets/template_method/diagrama_template.png)

---

## Código

### Superclasse Abstrata

```python
from abc import ABC, abstractmethod

class QuizTemplate(ABC):
    def executar_quiz(self, usuario):
        self.boas_vindas()
        respostas = self.fazer_perguntas()
        self.salvar_preferencias(usuario, respostas)
        self.finalizar()

    def boas_vindas(self):
        print("\n🎉 Bem-vindo ao quiz de preferências para sua festa!")

    @abstractmethod
    def fazer_perguntas(self):
        pass

    @abstractmethod
    def salvar_preferencias(self, usuario, respostas):
        pass

    def finalizar(self):
        print("✅ Preferências salvas com sucesso!\n")
```

### Subclasse: Terminal

```
from .base_quiz import QuizTemplate

class QuizPreferenciasTerminal(QuizTemplate):
    def fazer_perguntas(self):
        perguntas = {
            "lugares": [
                "Praia", "Campo", "Parque", "Cinema", "Boate", "Restaurante", "Casa de amigos",
                "Clube", "Cobertura com vista", "Chácara", "Balada temática", "Piquenique no parque"
            ],
            "comidas": [
                "Pizza", "Churrasco", "Sushi", "Hambúrguer", "Tábua de frios", "Docinhos de festa",
                "Espetinhos", "Massas (lasanha, macarronada)", "Comida mexicana", "Cachorro-quente",
                "Salgadinhos variados", "Sorvete e milk-shake"
            ],
            "musicas": [
                "Sertanejo", "Rock", "Funk", "MPB", "Pop", "Eletrônica", "Axé", "Pagode",
                "Brega funk", "Trap", "Forró", "K-pop", "Anos 2000", "Reggaeton"
            ]
        }

        respostas = {}

        for categoria, opcoes in perguntas.items():
            print(f"\n{categoria.capitalize()} que você gostaria no seu aniversário:")
            for i, opcao in enumerate(opcoes, 1):
                print(f"{i}. {opcao}")
            entrada = input("Escolha os números separados por vírgula: ")
            selecionados = [opcoes[int(i.strip()) - 1] for i in entrada.split(",") if i.strip().isdigit()]
            respostas[categoria] = selecionados

        return respostas

    def salvar_preferencias(self, usuario, respostas):
        usuario["preferencias"] = respostas
```

## Saída

Exemplo de execução do quiz no terminal:

```python
🎉 Bem-vindo ao quiz de preferências para sua festa!

Lugares que você gostaria no seu aniversário:
1. Praia
2. Campo
3. Parque
...
Escolha os números separados por vírgula: 1,4,7

...

