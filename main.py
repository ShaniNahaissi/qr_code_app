import streamlit as st
import qrcode
from PIL import Image
from io import BytesIO

st.set_page_config(page_title="QR Code Generator", layout="centered")

# Add CSS to shift button slightly left
st.markdown("""
    <style>
    div.stDownloadButton > button {
        display: block;
        margin: 0 auto;
        transform: translateX(-20px); /* move left by 20px */
    }
    </style>
""", unsafe_allow_html=True)

def main():
    st.title("📱 QR Code Generator")
    st.write("Enter text or URL to generate a QR code.")

    user_input = st.text_input("Enter text or URL:", key="text_input_1")

    if user_input:
        # Generate QR code
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_H,
            box_size=8,
            border=4,
        )
        qr.add_data(user_input)
        qr.make(fit=True)

        qr_img = qr.make_image(fill_color="black", back_color="white").convert("RGB")
        qr_img = qr_img.resize((300, 300))

        buf = BytesIO()
        qr_img.save(buf, format="PNG")
        byte_im = buf.getvalue()

        # Center QR code horizontally
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            st.image(qr_img, caption="Generated QR Code")

            # Button slightly to the left
            st.download_button(
                label="⬇️ Download QR Code",
                data=byte_im,
                file_name="qr_code.png",
                mime="image/png"
            )

if __name__ == "__main__":
    main()

# Command to run the app:
# streamlit run main.py