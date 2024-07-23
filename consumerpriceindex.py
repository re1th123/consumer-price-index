import streamlit as st
import pandas as pd
import sqlite3
from sklearn import tree
from sklearn.preprocessing import LabelEncoder
def home():
    st.markdown("# CONSUMER PRICE INDEX")
    st.sidebar.markdown("# Home🏠")

    st.subheader("Enter the amount of every type")

    st.write("from this we can able to write the consumer price index of the year and inflation in that year gives us change in the price of the product")

    
    st.success("👈To find average price of the type of In the State go to average ")
    st.success("👈enter the values of the prices of sector to know the cpi ")
    st.success("👈to see the data of all the months press the sector visualization  ")



def average():

    st.sidebar.markdown("# AVERAGE")

    st.subheader("AVERAGE PRICE CALCULATOR")

    st.subheader("from this we can able to write the average price of that type in that state")
    st.subheader("Jammu and Kashmir")
    Jammu = st.number_input("Jammu and Kashmir price ",50)
    st.subheader("Himachal Pradesh")
    Himachal = st.number_input("Himachal Pradesh price ",50)
    st.subheader("Punjab")
    p3 = st.number_input("Punjab price ",50)
    st.subheader("Delhi")
    Delhi = st.number_input("Delhi price ",50)
    st.subheader("Rajasthan")
    rajasthan = st.number_input("Rajasthan price ",50)
    st.subheader("Uttar Pradesh")
    Uttar = st.number_input(" Uttar Pradesh price ",50)
    st.subheader("Arunachal Pradesh")
    Arunachal = st.number_input("Arunachal Pradesh price ",50)
    st.subheader("Nagaland")
    p13 = st.number_input("Nagaland price ",50)
    st.subheader("Manipur")
    p14 = st.number_input("Manipur price ",50)
    st.subheader("Mizoram")
    p15 = st.number_input(" Mizoram price ",50)
    st.subheader("Tripura")
    p16 = st.number_input("Tripura price ",50)
    st.subheader("Meghalaya")
    p17 = st.number_input("Meghalaya price ",50)
    st.subheader("Assam")
    p18 = st.number_input("Assam price ",50)
    st.subheader("West Bengal")
    p19 = st.number_input("West Benga price ",50)
    st.subheader("Jharkhand")
    p20 = st.number_input("Jharkhand price ",50)
    st.subheader("Odisha")
    p21 = st.number_input("Odisha price ",50)
    st.subheader("Chhattisgarh")
    p22 = st.number_input("Chhattisgarh price ",50)
    st.subheader("Madhya Pradesh")
    p23 = st.number_input("Madhya Pradesh price ",50)
    st.subheader("Gujarat")
    p24 = st.number_input("Gujarat price ",50)
    st.subheader("Maharashtra")
    p25 = st.number_input("Maharashtra price ",50)
    st.subheader("Andhra Pradesh")
    p26 = st.number_input("Andhra Pradesh price ",50)
    st.subheader("Karnataka")
    p27 = st.number_input("Karnataka price ",50)
    st.subheader("Goa")
    p28 = st.number_input("Goa  price ",50)
    st.subheader("Kerala")
    p29 = st.number_input("Kerala price ",50)
    st.subheader("Tamil Nadu")
    p30 = st.number_input("Tamil Nadu price ",50)
    st.subheader("Telangana")
    p31 = st.number_input("Telangana price ",50)
    
    


    
    sum=Jammu+Himachal+Delhi+rajasthan+p3+Uttar+Arunachal+p13+p14+p15+p16+p17+p18+p19+p20+p21+p22+p23+p24+p25+p26+p27+p28+p29+p30
    avg=sum//30
    st.subheader(avg)

