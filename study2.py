import streamlit as st
import streamlit_survey as ss

def anchor(name: str):
    st.markdown(f"<div id='{name}'></div>", unsafe_allow_html=True)

st.set_page_config(page_title="Study 2", layout="wide")

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
        - [3.3. Causal Mediation Analysis](#causalmediation)
    """,
    unsafe_allow_html=True
)

st.title("Study 2: AI Content Substitution")

anchor("overview")
st.markdown("""
### 1. Experiment Overview  

This study examines the **effect of AI content substitution on viewer engagement**, focusing on how the alignment between a creator’s identity and the AI-generated voice moderates this effect.  

To manipulate identity alignment through **visual–vocal pairing**, we recruited one male actor and one female actor to film the same workout video in a gym. Each video was then dubbed with either a male or a female AI voice, creating four conditions:  

- **Identity-Aligned Videos**  
  * Male actor video with a male AI voice  
  * Female actor video with a female AI voice  

- **Identity-Misaligned Videos**  
  * Male actor video with a female AI voice  
  * Female actor video with a male AI voice  

Grounded in the **partial AI content substitution** mechanism, we hypothesize that **identity-aligned videos will generate higher viewer engagement** than identity-misaligned videos.  
""")

anchor("design")
st.markdown("""         
### 2. Experiment Design
            
We recruited **400 participants from Prolific** and randomly assigned them to one of four conditions.  
-  Male actor video with a male AI voice  (Identity-Aligned)
-  Female actor video with a female AI voice  (Identity-Aligned)
-  Male actor video with a female AI voice  (Identity-Misaligned)
-  Female actor video with a male AI voice  (Identity-Misaligned)
""")

anchor("videos")
st.markdown("##### 2.1. Experiment Videos:")

# First row: three videos
anchor("videos")
st.markdown("##### 2.1. Experiment Videos (2×2)")

# Row 1 — Identity-Aligned
cols = st.columns(2)
with cols[0]:
    st.markdown("**Aligned:** Male actor × Male AI voice")
    st.video("videos/study2/male_male.mp4")   # <- update path
with cols[1]:
    st.markdown("**Aligned:** Female actor × Female AI voice")
    st.video("videos/study2/female_female.mp4")  # <- update path

# Row 2 — Identity-Misaligned
cols = st.columns(2)
with cols[0]:
    st.markdown("**Misaligned:** Male actor × Female AI voice")
    st.video("videos/study2/male_female.mp4")  # <- update path
with cols[1]:
    st.markdown("**Misaligned:** Female actor × Male AI voice")
    st.video("videos/study2/female_male.mp4")  # <- update path

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
##### 2.3. Manipulation Check
In addition to measuring engagement, it is important to confirm that participants **perceived the manipulation as intended**.  
Since our experiment manipulate the visual-vocal identity alignment, we specifically asked participants about their perceptions of this alignment with the following question at the end of the survey.

Please indicate how much you agree or disagree with the following statements based on your perception of the video you just watched:
""")

survey = ss.StreamlitSurvey("Survey Example")

options = ["Strongly Disagree", "Somewhat Disagree", "Neutral", "Somewhat Agree", "Strongly Agree"]

survey.radio("#### **The creator's voice aligns well with their appearance.**", options=options, horizontal=True)
survey.radio("#### **The voice is well matched to the creator's appearance.**", options=options, horizontal=True)
survey.radio("#### **There is a good fit between how the creator looks and how the creator sounds**", options=options, horizontal=True)

st.markdown(""" ###### Manipulation Check Results
According to our manipulation check results, the mean **perceived identity alignment** for the identity-aligned group is 3.210 and the mean for the identity-misaligned group is 2.068. The difference is statistically significant (T = 8.20, p < 0.001).

In summary, our manipulation check confirmed that participants accurately perceived the intended visual-vocal identity alignment in the videos.
""")


anchor("results")
st.markdown("### 3. Experiment Results")

anchor("randomcheck")
st.markdown("""#### 3.1. Randomization Check
            
To verify that participants were randomly and evenly distributed across the **identity-aligned** and **identity-misaligned** groups, we conducted **two-sample t-tests** on baseline characteristics (age, gender, minority status, and student status).  

The table below reports group means/proportions along with the differences, t-statistics, and p-values.  

According to the results, all p-values are greater than 0.05, indicating **no significant baseline differences** between the two groups. This confirms that randomization was successful.  

| Variable        | Aligned Mean | Misaligned Mean | Difference | t-statistic | p-value |
|-----------------|--------------|-----------------|------------|-------------|---------|
| **Age (mean)**  | 37.62        | 39.60           | -1.98      | -1.54       | 0.124   |
| **Female (%)**  | 0.48         | 0.47            | 0.02       | 0.30        | 0.765   |
| **Minority (%)**| 0.41         | 0.41            | 0.01       | 0.10        | 0.919   |
| **Student (%)** | 0.16         | 0.12            | 0.04       | 1.02        | 0.311   |

""")

anchor("mainresults")
st.markdown("""#### 3.2. Main Results
The results indicate that voice–identity alignment increases viewer engagement. Videos with aligned voices generate significantly higher engagement (M = 3.67, SD = 1.17) compared to videos with misaligned voices (M = 3.38, SD = 1.29; T = 2.37, p = 0.018).
""")

st.image("videos/study2/output.png", caption="Main Results")

anchor("causalmediation")
st.markdown("""### 3.3. Causal Mediation Analysis
            
To further examine the mechanism underlying the effect of **visual–vocal alignment** on **user engagement**, we conducted a **causal mediation analysis** using nonparametric bootstrapping (5,000 resamples).  
The analysis tested whether **perceived identity alignment** mediates this relationship between **visual–vocal alignment** and **user engagement**.
We use the metrics obtained from our manipulation check to assess perceived identity alignment.

According to the causal mediation analysis results:
- The **Average Causal Mediation Effect (ACME)** is positive and significant (Estimate = 0.62, 95% CI [0.46, 0.80], p < 0.001), indicating that perceived identity alignment significantly mediates the effect of alignment on engagement.  
- The **Total Effect** remains positive and significant (Estimate = 0.29, 95% CI [0.04, 0.53], p = 0.020).  
- Importantly, the **Proportion Mediated** is greater than 1 (Estimate = 2.12, 95% CI [1.22, 9.77], p = 0.020), indicating that **perceived identity alignment is a key psychological mechanism** through which voice–identity alignment enhances user engagement.  

---

#### Mediation Results (Nonparametric Bootstrap Confidence Intervals)

| Effect            | Estimate | 95% CI Lower | 95% CI Upper | p-value   |
|-------------------|----------|--------------|--------------|-----------|
| **ACME**          | 0.6200   | 0.4632       | 0.8000       | <0.001 *** |
| **ADE**           | -0.3275  | -0.5274      | -0.1300      | 0.002 **  |
| **Total Effect**  | 0.2925   | 0.0411       | 0.5300       | 0.020 *   |
| **Prop. Mediated**| 2.1196   | 1.2227       | 9.7700       | 0.020 *   |

*Sample Size: 400*  
*Significance codes: `***` p < 0.001, `**` p < 0.01, `*` p < 0.05*  """)