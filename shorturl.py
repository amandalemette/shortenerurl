
import pyshorteners
import qrcode
import streamlit as st
from PIL import Image
from io import BytesIO
#background-image: url("https://github.com/amandalemette/images/blob/865385d58577f7d8fb5c3bfbfae8692e178e9624/general/foto3.jpg?raw=true");

page_bg_img = """
<style>
[data-testid = "stAppViewContainer"]{
background-image: url("https://github.com/amandalemette/images/blob/main/general/foto7.jpg?raw=true");
background-size:cover;
}

[data-testid = 'stHeader']{
background-color: rgba(0,0,0,0);
}

<style>

"""
st.markdown(page_bg_img,unsafe_allow_html = True)

#"st.session_state object:", st.session_state
if 'button1' not in st.session_state:
    st.session_state.button1 = False

def click_button1():
    st.session_state.button1 = True


type_tiny = pyshorteners.Shortener()

st.markdown("# Shortener URL")

long_url = st.text_area("Paste the URL:")
st.write('The entered URL is:',long_url)

st.button('Shorten the URL', on_click=click_button1)

if st.session_state.button1:
    short_url = type_tiny.tinyurl.short(long_url)

    st.write('The shortened URL is:',short_url)
    st.code(short_url)
    st.write('You can copy it')

    if 'short_url' not in st.session_state:
        st.session_state['short_url'] = short_url

#st.write(st.session_state)


button2 = st.button('Generate the QR code')


if button2:
    short_url = st.session_state['short_url']
    img = qrcode.make(short_url )
    # Convert the PIL image to a bytes-like object
    image_bytes = BytesIO()
    img.save(image_bytes, format="PNG")

    st.image(image_bytes, caption='QR code', width=100)
    button3 = st.download_button(label = 'Download QR code as png', data = image_bytes, file_name = 'QRcode.png')
