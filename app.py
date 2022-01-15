import requests
import streamlit as st
from streamlit_lottie import st_lottie
from PIL import Image

st.set_page_config(page_title="Liyu tech Studio",
                   page_icon="🤖", layout="wide")


def load_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


def load_lottie_url(url):
    response = requests.get(url)
    if response.status_code != 200:
        return None
    return response.json()


load_css('style/style.css')

lottie_coding = load_lottie_url(
    "https://assets5.lottiefiles.com/packages/lf20_x5jglqn9.json")
lottie_coder = load_lottie_url(
    "https://assets2.lottiefiles.com/packages/lf20_xu3jsjrn.json")

developer_img = Image.open("images/developer.png")


with st.container():
    # header Section
    st.header("Hi, I am Kidus 👋")
    st.title("Software developer and data scientist")
    st.write("I am passionate about making super efficient apps and also enhancing AI and it's applications")
    st.write("[Check out my GitHub >](https://github.com/liyuKnow) ")

# what i do section
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("What I do")
        st.write("##")
        st.write("""lorem ipsum dolor sit amet, consectetur adipiscing elit,
        sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
        Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi
        ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in
        voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat
        cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.""")
    with right_column:
        st_lottie(lottie_coding, width=400, height=400, key="coding")

# Projects section
with st.container():
    st.write("---")
    st.header("Projects")
    st.write("##")
    image_column, text_column = st.columns(2)

    with image_column:
        st.image(developer_img)

    with text_column:
        st.subheader("Integrate Lottie Animation")
        st.write("""lorem ipsum dolor sit amet, consectetur adipiscing elit,
                sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
                Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi
                ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in
                voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat"""
                 )

        st.markdown("[Check out my GitHub >](https://github.com/liyuKnow) ")

with st.container():
    st.write("---")
    st.header("Project 2")
    st.write("##")
    image_column, text_column = st.columns(2)

    with image_column:
        st.image(developer_img)

    with text_column:
        st.subheader("Integrate Lottie Animation")
        st.write("""lorem ipsum dolor sit amet, consectetur adipiscing elit,
                sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
                Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi
                ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in
                voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat"""
                 )

        st.markdown("[Check out my GitHub >](https://github.com/liyuKnow) ")


# Contact section
with st.container():
    st.write("---")
    st.header("Contact Me")
    st.write("##")

    contact_form = """
                    <form action="https://formsubmit.co/4cdeb805887f6741bb092cba75ee36b0 " method="POST">
                        <input type="hidden" name="_capthca" value="false">
                        <input type="text" name="name" placeholder="Enter your name" required>
                        <input type="email" name="email" placeholder="Enter your email" required>
                        <textarea name="message" placeholder="Enter your message" required></textarea>
                        <button type="submit">Send</button>
                    </form>
                    """
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)

    with right_column:
        st_lottie(lottie_coder, width=400, height=400, key="coder")
