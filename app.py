import streamlit as st
import streamlit.components.v1 as components

# --- Configuração da Página ---
st.set_page_config(page_title="Calculadora de Preços | Hub", layout="centered")

# --- Título e Subtítulo ---
st.title("Calculadora de Preços para Eventos")
st.markdown("Uma ferramenta do **Encontro D'Água Hub** 💧")
st.markdown("Calcule preços justos para seus produtos e serviços de festas e eventos.")

# --- 1. Materiais ---
st.header("1. Custo de Materiais")
materiais = []

# Loop principal para os 3 primeiros materiais
for i in range(1, 4):
    nome = st.text_input(f"Material {i}", key=f"nome_{i}")
    preco = st.number_input(f"Valor pago por {nome} (R$)", min_value=0.0, key=f"preco_{i}")
    porcentagem = st.slider(f"Porcentagem usada (%)", 0, 100, 0, key=f"porcentagem_{i}")
    
    if nome and preco > 0 and porcentagem > 0:
        custo = (porcentagem / 100) * preco
        materiais.append((nome, custo))

# Expander para mais materiais (até 10)
with st.expander("➕ Adicionar mais materiais"):
    for i in range(4, 11):
        nome = st.text_input(f"Material {i}", key=f"nome_{i}")
        preco = st.number_input(f"Valor pago por {nome} (R$)", min_value=0.0, key=f"preco_{i}")
        porcentagem = st.slider(f"Porcentagem usada (%)", 0, 100, 0, key=f"porcentagem_{i}")
        
        if nome and preco > 0 and porcentagem > 0:
            custo = (porcentagem / 100) * preco
            materiais.append((nome, custo))

# --- 2. Tempo, Produção e Transporte ---
st.header("2. Tempo, Produção e Transporte")

col1, col2 = st.columns(2)
with col1:
    tempo_total = st.number_input("Tempo total (minutos) *Ex: 60*", min_value=1)
    qtd_total = st.number_input("Quantidade total produzida *Ex: 50*", min_value=1)
with col2:
    tempo_valor_hora = st.number_input("Quanto vale sua hora (R$) *Ex: 25*", min_value=0.0)
    transporte_total = st.number_input("Custo total com transporte (R$)", min_value=0.0)

# Cálculos de tempo e transporte
tempo_valor_minuto = tempo_valor_hora / 60
tempo_por_unidade = tempo_total / qtd_total
transporte_por_unidade = transporte_total / qtd_total

# --- 3. Embalagem e Lucro ---
st.header("3. Embalagem e Lucro")

col3, col4 = st.columns(2)
with col3:
    embalagem_total = st.number_input("Custo total com embalagens (R$)", min_value=0.0)
with col4:
    lucro = st.slider("Margem de lucro desejada (%)", 0, 200, 30)

embalagem_por_unidade = embalagem_total / qtd_total

# --- Botão de Cálculo ---
if st.button("Calcular Preço Sugerido"):
    
    custo_materiais = sum([c for _, c in materiais])
    custo_producao = (tempo_por_unidade * tempo_valor_minuto) + transporte_por_unidade + embalagem_por_unidade
    custo_unitario = custo_materiais + custo_producao
    
    preco_sugerido = custo_unitario * (1 + lucro / 100)

    st.markdown("---")
    st.header("Resultados do Cálculo")
    
    col5, col6 = st.columns(2)
    col5.metric(label="Custo Total por Unidade", value=f"R$ {custo_unitario:.2f}")
    col6.metric(label="Preço Sugerido (com Lucro)", value=f"R$ {preco_sugerido:.2f}")

    preco_final = st.number_input("Qual será seu preço final de venda? (R$)", min_value=0.0)
    if preco_final > 0:
        lucro_real = preco_final - custo_unitario
        st.metric(label="Seu Lucro Real por Unidade", value=f"R$ {lucro_real:.2f}")

    # Lembrete pós-cálculo
    st.subheader("📌 Lembrete Importante")
    st.markdown("""
    Valor não é só o preço. É o cuidado com seu tempo, materiais, criatividade e a experiência que você entrega.
    Esta calculadora existe para **te ajudar a honrar seu trabalho com consciência, justiça e sustentabilidade.**
    Tudo que é feito com amor, merece ser valorizado com dignidade.
    """)

# --- Rodapé e Links ---
st.markdown("---")
st.markdown("Esta ferramenta é gratuita porque acreditamos em um mundo digital mais justo. Se quiser apoiar nosso trabalho, agradecemos! Pix: `encontrodaguahub@gmail.com`")
st.markdown("---")
st.markdown("[Solicite uma versão personalizada](https://tally.so/r/SEULINKAQUI) | [Avalie ou envie sugestões](https://tally.so/r/wbGRAy) | [Fale com a gente](https://wa.me/554192557600)")

with st.expander("Sobre o Encontro D'Água Hub 💧"):
    st.markdown("""
    O Hub Encontro D’Água é um espaço digital colaborativo que une **tecnologia, ética e impacto social**.
    Criamos ferramentas com alma para apoiar mães, artistas e pequenos negócios.
    Aqui, tecnologia é cuidado. É tempo devolvido. É sistema circular.
    
    👉 [@encontrodagua.hub](https://instagram.com/encontrodagua.hub)
    """)

# --- INTEGRAÇÃO DA AMAZÔ (TYPEBOT) ---
# (Este código insere a "bolha" do chatbot na página)

CODIGO_EMBED_TYPEBOT = """
<script>
  const typebotInitScript = document.createElement("script");
  typebotInitScript.type = "module";
  typebotInitScript.innerHTML = `
    import Typebot from 'https://cdn.jsdelivr.net/npm/@typebot.io/js@0/dist/web.js'
    
    Typebot.initBubble({
      typebot: "amazo-chatbot-landingpage",
      theme: {
        button: { backgroundColor: "#1D1D1D" },
        chatWindow: { backgroundColor: "#F8F8F8" },
      },
    });
  `;
  document.body.append(typebotInitScript);
</script>
"""

components.html(CODIGO_EMBED_TYPEBOT, height=100)

# --- Fim do Código ---
