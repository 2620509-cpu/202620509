import streamlit as st

# 1. 체육관 데이터베이스 (예시 데이터)
gym_database = [
    {"name": "코리안좀비 MMA", "location": "서울 강남구", "sports": ["MMA", "주짓수"], "parking": True, "rating": 4.9},
    {"name": "팀매드", "location": "부산 해운대구", "sports": ["MMA", "킥복싱"], "parking": True, "rating": 4.8},
    {"name": "블랙컴뱃 복싱짐", "location": "서울 마포구", "sports": ["복싱"], "parking": False, "rating": 4.7},
    {"name": "와이어 주짓수", "location": "서울 강남구", "sports": ["주짓수"], "parking": True, "rating": 4.6},
    {"name": "팀파시 무에타이", "location": "서울 서초구", "sports": ["무에타이", "킥복싱"], "parking": False, "rating": 4.5},
    {"name": "싸비 MMA", "location": "서울 마포구", "sports": ["MMA", "주짓수", "복싱"], "parking": True, "rating": 4.8},
]

# 웹페이지 제목 및 레이아웃 설정
st.set_page_config(page_title="격투기 체육관 찾기", page_icon="🥊", layout="centered")

st.title("🥊 맞춤형 격투기 체육관 찾기")
st.markdown("원하는 조건의 격투기 체육관을 빠르게 검색해 보세요!")
st.divider()

# 2. 사이드바 - 사용자 조건 입력창
st.sidebar.header("🔍 검색 필터")

# 지역 입력 (텍스트 검색)
search_location = st.sidebar.text_input("📍 희망 지역 입력 (예: 강남구, 부산)", "")

# 종목 선택 (셀렉트 박스)
sports_options = ["전체", "MMA", "주짓수", "복싱", "킥복싱", "무에타이"]
search_sport = st.sidebar.selectbox("🥋 선호 종목", sports_options)

# 주차 여부 (라디오 버튼)
parking_option = st.sidebar.radio("🚗 주차 여부", ["상관없음", "주차 가능만", "주차 불가만"])

# 3. 필터링 로직
filtered_gyms = []
for gym in gym_database:
    # 지역 필터
    if search_location and search_location not in gym["location"]:
        continue
    
    # 종목 필터
    if search_sport != "전체" and search_sport not in gym["sports"]:
        continue
        
    # 주차 필터
    if parking_option == "주차 가능만" and not gym["parking"]:
        continue
    elif parking_option == "주차 불가만" and gym["parking"]:
        continue
        
    filtered_gyms.append(gym)

# 4. 결과 출력 영역
st.subheader(f"🔍 검색 결과 (총 {len(filtered_gyms)}곳)")

if not filtered_gyms:
    st.error("❌ 조건에 맞는 체육관이 없습니다. 필터를 변경해 보세요.")
else:
    # 평점 높은 순으로 정렬
    filtered_gyms.sort(key=lambda x: x["rating"], reverse=True)
    
    # 결과를 이쁜 카드로 출력
    for gym in filtered_gyms:
        # 주차 여부 아이콘 표시
        parking_status = "🚗 주차 가능" if gym["parking"] else "❌ 주차 불가"
        # 종목들을 해시태그 형태로 변환
        sports_tags = " ".join([f"`#{sport}`" for sport in gym["sports"]])
        
        # 스트림릿 내장 컨테이너 상자로 시각화
        with st.container(border=True):
            col1, col2 = st.columns([3, 1])
            with col1:
                st.markdown(f"### {gym['name']}")
                st.caption(f"📍 {gym['location']}")
                st.markdown(f"**종목:** {sports_tags}")
            with col2:
                st.markdown(f"## ⭐ {gym['rating']}")
                st.caption(parking_status)