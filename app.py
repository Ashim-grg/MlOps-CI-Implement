import streamlit as st

st.title('Power Calculator')
st.write('Enter the number to calculate its square, cube and fifth power')

n = st.number_input('Enter an Integer..',value=1,step=1)

square = n ** 2
cube = n ** 3
fifth = n ** 5

st.write(f'The square of number {n} is {square}')
st.write(f'The cube value of number {n} is {cube}')
st.write(f'The fifth power value of number {n} is {fifth}')