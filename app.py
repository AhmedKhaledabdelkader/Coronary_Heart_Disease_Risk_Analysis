
import streamlit as st
import pandas as pd
import plotly.express as px


st.set_page_config(layout="wide")

st.sidebar.title("Coronary Heart Disease Risk Dashboard")
df=pd.read_csv("predict-CHD.csv")
# Define functions first
def page1():
    st.title("Framingham Heart Study")
    st.markdown("<h5 style='color: grey;'>    Risk of Coronary Heart Disease</h4>", unsafe_allow_html=True)
    st.write()
    st.write()
    st.markdown("<h2>About Dataset</h2>", unsafe_allow_html=True)
    st.markdown("""<p style='color: grey;'>The Framingham Heart Study Dataset is a 
    comprehensive collection of patient information from an ongoing cardiovascular study in Framingham,
    Massachusetts. The dataset aims to predict the 10-year risk of future coronary heart disease (CHD) in 
    patients based on various health attributes. It includes over 4,000 records and 15 attributes and categories for their attributes , making it a 
    valuable resource for researchers and data scientists working 
    on predictive modeling in healthcare.</p>""", unsafe_allow_html=True)
    st.write()
    st.write()
    st.markdown("<h2>Key Features</h2>", unsafe_allow_html=True)
    st.write()
    st.markdown("""
    <ul>
    <li >gender: <span style="color: grey;">The biological sex of the person (male or female), which can affect heart disease risk.</span></li>
    
    <li >age: <span style="color: grey;">The person's age in years; older individuals have a higher risk of heart disease.</span></li>
    <li >age_cat: <span style="color: grey;">ranges for age (30-40),(40-50)....</span></li>
    <li >education: <span style="color: grey;">The number of years or level of formal education completed by the person.</span></li>
    <li >education_cat: <span style="color: grey;">A categorized version of the education level, grouping individuals into different education categories.</span></li>
    <li >currentSmoker: <span style="color: grey;">Indicates whether the person is currently smoking (1 = Yes, 0 = No); smoking increases heart disease risk.</span></li>
    <li >cigsPerDay: <span style="color: grey;">The number of cigarettes the person smokes per day; more cigarettes lead to higher risk.</span></li>
    <li >BPMeds: <span style="color: grey;">Whether the person is taking blood pressure medication (1 = Yes, 0 = No), which helps manage hypertension.</span></li>
    <li >prevalentStroke: <span style="color: grey;">Indicates if the person has had a stroke before (1 = Yes, 0 = No); having a stroke increases heart disease risk.</span></li>
    <li >prevalentHyp: <span style="color: grey;">Whether the person has a history of hypertension (high blood pressure), which is a major risk factor for heart disease.</span></li>
    <li >diabetes: <span style="color: grey;">Whether the person has diabetes (1 = Yes, 0 = No), which increases the risk of heart disease.</span></li>
    <li >totChol: <span style="color: grey;">The total cholesterol level in the blood; high cholesterol can contribute to heart disease.</span></li>
    <li >totChol_cat: <span style="color: grey;">A categorized version of total cholesterol levels, grouping individuals based on cholesterol risk categories.</span></li>
    <li >sysBP: <span style="color: grey;">Systolic blood pressure (the pressure in arteries when the heart beats); high levels can indicate heart disease risk.</span></li>
    <li >diaBP: <span style="color: grey;">Diastolic blood pressure (the pressure in arteries when the heart is resting between beats).</span></li>
    <li >BP_Cat: <span style="color: grey;">A categorized version of blood pressure, classifying individuals into normal, pre-hypertensive, or hypertensive groups.</span></li>
    <li >BMI: <span style="color: grey;">Body Mass Index, calculated from weight and height to determine if a person has a healthy weight for their height.</span></li>
    <li >BMI_cat: <span style="color: grey;">A categorized version of BMI, grouping individuals into underweight, normal weight, overweight, or obese categories.</span></li>
    <li >heartRate: <span style="color: grey;">The number of heartbeats per minute while at rest; an abnormal heart rate can signal heart issues.</span></li>
    <li >heartRate_cat: <span style="color: grey;">A categorized version of heart rate, grouping individuals into low, normal, or high heart rate categories.</span></li>
    <li >glucose: <span style="color: grey;">The blood sugar level; high glucose levels can indicate diabetes, which is a heart disease risk factor.</span></li>
    <li >glucose_cat: <span style="color: grey;">A categorized version of glucose levels, classifying individuals into normal, prediabetic, or diabetic groups.</span></li>
    <li >TenYearCHD: <span style="color: grey;">The predicted risk of developing coronary heart disease within the next 10 years (1 = High risk, 0 = Low risk).</span></li>
    
    </ul>
    """, unsafe_allow_html=True)
    st.divider()

    

def age_BiAnalysis():
    age = st.select_slider("Select an age", options=sorted(df["age"].unique().tolist()))
    no_of_rows=df[df["age"]==age].shape[0]
    
    
    col1, col2 = st.columns(2)
    
    
    with col1:
        st.markdown(f"<h6>Number of individuals found: {no_of_rows}</h6>", unsafe_allow_html=True)
    
    
    with col2:
        wanted_rows = st.text_input("Enter your number of rows", value="5")

    st.table(df[df['age'] == age].head(int(wanted_rows)))
    col1,col2=st.columns(2)
    with col1:
            fig1=px.histogram(data_frame=df,x="age_cat",color="education_cat",template="presentation"
                    ,text_auto=True,barmode="group",labels={"age_cat":"categories of age","education_cat":"categories of education"},
                    category_orders={"age_cat":["age(30-40)","age(41-50)","age(51-60)","age(61-70)"],
                                   "education_cat":["low level","intermediate level","high level","advanced level"]},color_discrete_sequence=
                              ['green','gold','red','beige'],
                             title="the education level among the ranges of age")
            st.plotly_chart(fig1,use_container_width=True)
            
            fig2=px.histogram(data_frame=df,x="age_cat",color="currentSmoker",template="presentation"
                    ,text_auto=True,barmode="group",labels={"age_cat":"categories of age"},
                    category_orders={"age_cat":["age(30-40)","age(41-50)","age(51-60)","age(61-70)"],
                                   "currentSmoker":["Yes","No"]},color_discrete_sequence=['green','gold','red'],
                             title="what is the number of smokers in every range of age ")
            st.plotly_chart(fig2,use_container_width=True)
        
            fig5=px.histogram(data_frame=df,x="age_cat",color="prevalentHyp",template="presentation"
            ,text_auto=True,barmode="group",labels={"age_cat":"categories of age"},
            category_orders={"age_cat":["age(30-40)","age(41-50)","age(51-60)","age(61-70)"],
                           "prevalentHyp":["Yes","No"]},color_discrete_sequence=['green','gold','red'],
                     title="people that have prevalent hypertension among the ranges of age")
            st.plotly_chart(fig5,use_container_width=True)
        
            fig7=px.histogram(data_frame=df,x="age_cat",color="totChol_cat",template="presentation"
            ,text_auto=True,barmode="group",labels={"age_cat":"categories of age","totChol_cat":"categories of total cholestral"},
            category_orders={"age_cat":["age(30-40)","age(41-50)","age(51-60)","age(61-70)"],
                           "totChol_cat":["Desirable",'BorderLine',"High"]},color_discrete_sequence=['green','gold','red'],
                     title="people that have high Cholestral among the ranges of age")
        
            st.plotly_chart(fig7,use_container_width=True)
            fig9=px.histogram(data_frame=df,x="age_cat",color="BMI_cat",template="presentation"
            ,text_auto=True,barmode="group",labels={"age_cat":"categories of age","BMI_cat":"categories of BMI"},
            category_orders={"age_cat":["age(30-40)","age(41-50)","age(51-60)","age(61-70)"],
                           "BMI_cat":['Underweight','Normal Weight','Overweight','Obese (Class 1)','Obese (Class 2)','Obese (Class 3)']},
                              color_discrete_sequence=['green','gold','red','beige','purple'],
                     title="people that have overweight among the ranges of age")
            st.plotly_chart(fig9,use_container_width=True)
            fig11=px.histogram(data_frame=df,x="age_cat",color="glucose_cat",template="presentation"
            ,text_auto=True,barmode="group",labels={"age_cat":"categories of age","glucose_cat":"categories of glucose"},
            category_orders={"age_cat":["age(30-40)","age(41-50)","age(51-60)","age(61-70)"]}, 
                              color_discrete_sequence=['green','gold','red'],
                     title="check glucose for people among the ranges of age")
            st.plotly_chart(fig11,use_container_width=True)
        
    
    with col2:   
                fig3=px.histogram(data_frame=df,x="age_cat",color="BPMeds",template="presentation"
                        ,text_auto=True,barmode="group",labels={"age_cat":"categories of age"},
                        category_orders={"age_cat":["age(30-40)","age(41-50)","age(51-60)","age(61-70)"],
                                       "BPMeds":["Yes","No"]},color_discrete_sequence=['green','gold','red'],
                                 title="people that take blood pressure medication in every range of age")
                st.plotly_chart(fig3,use_container_width=True)
                
                fig4=px.histogram(data_frame=df,x="age_cat",color="prevalentStroke",template="presentation"
                        ,text_auto=True,barmode="group",labels={"age_cat":"categories of age"},
                        category_orders={"age_cat":["age(30-40)","age(41-50)","age(51-60)","age(61-70)"],
                                       "prevalentStroke":["Yes","No"]},color_discrete_sequence=['green','gold','red'],
                                 title="people that have prevalent stroke among the ranges of age")
                st.plotly_chart(fig4,use_container_width=True)
                fig6=px.histogram(data_frame=df,x="age_cat",color="diabetes",template="presentation"
            ,text_auto=True,barmode="group",labels={"age_cat":"categories of age"},
            category_orders={"age_cat":["age(30-40)","age(41-50)","age(51-60)","age(61-70)"],
                           "diabetes":["Yes","No"]},color_discrete_sequence=['green','gold','red'],
                     title="people that have diabetes among the ranges of age")
                st.plotly_chart(fig6,use_container_width=True)
        
                fig8=px.histogram(data_frame=df,x="age_cat",color="BP_Cat",template="presentation"
            ,text_auto=True,barmode="group",labels={"age_cat":"categories of age","BP_Cat":"categories of blood pressure"},
            category_orders={"age_cat":["age(30-40)","age(41-50)","age(51-60)","age(61-70)"],
                           "BP_Cat":['Low (Hypotension)','Normal','Elevated','High (Hypertension Stage 1)',
                                 'High (Hypertension Stage 2)','Hypertensive Crisis (Seek Medical Attention)']},color_discrete_sequence=
                                  ['green','gold','red','beige','purple'],
                     title="check blood pressure for people among the ranges of age")
        
                st.plotly_chart(fig8,use_container_width=True)
                fig10=px.histogram(data_frame=df,x="age_cat",color="heartRate_cat",template="presentation"
            ,text_auto=True,barmode="group",labels={"age_cat":"categories of age","heartRate_cat":"categories of heart rate"},
            category_orders={"age_cat":["age(30-40)","age(41-50)","age(51-60)","age(61-70)"]
                           ,"heartRate_cat":["Bradycardia (Low)","Normal","Tachycardia (High)"]}, 
                              color_discrete_sequence=['green','gold','red'],
                     title="check people that have Bradycardia and<br> Tachycardia among the ranges of age")
                             
                st.plotly_chart(fig10,use_container_width=True)
                fig12=px.histogram(data_frame=df,x="age_cat",color="TenYearCHD",template="presentation"
            ,text_auto=True,barmode="group",labels={"age_cat":"categories of age"},
            category_orders={"age_cat":["age(30-40)","age(41-50)","age(51-60)","age(61-70)"],"TenYearCHD":["Yes","No"]},
                              color_discrete_sequence=['green','gold','red'],
                     title="Which Age Range Has the Highest Predicted Risk of Coronary<br> Heart Disease in the Next Ten Years")
                st.plotly_chart(fig12,use_container_width=True)
        