def food():
    st.subheader("Food Stats📈")
    st.sidebar.markdown("# FOOD")
    st.subheader("PLEASE ENTER THE VALUES OF FOOD")
    year=st.number_input("enter the current year",2023)
    month = st.selectbox("Select  the",["JAN","FEB","MAR","APR","MAY","JUN","JUL","AUG","SEP","OCT","NOV","DEC"])
    st.subheader("Cereals_and_products🍚🍚")
    Cereals_and_products = st.number_input("enter the averege price of the Cereals_and_products  in this month ",50)
    st.subheader("meat and fish🥩🍗🍖")
    Meat_and_fish= st.number_input("enter the averege price of the Meat_and_fish in this month ",50) 
    st.subheader("Milk and product🥛🧀")
    milk_and_product = st.number_input("enter the averege price of the milk_and_product in this month ",50) 
    st.subheader("Oils and fats🛢️")
    oils_and_fats = st.number_input("enter the averege price of the oils_and_fats in this month ",50) 
    st.subheader("Fruits🍎🍊🍓")
    Fruits = st.number_input("enter the averege price of the Fruits in this month ",50) 
    st.subheader("Vegetable🥕🍅🫑")
    Vegetable = st.number_input("enter the averege price of the Vegetable in this month ",50) 
    st.subheader("Pulses and products 🌾🌾🌾")
    Pulses_and_products = st.number_input("enter the averege price of the Pulses_and_products in this month ",50) 
    st.subheader("Sugar and Confectionery 🥞🍦")
    Sugar_and_Confectionery= st.number_input("enter the averege price of the Sugar_and_Confectionery in this month ",50) 
    st.subheader("Spices🌶️🌶️🌶️")
    Spices = st.number_input("enter the averege price of the Spices in this month ",50) 
    st.subheader("Prepared meals, snacks, sweets etc🥪🍿🍟")
    Prepared = st.number_input("enter the averege price of the Prepared in this month ",50)
    st.subheader("enter the sum of previous month")
    conn = sqlite3.connect("consumer.db")
    df = pd.read_sql_query("SELECT month,sum_of_fprices FROM food_prices ",conn)
    df_last=df.tail(2)
    st.dataframe(df_last)    
    Pre_fsum = st.number_input("please enter the sum of previous month shown in the food data visualization table",2050)
    food_submit = st.button("submit")
    if food_submit:
        conn = sqlite3.connect("consumer.db")
        ff = pd.read_sql_query("SELECT year,month,sum_of_fprices,cpi FROM food_prices",conn)
        food_prices = [year,month,Cereals_and_products,Meat_and_fish,milk_and_product,oils_and_fats,Fruits,Vegetable,Pulses_and_products,Sugar_and_Confectionery,Spices,Prepared,Pre_fsum]
        st.snow()
        st.success("You are reponses are submitted")
        try:
            cursor = conn.cursor()
            cursor.execute(f'''INSERT INTO food_prices VALUES ({year},'{month}',{Cereals_and_products},{Meat_and_fish},{milk_and_product},{oils_and_fats},{Fruits},{Vegetable},{Pulses_and_products},{Sugar_and_Confectionery},{Spices},{Prepared},{Pre_fsum})''')

            conn.commit()
        except Exception as e:
            print(e)
def food_display():
    st.markdown("# food Stats📈")
    st.sidebar.markdown("# food  Display Stats📈")

    conn = sqlite3.connect("consumer.db")

    df = pd.read_sql_query("SELECT * FROM food_prices",conn)

    st.dataframe(df)

    st.subheader("BarChart:")

    st.subheader("Correlation between cpi changes and  month")

    st.bar_chart(df,y="cpi",x="month")

    st.subheader("LineChart:")

    st.write("line chat of Correlation between cpi changes and  month")

    st.line_chart(df,x="month",y="cpi")
def intoxicants():
    st.subheader("INTOXICANTS SECTOR")
    st.sidebar.markdown("# INTOXICANTS")
    st.write("PLEASE ENTER THE VALUES OF INTOXICANTS")
    year=st.number_input("enter the current year",2023)
    month = st.selectbox("Select  the",["JAN","FEB","MAR","APR","MAY","JUN","JUL","AUG","SEP","OCT","NOV","DEC"])
    st.subheader("intoxicants🍁🍁🍁")
    intoxicants = st.number_input("enter the averege price of the intoxicants in this month ",50)
    st.subheader("pan and ingredients🌿🌿🌿")
    pan_and_ingredients = st.number_input("enter the averege price of the pan_and_ingredients in this month ",50) 
    st.subheader("tobaco products🍾🍺🍻")
    tobaco_products= st.number_input("enter the averege price of the tobaco_products in this month ",50)
    st.write("enter the sum of previous month")
    conn = sqlite3.connect("consumer.db")
    df = pd.read_sql_query("SELECT month,sum_of_iprices FROM intoxicants_prices ",conn)
    df_last=df.tail(2)
    st.dataframe(df_last)
    Pre_isum = st.number_input("please enter the sum of previous month shown in the exercise data visualization table",2200)
    intoxicants_submit = st.button("submit")
    
    
    if intoxicants_submit:
        conn = sqlite3.connect("consumer.db")
        ff = pd.read_sql_query("SELECT * FROM intoxicants_prices",conn)
        intoxicants_prices = [intoxicants,pan_and_ingredients,tobaco_products,Pre_isum]
        st.balloons()
        st.success("You are reponses are submitted")
        try:
            cursor = conn.cursor()
            cursor.execute(f'''INSERT INTO intoxicants_prices VALUES ({year},'{month}',{intoxicants},{pan_and_ingredients},{tobaco_products},{Pre_isum})''')
            conn.commit()
        except Exception as e:
            print(e)
