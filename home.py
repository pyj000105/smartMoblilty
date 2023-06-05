import streamlit as st
from PIL import Image
import pandas as pd
import matplotlib.pyplot as plt

add_selectbox = st.sidebar.selectbox(
    "목차",
    ("체질량 계산기", "갭마인더", "마이페이지")
)
if add_selectbox == "체질량 계산기":
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
elif add_selectbox == "갭마인더":
    st.write('# 여기는 갭마인더 입니다.')

    data = pd.read_csv('gapminder.csv')

    st.write(data)

    colors =[]
    for x in data['continent']:
        if x == 'Asia':
            colors.append('tomato')
        elif x == 'Europe':
            colors.append('blue')
        elif x == 'Africa':
            colors.append('olive')
        elif x == 'Americas':
            colors.append('green')
        else:
            colors.append('orange')
    data['colors'] = colors
    year = st.slider('년도를 선택하세요', 1952, 2005, 1952,5)
    st.write(year, '년도')

    data = data[data['year']==year]

    fig, ax = plt.subplots()
    ax.scatter(data['gdpPercap'],data['lifeExp'],s=data['pop']*0.000001, color = data['colors'])
    ax.set_title('How Does Gdp per Capital relate to Life Experctancy?')
    ax.set_xlabel("Gdp per Capital")
    ax.set_ylabel("Life Expertancy")

    st.pyplot(fig)
else:
    st.write('# 여기는 마이페이지 입니다.')