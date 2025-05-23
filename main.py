import flet as ft
import csv
import os
import shutil

ARQUIVO = "audi_carros.csv"
PASTA_IMAGENS = "imagens"

if not os.path.exists(PASTA_IMAGENS):
    os.makedirs(PASTA_IMAGENS)

def carregar_carros():
    carros = []
    if os.path.exists(ARQUIVO):
        with open(ARQUIVO, newline='', encoding='utf-8') as f:
            reader = csv.reader(f)
            for row in reader:
                if row and len(row) == 5:  # Adicionando uma coluna para a foto
                    carros.append({
                        "modelo": row[0],
                        "ano": row[1],
                        "especificacao": row[2],
                        "km": row[3],
                        "foto": row[4]  # Caminho da imagem
                    })
    return carros

def salvar_carros(carros):
    with open(ARQUIVO, "w", newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        for carro in carros:
            writer.writerow([carro["modelo"], carro["ano"], carro["especificacao"], carro["km"], carro["foto"]])

def main(page: ft.Page):
    page.title = "Cadastro de Carros Audi"
    page.scroll = "auto"

    carros = carregar_carros()
    editando_indice = [None]
    foto_atual = [None]  # Variável para armazenar a imagem selecionada

    modelo_input = ft.TextField(label="Modelo Audi", width=300)
    ano_input = ft.TextField(label="Ano", width=150)
    especificacao_input = ft.TextField(label="Especificação Técnica", width=400)
    km_input = ft.TextField(label="Quilometragem", width=200)
    
    # Componente FilePicker invisível, que será acionado pelo botão
    foto_input = ft.FilePicker(on_result=lambda e: escolher_foto(e))
    page.overlay.append(foto_input)  # Adiciona o FilePicker à página

    foto_preview = ft.Image(width=200, height=120)  # Pré-visualização da foto
    output = ft.Column()
    botao_salvar = ft.ElevatedButton("Adicionar", on_click=lambda e: adicionar_ou_editar_carro())

    # Botão para abrir o explorador de arquivos
    botao_foto = ft.ElevatedButton("Selecionar Foto", on_click=lambda e: foto_input.pick_files())

    def atualizar_lista():
        output.controls.clear()
        for i, carro in enumerate(carros):
            # Exibe a foto apenas se houver uma
            if carro["foto"]:
                img = ft.Image(src=carro["foto"], width=100, height=60)
            else:
                img = ft.Text("Sem foto", size=14)
            
            output.controls.append(
                ft.Column([
                    ft.Text(f"{i + 1}. Audi {carro['modelo']} ({carro['ano']})"),
                    ft.Text(f"🔧 {carro['especificacao']} | 🚗 {carro['km']}"),
                    img,  # Exibe a imagem ou texto "Sem foto"
                    ft.Row([
                        ft.IconButton(icon=ft.Icons.EDIT, tooltip="Editar", on_click=lambda e, i=i: iniciar_edicao(i)),
                        ft.IconButton(icon=ft.Icons.DELETE, tooltip="Remover", on_click=lambda e, i=i: remover_carro(i)),
                    ])
                ])
            )
        page.update()

    def adicionar_ou_editar_carro():
        modelo = modelo_input.value.strip()
        ano = ano_input.value.strip()
        especificacao = especificacao_input.value.strip()
        km = km_input.value.strip()

        if modelo and ano.isdigit() and especificacao and km:
            novo_carro = {
                "modelo": modelo,
                "ano": ano,
                "especificacao": especificacao,
                "km": km,
                "foto": foto_atual[0] if foto_atual[0] else ""  # Salvando o caminho da foto
            }

            if editando_indice[0] is None:
                carros.append(novo_carro)
            else:
                carros[editando_indice[0]] = novo_carro
                editando_indice[0] = None
                botao_salvar.text = "Adicionar"

            salvar_carros(carros)
            limpar_campos()
            atualizar_lista()
        else:
            page.snack_bar = ft.SnackBar(ft.Text("Preencha todos os campos corretamente."))
            page.snack_bar.open = True
            page.update()

    def escolher_foto(event):
        # Função para selecionar e mover a foto para a pasta de imagens
        if event.files:
            foto_nome = event.files[0].name
            caminho_foto = os.path.join(PASTA_IMAGENS, foto_nome)
            shutil.copy(event.files[0].path, caminho_foto)
            foto_atual[0] = caminho_foto
            foto_preview.src = caminho_foto  # Atualiza a imagem com o caminho da foto
            foto_preview.visible = True  # Garante que a imagem será visível
            page.update()

    def iniciar_edicao(index):
        carro = carros[index]
        modelo_input.value = carro["modelo"]
        ano_input.value = carro["ano"]
        especificacao_input.value = carro["especificacao"]
        km_input.value = carro["km"]
        foto_atual[0] = carro["foto"]
        
        if carro["foto"]:  # Se houver foto, exibe a imagem
            foto_preview.src = carro["foto"]
            foto_preview.visible = True
        else:
            foto_preview.visible = False  # Se não houver foto, não exibe nada

        botao_salvar.text = "Salvar Alteração"
        editando_indice[0] = index
        page.update()

    def remover_carro(index):
        if 0 <= index < len(carros):
            del carros[index]
            salvar_carros(carros)
            if editando_indice[0] == index:
                limpar_campos()
                botao_salvar.text = "Adicionar"
                editando_indice[0] = None
            atualizar_lista()

    def limpar_campos():
        modelo_input.value = ""
        ano_input.value = ""
        especificacao_input.value = ""
        km_input.value = ""
        foto_atual[0] = None
        foto_preview.src = ""
        foto_preview.visible = False  # Esconde a foto quando limpa os campos
        page.update()

    page.add(
        ft.Text("Cadastro de Carros da Audi", size=24, weight="bold"),
        modelo_input,
        ano_input,
        especificacao_input,
        km_input,
        botao_foto,  # Botão para abrir o explorador de arquivos
        foto_preview,  # Exibição da imagem carregada
        botao_salvar,
        ft.Divider(),
        ft.Text("Lista de Carros Cadastrados:", size=18),
        output
    )

    atualizar_lista()

ft.app(target=main)