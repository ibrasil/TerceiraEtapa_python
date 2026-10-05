import pandas as pd
import streamlit as st

st.title("Meu primeiro dash")
st.subheader("Isabela Aleixo")

nome = "Isabela Aleixo"
idade = 18
st.write(f"Nome: {nome} | Idade: {idade}")

df = pd.DataFrame({
    'Matéria': ['Português', 'Matemática', 'Python', 'Frame'],
    'Nota': [5, 9, 7, 10],
})

st.write(df)
