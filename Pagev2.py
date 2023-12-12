import streamlit as st
from PIL import Image

def main():
    # Carregando a imagem de plano de fundo
    background_image = Image.open("project2.png")  # Substitua pelo caminho real da sua imagem

    # Configurando a imagem como plano de fundo
    st.markdown(
        f"""
        <style>
            .reportview-container {{
                background: url(data:image/jpeg;base64,{image_to_base64(background_image)});
                background-size: cover;
            }}
        </style>
        """,
        unsafe_allow_html=True
    )

    # Conteúdo da página
    st.title("Aplicativo com Imagem de Plano de Fundo")
    st.write("Seu conteúdo vai aqui.")

# Função para converter imagem PIL para base64
def image_to_base64(image):
    from io import BytesIO
    import base64
    buffered = BytesIO()
    image.save(buffered, format="JPEG")
    return base64.b64encode(buffered.getvalue()).decode()

if __name__ == "__main__":
    main()
