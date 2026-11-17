# Pata Tech - Sistema para Pet Shop

Projeto desenvolvido em grupo para a disciplina *Software Product: Analysis, Specification, Project e Implementation* da faculdade. A ideia do sistema é facilitar o dia a dia de um pet shop, organizando o cadastro de clientes, pets, estoque e o agendamento de serviços.

## O que o sistema faz

* **Cadastros gerais:** Permite cadastrar, editar, visualizar e excluir (CRUD) clientes, pets, produtos do estoque e serviços.
* **Agendamento de serviços:** Módulo para marcar atendimentos com data, hora e valor financeiro, ligando cada serviço diretamente ao pet cadastrado no banco de dados (usando chave estrangeira).
* **Acompanhamento visual:** Tabela responsiva na tela com etiquetas de status (como "Pendente" ou "Concluído") que mudam de cor automaticamente usando Jinja2 conforme o serviço é atualizado.

## Tecnologias usadas

* Python (Flask)
* Banco de dados MySQL
* HTML e CSS
* Jinja2

## Como rodar o projeto na sua máquina

1. Baixe o repositório:
   ```bash
   git clone [https://github.com/BiancaMelo23/pata-tech-petshop.git](https://github.com/BiancaMelo23/pata-tech-petshop.git)
   ```

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
