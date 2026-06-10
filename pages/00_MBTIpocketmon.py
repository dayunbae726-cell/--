import streamlit as st

st.set_page_config(
    page_title="MBTI 포켓몬 추천",
    page_icon="⚡",
    layout="centered"
)

pokemon_data = {
    "INTJ": {
        "name": "뮤츠",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/150.png",
        "personality": "🧠 뛰어난 전략가! 독립적이고 목표를 향해 꾸준히 나아가는 타입이에요."
    },
    "INTP": {
        "name": "후딘",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/65.png",
        "personality": "🔬 호기심이 많고 분석을 좋아하는 지식 탐구형이에요."
    },
    "ENTJ": {
        "name": "리자몽",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/6.png",
        "personality": "🔥 리더십이 강하고 목표 달성을 위해 끊임없이 도전해요."
    },
    "ENTP": {
        "name": "팬텀",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/94.png",
        "personality": "😎 창의적이고 새로운 아이디어를 만들어내는 능력이 뛰어나요."
    },
    "INFJ": {
        "name": "루기아",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/249.png",
        "personality": "🌊 통찰력이 깊고 다른 사람을 배려하는 이상주의자예요."
    },
    "INFP": {
        "name": "이브이",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/133.png",
        "personality": "🌈 상상력이 풍부하고 따뜻한 감성을 가진 유형이에요."
    },
    "ENFJ": {
        "name": "피카츄",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/25.png",
        "personality": "⚡ 밝고 긍정적인 에너지로 주변 사람들을 이끌어요."
    },
    "ENFP": {
        "name": "토게키스",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/468.png",
        "personality": "✨ 자유롭고 창의적이며 사람들과 어울리는 것을 좋아해요."
    },
    "ISTJ": {
        "name": "거북왕",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/9.png",
        "personality": "🛡️ 책임감이 강하고 믿음직한 현실주의자예요."
    },
    "ISFJ": {
        "name": "해피너스",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/242.png",
        "personality": "💖 배려심이 많고 주변 사람들을 잘 챙겨주는 수호자예요."
    },
    "ESTJ": {
        "name": "보스로라",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/306.png",
        "personality": "🏆 체계적이고 책임감이 강한 관리자형이에요."
    },
    "ESFJ": {
        "name": "님피아",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/700.png",
        "personality": "🎀 친절하고 사교성이 뛰어나 사람들에게 사랑받아요."
    },
    "ISTP": {
        "name": "한카리아스",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/445.png",
        "personality": "⚔️ 실용적이고 문제 해결 능력이 뛰어나요."
    },
    "ISFP": {
        "name": "라프라스",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/131.png",
        "personality": "🎨 감수성이 풍부하고 평화를 사랑하는 예술가예요."
    },
    "ESTP": {
        "name": "번치코",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/257.png",
        "personality": "🚀 도전을 즐기고 행동력이 뛰어난 모험가예요."
    },
    "ESFP": {
        "name": "푸린",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/39.png",
        "personality": "🎤 밝고 활발하며 분위기를 띄우는 엔터테이너예요."
    }
}

st.title("⚡ MBTI 포켓몬 추천기")
st.write("MBTI를 선택하면 너와 잘 어울리는 포켓몬을 알려줄게! 😄")

mbti = st.selectbox(
    "📝 MBTI를 선택하세요",
    list(pokemon_data.keys())
)

if st.button("✨ 결과 보기"):
    pokemon = pokemon_data[mbti]

    st.markdown("---")

    st.subheader(f"🌟 {mbti} 유형의 추천 포켓몬")
    st.image(pokemon["image"], width=250)

    st.success(
        f"당신과 가장 잘 어울리는 포켓몬은 '{pokemon['name']}' 입니다!"
    )

    st.write(pokemon["personality"])

    st.info("💡 MBTI는 참고용이에요! 가장 중요한 건 자신의 개성과 장점을 발견하는 거랍니다 😊")

    st.balloons()