def totChol_BiAnalysis():
    st.markdown("<h3>Cholesterol Categories & Ranges</h3>", unsafe_allow_html=True) 
    cholesterol_data = [
    {"category": "Desirable", "range": "Less than 200 mg/dL", "color": "green"},
    {"category": "BorderLine", "range": "200-239 mg/dL", "color": "orange"},
    {"category": "High", "range": "240 mg/dL and above", "color": "red"},
    
     ]
    # Arrange data in columns for better visualization
    cols = st.columns(2)

    for index, item in enumerate(cholesterol_data):
        with cols[index % 2]:  # Distribute items across two columns
            if item["color"] == "green":
                st.success(f"**{item['category']}**\n\nRange: {item['range']}")
            elif item["color"] == "orange":
                st.warning(f"**{item['category']}**\n\nRange: {item['range']}")
            elif item["color"] == "red":
                st.error(f"**{item['category']}**\n\nRange: {item['range']}")
            else:
                st.info(f"**{item['category']}**\n\nRange: {item['range']}")
    col1,col2=st.columns(2)
    with col1:
        fig1=px.histogram(data_frame=df,x="totChol_cat",color="age_cat",template="presentation",
            text_auto=True,barmode="group",labels={"totChol_cat":"Categories Of Total Cholestral","age_cat":"categories of age"},
             category_orders={"totChol_cat":["Desirable","BorderLine","High"],"age_cat":["age(30-40)","age(41-50)","age(51-60)","age(61-70)"]},
                              color_discrete_sequence=["green","gold","red","beige","pruple"],
                  title="how the ranges of ages distributed<br>among the categories of cholestral")
        st.plotly_chart(fig1,use_container_width=True)
        fig3=px.histogram(data_frame=df,x="totChol_cat",color="currentSmoker",template="presentation",
            text_auto=True,barmode="group",labels={"totChol_cat":"Categories Of Total Cholestral"},
             category_orders={"totChol_cat":["Desirable","BorderLine","High"],"currentSmoker":["Yes","No"]},
                              color_discrete_sequence=["green","gold","red","beige","pruple"],
                  title="current smokers<br>among the categories of cholestral")
        st.plotly_chart(fig3,use_container_width=True)
        
        fig5=px.histogram(data_frame=df,x="totChol_cat",color="prevalentStroke",template="presentation",
            text_auto=True,barmode="group",labels={"totChol_cat":"Categories Of Total Cholestral"},
             category_orders={"totChol_cat":["Desirable","BorderLine","High"],"prevalentStroke":["Yes","No"]},
                              color_discrete_sequence=["green","gold","red","beige","pruple"],
                  title="people that have stroke among the<br>categories of cholestral")
        st.plotly_chart(fig5,use_container_width=True)
        fig7=px.histogram(data_frame=df,x="totChol_cat",color="diabetes",template="presentation",
            text_auto=True,barmode="group",labels={"totChol_cat":"Categories Of Total Cholestral"},
             category_orders={"totChol_cat":["Desirable","BorderLine","High"],"diabetes":["Yes","No"]},
                              color_discrete_sequence=["green","gold","red","beige","pruple"],
                  title="people that have diabetes among the<br>categories of cholestral")
        st.plotly_chart(fig7,use_container_width=True)
        
        fig9=px.histogram(data_frame=df,x="totChol_cat",color="BMI_cat",template="presentation",
            text_auto=True,barmode="group",labels={"totChol_cat":"Categories Of Total Cholestral","BMI_cat":"BMI categories"},
             category_orders={"totChol_cat":["Desirable","BorderLine","High"],
                             "BMI_cat":['Underweight','Normal Weight','Overweight','Obese (Class 1)','Obese (Class 2)','Obese (Class 3)']},
                              color_discrete_sequence=["green","gold","red","beige","purple","brown"],
                  title="BMI categories among the<br>categories of cholestral")
        st.plotly_chart(fig9,use_container_width=True)

        
        fig11=px.histogram(data_frame=df,x="totChol_cat",color="glucose_cat",template="presentation",
            text_auto=True,barmode="group",labels={"totChol_cat":"Categories Of Total Cholestral","glucose_cat":"gulcose categories"},
             category_orders={"totChol_cat":["Desirable","BorderLine","High"]},
                              color_discrete_sequence=["green","gold","red","beige","purple","brown"],
                  title="glucose categories among the<br>categories of cholestral")
        st.plotly_chart(fig11,use_container_width=True)
        
    with col2:
        fig2=px.histogram(data_frame=df,x="totChol_cat",color="education_cat",template="presentation",
            text_auto=True,barmode="group",labels={"totChol_cat":"Categories Of Total Cholestral","education_cat":"categories of education"},
             category_orders={"totChol_cat":["Desirable","BorderLine","High"],"education_cat":
                                                        ["low level","intermediate level","high level","advanced level"]},
            color_discrete_sequence=["green","gold","red","beige","pruple"],title="how the education levels distributed<br>among the categories of cholestral")
        st.plotly_chart(fig2,use_container_width=True)
        
        fig4=px.histogram(data_frame=df,x="totChol_cat",color="BPMeds",template="presentation",
            text_auto=True,barmode="group",labels={"totChol_cat":"Categories Of Total Cholestral"},
             category_orders={"totChol_cat":["Desirable","BorderLine","High"],"BPMeds":["Yes","No"]},
                              color_discrete_sequence=["green","gold","red","beige","pruple"],
                  title="people that take blood pressure medication<br>among the categories of cholestral")
        st.plotly_chart(fig4,use_container_width=True)
        
        fig6=px.histogram(data_frame=df,x="totChol_cat",color="prevalentHyp",template="presentation",
            text_auto=True,barmode="group",labels={"totChol_cat":"Categories Of Total Cholestral"},
             category_orders={"totChol_cat":["Desirable","BorderLine","High"],"prevalentHyp":["Yes","No"]},
                              color_discrete_sequence=["green","gold","red","beige","pruple"],
                  title="people that have Hypertension among the<br>categories of cholestral")
        st.plotly_chart(fig6,use_container_width=True)
        fig8=px.histogram(data_frame=df,x="totChol_cat",color="BP_Cat",template="presentation",
            text_auto=True,barmode="group",labels={"totChol_cat":"Categories Of Total Cholestral","BP_Cat":"blood pressure categories"},
             category_orders={"totChol_cat":["Desirable","BorderLine","High"],
                             "BP_Cat":['Low (Hypotension)','Normal','Elevated','High (Hypertension Stage 1)',
                                 'High (Hypertension Stage 2)','Hypertensive Crisis (Seek Medical Attention)']},
                              color_discrete_sequence=["green","gold","red","beige","purple"],
                  title="blood pressure categories among the<br>categories of cholestral")
        st.plotly_chart(fig8,use_container_width=True)
        fig10=px.histogram(data_frame=df,x="totChol_cat",color="heartRate_cat",template="presentation",
            text_auto=True,barmode="group",labels={"totChol_cat":"Categories Of Total Cholestral","heartRate_cat":"heart rate categories"},
             category_orders={"totChol_cat":["Desirable","BorderLine","High"],
                             "heartRate_cat":["Bradycardia (Low)","Normal","Tachycardia (High)"]},
                              color_discrete_sequence=["green","gold","red","beige","purple","brown"],
                  title="heart rate categories among the<br>categories of cholestral")
        st.plotly_chart(fig10,use_container_width=True)
        
        fig12=px.histogram(data_frame=df,x="totChol_cat",color="TenYearCHD",template="presentation",
            text_auto=True,barmode="group",labels={"totChol_cat":"Categories Of Total Cholestral"},
             category_orders={"totChol_cat":["Desirable","BorderLine","High"],
                             "TenYearCHD":["Yes","No"]},
                              color_discrete_sequence=["green","gold","red","beige","purple","brown"],
                  title="Is high cholestral affect coronary heart disease")
        st.plotly_chart(fig12,use_container_width=True)


##########################################################################################

