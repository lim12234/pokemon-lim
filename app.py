import streamlit as st

st.set_page_config(
    page_title="임현수 포켓몬 도감",
    page_icon="./images/monsterball.png"
)
st.markdown("""
<style>
img {
     max-height: 300px;
}
h1 {
    color: red;
}
[data-testid="stExpanderToggleIcon"] {
    visibility: hidden;
}                        
</style)
""", unsafe_allow_html=True)

st.title("streamlit 포켓몬 도감")

type_emoji_dict = {
    "노말": "⚪",
    "격투": "✊",
    "비행": "🕊",
    "독": "☠️",
    "땅": "🌋",
    "바위": "🪨",
    "벌레": "🐛",
    "고스트": "👻",
    "강철": "🤖",
    "불꽃": "🔥",
    "물": "💧",
    "풀": "🍃",
    "전기": "⚡",
    "에스퍼": "🔮",
    "얼음": "❄️",
    "드래곤": "🐲",
    "악": "😈",
    "페어리": "🧚"
}

init_pokemons = [    # 6강 session state에서 init으로 수정
    {
        "name": "피카츄",
        "types": ["전기"],
        "image_url": "https://storage.googleapis.com/firstpenguine-coding-school/pokemons/pikachu.webp"
    },
    {
        "name": "누오",
        "types": ["물", "땅"],
        "image_url": "https://storage.googleapis.com/firstpenguine-coding-school/pokemons/nuo.webp",
    },
    {
        "name": "갸라도스",
        "types": ["물", "비행"],
        "image_url": "https://storage.googleapis.com/firstpenguine-coding-school/pokemons/garados.webp",
    },
    {
        "name": "개굴닌자",
        "types": ["물", "악"],
        "image_url": "https://storage.googleapis.com/firstpenguine-coding-school/pokemons/frogninja.webp"
    },
    {
        "name": "루카리오",
        "types": ["격투", "강철"],
        "image_url": "https://storage.googleapis.com/firstpenguine-coding-school/pokemons/lukario.webp"
    },
    {
        "name": "에이스번",
        "types": ["불꽃"],
        "image_url": "https://storage.googleapis.com/firstpenguine-coding-school/pokemons/acebun.webp"
    },
]

example_pokemon = {
    "name": "메타몽",
    "types": ["노말"],
    "image_url": "https://i.namu.wiki/i/Y4N1DvjGjDYuhUmobflYoG2yd0vfsVHY7RIrUGCW-j7KRqTIV74Z-Mktg7CzNQAacK2ZlGaBlDINHircweQStl7IV-G-r2cMfQ489mr7BVcrcnK75TtpeuNEqUua8jn6c4LD5Hkd616ZfTqfaK0HKw.webp"
}

if "pokemons" not in st.session_state:
    st.session_state.pokemons = init_pokemons

auto_complete = st.toggle("예시 데이터로 채우기")  # 7강 toggle을 이용한 form 자동완성
print("page_reload, auto_complete", auto_complete)
with st.form(key="form"):
    col1, col2 = st.columns(2)
    with col1:
        name = st.text_input(
            label="포켓몬 이름",
            value=example_pokemon["name"] if auto_complete else ""
        )
    with col2:
        types = st.multiselect(
            label="포켓몬 속성", 
            options=list(type_emoji_dict.keys()),
            max_selections=2,
            default=example_pokemon["types"] if auto_complete else []
        )
    image_url = st.text_input(
        label="포켓몬 이미지 url",
        value=example_pokemon["image_url"] if auto_complete else ""
    )
    submit = st.form_submit_button(label="submit")
    if submit:
        if not name:
            st.error("포켓몬의 이름을 입력해주세요.")
        elif len(types) == 0:
            st.error("포켓몬의 속성을 적어도 한 개 선택해주세요.")
        else:
            st.success("포켓몬을 추가할 수 있습니다.")
            st.session_state.pokemons.append(
                {
                "name": name,
                "types": types,
                "image_url": image_url if image_url else "./images/default.png"
                }
            )    

for i in range(0, len(st.session_state.pokemons), 3):    # 0부터 간격을 3만큼
    row_pokemons = st.session_state.pokemons[i:i+3]
    cols = st.columns(3)
    for j in range(len(row_pokemons)):
        with cols[j]:
            pokemon = row_pokemons[j]
            with st.expander(label=f"**{i+j+1}, {pokemon['name']}**", expanded=True):
                st.image(pokemon["image_url"])
                emoji_types = [f"{type_emoji_dict[x]} {x}" for x in pokemon["types"]]
                st.text(f" / ".join(emoji_types))
                delete_button = st.button(label="삭제", key=i+j, use_container_width=True)
                if delete_button:
                    print("삭제 버튼 누르셨네요.")
                    del st.session_state.pokemons[i+j]
                    st.rerun()