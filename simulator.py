# Arquivo: simulador_streamlit.py (Versão 2.0 com novas funcionalidades)

import streamlit as st
from time import sleep

# Importa as nossas classes de lógica
from production_line import ProductionLine 
from product import Product
from stack import Stack

# --- Configuração da Página ---
st.set_page_config(
    page_title="Simulador de Linha de Produção",
    page_icon="🏭",
    layout="wide"
)

# --- URL do Sprite (FEATURE 3) ---
# Você pode trocar esta URL por qualquer outra imagem de uma caixa ou produto.
# Recomendo imagens .png com fundo transparente.
PRODUCT_SPRITE_URL = "https://opengameart.org/sites/default/files/RTS_Crate_0.png"


# --- Inicialização da Lógica (usando o Session State) ---
if 'fabrica' not in st.session_state:
    etapas = ["Corte", "Montagem", "Pintura", "Teste de Qualidade"]
    st.session_state.fabrica = ProductionLine(steps=etapas)

# --- Barra Lateral com a Busca (FEATURE 2) ---
st.sidebar.header("⚙️ Ferramentas")
st.sidebar.divider()
st.sidebar.subheader("🔎 Buscar Produto no Estoque")

# Campo para o usuário digitar o número de série
search_id = st.sidebar.number_input(
    "Digite o Nº de Série:", 
    min_value=1, 
    step=1,
    key="search_id_input" # Adiciona uma chave para limpar o campo depois
)

# Botão para iniciar a busca
if st.sidebar.button("Buscar", key="search_button"):
    # Chama o novo método que criamos na classe ProductionLine
    produto_encontrado = st.session_state.fabrica.find_finished_product(search_id)
    
    # Guarda o resultado na memória da sessão para exibi-lo
    st.session_state.produto_encontrado = produto_encontrado
    st.session_state.id_buscado = search_id

# Exibe o resultado da busca, se houver um
if 'produto_encontrado' in st.session_state:
    if st.session_state.produto_encontrado:
        st.sidebar.success(f"✅ Produto {st.session_state.id_buscado} encontrado!")
        # Usamos st.expander para não poluir a barra lateral com muita informação
        with st.sidebar.expander("Ver detalhes do produto"):
            st.write(f"**Nº de Série:** {st.session_state.produto_encontrado.serial_number}")
            st.write(f"**Etapa Final:** {st.session_state.produto_encontrado.current_step}")
            # Aqui mostramos o poder da nossa Pilha de histórico!
            st.write("**Histórico de Etapas:**")
            st.text(st.session_state.produto_encontrado.step_history)
    else:
        st.sidebar.error(f"❌ Produto {st.session_state.id_buscado} não encontrado no estoque.")


# --- Conteúdo Principal ---
st.title("🏭 Simulador de Linha de Produção")
st.markdown("Use os botões abaixo para controlar a simulação.")

# --- Controles da Simulação ---
col1, col2, _ = st.columns([1, 1, 3]) # Adicionamos um espaçador

with col1:
    if st.button("Adicionar Novo Produto", use_container_width=True, type="primary"):
        st.session_state.fabrica.add_new_product()
        st.success("Novo produto adicionado à linha!")
        sleep(0.5) # Pequena pausa para o usuário ver a mensagem de sucesso
        st.rerun() # Força a re-execução para atualizar a tela

with col2:
    if st.button("Processar Próxima Etapa", use_container_width=True):
        st.session_state.fabrica.line_process()
        st.rerun()

# --- Visualização do Status da Fábrica ---
st.divider()
col_andamento, col_finalizados = st.columns(2)

with col_andamento:
    st.header(f"🏃 Em Produção ({len(st.session_state.fabrica.products_in_progress)})")
    if not st.session_state.fabrica.products_in_progress:
        st.info("Nenhum produto na linha de produção.")
    else:
        for produto in st.session_state.fabrica.products_in_progress.values():
            st.markdown(f"- **Produto Nº {produto.serial_number}**: `{produto.current_step}`")

with col_finalizados:
    st.header(f"✅ Estoque Final ({len(st.session_state.fabrica.finished_products)})")
    
    # --- Botão de Ordenação (FEATURE 1) ---
    if st.button("Ordenar por Nº de Série", key="sort_button"):
        st.session_state.fabrica.sort_finished_products()
        st.success("Estoque ordenado!")
        sleep(0.5)
        st.rerun()

    if not st.session_state.fabrica.finished_products:
        st.info("Nenhum produto finalizado.")
    else:
        # --- Exibição com Sprites (FEATURE 3) ---
        for produto in st.session_state.fabrica.finished_products:
            # Criamos duas colunas para cada item: uma para a imagem, outra para o texto
            col_img, col_info = st.columns([1, 5])
            with col_img:
                st.image(PRODUCT_SPRITE_URL, width=60) # Exibe o sprite
            with col_info:
                st.markdown(f"**Produto Nº {produto.serial_number}**")
                st.markdown(f"`{produto.current_step}`")
            st.divider()