def bloodPressure_BiAnalysis():
    st.markdown("<h3>   Blood Pressure Categories & Ranges</h3>", unsafe_allow_html=True)
    bp_categories = [
        {"category": "Low (Hypotension)", "range": "Sys: <90 | Dia: <60", "color": "blue"},
        {"category": "Normal", "range": "Sys: 90-119 | Dia: 60-79", "color": "green"},
        {"category": "Elevated", "range": "Sys: 120-129 | Dia: <80", "color": "orange"},
        {"category": "High (Hypertension Stage 1)", "range": "Sys: 130-139 | Dia: 80-89", "color": "red"},
        {"category": "High (Hypertension Stage 2)", "range": "Sys: 140-179 | Dia: 90-119", "color": "darkred"},
        {"category": "Hypertensive Crisis", "range": "Sys: ≥180 | Dia: ≥120", "color": "purple"},
    ]

    

    # Arrange categories in columns for better visualization
    cols = st.columns(2)

    for index, item in enumerate(bp_categories):
        with cols[index % 2]:  # Distribute items across two columns
            if item["color"] == "green":
                st.success(f"**{item['category']}**\n\nRange: {item['range']}")
            elif item["color"] == "orange":
                st.warning(f"**{item['category']}**\n\nRange: {item['range']}")
            elif item["color"] == "red" or item["color"] == "darkred":
                st.error(f"**{item['category']}**\n\nRange: {item['range']}")
            elif item["color"] == "blue":
                st.info(f"**{item['category']}**\n\nRange: {item['range']}")
            elif item["color"] == "purple":
                st.error(f"**{item['category']}**\n\nRange: {item['range']}", icon="⚠️")
    col1, col2 = st.columns(2)
    with col1:
        fig1 = px.histogram(data_frame=df, x="BP_Cat", color="age_cat", template="presentation",
                            text_auto=True, barmode="group",
                            labels={"BP_Cat": "Categories Of Blood Pressure", "age_cat": "categories of age"},
                            category_orders={"BP_Cat": ['Low (Hypotension)', 'Normal', 'Elevated',
                                                        'High (Hypertension Stage 1)',
                                                        'High (Hypertension Stage 2)',
                                                        'Hypertensive Crisis (Seek Medical Attention)'],
                                             "age_cat": ["age(30-40)", "age(41-50)", "age(51-60)", "age(61-70)"]},
                            color_discrete_sequence=["green", "gold", "red", "beige", "pruple"],
                            title="how the ranges of ages distributed<br>among the categories of Blood Pressure")
        st.plotly_chart(fig1, use_container_width=True)
        fig3 = px.histogram(data_frame=df, x="BP_Cat", color="currentSmoker", template="presentation",
                            text_auto=True, barmode="group", labels={"BP_Cat": "Categories Of Blood Pressure"},
                            category_orders={"BP_Cat": ['Low (Hypotension)', 'Normal', 'Elevated',
                                                        'High (Hypertension Stage 1)',
                                                        'High (Hypertension Stage 2)',
                                                        'Hypertensive Crisis (Seek Medical Attention)'],
                                             "currentSmoker": ["Yes", "No"]},
                            color_discrete_sequence=["green", "gold", "red", "beige", "pruple"],
                            title="current smokers<br>among the categories of Blood Pressure")
        st.plotly_chart(fig3, use_container_width=True)

        fig5 = px.histogram(data_frame=df, x="BP_Cat", color="prevalentStroke", template="presentation",
                            text_auto=True, barmode="group", labels={"BP_Cat": "Categories Of Blood Pressure"},
                            category_orders={"BP_Cat": ['Low (Hypotension)', 'Normal', 'Elevated',
                                                        'High (Hypertension Stage 1)',
                                                        'High (Hypertension Stage 2)',
                                                        'Hypertensive Crisis (Seek Medical Attention)'],
                                             "prevalentStroke": ["Yes", "No"]},
                            color_discrete_sequence=["green", "gold", "red", "beige", "pruple"],
                            title="people that have stroke among the<br>categories of Blood Pressure")
        st.plotly_chart(fig5, use_container_width=True)
        fig7 = px.histogram(data_frame=df, x="BP_Cat", color="diabetes", template="presentation",
                            text_auto=True, barmode="group", labels={"BP_Cat": "Categories Of Blood Pressure"},
                            category_orders={"BP_Cat": ['Low (Hypotension)', 'Normal', 'Elevated',
                                                        'High (Hypertension Stage 1)',
                                                        'High (Hypertension Stage 2)',
                                                        'Hypertensive Crisis (Seek Medical Attention)'],
                                             "diabetes": ["Yes", "No"]},
                            color_discrete_sequence=["green", "gold", "red", "beige", "pruple"],
                            title="people that have diabetes among the<br>categories of Blood pressure")
        st.plotly_chart(fig7, use_container_width=True)

        fig9 = px.histogram(data_frame=df, x="BP_Cat", color="BMI_cat", template="presentation",
                            text_auto=True, barmode="group",
                            labels={"BP_Cat": "Categories Of Blood Pressure", "BMI_cat": "BMI categories"},
                            category_orders={"BP_Cat": ['Low (Hypotension)', 'Normal', 'Elevated',
                                                        'High (Hypertension Stage 1)',
                                                        'High (Hypertension Stage 2)',
                                                        'Hypertensive Crisis (Seek Medical Attention)'],
                                             "BMI_cat": ['Underweight', 'Normal Weight', 'Overweight',
                                                         'Obese (Class 1)', 'Obese (Class 2)', 'Obese (Class 3)']},
                            color_discrete_sequence=["green", "gold", "red", "beige", "purple", "brown"],
                            title="BMI categories among the<br>categories of Blood Pressure")
        st.plotly_chart(fig9, use_container_width=True)

        fig11 = px.histogram(data_frame=df, x="BP_Cat", color="glucose_cat", template="presentation",
                             text_auto=True, barmode="group", labels={"BP_Cat": "Categories Of Blood Pressure",
                                                                      "glucose_cat": "gulcose categories"},
                             category_orders={"BP_Cat": ['Low (Hypotension)', 'Normal', 'Elevated',
                                                        'High (Hypertension Stage 1)',
                                                        'High (Hypertension Stage 2)',
                                                        'Hypertensive Crisis (Seek Medical Attention)']},
                             color_discrete_sequence=["green", "gold", "red", "beige", "purple", "brown"],
                             title="glucose categories among the<br>categories of Blood Pressure")
        st.plotly_chart(fig11, use_container_width=True)

    with col2:
        fig2 = px.histogram(data_frame=df, x="BP_Cat", color="education_cat", template="presentation",
                            text_auto=True, barmode="group", labels={"BP_Cat": "Categories Of Blood Pressure",
                                                                     "education_cat": "categories of education"},
                            category_orders={"BP_Cat": ['Low (Hypotension)', 'Normal', 'Elevated',
                                                        'High (Hypertension Stage 1)',
                                                        'High (Hypertension Stage 2)',
                                                        'Hypertensive Crisis (Seek Medical Attention)'], "education_cat":
                                ["low level", "intermediate level", "high level", "advanced level"]},
                            color_discrete_sequence=["green", "gold", "red", "beige", "pruple"],
                            title="how the education levels distributed<br>among the categories of Blood Pressure")
        st.plotly_chart(fig2, use_container_width=True)

        fig4 = px.histogram(data_frame=df, x="BP_Cat", color="BPMeds", template="presentation",
                            text_auto=True, barmode="group", labels={"BP_Cat": "Categories Of Blood Pressure"},
                            category_orders={"BP_Cat": ['Low (Hypotension)', 'Normal', 'Elevated',
                                                        'High (Hypertension Stage 1)',
                                                        'High (Hypertension Stage 2)',
                                                        'Hypertensive Crisis (Seek Medical Attention)'],
                                             "BPMeds": ["Yes", "No"]},
                            color_discrete_sequence=["green", "gold", "red", "beige", "pruple"],
                            title="people that take blood pressure medication<br>among the categories of blood pressure")
        st.plotly_chart(fig4, use_container_width=True)

        fig6 = px.histogram(data_frame=df, x="BP_Cat", color="prevalentHyp", template="presentation",
                            text_auto=True, barmode="group", labels={"BP_Cat": "Categories Of Blood Pressure"},
                            category_orders={"BP_Cat": ['Low (Hypotension)', 'Normal', 'Elevated',
                                                        'High (Hypertension Stage 1)',
                                                        'High (Hypertension Stage 2)',
                                                        'Hypertensive Crisis (Seek Medical Attention)'],
                                             "prevalentHyp": ["Yes", "No"]},
                            color_discrete_sequence=["green", "gold", "red", "beige", "pruple"],
                            title="people that have Hypertension among the<br>categories of blood pressure")
        st.plotly_chart(fig6, use_container_width=True)
        fig8 = px.histogram(data_frame=df, x="BP_Cat", color="totChol_cat", template="presentation",
                            text_auto=True, barmode="group", labels={"totChol_cat": "Categories Of Total Cholestral",
                                                                     "BP_Cat": "blood pressure categories"},
                            category_orders={"totChol_cat": ["Desirable", "BorderLine", "High"],
                                             "BP_Cat": ['Low (Hypotension)', 'Normal', 'Elevated',
                                                        'High (Hypertension Stage 1)',
                                                        'High (Hypertension Stage 2)',
                                                        'Hypertensive Crisis (Seek Medical Attention)']},
                            color_discrete_sequence=["green", "gold", "red", "beige", "purple"],
                            title="cholestral categories among the<br>categories of blood pressure")
        st.plotly_chart(fig8, use_container_width=True)
        fig10 = px.histogram(data_frame=df, x="BP_Cat", color="heartRate_cat", template="presentation",
                             text_auto=True, barmode="group", labels={"BP_Cat": "Categories Of Blood Pressure",
                                                                      "heartRate_cat": "heart rate categories"},
                             category_orders={"BP_Cat": ['Low (Hypotension)', 'Normal', 'Elevated',
                                                        'High (Hypertension Stage 1)',
                                                        'High (Hypertension Stage 2)',
                                                        'Hypertensive Crisis (Seek Medical Attention)'],
                                              "heartRate_cat": ["Bradycardia (Low)", "Normal", "Tachycardia (High)"]},
                             color_discrete_sequence=["green", "gold", "red", "beige", "purple", "brown"],
                             title="heart rate categories among the<br>categories of blood pressure")
        st.plotly_chart(fig10, use_container_width=True)

        fig12 = px.histogram(data_frame=df, x="BP_Cat", color="TenYearCHD", template="presentation",
                             text_auto=True, barmode="group", labels={"BP_Cat": "Categories Of Blood Pressure"},
                             category_orders={"BP_Cat": ['Low (Hypotension)', 'Normal', 'Elevated',
                                                        'High (Hypertension Stage 1)',
                                                        'High (Hypertension Stage 2)',
                                                        'Hypertensive Crisis (Seek Medical Attention)'],
                                              "TenYearCHD": ["Yes", "No"]},
                             color_discrete_sequence=["green", "gold", "red", "beige", "purple", "brown"],
                             title="Is blood pressure affect coronary heart disease")
        st.plotly_chart(fig12, use_container_width=True)


