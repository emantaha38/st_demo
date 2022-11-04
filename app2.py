import streamlit as st

st.title('culculator')
st.image ('https://www.target.com/p/casio-sl-300sv-basic-calculator/-/A-16945586',width=100)
num1=st.number_input('pick a number',0,100)
num2=st.number_input('pick an number',0,100)

summ=num1 + num2
subt=num1 - num2

st.write('sum = ' ,summ)
st.write('sub = ',subt)

st.metric('salse',2500,-10)

if st.button('calculate'):
    st.write('sum = ' ,summ)
    st.write('sub = ',subt)



    
 