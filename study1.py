import streamlit as st
import streamlit_survey as ss

def anchor(name: str):
    st.markdown(f"<div id='{name}'></div>", unsafe_allow_html=True)

st.set_page_config(page_title="Study 1", layout="wide")

st.markdown("<div id='top'></div>", unsafe_allow_html=True)
st.sidebar.markdown(
    """
    ### On this page
    - [1. Experiment Overview](#overview)
    - [2. Experiment Design](#design)
        - [2.1. Experiment Videos](#videos)
        - [2.2. Main Study Question](#q1)
        - [2.3. Manipulation Check](#manipcheck)
    - [3. Experiment Results](#results)
        - [3.1. Randomization Check](#randomcheck)
        - [3.2. Main Results](#mainresults)
    """,
    unsafe_allow_html=True
)

st.title("Study 1: AI Process Augmentation")

anchor("overview")
st.markdown("""
### 1. Experiment Overview  

In this first study, we investigate the **effect of AI voice on viewer engagement** and assess how creators’ experience moderates this effect.  

Since experience level is difficult to manipulate directly, we use **English proficiency** as a proxy.
            
Based on the **partial AI process augmentation mechanism**, we expect that:  
- AI voice may **reduce engagement** for **English-proficient creators**,  
- but **increase engagement** for **non-native English speakers**.
""")

anchor("design")
st.markdown("""         
### 2. Experiment Design
            
We recruited **450 participants from Prolific** and randomly assigned them to one of three conditions.  
Each participant watched the **same video of a female athlete working out in a gym**, but with different voiceovers:  
1. **Non-native female human voice**  
2. **Female AI voice**  
3. **Native female human voice**

""")

anchor("videos")
st.markdown("##### 2.1. Experiment Videos:")

# First row: three videos
cols = st.columns(3)
with cols[0]:
    st.video("videos/study1/female_nonnative.mp4")  # replace with your actual path or URL
with cols[1]:
    st.video("videos/study1/female_ai.mp4")
with cols[2]:
    st.video("videos/study1/female_native.mp4")

# Second row: three condition descriptions
cols = st.columns(3)
with cols[0]:
    st.markdown("**Condition 1:** Non-native Voice")
with cols[1]:
    st.markdown("**Condition 2:** AI Voice")
with cols[2]:
    st.markdown("**Condition 3:** Native Voice")

anchor("q1")
st.markdown("""
##### 2.2. Main Study Question
After watching, participants rated their **engagement** on the following 5-point Likert scale:
""")

survey = ss.StreamlitSurvey("Survey Example")

options = ["Strongly Disagree", "Somewhat Disagree", "Neutral", "Somewhat Agree", "Strongly Agree"]

survey.radio("#### **I like this video:**", options=options, horizontal=True)
survey.radio("#### **I enjoy watching this video:**", options=options, horizontal=True)
survey.radio("#### **I would like to watch similar videos:**", options=options, horizontal=True)
survey.radio("#### **I would share this video with my friends:**", options=options, horizontal=True)

anchor("manipcheck")
st.markdown("""
##### 2.3. Manipulation Check Questions
In addition to measuring engagement, it is important to confirm that participants **perceived the voice manipulation as intended**.  
Because our experiment varies the type of voice (AI, non-native human, native human), a manipulation check ensures that participants indeed noticed differences in **clarity, fluency, and naturalness** of the voice.
Therefore, participants were asked to fill in the following 5-point Likert scale at the end of the survey:
            
The voice in the video is:
""")

survey = ss.StreamlitSurvey("Survey Example")

options = ["Strongly Disagree", "Somewhat Disagree", "Neutral", "Somewhat Agree", "Strongly Agree"]

survey.radio("#### **Clear**", options=options, horizontal=True)
survey.radio("#### **Fluent**", options=options, horizontal=True)
survey.radio("#### **Natural**", options=options, horizontal=True)

st.markdown("""###### Manipulation Check Results
To confirm that our experimental manipulation was effective, we compared participants’ ratings of voice fluency across the three conditions. A one-way ANOVA revealed a highly significant difference among groups (F(2, N–3) = 158.63, p < 0.001). This indicates that participants clearly distinguished between the conditions in terms of perceived fluency, demonstrating that our manipulation worked as intended.
""")


anchor("results")
st.markdown("### 3. Experiment Results")

anchor("randomcheck")
st.markdown("""#### 3.1. Randomization Check
            
To ensure that participants were randomly and evenly distributed across the three experimental conditions, we conducted **ANOVA F-tests** on baseline characteristics (age, gender, minority status, and student status).  
The table reports group means/proportions and the corresponding F-statistics and p-values.  

According to the randomization check results, the p-value for all coefficients are greater than 0.05, indicating no significant baseline differences across conditions.

| Variable        | AI Female | Native Female | Non-native Female | F-statistic | p-value |
|-----------------|-----------|---------------|-------------------|-------------|---------|
| **Age (mean)**  | 39.41     | 38.13         | 39.73             | 0.63        | 0.534   |
| **Female (%)**  | 0.55      | 0.55          | 0.60              | 0.49        | 0.614   |
| **Minority (%)**| 0.79      | 0.68          | 0.78              | 2.72        | 0.067   |
| **Student (%)** | 0.17      | 0.13          | 0.16              | 0.57        | 0.564   |

""")

anchor("mainresults")
st.markdown("""#### 3.2. Main Results
The results show that AI-voice videos elicit higher engagement than those with non-native human voices (AI-voice: 2.99, Non-native voice: 2.58; T = 3.44, p < 0.001), but lower engagement than videos with native human voices (Native voice: 3.27, AI-voice: 2.99; T = 2.40, p = 0.017). These findings demonstrate that the impact of AI voice on viewer engagement varies between experienced and inexperienced creators, supporting the mechanism on partial AI process augmentation.
""")

st.image("videos/study1/output.png", caption="Main Results")