##########################################################################3
    

def BMI_BiAnalysis():
    st.markdown("<h3>BMI Categories & Ranges</h3>", unsafe_allow_html=True)
    bmi_categories = [
        {"category": "Underweight", "range": "BMI < 18.5", "color": "blue"},
        {"category": "Normal Weight", "range": "BMI 18.5 - 24.9", "color": "green"},
        {"category": "Overweight", "range": "BMI 25 - 29.9", "color": "orange"},
        {"category": "Obese (Class 1)", "range": "BMI 30 - 34.9", "color": "red"},
        {"category": "Obese (Class 2)", "range": "BMI 35 - 39.9", "color": "darkred"},
        {"category": "Obese (Class 3)", "range": "BMI ≥ 40", "color": "purple"},
    ]

    

    # Arrange categories in columns for better visualization
    cols = st.columns(2)

    for index, item in enumerate(bmi_categories):
        with cols[index % 2]:  # Distribute items across two columns
            if item["color"] == "green":
                st.success(f"**{item['category']}**\n\nRange: {item['range']}")
            elif item["color"] == "orange":
                st.warning(f"**{item['category']}**\n\nRange: {item['range']}")
            elif item["color"] in ["red", "darkred"]:
                st.error(f"**{item['category']}**\n\nRange: {item['range']}")
            elif item["color"] == "blue":
                st.info(f"**{item['category']}**\n\nRange: {item['range']}")
            elif item["color"] == "purple":
                st.error(f"**{item['category']}**\n\nRange: {item['range']}", icon="⚠️")

    col1, col2 = st.columns(2)
    with col1:
        fig1 = px.histogram(data_frame=df, x="BMI_cat", color="age_cat", template="presentation",
                            text_auto=True, barmode="group",
                            labels={"BMI_cat":"categories of BMI", "age_cat": "categories of age"},
                            category_orders={"BMI_cat":['Underweight','Normal Weight','Overweight','Obese (Class 1)','Obese (Class 2)','Obese (Class 3)'],
                                             "age_cat": ["age(30-40)", "age(41-50)", "age(51-60)", "age(61-70)"]},
                            color_discrete_sequence=["green", "gold", "red", "beige", "pruple"],
                            title="how the ranges of ages distributed<br>among the categories of BMI")
        st.plotly_chart(fig1, use_container_width=True)
        fig3 = px.histogram(data_frame=df, x="BMI_cat", color="currentSmoker", template="presentation",
                            text_auto=True, barmode="group", labels={"BMI_cat": "Categories of BMI"},
                            category_orders={"BMI_cat":['Underweight','Normal Weight','Overweight','Obese (Class 1)','Obese (Class 2)','Obese (Class 3)'],
                                             "currentSmoker": ["Yes", "No"]},
                            color_discrete_sequence=["green", "gold", "red", "beige", "pruple"],
                            title="current smokers<br>among the categories of BMI")
        st.plotly_chart(fig3, use_container_width=True)

        fig5 = px.histogram(data_frame=df, x="BMI_cat", color="prevalentStroke", template="presentation",
                            text_auto=True, barmode="group", labels={"BMI_cat": "Categories Of BMI"},
                            category_orders={"BMI_cat":['Underweight','Normal Weight','Overweight','Obese (Class 1)','Obese (Class 2)','Obese (Class 3)'],
                                             "prevalentStroke": ["Yes", "No"]},
                            color_discrete_sequence=["green", "gold", "red", "beige", "pruple"],
                            title="people that have stroke among the<br>categories of BMI")
        st.plotly_chart(fig5, use_container_width=True)
        fig7 = px.histogram(data_frame=df, x="BMI_cat", color="diabetes", template="presentation",
                            text_auto=True, barmode="group", labels={"BMI_cat": "Categories Of BMI"},
                            category_orders={"BMI_cat":['Underweight','Normal Weight','Overweight','Obese (Class 1)','Obese (Class 2)','Obese (Class 3)'],
                                             "diabetes": ["Yes", "No"]},
                            color_discrete_sequence=["green", "gold", "red", "beige", "pruple"],
                            title="people that have diabetes among the<br>categories of BMI")
        st.plotly_chart(fig7, use_container_width=True)

        fig9 = px.histogram(data_frame=df, x="BMI_cat", color="BP_Cat", template="presentation",
                            text_auto=True, barmode="group",
                            labels={"BP_Cat": "Categories Of Blood Pressure", "BMI_cat": "BMI categories"},
                            category_orders={"BP_Cat": ['Low (Hypotension)', 'Normal', 'Elevated',
                                                        'High (Hypertension Stage 1)',
                                                        'High (Hypertension Stage 2)',
                                                        'Hypertensive Crisis (Seek Medical Attention)'],
                                             "BMI_cat": ['Underweight', 'Normal Weight', 'Overweight',
                                                         'Obese (Class 1)', 'Obese (Class 2)', 'Obese (Class 3)']},
                            color_discrete_sequence=["green", "gold", "red", "beige", "purple", "brown"],
                            title="Blood pressure categories among the<br>categories of BMI")
        st.plotly_chart(fig9, use_container_width=True)

        fig11 = px.histogram(data_frame=df, x="BMI_cat", color="glucose_cat", template="presentation",
                             text_auto=True, barmode="group", labels={"BMI_cat": "Categories Of BMI",
                                                                      "glucose_cat": "gulcose categories"},
                             category_orders={"BMI_cat":['Underweight','Normal Weight','Overweight','Obese (Class 1)','Obese (Class 2)','Obese (Class 3)']},
                             color_discrete_sequence=["green", "gold", "red", "beige", "purple", "brown"],
                             title="glucose categories among the<br>categories of BMI")
        st.plotly_chart(fig11, use_container_width=True)

    with col2:
        fig2 = px.histogram(data_frame=df, x="BMI_cat", color="education_cat", template="presentation",
                            text_auto=True, barmode="group", labels={"BMI_cat": "Categories Of BMI",
                                                                     "education_cat": "categories of education"},
                            category_orders={"BMI_cat":['Underweight','Normal Weight','Overweight','Obese (Class 1)','Obese (Class 2)','Obese (Class 3)'], "education_cat":
                                ["low level", "intermediate level", "high level", "advanced level"]},
                            color_discrete_sequence=["green", "gold", "red", "beige", "pruple"],
                            title="how the education levels distributed<br>among the categories of Blood Pressure")
        st.plotly_chart(fig2, use_container_width=True)

        fig4 = px.histogram(data_frame=df, x="BMI_cat", color="BPMeds", template="presentation",
                            text_auto=True, barmode="group", labels={"BMI_cat": "Categories Of BMI"},
                            category_orders={"BMI_cat":['Underweight','Normal Weight','Overweight','Obese (Class 1)','Obese (Class 2)','Obese (Class 3)'],
                                             "BPMeds": ["Yes", "No"]},
                            color_discrete_sequence=["green", "gold", "red", "beige", "pruple"],
                            title="people that take blood pressure medication<br>among the categories of BMI")
        st.plotly_chart(fig4, use_container_width=True)

        fig6 = px.histogram(data_frame=df, x="BMI_cat", color="prevalentHyp", template="presentation",
                            text_auto=True, barmode="group", labels={"BMI_cat": "Categories Of BMI"},
                            category_orders={"BMI_cat":['Underweight','Normal Weight','Overweight','Obese (Class 1)','Obese (Class 2)','Obese (Class 3)'],
                                             "prevalentHyp": ["Yes", "No"]},
                            color_discrete_sequence=["green", "gold", "red", "beige", "pruple"],
                            title="people that have Hypertension among the<br>categories of BMI")
        st.plotly_chart(fig6, use_container_width=True)
        fig8 = px.histogram(data_frame=df, x="BMI_cat", color="totChol_cat", template="presentation",
                            text_auto=True, barmode="group", labels={"totChol_cat": "Categories Of Total Cholestral",
                                                                     "BMI_cat": "BMI categories"},
                            category_orders={"totChol_cat": ["Desirable", "BorderLine", "High"],
                                             "BMI_cat":['Underweight','Normal Weight','Overweight','Obese (Class 1)','Obese (Class 2)','Obese (Class 3)']},
                            color_discrete_sequence=["green", "gold", "red", "beige", "purple"],
                            title="cholestral categories among the<br>categories of BMI")
        st.plotly_chart(fig8, use_container_width=True)
        fig10 = px.histogram(data_frame=df, x="BMI_cat", color="heartRate_cat", template="presentation",
                             text_auto=True, barmode="group", labels={"BMI_cat": "Categories Of BMI",
                                                                      "heartRate_cat": "heart rate categories"},
                             category_orders={"BMI_cat":['Underweight','Normal Weight','Overweight','Obese (Class 1)','Obese (Class 2)','Obese (Class 3)'],
                                              "heartRate_cat": ["Bradycardia (Low)", "Normal", "Tachycardia (High)"]},
                             color_discrete_sequence=["green", "gold", "red", "beige", "purple", "brown"],
                             title="heart rate categories among the<br>categories of BMI")
        st.plotly_chart(fig10, use_container_width=True)

        fig12 = px.histogram(data_frame=df, x="BMI_cat", color="TenYearCHD", template="presentation",
                             text_auto=True, barmode="group", labels={"BMI_cat": "Categories Of BMI"},
                             category_orders={"BMI_cat":['Underweight','Normal Weight','Overweight','Obese (Class 1)','Obese (Class 2)','Obese (Class 3)'],
                                              "TenYearCHD": ["Yes", "No"]},
                             color_discrete_sequence=["green", "gold", "red", "beige", "purple", "brown"],
                             title="Is overweight affect coronary heart disease")
        st.plotly_chart(fig12, use_container_width=True)


    



