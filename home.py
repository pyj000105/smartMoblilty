import streamlit as st
from PIL import Image

#체질량
#키, 몸무계

st.write('# 체질량 지수 계산기')
st.info("bmi는 당신의 몸무계를 키의 제곱으로 나누는 것입니다.")

height = st.number_input('키를 입력하세요. (cm)' , 100,200,178,1)
st.write('키', height,'(cm)')

weight = st.number_input('체중을 입력하세요. (kg)',0,200,98,1 )
st.write('체중', weight, '(kg)')

bmi = weight / ((height/100)**2)
def bmi_range(bmi):
    if bmi >= 25:
        st.error('비만입니다.')
    elif bmi >= 23:
        st.warning('과체중입니다.')
    elif bmi >= 18.5:
        st.success('정상입니다.')
    else:
        st.info('저체중입니다.')

if st.button('bmi계산'):
    st.write('당신의 bmi는',round(bmi,2),'입니다.')
    st.balloons()
    bmi_range(bmi)
image = Image.open('fitness.jpg')
st.image(image)