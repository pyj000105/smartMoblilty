import streamlit as st  #Streamlit을 사용하기 위한 라이브러리
from PIL import Image #PIL은 이미지 처리와 조작을 위한 파이썬 라이브러리
import pandas as pd  #계산을 위한 라이브러리

add_selectbox = st.sidebar.selectbox( #Sidebar에 Select Box를 추가하는 함수
   "구/군 선택",  #목차
   ("머릿말","해운대","광안리", "기장", "남포동", "동래", "사상/사하", "강서구", "서면", "영도") 
)

if add_selectbox == "머릿말": #변수의 값이 "머릿말"인지 확인하기 위해 사용
   st.write('프로그래밍 과제 1922739 박영준') # 텍스트를 출력하는 것
   st.write('# 부산 놀거리') #Markdown 제목으로 표시하는 것
   st.balloons()
   image = Image.open('부산지도.jpg') #이미지 파일을 열어 image에 저장
   st.image(image) #이미지를 표시하는 함수
   
   st.header('부산에 각 지역의 놀 곳을 소개할려고 합니다.') #제목 생성하는 함수
   
elif add_selectbox == "해운대": #변수의 값이 "해운대"인지 확인하기 위해 사용
   st.write('# <광안리 놀거리>') #Markdown 제목으로 표시하는 것
   st.snow() #눈을 내려오게 하는 함수
   col1, col2 = st.columns(2) #열을 생성하여 컨텐츠를 배치
   
   with col1: #col1에 속하는 내용을 지정하는 블록을 시작하는 것을 의미
      st.header("동백섬") #제목 생성하는 함수
      st.image("해운대 동백섬.jpg") #이미지를 표시하는 함수

   with col2: #col2에 속하는 내용을 지정하는 블록을 시작하는 것을 의미
      st.header("블루라인파크") #제목 생성하는 함수
      st.image("해운대 블루라인파크.jpg") #이미지를 표시하는 함수
   
   col3, col4 = st.columns(2) #열을 생성하여 컨텐츠를 배치
   
   with col3: #col3에 속하는 내용을 지정하는 블록을 시작하는 것을 의미
      st.header("해운대 수목원") #제목 생성하는 함수
      st.image("해운대 수목원.jpg") #이미지를 표시하는 함수

   with col4: #col4에 속하는 내용을 지정하는 블록을 시작하는 것을 의미
      st.header("해운대 해수욕장") #제목 생성하는 함수
      st.image("해운대 해수욕장.jpg")#이미지를 표시하는 함수
 
   st.info('좌표를 통해 지도로 확인하기') #info는 파란색 박스 안에 ('')있는 내용을 표시
   df = pd.DataFrame( #빈 데이터프레임을 생성
       [[35.154807 , 129.152568]#동백섬
        ,[35.161250, 129.191532]#블루라인파크
        ,[35.229988, 129.133074]#해운대수목원
        ,[35.158400 , 129.160594]],#해운대해수욕장 
       columns=['lat', 'lon'] #'lat'은 위도, 'lon'은 경도를 의미
   )

   st.map(df) #위치 정보를 지도에 표시

elif add_selectbox == "광안리": #변수의 값이 "광안리"인지 확인하기 위해 사용
   st.snow() #눈을 내려오게 하는 함수
   st.write('# <광안리 놀거리>') #Markdown 제목으로 표시하는 것
   st.header('광안리 해수욕장 드론쇼') #제목 생성하는 함수
   image = Image.open('광안리 해수욕장+드론쇼.jpg') #이미지 파일을 열어 image에 저장
   st.image(image) #이미지를 표시하는 함수
   
   col1, col2 = st.columns(2) #열을 생성하여 컨텐츠를 배치

   with col1: #col1에 속하는 내용을 지정하는 블록을 시작하는 것을 의미
      st.header("밀락더마켓") #제목 생성하는 함수
      st.image("광안리 밀락더마켓.jpg") #이미지를 표시하는 함수

   with col2: #col2에 속하는 내용을 지정하는 블록을 시작하는 것을 의미
      st.header("광안리 수변공원") #제목 생성하는 함수
      st.image("광안리 수변공원.jpg") #이미지를 표시하는 함수
   
   st.info('좌표를 통해 지도로 확인하기') #info는 파란색 박스 안에 ('')있는 내용을 표시
   df = pd.DataFrame( #빈 데이터프레임을 생성
       [[35.150862 , 129.116894]#광안리해수욕장
        , [35.154160 , 129.126960]#밀락더마켓
        ,[35.154579 , 129.131982]],#수변공원
       columns=['lat', 'lon'] #'lat'은 위도, 'lon'은 경도를 의미
   )

   st.map(df) #위치 정보를 지도에 표시
    
