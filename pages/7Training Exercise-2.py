import streamlit as st
from streamlit import session_state
import random
import math
import webbrowser

st.set_page_config(page_title="Guess The Number", page_icon="🔢")

if hasattr(session_state,'login'):
    if session_state.login==True:
        def answer(max: int) -> int:
            st.session_state.total = round(math.log(max + 1, 2))
            return random.randint(1, max)


        def init(max: int = 10, pastinit=False):
            if not pastinit:
                st.session_state.input = 0
                st.session_state.wins = 0
                st.session_state.cheatcode = 0
            st.session_state.ans = answer(max)
            st.session_state.tries = 0
            st.session_state.over = False


        def restart():
            init(st.session_state.max, pastinit=True)
            st.session_state.input += 1


        def number():
            st.title('Guess the Number 🔢')
            head, victory = st.columns([1, 0.3])
            head.write('This Game chooses a number at random and its your job to guess that number. You only have limited '
                    ' number of guesses. All the Best!')
            st.write("---")
            if 'ans' not in st.session_state:
                init()
            st.slider('Select Maximum Range ', min_value=00, max_value=1000, value=10, key='max', on_change=restart)
            floor, result = st.empty(), st.empty()
            guess = floor.number_input('Enter your Guess', min_value=0, max_value=st.session_state.max,
                                    key=st.session_state.input)
            if guess == 666 and 666 <= st.session_state.max <= 700:
                st.session_state.cheatcode = 1
            if st.session_state.cheatcode == 1:
                st.write(st.session_state.ans)
            if guess:
                flag = 0
                st.session_state.tries += 1
                st.session_state.total -= 1
                if guess < st.session_state.ans and st.session_state.total > 0:
                    result.warning(f'{guess} is too low ! You have {st.session_state.total} Guesses remaining')
                elif guess > st.session_state.ans and st.session_state.total > 0:
                    result.warning(f'{guess} is too high You have {st.session_state.total} Guesses remaining!')
                elif guess == st.session_state.ans:
                    if st.session_state.tries == 1:
                        tri = 'attempt'
                    else:
                        tri = 'attempts'
                    result.success(f'{guess} was the right Answer ! It took you {st.session_state.tries} {tri}')
                    st.balloons()
                    flag = 1
                    st.session_state.wins += 1
                    st.session_state.over = True
                    floor.empty()
                    floor.button('Go Again!', on_click=restart)
                if st.session_state.total <= 0 and flag == 0:
                    st.error(f'The number was {st.session_state.ans}')
                    st.session_state.over = True
                    floor.empty()
                    floor.button('Try Again!', on_click=restart)

            victory.button(f'Total Wins 🏆 {st.session_state.wins}')


        number()
else:
    session_state.login=False
    webbrowser.open("http://localhost:8501/")


    st.write("please login or register")

