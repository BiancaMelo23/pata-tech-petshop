# Pata Tech - Sistema para Pet Shop

Projeto desenvolvido em grupo para a disciplina **Produto de Software: Análise, Especificação, Projeto e Implementação** da faculdade. A ideia do sistema é facilitar o dia a dia de um pet shop, organizando o cadastro de clientes, animais de estimação, estoque e o agendamento de serviços.

## O que o sistema faz

- **Cadastros gerais:** Permite cadastrar, editar, visualizar e excluir (CRUD) clientes, animais de estimação, produtos do estoque e serviços.
- **Agendamento de serviços:** Módulo para marcar atendimentos com data, hora e valor financeiro, ligando cada serviço diretamente ao pet cadastrado no banco de dados (usando chave estrangeira).
- **Acompanhamento visual:** Tabela responsiva na tela com etiquetas de status (como "Pendente" ou "Concluído") que mudam de cor automaticamente usando Jinja2 conforme o serviço é atualizado, além de dashboard com confirmação e opção de desfazer conclusão.

## Tecnologias utilizadas ✅

- Python (Flask)
- Banco de dados MySQL
- HTML e CSS
- Jinja2

## Diagramas UML

### Diagrama de Classes
Representa a estrutura das entidades do sistema (como tutores, animais de estimação e agendamentos), seus atributos, relacionamentos e chaves estrangeiras.

![Diagrama de Classes](Imagens-diagramas/Diagramas%20de%20Classes%20Pata%20Tech%20Petshop.drawio.png)

### Diagrama de Caso de Uso
Mostra as principais interações do usuário com o sistema, como gerenciar pets e tutores, gerenciar agendamentos e visualizar o dashboard com conclusão de serviços.

![Diagrama de Caso de Uso](Imagens-diagramas/Diagrama%20de%20Caso%20de%20Uso%20Pata%20Tech%20Petshop.drawio.png)

## Como rodar o projeto na sua máquina

1. Baixe o repositório:
   ```bash
   git clone [https://github.com/BiancaMelo23/pata-tech-petshop.git](https://github.com/BiancaMelo23/pata-tech-petshop.git)

2. Entre na pasta do projeto:
   ```bash
   cd pata-tech-petshop
   ```

3. Instale as dependências:
   ```bash
   pip install -r requisitos.txt
   ```

4. Configure a conexão com o seu banco de dados MySQL local.

5. Inicie o sistema:
   ```bash
   python app.py
   ```

## Integrantes do grupo

* Bianca de Melo Silva
* Cindy Louise Alves dos Santos
* Natã Gomes da Silva