elif add_selectbox == "기장": #변수의 값이 "기장"인지 확인하기 위해 사용
   st.snow() #눈을 내려오게 하는 함수
   st.write('# <광안리 놀거리>') #Markdown 제목으로 표시하는 것
   st.header('롯데월드') #제목 생성하는 함수
   image = Image.open('기장 롯데월드.jpg') #이미지 파일을 열어 image에 저장
   st.image(image) #이미지를 표시하는 함수
   
   col1, col2 = st.columns(2) #열을 생성하여 컨텐츠를 배치
   
   with col1:#col1에 속하는 내용을 지정하는 블록을 시작하는 것을 의미
      st.header("스카이라인 루지") #제목 생성하는 함수
      st.image("기장 스카이라인 루지.jpg") #이미지를 표시하는 함수

   with col2: #col2에 속하는 내용을 지정하는 블록을 시작하는 것을 의미
      st.header("아홉산숲") #제목 생성하는 함수
      st.image("기장 아홉산숲.jpg") #이미지를 표시하는 함수
   
   col3, col4 = st.columns(2) #열을 생성하여 컨텐츠를 배치
   
   with col3: #col3에 속하는 내용을 지정하는 블록을 시작하는 것을 의미
      st.header("죽성성당") #제목 생성하는 함수
      st.image("기장 죽성성당.jpg") #이미지를 표시하는 함수

   with col4: #col4에 속하는 내용을 지정하는 블록을 시작하는 것을 의미
      st.header("해동용궁사") #제목 생성하는 함수
      st.image("기장 해동용궁사.jpg") #이미지를 표시하는 함수
      
   st.info('좌표를 통해 지도로 확인하기') #info는 파란색 박스 안에 ('')있는 내용을 표시
   df = pd.DataFrame( #빈 데이터프레임을 생성
       [[35.196242, 129.214764]#롯데월드
        ,[35.194319, 129.220022]#스카이라인루지
        ,[35.287062 , 129.171463]#아홉산숲
        ,[35.240934, 129.248406]#죽성성당
        ,[35.188752, 129.223084]],#해동용궁사
       columns=['lat', 'lon'] #'lat'은 위도, 'lon'은 경도를 의미
   )

   st.map(df) #위치 정보를 지도에 표시
elif add_selectbox == "남포동": #변수의 값이 "남포동"인지 확인하기 위해 사용
   st.snow() #눈을 내려오게 하는 함수
   st.write('# <남포 놀거리>') #Markdown 제목으로 표시하는 것
   st.header('용두산공원') #제목 생성하는 함수
   image = Image.open('남포 용두산공원.jpg') #이미지 파일을 열어 image에 저장
   st.image(image) #이미지를 표시하는 함수
   
   col1, col2 = st.columns(2) #열을 생성하여 컨텐츠를 배치
   
   with col1: #col1에 속하는 내용을 지정하는 블록을 시작하는 것을 의미
      st.header("비프광장") #제목 생성하는 함수
      st.image("남포 비프광장.jpg") #이미지를 표시하는 함수

   with col2: #col2에 속하는 내용을 지정하는 블록을 시작하는 것을 의미
      st.header("깡동야시장") #제목 생성하는 함수
      st.image("남포 깡통야시장.jpg") #이미지를 표시하는 함수
   
   st.info('좌표를 통해 지도로 확인하기') #info는 파란색 박스 안에 ('')있는 내용을 표시
   df = pd.DataFrame( #빈 데이터프레임을 생성
       [[35.100559, 129.032671]#용두산공원
        ,[35.098719, 129.027610]#비프광장
        ,[35.101835,129.025949]],#깡통시장
       columns=['lat', 'lon'] #'lat'은 위도, 'lon'은 경도를 의미
   )

   st.map(df) #위치 정보를 지도에 표시
