import random
import datetime
import streamlit as st

# 페이지 설정
st.set_page_config(page_title="오늘의 띠별 운세", page_icon="🔮", layout="centered")

# 12지신 정보 및 띠별 기본 운세 데이터
ZODIAC_DATA = {
    "쥐띠 🐭": {
        "fortunes": [
            "새로운 기회가 찾아오는 날입니다. 주저하지 말고 도전해보세요.",
            "주변 사람들과의 소통이 중요한 날입니다. 경청하는 태도가 행운을 부릅니다.",
            "차분하게 내실을 다지기 좋은 날입니다. 무리한 추진은 피하세요."
        ]
    },
    "소띠 🐮": {
        "fortunes": [
            "꾸준히 노력해온 일이 결실을 맺는 날입니다. 성실함이 빛을 발합니다.",
            "급하게 서두르지 말고 순리대로 풀어가면 좋은 결과가 있습니다.",
            "금전운이 상승하는 날입니다. 뜻밖의 이득이 생길 수 있습니다."
        ]
    },
    "호랑이띠 🐯": {
        "fortunes": [
            "자신감 있게 행동하면 큰 성과를 얻을 수 있는 에너지가 넘치는 날입니다.",
            "충동적인 결정보다는 한 번 더 고민하고 실행하는 지혜가 필요합니다.",
            "귀인을 만나 어려운 문제가 해결될 징조가 보입니다."
        ]
    },
    "토끼띠 🐰": {
        "fortunes": [
            "평온하고 차분한 하루입니다. 나만을 위한 휴식 시간을 가져보세요.",
            "인간관계에서 세심한 배려가 빛을 발하여 호감을 얻게 됩니다.",
            "세워둔 계획을 차근차근 실행으로 옮기기에 적합한 날입니다."
        ]
    },
    "용띠 🎭": {
        "fortunes": [
            "리더십을 발휘하여 주도적으로 일을 이끌어가기 좋은 날입니다.",
            "주변의 시기나 오해를 사지 않도록 겸손한 태도를 유지하세요.",
            "창의적인 아이디어가 샘솟아 좋은 평가를 받게 됩니다."
        ]
    },
    "뱀띠 🐍": {
        "fortunes": [
            "직관력과 순발력이 뛰어난 날입니다. 중요한 결정을 내리기 좋습니다.",
            "지출 관리에 신경 써야 하는 날입니다. 꼼꼼하게 살피세요.",
            "마음의 여유를 가지면 의외의 곳에서 문제의 답을 찾을 수 있습니다."
        ]
    },
    "말띠 🐴": {
        "fortunes": [
            "활력이 넘치고 이동운이 좋은 날입니다. 야외 활동이나 미팅에 이롭습니다.",
            "성급한 언행은 오해를 부를 수 있으니 말과 행동을 신중히 하세요.",
            "목표에 집중하면 예상보다 빠르게 성과를 달성할 수 있습니다."
        ]
    },
    "양띠 🐑": {
        "fortunes": [
            "따뜻하고 화목한 기운이 감도는 날입니다. 협동 작업에 매우 좋습니다.",
            "작은 사안에 연연하기보다는 넓은 안목으로 상황을 바라보세요.",
            "취미 활동이나 자기계발에 투자하면 보람찬 하루가 됩니다."
        ]
    },
    "원숭이띠 🐵": {
        "fortunes": [
            "재치와 순발력으로 어려운 상황도 재치 있게 넘어갈 수 있습니다.",
            "집중력이 필요한 날입니다. 여러 일을 한 번에 벌이지 마세요.",
            "반가운 사람에게 연락이 오거나 즐거운 제안을 받을 수 있습니다."
        ]
    },
    "닭띠 🐔": {
        "fortunes": [
            "분석력과 정리 정돈 능력이 빛나는 날입니다. 일의 우선순위를 정하세요.",
            "타인과의 경쟁보다는 스스로의 목표 달성에 집중하는 것이 좋습니다.",
            "기본에 충실할 때 예상외의 정당한 보상을 얻게 됩니다."
        ]
    },
    "개띠 🐶": {
        "fortunes": [
            "신뢰를 바탕으로 한 협력에서 좋은 결과가 나오는 날입니다.",
            "약속이나 시간을 철저히 지키면 상대에게 큰 신뢰를 얻습니다.",
            "솔직하고 진실된 마음으로 다가가면 관계가 더욱 깊어집니다."
        ]
    },
    "돼지띠 🐷": {
        "fortunes": [
            "마음이 풍요롭고 보람을 느끼는 기분 좋은 하루가 예상됩니다.",
            "너그러운 마음으로 상대를 대하면 나에게도 큰 복으로 돌아옵니다.",
            "건강 관리와 컨디션 조절에 유의하며 무리하지 않는 것이 좋습니다."
        ]
    }
}

COLORS = ["빨강 🔴", "파랑 🔵", "노랑 🟡", "초록 🟢", "보라 🟣", "흰색 ⚪", "검정 🖤"]


def main():
    today = datetime.date.today().strftime("%Y년 %m월 %d일")

    st.title("🔮 오늘의 띠별 운세")
    st.caption(f"📅 기준일: {today}")
    st.markdown("---")

    # 띠 선택 드롭다운
    selected_zodiac = st.selectbox(
        "당신의 띠를 선택해 주세요:",
        list(ZODIAC_DATA.keys())
    )

    if st.button("운세 확인하기 ✨", use_container_width=True):
        # 매일 일정한 결과를 보여주기 위해 날짜와 띠 기반 시드 설정
        today_seed = int(datetime.date.today().strftime("%Y%m%d"))
        zodiac_seed = hash(selected_zodiac)
        random.seed(today_seed + zodiac_seed)

        # 운세 추출
        fortunes = ZODIAC_DATA[selected_zodiac]["fortunes"]
        selected_fortune = random.choice(fortunes)
        score = random.randint(65, 100)
        lucky_number = random.randint(1, 99)
        lucky_color = random.choice(COLORS)

        # 결과 UI 출력
        st.subheader(f"[{selected_zodiac}] 오늘의 운세 결과")

        # 운세 박스
        st.info(f"**📜 운세 총평**\n\n{selected_fortune}")

        # 행운 지수 및 디테일 지표
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric(label="🍀 행운 지수", value=f"{score}점")
        with col2:
            st.metric(label="🔢 행운의 숫자", value=str(lucky_number))
        with col3:
            st.metric(label="🎨 행운의 색상", value=lucky_color)


if __name__ == "__main__":
    main()
