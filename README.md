# 🚗 Cadastro de Carros Audi

Este é um aplicativo desktop simples feito com [Flet](https://flet.dev) em Python para cadastrar, visualizar, editar e remover informações de carros da marca **Audi**, incluindo a foto de cada veículo.

## 📚 Sobre o Projeto

Este projeto foi desenvolvido como uma **atividade acadêmica**. Os autores do trabalho são:

- **Juan Pedro**
- **Matheus Barros**

## 📸 Funcionalidades

- Cadastro de modelos da Audi com:
  - Modelo
  - Ano
  - Especificações Técnicas
  - Quilometragem
  - Foto do carro
- Edição e remoção de carros já cadastrados.
- Armazenamento persistente em arquivo CSV.
- Visualização das fotos dos veículos cadastrados.

## 🧰 Tecnologias Utilizadas

- [Python 3.10+](https://www.python.org/)
- [Flet](https://flet.dev) - Biblioteca para criar UIs com Python
- Manipulação de arquivos CSV e imagens com bibliotecas padrão (`csv`, `os`, `shutil`)

## 📁 Estrutura de Arquivos

```
📁 projeto/
├── imagens/               # Pasta onde as fotos dos carros são salvas
├── audi_carros.csv        # Arquivo onde os dados dos carros são armazenados
└── main.py                # Código principal do aplicativo
```

## ▶️ Como Executar

1. **Clone o repositório:**

```bash
git clone https://github.com/juanpfr/WebMotors-Audi
cd cadastro-audi
```

2. **Crie um ambiente virtual e ative (opcional, mas recomendado):**

```bash
python -m venv venv
# No Windows:
venv\Scripts\activate
# No macOS/Linux:
source venv/bin/activate
```

3. **Instale as dependências:**

```bash
pip install -r requirements.txt
```

4. **Execute o aplicativo:**

```bash
python main.py
```

O aplicativo abrirá em uma nova janela com a interface gráfica.

## 📝 Observações

- As imagens dos carros são copiadas para a pasta `imagens/` ao serem selecionadas.
- O arquivo `audi_carros.csv` será criado automaticamente se não existir.
- É importante ter permissão de escrita na pasta onde o projeto está rodando.

## 📷 Exemplo da Interface

*(Insira aqui um screenshot do app rodando com carros cadastrados)*

---

## 🛠️ Contribuição

Sinta-se à vontade para abrir *issues* ou enviar *pull requests* com melhorias e correções!

---

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.