elif add_selectbox == "동래": #변수의 값이 "동래"인지 확인하기 위해 사용
   st.write('# <동래 놀거리>') #Markdown 제목으로 표시하는 것
   st.snow() #눈을 내려오게 하는 함수
   st.header('동래읍성') #제목 생성하는 함수
   image = Image.open('동래읍성.jpg') #이미지 파일을 열어 image에 저장
   st.image(image) #이미지를 표시하는 함수
   
   col1, col2 = st.columns(2) #열을 생성하여 컨텐츠를 배치
   
   with col1: #col1에 속하는 내용을 지정하는 블록을 시작하는 것을 의미
      st.header("온천천") #제목 생성하는 함수
      st.image("동래 온천천.jpg") #이미지를 표시하는 함수
   with col2: #col2에 속하는 내용을 지정하는 블록을 시작하는 것을 의미
      st.header("사직야구장") #제목 생성하는 함수
      st.image("동래 사직야구장.jpg") #이미지를 표시하는 함수

   st.info('좌표를 통해 지도로 확인하기') #info는 파란색 박스 안에 ('')있는 내용을 표시
   df = pd.DataFrame( #빈 데이터프레임을 생성
       [[35.209840 , 129.092241]#동래읍성
        ,[35.191474,129.102003]#온천천
        ,[35.194429, 129.061482]],#사직야구장
       columns=['lat', 'lon'] #'lat'은 위도, 'lon'은 경도를 의미
   )

   st.map(df) #위치 정보를 지도에 표시
elif add_selectbox == "사상/사하": #변수의 값이 "사상/사하"인지 확인하기 위해 사용
   st.snow() #눈을 내려오게 하는 함수
   st.write('# <사상/사하 놀거리>') #Markdown 제목으로 표시하는 것

   col1, col2 = st.columns(2)#열을 생성하여 컨텐츠를 배치
   
   with col1: #col1에 속하는 내용을 지정하는 블록을 시작하는 것을 의미
      st.header("감천문화마을") #제목 생성하는 함수
      st.image("사상,사하 감천문화마을.jpg") #이미지를 표시하는 함수

   with col2: #col2에 속하는 내용을 지정하는 블록을 시작하는 것을 의미
      st.header("다대포 해수욕장") #제목 생성하는 함수
      st.image("사상,사하 다대포 해수욕장.jpg") #이미지를 표시하는 함수
   
   col3, col4 = st.columns(2) #열을 생성하여 컨텐츠를 배치
   
   with col3: #col3에 속하는 내용을 지정하는 블록을 시작하는 것을 의미
      st.header("장림포구") #제목 생성하는 함수
      st.image("사상,사하 장림포구.jpg") #이미지를 표시하는 함수

   with col4: #col4에 속하는 내용을 지정하는 블록을 시작하는 것을 의미
      st.header("삼락생태공원") #제목 생성하는 함수
      st.image("사상,사하 삼락생태공원.jpg") #이미지를 표시하는 함수

   st.info('좌표를 통해 지도로 확인하기') #info는 파란색 박스 안에 ('')있는 내용을 표시
   df = pd.DataFrame( #빈 데이터프레임을 생성
       [[35.097425,129.010753]#문화마을
        ,[35.047722, 128.965720]#다대포
        ,[35.081377,128.958088]#장림포구
        ,[35.167556, 128.973336]],#삼락공원
       columns=['lat', 'lon'] #'lat'은 위도, 'lon'은 경도를 의미
   )

   st.map(df) #위치 정보를 지도에 표시
