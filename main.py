import streamlit as st
import subprocess
import sys
import os

st.set_page_config(layout="wide")

def download_tracks(url):
    result = subprocess.call("script.sh")
    return result

def autentificar(client_id, client_secret):
    os.environ["SPOTIPY_CLIENT_ID"] = f"{client_id}"
    os.environ["SPOTIPY_CLIENT_SECRET"] = f"{client_secret}"
   
autentificar("fff3b401f2ec4642b50e61db8bb4e627" ,"6cf955664ec5444fbe7c437cd37c29ae")

ruta_descarga = st.text_input("Carpeta de descarga")

st.sidebar.header("Descargar Musica")
playlist_link = st.sidebar.text_input("Link de la Playlist")
btn_descargar= st.sidebar.button("Descargar Playlist")



if ruta_descarga:
    folder = st.selectbox("📁 Mis Playlists",[i for i in os.listdir(ruta_descarga) if not i.startswith(".")])
    btn_listar_sub = st.button("Listar Mi Musica")
    if btn_listar_sub:
        for i,j in enumerate([j for j in os.listdir(os.path.join(ruta_descarga, folder)) if j.endswith(".mp3")]):
            st.write(f"{i+1}. 🎵 {j}")
        

if btn_descargar:
    try:
        st.success("Running...")
        subprocess.Popen(["spotify_dl", "-l", f"{playlist_link}" , "-o",  f"{ruta_descarga}",  "-s",  "yes"])
    except:
        st.warning("Error")
