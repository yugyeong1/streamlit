

# 웹 대시보드에 이미지파일, 동영상 파일 넣는 방법
import streamlit as st

# 이미지 처리를 위한 라이브러리
from PIL import Image


def main() :
    img = Image.open('streamlit_data/image_03.jpg')

    st.image(img)

    # 웹브라우저 가로 사이즈와 일치하게 출력
    st.image(img, use_column_width= True)

    image_url = 'https://image.zdnet.co.kr/2022/12/12/deb36f62c0aa0d325b9db91848c7da9e.jpg'    
    st.image(image_url)

    # 동영상
    video_file = open('streamlit_data/secret_of_success.mp4', 'rb')
    st.video(video_file)



if __name__ == '__main__' :
    main()

