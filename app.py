
import streamlit as st

st.set_page_config(
    page_title="Controle de Estoque",
    page_icon="📦"
)

if "produtos" not in st.session_state:
    st.session_state.produtos = {}

st.title("📦 Controle de Estoque")
st.write("Sistema de controle de produtos para mercearias.")

opcao = st.sidebar.radio(
    "Menu principal",
    ["Cadastrar produto", "Consultar estoque", "Atualizar estoque"]
)

if opcao == "Cadastrar produto":
    st.header("Cadastrar produto")

    nome = st.text_input("Nome do produto").strip().lower()
    quantidade = st.number_input(
        "Quantidade em estoque",
        min_value=1,
        step=1
    )

    if st.button("Cadastrar"):
        if not nome:
            st.error("Informe o nome do produto.")
        elif nome in st.session_state.produtos:
            st.warning("Esse produto já está cadastrado.")
        else:
            st.session_state.produtos[nome] = quantidade
            st.success("Produto cadastrado com sucesso!")

elif opcao == "Consultar estoque":
    st.header("Estoque atual")

    if st.session_state.produtos:
        for nome, quantidade in st.session_state.produtos.items():
            st.write(f"**{nome}**: {quantidade} unidade(s)")
    else:
        st.info("Nenhum produto cadastrado.")

elif opcao == "Atualizar estoque":
    st.header("Atualizar estoque")

    if st.session_state.produtos:
        nome = st.selectbox(
            "Selecione o produto",
            list(st.session_state.produtos.keys())
        )

        quantidade = st.number_input(
            "Nova quantidade",
            min_value=1,
            step=1
        )

        if st.button("Atualizar"):
            st.session_state.produtos[nome] = quantidade
            st.success("Estoque atualizado com sucesso!")
    else:
        st.info("Cadastre um produto antes de atualizar.")