def intoxicants_display():
    st.markdown("# intoxicants Stats📈")    
    st.sidebar.markdown("# intoxicants  Display Stats📈")

    conn = sqlite3.connect("consumer.db")

    df = pd.read_sql_query("SELECT * FROM intoxicants_prices",conn)

    st.dataframe(df)

    st.subheader("BarChart:")

    st.write("Correlation between cpi changes and  month")

    st.bar_chart(df,y="i_cpi",x="month")

    st.subheader("LineChart:")

    st.write("line chat of Correlation between cpi changes and  month")

    st.line_chart(df,x="month",y="i_cpi")
        
def clothandfoot():
    st.subheader("CLOTH AND FOOT SECTOR")
    st.sidebar.markdown("# CLOTH AND FOOT")
    st.write("PLEASE ENTER THE VALUES OF CLOTH AND FOOT")
    year=st.number_input("enter the current year",2023)
    month = st.selectbox("Select  the",["JAN","FEB","MAR","APR","MAY","JUN","JUL","AUG","SEP","OCT","NOV","DEC"])
    st.subheader("cloth👖👔👕")
    cloth= st.number_input("enter the averege price of the cloth in this month ",1000)
    st.subheader("foot🩴👟👠")
    conn = sqlite3.connect("consumer.db")
    df = pd.read_sql_query("SELECT month,sum_of_cprices FROM clothandfoot_prices ",conn)
    df_last=df.tail(2)
    st.dataframe(df_last)
    foot= st.number_input("enter the averege price of the foot in this month ",1000)
    st.write("enter the sum of previous month")
    Pre_csum = st.number_input("please enter the sum of previous month shown in the exercise data visualization table",1800)
    
    clothandfoot_submit = st.button("submit")
    if clothandfoot_submit:
        conn = sqlite3.connect("consumer.db")
        ff = pd.read_sql_query("SELECT * FROM clothandfoot_prices",conn)
        clothandfoot_prices = [cloth,foot,Pre_csum]
        st.snow()
        st.success("You are reponses are submitted")
        try:
            cursor = conn.cursor()
            cursor.execute(f'''INSERT INTO clothandfoot_prices VALUES ('{year}','{month}',{cloth},{foot},{Pre_csum})''')

            conn.commit()
        except Exception as e:
            print(e)
def clothandfoot_display():
    st.markdown("# clothandfoot Stats📈")
    st.sidebar.markdown("# clothandfoot  Display Stats📈")

    conn = sqlite3.connect("consumer.db")

    df = pd.read_sql_query("SELECT year,month,sum_of_cprices,c_cpi FROM clothandfoot_prices",conn)

    st.dataframe(df)

    st.subheader("BarChart:")

    st.write("Correlation between cpi changes and  month")

    st.bar_chart(df,y="c_cpi",x="month")

    st.subheader("LineChart:")

    st.write("line chat of Correlation between cpi changes and  month")

    st.line_chart(df,x="month",y="c_cpi")
