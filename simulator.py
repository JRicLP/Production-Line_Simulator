import streamlit as st
from time import sleep
from production_line import ProductionLine 
from product import Product
from stack import Stack

#Configuração inicial da página
st.set_page_config(
    page_title="Simulador de Linha de Produção",
    page_icon="🏭",
    layout="wide"
)

#Link do Sprite que está sendo usado para representar o produto (É uma caixa de madeira)
PRODUCT_SPRITE_URL = "https://opengameart.org/sites/default/files/RTS_Crate_0.png"


#Inicialização da Lógica (usando o Session State)
if 'fabrica' not in st.session_state:
    etapas = ["Corte", "Montagem", "Pintura", "Teste de Qualidade"]
    st.session_state.fabrica = ProductionLine(steps=etapas)

#Barra Lateral com a Busca
st.sidebar.header("⚙️ Ferramentas")
st.sidebar.divider()
st.sidebar.subheader("🔎 Buscar Produto no Estoque")

#Campo para o usuário possa digitar o número de série do produto
search_id = st.sidebar.number_input(
    "Digite o Nº de Série:", 
    min_value=1, 
    step=1,
    key="search_id_input" #Aqui é só uma chave para limpar o campo depois
)

#Botão para iniciar a busca
if st.sidebar.button("Buscar", key="search_button"):
    produto_encontrado = st.session_state.fabrica.find_finished_product(search_id)
    #Aqui, basicamente o produto é armazenado em uma variável para ser retornado na exibição
    st.session_state.produto_encontrado = produto_encontrado
    st.session_state.id_buscado = search_id

#Exibe o resultado da busca, se houver um produto que sera coerente com o que foi buscado
if 'produto_encontrado' in st.session_state:
    if st.session_state.produto_encontrado:
        st.sidebar.success(f"✅ Produto {st.session_state.id_buscado} encontrado!")
        with st.sidebar.expander("Ver detalhes do produto"):
            st.write(f"**Nº de Série:** {st.session_state.produto_encontrado.serial_number}")
            st.write(f"**Etapa Final:** {st.session_state.produto_encontrado.current_step}")
            st.write("**Histórico de Etapas:**")
            st.text(st.session_state.produto_encontrado.step_history)
    else:
        st.sidebar.error(f"❌ Produto {st.session_state.id_buscado} não encontrado no estoque.")


#Conteúdo Principal da Interface Inicial
st.title("🏭 Simulador de Linha de Produção")
st.markdown("Use os botões abaixo para controlar a simulação.")

#Controles da Simulação - São os botões de controle dos processos
col1, col2, _ = st.columns([1, 1, 3])

with col1:
    if st.button("Adicionar Novo Produto", use_container_width=True, type="primary"):
        st.session_state.fabrica.add_new_product()
        st.success("Novo produto adicionado à linha!")
        sleep(0.5) 
        st.rerun()

with col2:
    if st.button("Processar Próxima Etapa", use_container_width=True):
        st.session_state.fabrica.line_process()
        st.rerun()

#Aqui, basicamente conseguimos isualizar o status da fábrica, em relação aos produtos em produção e os finalizados
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
    
    #Botão para executar o método de ordenação
    if st.button("Ordenar por Nº de Série", key="sort_button"):
        st.session_state.fabrica.sort_finished_products()
        st.success("Estoque ordenado!")
        sleep(0.5)
        st.rerun()

    if not st.session_state.fabrica.finished_products:
        st.info("Nenhum produto finalizado.")
    else:
        #Exibição dos produtos finalizados
        for produto in st.session_state.fabrica.finished_products:
            col_img, col_info = st.columns([1, 5])
            with col_img:
                st.image(PRODUCT_SPRITE_URL, width=60)
            with col_info:
                st.markdown(f"**Produto Nº {produto.serial_number}**")
                st.markdown(f"`{produto.current_step}`")
            st.divider()