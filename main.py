import pandas as pd
from pandasai import PandasAI
import streamlit as st
import matplotlib.pyplot as plt
import pywhatkit


# Instantiate a LLM
from pandasai.llm.openai import OpenAI
llm = OpenAI(api_token="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", enforce_privacy = True)


#Estrutura
st.title("Pandas Artificial Intelligence")

prompt = st.text_input("Type what you want to know")

# Sample DataFrame
df = pd.read_csv(r'dataset.csv')
df = df[['artists', 'album_name', 'track_name','popularity', 'danceability', 'energy', 'loudness','track_genre']]


#Prompt
pandas_ai = PandasAI(llm)
resultado = pandas_ai(df, prompt=prompt)
st.text(pandas_ai(df, prompt=prompt))
resultado = resultado['track_name'].iloc[0]


resultado = pywhatkit.playonyt(resultado)