elif add_selectbox == "강서구": #변수의 값이 "강서구"인지 확인하기 위해 사용
   st.write('# <강서구 놀거리>') #Markdown 제목으로 표시하는 것
   st.snow() #눈을 내려오게 하는 함수
   st.header('가덕도') #제목 생성하는 함수
   image = Image.open('강서구 가덕도.jpg') #이미지 파일을 열어 image에 저장
   st.image(image) #이미지를 표시하는 함수
   
   col1, col2 = st.columns(2) #열을 생성하여 컨텐츠를 배치
   
   with col1: #col1에 속하는 내용을 지정하는 블록을 시작하는 것을 의미
      st.header("대저생태공원") #제목 생성하는 함수
      st.image("강서구 대저생태공원.jpg") #이미지를 표시하는 함수

   with col2: #col2에 속하는 내용을 지정하는 블록을 시작하는 것을 의미
      st.header("스타필드명지") #제목 생성하는 함수
      st.image("강서구 스타필드명지.jpg") #이미지를 표시하는 함수

   st.info('좌표를 통해 지도로 확인하기') #info는 파란색 박스 안에 ('')있는 내용을 표시
   df = pd.DataFrame(  #빈 데이터프레임을 생성
       [[35.052654 , 128.8310590]#가덕도
        ,[35.206845 , 128.981137]#대저생태공원
        ,[35.093035 , 128.918798]],#스타필드명지
       columns=['lat', 'lon'] #'lat'은 위도, 'lon'은 경도를 의미
   )

   st.map(df) #위치 정보를 지도에 표시
elif add_selectbox == "서면": #변수의 값이 "서면"인지 확인하기 위해 사용
   st.snow() #눈을 내려오게 하는 함수
   st.write('# <서면 놀거리>') #Markdown 제목으로 표시하는 것

   st.header('레이저아레나') #제목 생성하는 함수
   image = Image.open('서면 레이저아레나.jpg') #이미지 파일을 열어 image에 저장
   st.image(image) #이미지를 표시하는 함수
   
   col1, col2 = st.columns(2) #열을 생성하여 컨텐츠를 배치
   
   with col1: #col1에 속하는 내용을 지정하는 블록을 시작하는 것을 의미
      st.header("스위트시네마") #제목 생성하는 함수
      st.image("서면 스위트시네마.jpg") #이미지를 표시하는 함수
      
   with col2: #col2에 속하는 내용을 지정하는 블록을 시작하는 것을 의미
      st.header("삼보게임랜드") #제목 생성하는 함수
      st.image("서면 삼보게임랜드.jpg") #이미지를 표시하는 함수

   st.info('좌표를 통해 지도로 확인하기') #info는 파란색 박스 안에 ('')있는 내용을 표시
   df = pd.DataFrame( #빈 데이터프레임을 생성
       [[35.155240, 129.060672]#레이저아레나
        ,[35.154277, 129.057292]#스위티시네마
        ,[35.155172, 129.060129]],#삼보게임랜드
       columns=['lat', 'lon'] #'lat'은 위도, 'lon'은 경도를 의미
   )

   st.map(df) #위치 정보를 지도에 표시
   
else:
   st.write('# <영도 놀거리>') #Markdown 제목으로 표시하는 것
   st.snow() #눈을 내려오게 하는 함수
   st.header('흰여울해안터널') #제목 생성하는 함수
   image = Image.open('영도 흰여울해안터널.jpg') #이미지 파일을 열어 image에 저장
   st.image(image) #이미지를 표시하는 함수
   
   col1, col2 = st.columns(2) #열을 생성하여 컨텐츠를 배치
   
   with col1: #col1에 속하는 내용을 지정하는 블록을 시작하는 것을 의미
      st.header("국립해양박물관") #제목 생성하는 함수
      st.image("영도 국립해양박물관.jpg") #이미지를 표시하는 함수

   with col2: #col2에 속하는 내용을 지정하는 블록을 시작하는 것을 의미
      st.header("태종대") #제목 생성하는 함수
      st.image("영도 태종대.jpg")#이미지를 표시하는 함수
      
   st.info('좌표를 통해 지도로 확인하기') #info는 파란색 박스 안에 ('')있는 내용을 표시
   df = pd.DataFrame( #빈 데이터프레임을 생성
       [[35.075858, 129.047329]#흰여울해안터널] 
        ,[35.078703, 129.080178]#국립해양박물관
        ,[35.052646, 129.086719]],#태종대
       columns=['lat', 'lon'] #'lat'은 위도, 'lon'은 경도를 의미
   )

   st.map(df) #위치 정보를 지도에 표시