############################################################################

def heartRate_BiAnalysis():
    st.markdown("<h3>Heart Rate Categories & Ranges</h3>", unsafe_allow_html=True)
    # Define heart rate categories and ranges
    heart_rate_categories = [
        {"category": "Bradycardia (Low)", "range": "HR < 60 bpm", "color": "blue"},
        {"category": "Normal", "range": "HR 60 - 100 bpm", "color": "green"},
        {"category": "Tachycardia (High)", "range": "HR > 100 bpm", "color": "red"},
    ]

    

    # Arrange categories in columns for better visualization
    cols = st.columns(2)

    for index, item in enumerate(heart_rate_categories):
        with cols[index % 2]:  # Distribute items across two columns
            if item["color"] == "green":
                st.success(f"**{item['category']}**\n\nRange: {item['range']}")
            elif item["color"] == "red":
                st.error(f"**{item['category']}**\n\nRange: {item['range']}")
            elif item["color"] == "blue":
                st.info(f"**{item['category']}**\n\nRange: {item['range']}")

    col1, col2 = st.columns(2)
    with col1:
        fig1 = px.histogram(data_frame=df, x="heartRate_cat", color="age_cat", template="presentation",
                            text_auto=True, barmode="group",
                            labels={"heartRate_cat":"categories of heart rate", "age_cat": "categories of age"},
                            category_orders={"heartRate_cat":["Bradycardia (Low)","Normal","Tachycardia (High)"],
                                             "age_cat": ["age(30-40)", "age(41-50)", "age(51-60)", "age(61-70)"]},
                            color_discrete_sequence=["green", "gold", "red", "beige", "pruple"],
                            title="how the ranges of ages distributed<br>among the categories of heart rate")
        st.plotly_chart(fig1, use_container_width=True)
        fig3 = px.histogram(data_frame=df, x="heartRate_cat", color="currentSmoker", template="presentation",
                            text_auto=True, barmode="group", labels={"heartRate_cat": "Categories of heart rate"},
                            category_orders={"heartRate_cat":["Bradycardia (Low)","Normal","Tachycardia (High)"],
                                             "currentSmoker": ["Yes", "No"]},
                            color_discrete_sequence=["green", "gold", "red", "beige", "pruple"],
                            title="current smokers<br>among the categories of heart rate")
        st.plotly_chart(fig3, use_container_width=True)

        fig5 = px.histogram(data_frame=df, x="heartRate_cat", color="prevalentStroke", template="presentation",
                            text_auto=True, barmode="group", labels={"heartRate_cat": "Categories Of heart rate"},
                            category_orders={"heartRate_cat":["Bradycardia (Low)","Normal","Tachycardia (High)"],
                                             "prevalentStroke": ["Yes", "No"]},
                            color_discrete_sequence=["green", "gold", "red", "beige", "pruple"],
                            title="people that have stroke among the<br>categories of heart rate")
        st.plotly_chart(fig5, use_container_width=True)
        fig7 = px.histogram(data_frame=df, x="heartRate_cat", color="diabetes", template="presentation",
                            text_auto=True, barmode="group", labels={"heartRate_cat": "Categories Of heart rate"},
                            category_orders={"heartRate_cat":["Bradycardia (Low)","Normal","Tachycardia (High)"],
                                             "diabetes": ["Yes", "No"]},
                            color_discrete_sequence=["green", "gold", "red", "beige", "pruple"],
                            title="people that have diabetes among the<br>categories of heart rate")
        st.plotly_chart(fig7, use_container_width=True)

        fig9 = px.histogram(data_frame=df, x="heartRate_cat", color="BP_Cat", template="presentation",
                            text_auto=True, barmode="group",
                            labels={"BP_Cat": "Categories Of Blood Pressure", "heartRate_cat": "heart rate categories"},
                            category_orders={"BP_Cat": ['Low (Hypotension)', 'Normal', 'Elevated',
                                                        'High (Hypertension Stage 1)',
                                                        'High (Hypertension Stage 2)',
                                                        'Hypertensive Crisis (Seek Medical Attention)'],
                                             "heartRate_cat":["Bradycardia (Low)","Normal","Tachycardia (High)"]},
                            color_discrete_sequence=["green", "gold", "red", "beige", "purple", "brown"],
                            title="Blood pressure categories among the<br>categories of heart rate")
        st.plotly_chart(fig9, use_container_width=True)

        fig11 = px.histogram(data_frame=df, x="heartRate_cat", color="glucose_cat", template="presentation",
                             text_auto=True, barmode="group", labels={"heartRate_cat": "Categories Of heart rate",
                                                                      "glucose_cat": "gulcose categories"},
                             category_orders={"heartRate_cat":["Bradycardia (Low)","Normal","Tachycardia (High)"]},
                             color_discrete_sequence=["green", "gold", "red", "beige", "purple", "brown"],
                             title="glucose categories among the<br>categories of heart rate")
        st.plotly_chart(fig11, use_container_width=True)

    with col2:
        fig2 = px.histogram(data_frame=df, x="heartRate_cat", color="education_cat", template="presentation",
                            text_auto=True, barmode="group", labels={"heartRate_cat": "Categories Of heart rate",
                                                                     "education_cat": "categories of education"},
                            category_orders={"heartRate_cat":["Bradycardia (Low)","Normal","Tachycardia (High)"], "education_cat":
                                ["low level", "intermediate level", "high level", "advanced level"]},
                            color_discrete_sequence=["green", "gold", "red", "beige", "pruple"],
                            title="how the education levels distributed<br>among the categories of heart rate")
        st.plotly_chart(fig2, use_container_width=True)

        fig4 = px.histogram(data_frame=df, x="heartRate_cat", color="BPMeds", template="presentation",
                            text_auto=True, barmode="group", labels={"heartRate_cat": "Categories Of heart rate"},
                            category_orders={"heartRate_cat":["Bradycardia (Low)","Normal","Tachycardia (High)"],
                                             "BPMeds": ["Yes", "No"]},
                            color_discrete_sequence=["green", "gold", "red", "beige", "pruple"],
                            title="people that take blood pressure medication<br>among the categories of heart rate")
        st.plotly_chart(fig4, use_container_width=True)

        fig6 = px.histogram(data_frame=df, x="heartRate_cat", color="prevalentHyp", template="presentation",
                            text_auto=True, barmode="group", labels={"BMI_cat": "Categories Of heart rate"},
                            category_orders={"heartRate_cat":["Bradycardia (Low)","Normal","Tachycardia (High)"],
                                             "prevalentHyp": ["Yes", "No"]},
                            color_discrete_sequence=["green", "gold", "red", "beige", "pruple"],
                            title="people that have Hypertension among the<br>categories of heart rate")
        st.plotly_chart(fig6, use_container_width=True)
        fig8 = px.histogram(data_frame=df, x="heartRate_cat", color="totChol_cat", template="presentation",
                            text_auto=True, barmode="group", labels={"totChol_cat": "Categories Of Total Cholestral",
                                                                     "heartRate_cat": "heart rate categories"},
                            category_orders={"totChol_cat": ["Desirable", "BorderLine", "High"],
                                             "heartRate_cat":["Bradycardia (Low)","Normal","Tachycardia (High)"]},
                            color_discrete_sequence=["green", "gold", "red", "beige", "purple"],
                            title="cholestral categories among the<br>categories of heart rate")
        st.plotly_chart(fig8, use_container_width=True)
        fig10 = px.histogram(data_frame=df, x="heartRate_cat", color="BMI_cat", template="presentation",
                             text_auto=True, barmode="group", labels={"BMI_cat": "Categories Of BMI",
                                                                      "heartRate_cat": "heart rate categories"},
                             category_orders={"BMI_cat":['Underweight','Normal Weight','Overweight','Obese (Class 1)','Obese (Class 2)','Obese (Class 3)'],
                                              "heartRate_cat": ["Bradycardia (Low)", "Normal", "Tachycardia (High)"]},
                             color_discrete_sequence=["green", "gold", "red", "beige", "purple", "brown"],
                             title="BMI categories among the<br>categories of heart rate")
        st.plotly_chart(fig10, use_container_width=True)

        fig12 = px.histogram(data_frame=df, x="heartRate_cat", color="TenYearCHD", template="presentation",
                             text_auto=True, barmode="group", labels={"heartRate_cat": "Categories Of heart rate"},
                             category_orders={"heartRate_cat":["Bradycardia (Low)","Normal","Tachycardia (High)"],
                                              "TenYearCHD": ["Yes", "No"]},
                             color_discrete_sequence=["green", "gold", "red", "beige", "purple", "brown"],
                             title="is higher or lower heart rate affect coronary heart disease")
        st.plotly_chart(fig12, use_container_width=True)




###########################################################################