def others():
    st.subheader("TRANSPORT EDUCATION HEALTH HOUSING ")
    st.sidebar.markdown("# MISCELLOENOUS")
    st.write("PLEASE ENTER THE VALUES OF SUGGESTED TYPE")
    year=st.number_input("enter the current year",2023)
    month = st.selectbox("Select  the",["JAN","FEB","MAR","APR","MAY","JUN","JUL","AUG","SEP","OCT","NOV","DEC"])
    st.subheader("house rent🏠🏠🏠")
    house_rent= st.number_input("enter the averege price of the house_rent in this month ",500)
    st.subheader("house charges 💵💵💵")
    house_charges= st.number_input("enter the averege price of the house_charges in this month ",500)
    st.subheader("furniture and furnishing 🪵🪜🪵")
    furniture_and_furnishing= st.number_input("enter the averege price of the furniture_and_furnishing in this month ",500)
    st.subheader("bedding🛏️🛏️🛏️")
    bedding= st.number_input("enter the averege price of the bedding in this month ",500)
    st.subheader("household appliances📺🧺")
    household_appliances= st.number_input("enter the averege price of the household_appliances in this month ",500)
    st.subheader("house hold utensils and cookery🥄🍽️🍴")
    house_hold_utensils_and_cookery= st.number_input("enter the averege price of the house_hold_utensils_and_cookery in this month ",500)
    st.subheader("tools equipment for house🔨🛠️🔧")
    tools= st.number_input("enter the averege price of the tools in this month ",500)
    st.subheader("house hold services💧🔌🔋")
    services= st.number_input("enter the averege price of the services in this month ",500)
    st.subheader("health🏥🩻🩺")
    health= st.number_input("enter the averege price of the health in this month ",500)
    st.subheader("transport🚗🚎🚛")
    transport= st.number_input("enter the averege price of the transport in this month ",500)
    st.subheader("recreation and service of items🧑‍🔧🧑‍🔧🧑‍🔧")
    recreation= st.number_input("enter the averege price of the recreation in this month ",500)
    st.subheader("education📚📖🧑‍🏫")
    education= st.number_input("enter the averege price of the education in this month ",500)
    st.subheader("personal care and effects like ornaments rings all makup ...💊💉")
    personal= st.number_input("enter the averege price of the personal in this month ",500)
    st.write("enter the sum of previous month")
    conn = sqlite3.connect("consumer.db")
    df = pd.read_sql_query("SELECT month,sum_of_mprices FROM other_prices ",conn)
    df_last=df.tail(2)
    st.dataframe(df_last)
    Pre_msum = st.number_input("please enter the sum of previous month shown in the exercise data visualization table",40000)
    others_submit = st.button("submit")
    if others_submit:
        conn = sqlite3.connect("consumer.db")
        ff = pd.read_sql_query("SELECT * FROM other_prices",conn)
        others_prices = [house_rent,house_charges,furniture_and_furnishing,bedding,household_appliances,house_hold_utensils_and_cookery,tools,services,health,transport,recreation,education,personal,Pre_msum]
        st.balloons()
        st.success("You are reponses are submitted")
        try:
            cursor = conn.cursor()
            cursor.execute(f'''INSERT INTO other_prices VALUES ('{year}','{month}',{house_rent},{house_charges},{furniture_and_furnishing},{bedding},{household_appliances},{house_hold_utensils_and_cookery},{tools},{services},{health},{transport},{recreation},{education},{personal},{Pre_msum})''')

            conn.commit()
        except Exception as e:
            print(e)
def others_display():
    st.markdown("# others Stats📈")
    st.sidebar.markdown("# others  Display Stats📈")

    conn = sqlite3.connect("consumer.db")

    df = pd.read_sql_query("SELECT * FROM other_prices",conn)

    st.dataframe(df)

    st.subheader("BarChart:")

    st.write("Correlation between cpi changes and  month")

    st.bar_chart(df,y="m_cpi",x="month")

    st.subheader("LineChart:")

    st.write("line chat of Correlation between cpi changes and  month")

    st.line_chart(df,x="month",y="m_cpi")


    st.area_chart(df,x="month",y="m_cpi")


    
page_names_to_funcs = {
    "Home🏠": home,
    "Average":average,
    "Food Sector":food,
    "Food-Data-Visualization":food_display,
    "Execise-Sector":intoxicants,
    "Exercise-Data-Visualization":intoxicants_display,
    "Clothfoot Sector":clothandfoot,
    "Clothandfoot-Data-Visualization":clothandfoot_display,
    "All Sectors":others,
    "Remaining-Data-Visualization":others_display,
    

    
}

selected_page = st.sidebar.selectbox("Select a page", page_names_to_funcs.keys())
page_names_to_funcs[selected_page]()


        