import streamlit as st

st.write('# Hi! Welcome to My App!')

st.write('반갑습니다. 저의 앱에 오신것을 환영합니다.')

if st.button('Say hello'):
    st.write('Why hello there')
else:
    st.write('Goodbye')

option = st.selectbox(
    '좋아하는 동물은?',
    ('강아지', '고양이', '곰', '사자', '기린'))

st.write('내가 좋아하는 동물은?:', option,'입니다.')
st.write('좋아하는 동물은', {option}, '입니다.')

txt = st.text_area('자기 소개를 해보세요', '''
    
    ''')
st.write('입력한 내용은:', txt)

age = st.slider('나이를 선택하세요?', 0, 130, 24)
st.write("저의 나이는", age, '입니다.')