def glucose_BiAnalysis():
    st.markdown("<h3>Glucose Categories & Ranges</h3>", unsafe_allow_html=True)
    # Define heart rate categories and ranges
    glucose_categories = [
        {"category": "Normal", "range": "Fasting Glucose < 100 mg/dL", "color": "green"},
        {"category": "Prediabetes", "range": "Fasting Glucose 100 - 125 mg/dL", "color": "orange"},
        {"category": "Diabetes", "range": "Fasting Glucose ≥ 126 mg/dL", "color": "red"},
    ]

    

    # Arrange categories in columns for better visualization
    cols = st.columns(2)

    for index, item in enumerate(glucose_categories):
        with cols[index % 2]:  # Distribute items across two columns
            if item["color"] == "green":
                st.success(f"**{item['category']}**\n\nRange: {item['range']}")
            elif item["color"] == "orange":
                st.warning(f"**{item['category']}**\n\nRange: {item['range']}")
            elif item["color"] == "red":
                st.error(f"**{item['category']}**\n\nRange: {item['range']}")

    col1, col2 = st.columns(2)
    with col1:
        fig1 = px.histogram(data_frame=df, x="glucose_cat", color="age_cat", template="presentation",
                            text_auto=True, barmode="group",
                            labels={"glucose_cat":"categories of glucose", "age_cat": "categories of age"},
                            category_orders={
                                             "age_cat": ["age(30-40)", "age(41-50)", "age(51-60)", "age(61-70)"]},
                            color_discrete_sequence=["green", "gold", "red", "beige", "pruple"],
                            title="how the ranges of ages distributed<br>among the categories of glucose")
        st.plotly_chart(fig1, use_container_width=True)
        fig3 = px.histogram(data_frame=df, x="glucose_cat", color="currentSmoker", template="presentation",
                            text_auto=True, barmode="group", labels={"glucose_cat": "Categories of glucose"},
                            category_orders={
                                             "currentSmoker": ["Yes", "No"]},
                            color_discrete_sequence=["green", "gold", "red", "beige", "pruple"],
                            title="current smokers<br>among the categories of glucose")
        st.plotly_chart(fig3, use_container_width=True)

        fig5 = px.histogram(data_frame=df, x="glucose_cat", color="prevalentStroke", template="presentation",
                            text_auto=True, barmode="group", labels={"glucose_cat": "Categories Of glucose"},
                            category_orders={
                                             "prevalentStroke": ["Yes", "No"]},
                            color_discrete_sequence=["green", "gold", "red", "beige", "pruple"],
                            title="people that have stroke among the<br>categories of glucose")
        st.plotly_chart(fig5, use_container_width=True)
        fig7 = px.histogram(data_frame=df, x="glucose_cat", color="diabetes", template="presentation",
                            text_auto=True, barmode="group", labels={"glucose_cat": "Categories Of glucose"},
                            category_orders={
                                             "diabetes": ["Yes", "No"]},
                            color_discrete_sequence=["green", "gold", "red", "beige", "pruple"],
                            title="people that have diabetes among the<br>categories of glucose")
        st.plotly_chart(fig7, use_container_width=True)

        fig9 = px.histogram(data_frame=df, x="glucose_cat", color="BP_Cat", template="presentation",
                            text_auto=True, barmode="group",
                            labels={"BP_Cat": "Categories Of Blood Pressure", "glucose_cat": "glucose categories"},
                            category_orders={"BP_Cat": ['Low (Hypotension)', 'Normal', 'Elevated',
                                                        'High (Hypertension Stage 1)',
                                                        'High (Hypertension Stage 2)',
                                                        'Hypertensive Crisis (Seek Medical Attention)']},
                            color_discrete_sequence=["green", "gold", "red", "beige", "purple", "brown"],
                            title="Blood pressure categories among the<br>categories of glucose")
        st.plotly_chart(fig9, use_container_width=True)

        fig11 = px.histogram(data_frame=df, x="glucose_cat", color="heartRate_cat", template="presentation",
                             text_auto=True, barmode="group", labels={"heartRate_cat": "Categories Of heart rate",
                                                                      "glucose_cat": "gulcose categories"},
                             category_orders={"heartRate_cat":["Bradycardia (Low)","Normal","Tachycardia (High)"]},
                             color_discrete_sequence=["green", "gold", "red", "beige", "purple", "brown"],
                             title="heart rate categories among the<br>categories of glucose")
        st.plotly_chart(fig11, use_container_width=True)

    with col2:
        fig2 = px.histogram(data_frame=df, x="glucose_cat", color="education_cat", template="presentation",
                            text_auto=True, barmode="group", labels={"glucose_cat": "Categories Of glucose",
                                                                     "education_cat": "categories of education"},
                            category_orders={"education_cat":
                                ["low level", "intermediate level", "high level", "advanced level"]},
                            color_discrete_sequence=["green", "gold", "red", "beige", "pruple"],
                            title="how the education levels distributed<br>among the categories of glucose")
        st.plotly_chart(fig2, use_container_width=True)

        fig4 = px.histogram(data_frame=df, x="glucose_cat", color="BPMeds", template="presentation",
                            text_auto=True, barmode="group", labels={"glucose_cat": "Categories Of glucose"},
                            category_orders={
                                             "BPMeds": ["Yes", "No"]},
                            color_discrete_sequence=["green", "gold", "red", "beige", "pruple"],
                            title="people that take blood pressure medication<br>among the categories of glucose")
        st.plotly_chart(fig4, use_container_width=True)

        fig6 = px.histogram(data_frame=df, x="glucose_cat", color="prevalentHyp", template="presentation",
                            text_auto=True, barmode="group", labels={"glucose_cat": "Categories Of glucose"},
                            category_orders={
                                             "prevalentHyp": ["Yes", "No"]},
                            color_discrete_sequence=["green", "gold", "red", "beige", "pruple"],
                            title="people that have Hypertension among the<br>categories of glucose")
        st.plotly_chart(fig6, use_container_width=True)
        fig8 = px.histogram(data_frame=df, x="glucose_cat", color="totChol_cat", template="presentation",
                            text_auto=True, barmode="group", labels={"totChol_cat": "Categories Of Total Cholestral",
                                                                     "glucose_cat": "glucose categories"},
                            category_orders={"totChol_cat": ["Desirable", "BorderLine", "High"]
                                             },
                            color_discrete_sequence=["green", "gold", "red", "beige", "purple"],
                            title="cholestral categories among the<br>categories of glucose")
        st.plotly_chart(fig8, use_container_width=True)
        fig10 = px.histogram(data_frame=df, x="glucose_cat", color="BMI_cat", template="presentation",
                             text_auto=True, barmode="group", labels={"BMI_cat": "Categories Of BMI",
                                                                      "glucose_cat": "glucose categories"},
                             category_orders={"BMI_cat":['Underweight','Normal Weight','Overweight','Obese (Class 1)','Obese (Class 2)','Obese (Class 3)']
                                              },
                             color_discrete_sequence=["green", "gold", "red", "beige", "purple", "brown"],
                             title="BMI categories among the<br>categories of glucose")
        st.plotly_chart(fig10, use_container_width=True)

        fig12 = px.histogram(data_frame=df, x="glucose_cat", color="TenYearCHD", template="presentation",
                             text_auto=True, barmode="group", labels={"glucose_cat": "Categories Of glucose"},
                             category_orders={
                                              "TenYearCHD": ["Yes", "No"]},
                             color_discrete_sequence=["green", "gold", "red", "beige", "purple", "brown"],
                             title="is high glucose affect coronary heart disease")
        st.plotly_chart(fig12, use_container_width=True)




#############################################################################


def TenYearCHD_BiAnalysis():
    st.markdown("<h3>Predict Coronary Heart Disease Risk In The Next 10 Years</h3>", unsafe_allow_html=True)
    # Define heart rate categories and ranges
    chd_risk_categories = [
        {"category": "Low Risk (No)","count":"3596", "range": "10-year risk = 85%", "color": "green"},
        {"category": "High Risk (Yes)","count":"644", "range": "10-year risk = 15%", "color": "red"},
    ]

    
    cols = st.columns(2)

    for index, item in enumerate(chd_risk_categories):
        with cols[index % 2]: 
        # Display categories with color-coded messages
            if item["color"] == "green":
                st.success(f"**{item['category']}**\n\nCount: {item['count']}\n\nRange: {item['range']}")
            elif item["color"] == "yellow":
                st.warning(f"**{item['category']}**\n\nCount: {item['count']}\n\nRange: {item['range']}")
            elif item["color"] == "red":
                st.error(f"**{item['category']}**\n\nCount: {item['count']}\n\nRange: {item['range']}")

    col1, col2 = st.columns(2)
    with col1:
        fig1 = px.histogram(data_frame=df, x="TenYearCHD", color="age_cat", template="presentation",
                            text_auto=True, barmode="group",
                            labels={"age_cat": "categories of age"},
                            category_orders={
                                             "age_cat": ["age(30-40)", "age(41-50)", "age(51-60)", "age(61-70)"],"TenYearCHD":["Yes","No"]},
                            color_discrete_sequence=["green", "gold", "red", "beige", "pruple"],
                            title="predict heart coronary risk<br>according to the age")
        st.plotly_chart(fig1, use_container_width=True)
        fig3 = px.histogram(data_frame=df, x="TenYearCHD", color="currentSmoker", template="presentation",
                            text_auto=True, barmode="group",
                            category_orders={
                                             "currentSmoker": ["Yes", "No"],"TenYearCHD":["Yes","No"]},
                            color_discrete_sequence=["green", "gold", "red", "beige", "pruple"],
                            title="predict heart coronary risk<br>according to smokers")
        st.plotly_chart(fig3, use_container_width=True)

        fig5 = px.histogram(data_frame=df, x="TenYearCHD", color="prevalentStroke", template="presentation",
                            text_auto=True, barmode="group",
                            category_orders={
                                             "prevalentStroke": ["Yes", "No"],"TenYearCHD":["Yes","No"]},
                            color_discrete_sequence=["green", "gold", "red", "beige", "pruple"],
                            title="predict heart coronary risk<br>according to stroke")
        st.plotly_chart(fig5, use_container_width=True)

        fig7 = px.histogram(data_frame=df, x="TenYearCHD", color="diabetes", template="presentation",
                            text_auto=True, barmode="group",
                            category_orders={
                                             "diabetes": ["Yes", "No"],"TenYearCHD":["Yes","No"]},
                            color_discrete_sequence=["green", "gold", "red", "beige", "pruple"],
                            title="predict heart coronary risk<br>according to diabetes")
        st.plotly_chart(fig7, use_container_width=True)

        fig9 = px.histogram(data_frame=df, x="TenYearCHD", color="BP_Cat", template="presentation",
                            text_auto=True, barmode="group",
                            labels={"BP_Cat": "Categories Of Blood Pressure"},
                            category_orders={"BP_Cat": ['Low (Hypotension)', 'Normal', 'Elevated',
                                                        'High (Hypertension Stage 1)',
                                                        'High (Hypertension Stage 2)',
                                                        'Hypertensive Crisis (Seek Medical Attention)'],"TenYearCHD":["Yes","No"]},
                            color_discrete_sequence=["green", "gold", "red", "beige", "purple", "brown"],
                            title="predict heart coronary risk<br>according to blood pressure")
        st.plotly_chart(fig9, use_container_width=True)

        fig11 = px.histogram(data_frame=df, x="TenYearCHD", color="heartRate_cat", template="presentation",
                             text_auto=True, barmode="group", labels={"heartRate_cat": "Categories Of heart rate"},
                                                                      
                             category_orders={"heartRate_cat":["Bradycardia (Low)","Normal","Tachycardia (High)"],"TenYearCHD":["Yes","No"]},
                             color_discrete_sequence=["green", "gold", "red", "beige", "purple", "brown"],
                             title="predict heart coronary risk<br>according to heart rate")
        st.plotly_chart(fig11, use_container_width=True)

    with col2:
        fig2 = px.histogram(data_frame=df, x="TenYearCHD", color="education_cat", template="presentation",
                            text_auto=True, barmode="group", labels={
                                                                     "education_cat": "categories of education"},
                            category_orders={"education_cat":
                                ["low level", "intermediate level", "high level", "advanced level"],"TenYearCHD":["Yes","No"]},
                            color_discrete_sequence=["green", "gold", "red", "beige", "pruple"],
                            title="predict heart coronary risk<br>according to education level")
        st.plotly_chart(fig2, use_container_width=True)

        fig4 = px.histogram(data_frame=df, x="TenYearCHD", color="BPMeds", template="presentation",
                            text_auto=True, barmode="group",
                            category_orders={
                                             "BPMeds": ["Yes", "No"],"TenYearCHD":["Yes","No"]},
                            color_discrete_sequence=["green", "gold", "red", "beige", "pruple"],
                            title="predict heart coronary risk<br>for people that take blood pressure medication")
        st.plotly_chart(fig4, use_container_width=True)

        fig6 = px.histogram(data_frame=df, x="TenYearCHD", color="prevalentHyp", template="presentation",
                            text_auto=True, barmode="group",
                            category_orders={
                                             "prevalentHyp": ["Yes", "No"],"TenYearCHD":["Yes","No"]},
                            color_discrete_sequence=["green", "gold", "red", "beige", "pruple"],
                            title="predict heart coronary risk<br>according to people that have hypertension")
        st.plotly_chart(fig6, use_container_width=True)
        fig8 = px.histogram(data_frame=df, x="TenYearCHD", color="totChol_cat", template="presentation",
                            text_auto=True, barmode="group", labels={"totChol_cat": "Categories Of Total Cholestral"
                                                                     },
                            category_orders={"totChol_cat": ["Desirable", "BorderLine", "High"],"TenYearCHD":["Yes","No"]
                                             },
                            color_discrete_sequence=["green", "gold", "red", "beige", "purple"],
                            title="predict heart coronary risk<br>according to cholestral")
        st.plotly_chart(fig8, use_container_width=True)
        
        fig10 = px.histogram(data_frame=df, x="TenYearCHD", color="BMI_cat", template="presentation",
                             text_auto=True, barmode="group", labels={"BMI_cat": "Categories Of BMI"
                                                                      },
                             category_orders={"BMI_cat":['Underweight','Normal Weight','Overweight','Obese (Class 1)','Obese (Class 2)','Obese (Class 3)'],
                                              "TenYearCHD": ["Yes", "No"]
                                              },
                             color_discrete_sequence=["green", "gold", "red", "beige", "purple", "brown"],
                             title="predict heart coronary risk<br>according to BMI(overweight)")
        st.plotly_chart(fig10, use_container_width=True)

        fig12 = px.histogram(data_frame=df, x="TenYearCHD", color="glucose_cat", template="presentation",
                             text_auto=True, barmode="group", labels={"glucose_cat": "Categories Of glucose"},
                             category_orders={
                                              "TenYearCHD": ["Yes", "No"]},
                             color_discrete_sequence=["green", "gold", "red", "beige", "purple", "brown"],
                             title="predict heart coronary risk<br>according to glucose")
        st.plotly_chart(fig12, use_container_width=True)


