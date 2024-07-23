import streamlit as st
import pandas as pd
import sqlite3
from sklearn import tree
from sklearn.preprocessing import LabelEncoder

def home():
    st.markdown("# Welcome to our Interest-Predictor")
    st.sidebar.markdown("# Home🏠")

    st.subheader("Enter Your Details in the forms Page of our Website to predict your interest in going to college")

    st.write("In this Session you will build a website that takes values from the user,stores the value in a database and uses the data to predict whether the user will be regular in going to college.")

    st.success("👈Choose the Forms option in the sidebar to predict your result.")
    st.success("👈Choose the Display Stats option to visualize the response of different users.")


def forms():
    st.markdown("# Form📑")
    st.sidebar.markdown("# Form📑")

    skl_type = st.selectbox("Choose your school type:",["Academic","Vocational"])

    interest = st.selectbox("Select How interested are you in going to college?",["Less Interested","Very Interested","Uncertain"])

    residence = st.selectbox("Select your Residence area:",["Urban","Rural"])

    parent_salary = st.number_input("Enter your parent's salary",0)

    percent = st.slider("Enter your Percentage}:",0,100)

    form_submit = st.button("Predict my Values")

    if form_submit:
        conn = sqlite3.connect("data.db")

        df = pd.read_sql_query("SELECT * FROM user_data",conn)

        enc = LabelEncoder()

        for i in df.columns:
            if df[i].dtype == "O":
                df[i] = enc.fit_transform(df[i])

        X = df.iloc[:,:-1]
        Y = df.iloc[:,-1]

        model = tree.DecisionTreeClassifier()
        model = model.fit(X,Y)

        user_data = [skl_type,interest,residence,parent_salary,percent]

        new_df = pd.DataFrame([user_data])

        for i in new_df.columns:
            if new_df[i].dtype == "O":
                new_df[i] = enc.fit_transform(new_df[i])

        predict = model.predict(new_df[new_df.columns])

        if predict == 1:
            st.balloons()
            st.success("You are Expected to maintain attendance")
        
        else:
            st.snow()
            st.error("You are not Expected to maintain attendance")

        try:
            cursor = conn.cursor()
            cursor.execute(f'''INSERT INTO user_data VALUES ('{skl_type}','{interest}','{residence}',{parent_salary},{percent},{predict[0]})''')
            conn.commit()
        except Exception as e:
            print(e)

def data_display():
    st.markdown("# Display Stats📈")
    st.sidebar.markdown("# Display Stats📈")

    conn = sqlite3.connect("data.db")

    df = pd.read_sql_query("SELECT * FROM user_data",conn)

    st.dataframe(df)

    st.subheader("BarChart:")

    st.write("Correlation between resident area and Interest to college")

    st.bar_chart(df,y="parent_salary",x="will_go_to_college")

    st.subheader("LineChart:")

    st.write("Correlation between percentage and parent salary")

    st.line_chart(df,x="percentage",y="parent_salary")


page_names_to_funcs = {
    "Home🏠": home,
    "Forms📑": forms,
    "Data Visualization📈": data_display,
}

selected_page = st.sidebar.selectbox("Select a page", page_names_to_funcs.keys())
page_names_to_funcs[selected_page]()