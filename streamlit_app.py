import streamlit as st

intro_page = st.Page("intro.py", title="Introduction")
study1_page = st.Page("study1.py", title="Experiment on AI Process Augmentation")
study2_page = st.Page("study2.py", title="Experiment on AI Content Substitution")

pg = st.navigation([intro_page, study1_page, study2_page])
st.set_page_config(page_title='Experiment Demo for "AI Voice in Online Video Platforms"', page_icon=":material/edit:")
pg.run()