#####################################################################


def make_agregationFunct():
    feature=st.selectbox("select a numeric feature",['age', 'cigsPerDay', 'totChol', 'sysBP', 'diaBP', 'BMI',
       'heartRate', 'glucose'],index=0)
    st.write()
    st.write()
    if feature=="cigsPerDay":
        min_value=df[df[feature]>0][feature].min()
        avg_value=round(df[df[feature]>0][feature].mean(),2)
        max_value=df[df[feature]>0][feature].max()
    else:
        min_value=df[feature].min()
        avg_value=round(df[feature].mean(),2)
        max_value=df[feature].max()
        
    st.write()
    col1,col2,col3=st.columns(3)
    with col1:
        
        st.markdown(f"<h4>min: {min_value} </h4>", unsafe_allow_html=True)
    with col2:
        
        st.markdown(f"<h4>average: {avg_value}</h4>", unsafe_allow_html=True)
    with col3:
        
        st.markdown(f"<h4>max: {max_value} </h4>", unsafe_allow_html=True)
    st.divider()
  
    st.markdown(f"<h4>Overview about data that has a minmium value </h4>", unsafe_allow_html=True)
    st.dataframe(df[df[feature]==min_value])
    st.divider()
    st.markdown(f"<h4>Overview about data that has a maxmium value </h4>", unsafe_allow_html=True)
    st.dataframe(df[df[feature]==max_value])


    


        







########################################################################

