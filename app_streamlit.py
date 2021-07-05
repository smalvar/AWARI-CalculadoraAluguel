import numpy as np
import streamlit as st
import pickle

model = pickle.load(open('rf_regressor.pkl','rb'))

zona_to_onehot = {'centro':np.array([1,0,0,0,0]),
                  'leste': np.array([0,1,0,0,0]),
                  'norte': np.array([0,0,1,0,0]),
                  'oeste': np.array([0,0,0,1,0]),
                  'sul'  : np.array([0,0,0,0,1])
                  }

def preparing(zona,quartos,area,vagas,banheiros,condo):
	zona_prep = zona_to_onehot[zona.lower()]
	features = np.hstack([area, quartos, banheiros,float(vagas), condo, zona_prep]).reshape(1,-1)
	return features

def main():
	st.image('https://www.99contratos.com.br/imagens/calculadora.png')
	st.title('Calculadora de aluguel - São Paulo')
	st.sidebar.title('Selecione as informações do seu apartamento')
	country_list = ['Norte','Sul','Leste','Oeste','Centro']
	zona = st.sidebar.selectbox('Selecione a zona aqui:', country_list, key='1')
	#zona = st.text_input('Zona')
	quartos = st.sidebar.slider('Quartos', min_value=1, max_value=10, value=5)
	area = st.sidebar.text_input('Area')
	banheiros = st.sidebar.slider('Banheiros', min_value=1, max_value=10, value=5)
	vagas = st.sidebar.slider('Vagas', min_value=0, max_value=10, value=5)
	condo = st.sidebar.text_input('Condomínio')
	st.write('Olá! Vamos calcular o valor do aluguel do seu apartamento em São Paulo, utilizando Machine Learning. Qual o seu nome?')
	nome = st.text_input('Nome')
	pred = st.button('Calcular')
	if pred:
		features = preparing(zona=zona,quartos=quartos,area=area, banheiros=banheiros,vagas=vagas, condo=condo)
		prediction = round((model.predict(features))[0],2)
		output = st.success(f'{nome}, o valor do aluguel é: R$ {prediction}')

if __name__=='__main__':
	main()