def page2():
    
    st.title("Coronary Heart Disease Analysis")
    tab1,tab2,tab3,tab4,tab5=st.tabs(["Feature Insights","Metrics Overview","Feature Relationships","Deep Discovery","Ten-Year CHD Breakdown"])
    with tab1:
        col1,col2=st.columns(2)
        with col1:
            fig1=px.histogram(data_frame=df,y="gender",text_auto=True,color_discrete_sequence=['green'],template='presentation',
                              title="Distribution of gender",orientation="h")
            st.plotly_chart(fig1,use_container_width=True)
            
            fig2=px.histogram(data_frame=df,y="age_cat",text_auto=True,template="presentation",color_discrete_sequence=["green"],
                             title='Distribution of age',labels={"age_cat":"categories of age"},orientation="h")
            st.plotly_chart(fig2,use_container_width=True)
            
            fig3=px.histogram(df, y='education_cat', title='Education Level Distribution',
             category_orders={"education_cat": ['low level', 'intermediate level', 'high level', 'advanced level']},
             labels={'education_cat': 'Education Level', 'count': 'Count'},
             text_auto=True,template="presentation",color_discrete_sequence=['green'],orientation="h")
            st.plotly_chart(fig3,use_container_width=True)
            
            fig4=px.histogram(data_frame=df,y="currentSmoker",text_auto=True,template="presentation",
                             color_discrete_sequence=['green'],category_orders={"currentSmoker":["Yes","No"]}
                              ,title="Analysis of Individuals Who Smoke Currently",orientation="h")
            st.plotly_chart(fig4,use_container_width=True)

        
            

        

        
        with col2:
            fig1=px.pie(data_frame=df,names="gender",color_discrete_sequence=['green','gold'],template='presentation')
            st.plotly_chart(fig1,use_container_width=True)
            
            fig2=px.pie(data_frame=df,names="age_cat",color_discrete_sequence=["green","gold"],template='presentation')
            st.plotly_chart(fig2,use_container_width=True)
            
            fig3=px.pie(data_frame=df,names="education_cat",color_discrete_sequence=['green','gold'],template='presentation')
            st.plotly_chart(fig3,use_container_width=True)
            fig4=px.pie(data_frame=df,names="currentSmoker",template="presentation",
                        color_discrete_sequence=['green','gold'],category_orders={"currentSmoker":["Yes","No"]})
            st.plotly_chart(fig4,use_container_width=True)
        fig_5=px.histogram(data_frame=df,x="cigsPerDay",text_auto=True,
            labels={"cigsPerDay":"Cigrattes Per Day"},template="presentation",title="Howmany cigrattes per day",
                          color_discrete_sequence=["green"])
        st.plotly_chart(fig_5,use_container_width=True)

        col1,col2=st.columns(2)
        with col1:
            fig6=px.histogram(data_frame=df,y="BPMeds",text_auto=True,template='presentation',
            labels={"BPMeds":"Blood Pressure Medication"},color_discrete_sequence=['green']
                              ,title="what is the number of indvidual that take blood pressure medication",
                             category_orders={"BPMeds":["Yes","No"]},orientation="h")
            st.plotly_chart(fig6,use_container_width=True)
            fig7=px.histogram(data_frame=df,y="prevalentStroke",text_auto=True,template='presentation',
            labels={"prevalentStroke":"prevalent Stroke"},color_discrete_sequence=['green'],title='Do individuals have a prevalent stroke or not',
                            category_orders={"prevalentStroke":["Yes","No"]},orientation="h" )
            st.plotly_chart(fig7,use_container_width=True)
            
            fig8=px.histogram(data_frame=df,y="prevalentHyp",text_auto=True,template='presentation',
            labels={"prevalentHyp":"prevalent Hypertension"},color_discrete_sequence=['green'],title='Do individuals have a prevalent hypertension or not',
                            category_orders={"prevalentHyp":["Yes","No"]},orientation="h" )
            st.plotly_chart(fig8,use_container_width=True)
            
            fig9=px.histogram(data_frame=df,y="diabetes",text_auto=True,template='presentation'
            ,color_discrete_sequence=['green'],title='Do individuals have a diabetes or not',
                            category_orders={"diabetes":["Yes","No"]},orientation="h" )
            st.plotly_chart(fig9,use_container_width=True)
            
        with col2:
            fig6=px.pie(data_frame=df,names='BPMeds',template='presentation',color_discrete_sequence=['green','gold'])
            st.plotly_chart(fig6,use_container_width=True)
            fig7=px.pie(data_frame=df,names='prevalentStroke',template="presentation",color_discrete_sequence=['green','gold'],
                       category_orders={"prevalentStroke":["Yes","No"]})
            st.plotly_chart(fig7,use_container_width=True)
            fig8=px.pie(data_frame=df,names='prevalentHyp',template="presentation",color_discrete_sequence=['green','gold'],
                       category_orders={"prevalentHyp":["Yes","No"]})
            st.plotly_chart(fig8,use_container_width=True)
            
            fig9=px.pie(data_frame=df,names='diabetes',template="presentation",color_discrete_sequence=['green','gold'],
                       category_orders={"diabetes":["Yes","No"]})
            st.plotly_chart(fig9,use_container_width=True)

        
        fig = px.histogram(df, x="totChol", 
                   marginal="violin",  # Can also use "rug" or "box"
                   histnorm='density',  # Normalize to show density
                   title="Distribution of Total Cholestral",
                   color_discrete_sequence=["green"])
        st.plotly_chart(fig,use_container_width=True)
        col1,col2=st.columns(2)
        with col1:
            fig10=px.histogram(data_frame=df,y="totChol_cat",text_auto=True,
            category_orders={"totChol_cat":["Desirable","BorderLine","High"]},template="presentation",
            labels={"totChol_cat":"Categories Of Total Cholestral"},title="distribution of cholestral",color_discrete_sequence=["green","gold"],
                              orientation="h")
            st.plotly_chart(fig10,use_container_width=True)
        with col2:
            fig10=px.pie(data_frame=df,names="totChol_cat",template="presentation",category_orders={"totChol_cat":["Desirable","BorderLine","High"]},
            color_discrete_sequence=['green','gold'])
            st.plotly_chart(fig10,use_container_width=True)
        fig = px.histogram(df, x=['sysBP', 'diaBP'], 
                   barmode='overlay', 
                   title="Distribution of Systolic & Diastolic BP",
                   color_discrete_map={'sysBP': 'green', 'diaBP': 'gold'})
        st.plotly_chart(fig,use_container_width=True)
        
        col1,col2=st.columns(2)
        with col1:
            fig11=px.histogram(data_frame=df,y="BP_Cat",text_auto=True,
             category_orders={"BP_Cat":['Low (Hypotension)',"Normal","Elevated","High (Hypertension Stage 1)","High (Hypertension Stage 2)",
                                        "Hypertensive Crisis (Seek Medical Attention)"]},
             template="presentation",
            labels={"BP_Cat":"Categories Of Blood Pressure"},color_discrete_sequence=["green","gold","red"],
                              title="distribution of blood pressure",orientation="h")
            st.plotly_chart(fig11,use_container_width=True)
        with col2:
            fig11=px.pie(data_frame=df,names="BP_Cat",template="presentation",
                        category_orders={"BP_Cat":['Low (Hypotension)',"Normal","Elevated","High (Hypertension Stage 1)","High (Hypertension Stage 2)",
                                        "Hypertensive Crisis (Seek Medical Attention)"]},color_discrete_sequence=['green','gold','red'])
            st.plotly_chart(fig11,use_container_width=True)
        fig=px.histogram(data_frame=df,x="BMI",text_auto=True,template='presentation',color_discrete_sequence=['green'],
                        title="Distribution of BMI")
        st.plotly_chart(fig,use_container_width=True)
        col1,col2=st.columns(2)
        
        with col1:
            fig12=px.histogram(data_frame=df,y="BMI_cat",template='presentation',text_auto=True,
            labels={"BMI_cat":"Categories Of BMI"},
            category_orders={"BMI_cat":["Underweight","Normal Weight","Overweight",
                                       "Obese (Class 1)","Obese (Class 2)","Obese (Class 3)"]},color_discrete_sequence=['green'],
                              title="Distribution for Categories of BMI",orientation="h")
            st.plotly_chart(fig12,use_container_width=True)
        with col2:
            fig12=px.pie(data_frame=df,names='BMI_cat',title="Categories Of BMI",template='presentation',
                         category_orders={"BMI_cat":["Underweight","Normal Weight","Overweight",
                                       "Obese (Class 1)","Obese (Class 2)","Obese (Class 3)"]},
                         color_discrete_sequence=['green','gold','red']
                        )
            st.plotly_chart(fig12,use_container_width=True)
            
        fig=px.histogram(data_frame=df,x="heartRate",text_auto=True,template='presentation',color_discrete_sequence=['green'],
                        title="Distribution of Heart Rate")
        st.plotly_chart(fig,use_container_width=True)
        col1,col2=st.columns(2)
        with col1:
            fig13=px.histogram(data_frame=df,y="heartRate_cat",template='presentation',text_auto=True,
            category_orders={"heartRate_cat":["Bradycardia (Low)","Normal","Tachycardia (High)"]},
            labels={"heartRate_cat":"Categories Of Heart Rate"},color_discrete_sequence=['green'],title="Distribution for Categories of heart rate",
                              orientation="h")
            st.plotly_chart(fig13,use_container_width=True)
        with col2:
            fig13=px.pie(data_frame=df,names="heartRate_cat",template="presentation",color_discrete_sequence=["green","gold"],
                         category_orders={"heartRate_cat":["Bradycardia (Low)","Normal","Tachycardia (High)"]})
            st.plotly_chart(fig13,use_container_width=True)
        fig=px.histogram(data_frame=df,x="glucose",text_auto=True,template='presentation',color_discrete_sequence=['green'],
                        title="Distribution of glucose")
        st.plotly_chart(fig,use_container_width=True)
        col1,col2=st.columns(2)
        with col1:
            fig14=px.histogram(data_frame=df,y="glucose_cat",text_auto=True,template='presentation',
            labels={"glucose_cat":"categories of glucose"},color_discrete_sequence=['green'],title="distribution for Categories of glucose")
            st.plotly_chart(fig14,use_container_width=True,orientation="h")
        with col2:
            fig14=px.pie(data_frame=df,names="glucose_cat",color_discrete_sequence=['green','gold'],template="presentation")
            st.plotly_chart(fig14,use_container_width=True)
        st.divider()
        col1,col2=st.columns(2)
        with col1:
            fig15=px.histogram(data_frame=df,y="TenYearCHD",template="presentation",text_auto=True,color_discrete_sequence=["green"],
            title="Distribution for coronary heart disease risk in the coming ten years(target column)",category_orders={"TenYearCHD":["Yes","No"]})
            st.plotly_chart(fig15,use_container_width=True,orientation="h")
        with col2:
            fig15=px.pie(data_frame=df,names="TenYearCHD",template="presentation",
                         category_orders={"TenYearCHD":["Yes","No"]},color_discrete_sequence=['green','gold'])
            st.plotly_chart(fig15,use_container_width=True)
        with tab2:
            make_agregationFunct()
            
        with tab3:

            feature=st.selectbox("select a feature",["age","total cholestral","blood pressure","BMI","heart rate","glucose",
                                                    "CHD risk in the nextt 10 years (target column)"],index=0)
            st.divider()
            
            if feature=="age":
                 age_BiAnalysis()
            elif feature=="blood pressure":
                bloodPressure_BiAnalysis()
            elif feature=="BMI":
                BMI_BiAnalysis()
            elif feature=="heart rate":
                heartRate_BiAnalysis()
            elif feature=="glucose":
                glucose_BiAnalysis()
            elif feature=="CHD risk in the nextt 10 years (target column)":
                TenYearCHD_BiAnalysis()
            else:
                totChol_BiAnalysis()
        with tab5:
            st.markdown("<h3>Analyze Accepted Coronary Heart Disease Risk Over the Next Ten Years</h3>", unsafe_allow_html=True)
            st.write()
            my_features=st.multiselect("select your features",['gender', 'age_cat', 'education_cat', 'currentSmoker', 'BPMeds',
                        'prevalentStroke', 'prevalentHyp', 'diabetes', 'totChol_cat',
                 'BP_Cat', 'BMI_cat', 'heartRate_cat', 'glucose_cat'],default=['gender', 'age_cat', 'currentSmoker'])
            fig = px.treemap(
                df[df["TenYearCHD"] == "Yes"], 
                path=my_features,  
                color='currentSmoker', 
                    labels={'currentSmoker': 'Smoker Status (Yes = Current Smoker)',
                    'BPMeds': 'Blood Pressure Medication',
                    'prevalentStroke': 'Stroke (Yes or No)',
                    'prevalentHyp': 'Hypertension Status',
                    'diabetes': 'Diabetes Status',
                    'totChol_cat': 'Total Cholesterol Category',
                    'BP_Cat': 'Blood Pressure Category',
                    'BMI_cat': 'BMI Category',
                    'heartRate_cat': 'Heart Rate Category',
                    'glucose_cat': 'Glucose Category'
                },
                template="presentation", 
                color_discrete_sequence=["orange", "green", "red"],title="Accepted CHD"
            )

            # Adjust layout if needed
            fig.update_layout(
                  margin=dict(t=50, l=25, r=25, b=25),
                  title_font_size=18
                )
                        # Customize layout
            fig.update_layout(
                            height=1000,
                            width=1100,
                            margin=dict(t=50, l=25, r=25, b=25),
                            title_font_size=18
                        )
                        
            st.plotly_chart(fig,use_container_width=True)
            st.divider()
            number_of_rows=st.number_input("enter number of rows",value=5, key="num_input_2")
            st.markdown(f"<h4>Accepted CHD Risk: {df[df["TenYearCHD"]=="Yes"].shape[0]}</h4>", unsafe_allow_html=True)
            st.dataframe(df[df["TenYearCHD"]=="Yes"].head(number_of_rows))
        with tab4:
            st.markdown("<h4>Highest number of cigrattes per day how it is affected</h4>", unsafe_allow_html=True)
            number=st.number_input("enter number of rows",value=5)
            filtered_df=df[((df["cigsPerDay"] == 60) | (df["cigsPerDay"] == 70))]
            st.markdown(f"<h4>total rows: {filtered_df.shape[0]}</h4>", unsafe_allow_html=True)
            st.dataframe(filtered_df.head(number))
            st.divider()


            
            
            
            
            


            
            
            
        
      
        



            
        
            
        


    

# Create a dictionary after defining functions
pages = {
    "Data Overview": page1,
    "Data Analysis": page2
}

# Sidebar for navigation
checkbox_select = st.sidebar.radio("Overview and Detailed Analysis", pages.keys())
gender=st.sidebar.selectbox("Filter by gender",["all","males","females"],index=0)

if gender=="all":
    df=df
elif gender=="males":
    df=df[df["gender"]=="male"]

else:
    df=df[df["gender"]=="female"]

# Call the selected page function
pages[checkbox_select]()
