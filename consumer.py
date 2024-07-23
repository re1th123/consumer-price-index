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

    st.success("👈enter the price of the every type")
    st.success("👈to see the line chart and bar graph of the consumerprice index and inflation press at the data visuvalization")
def prices_of_all_sectors():
    year=st.number_input("enter the current year",2023)
    month = st.selectbox("Select  the",["JAN","FEB","MAR","APR","MAY","JUN","JUL","AUG","SEP","OCT","NOV","DEC"])
    st.subheader("food")
    st.write("Cereals and products")
    Cereals_and_products = st.number_input("enter the averege price of the Cereals_and_products  in this month ",50)
    st.write("meat and fish")
    Meat_and_fish= st.number_input("enter the averege price of the Meat_and_fish in this month ",50) 
    st.write("Milk and product")
    milk_and_product = st.number_input("enter the averege price of the milk_and_product in this month ",50) 
    st.write("Oils and fats")
    oils_and_fats = st.number_input("enter the averege price of the oils_and_fats in this month ",50) 
    st.write("Fruits")
    Fruits = st.number_input("enter the averege price of the Fruits in this month ",50) 
    st.write("Vegetable")
    Vegetable = st.number_input("enter the averege price of the Vegetable in this month ",50) 
    st.write("Pulses and products")
    Pulses_and_products = st.number_input("enter the averege price of the Pulses_and_products in this month ",50) 
    st.write("Sugar and Confectionery")
    Sugar_and_Confectionery= st.number_input("enter the averege price of the Sugar_and_Confectionery in this month ",50) 
    st.write("Spices")
    Spices = st.number_input("enter the averege price of the Spices in this month ",50) 
    st.write("Prepared meals, snacks, sweets etc")
    Prepared = st.number_input("enter the averege price of the Prepared in this month ",50)
    st.subheader("intoxicants and tobaco products")
    st.write("intoxicants")
    intoxicants = st.number_input("enter the averege price of the intoxicants in this month ",50)
    st.write("pan and ingredients")
    pan_and_ingredients = st.number_input("enter the averege price of the pan_and_ingredients in this month ",50) 
    st.write("tobaco products")
    tobaco_products= st.number_input("enter the averege price of the tobaco_products in this month ",50)
    
    st.subheader("cloth_and_foot")
    st.write("cloth")
    cloth= st.number_input("enter the averege price of the cloth in this month ",50)
    st.write("foot")
    foot= st.number_input("enter the averege price of the foot in this month ",50)
    st.subheader("housing")
    st.write("house rent")
    house_rent= st.number_input("enter the averege price of the house_rent in this month ",50)
    st.write("house charges")
    house_charges= st.number_input("enter the averege price of the house_charges in this month ",50)
    st.write("furniture and furnishing")
    furniture_and_furnishing= st.number_input("enter the averege price of the furniture_and_furnishing in this month ",50)
    st.write("bedding")
    bedding= st.number_input("enter the averege price of the bedding in this month ",50)
    st.write("household appliances")
    household_appliances= st.number_input("enter the averege price of the household_appliances in this month ",50)
    st.write("house hold utensils and cookery")
    house_hold_utensils_and_cookery= st.number_input("enter the averege price of the house_hold_utensils_and_cookery in this month ",50)
    st.write("tools equipment for house")
    tools= st.number_input("enter the averege price of the tools in this month ",50)
    st.write("house hold services")
    services= st.number_input("enter the averege price of the services in this month ",50)
    st.write("health")
    health= st.number_input("enter the averege price of the health in this month ",50)
    st.write("transport")
    transport= st.number_input("enter the averege price of the transport in this month ",50)
    st.write("recreation and service of items")
    recreation= st.number_input("enter the averege price of the recreation in this month ",50)
    st.write("education")
    education= st.number_input("enter the averege price of the education in this month ",50)
    st.write("personal care and effects like ornaments rings all makup ...")
    personal= st.number_input("enter the averege price of the personal in this month ",50)
    form_submit = st.button("submit")
    if form_submit:
        conn = sqlite3.connect("cpi.db")
        df = pd.read_sql_query("SELECT * FROM Consumer_prices",conn)
        Consumer_prices = [year,month,Cereals_and_products,Meat_and_fish,milk_and_product,oils_and_fats,Fruits,Vegetable,Pulses_and_products,Sugar_and_Confectionery,Spices,Prepared,intoxicants,pan_and_ingredients,tobaco_products,cloth,foot,house_rent,house_charges,furniture_and_furnishing,bedding,household_appliances,house_hold_utensils_and_cookery,tools,services,health,transport,recreation,education,personal]
        st.balloons()
        st.success("You are reponses are submitted")
        try:
            cursor = conn.cursor()
            cursor.execute(f'''INSERT INTO Consumer_prices VALUES ('{year}','{month}',{Cereals_and_products},{Meat_and_fish},{milk_and_product},{oils_and_fats},{Fruits},{Vegetable},{Pulses_and_products},{Sugar_and_Confectionery},{Spices},{Prepared},{intoxicants},{pan_and_ingredients},{tobaco_products},{cloth},{foot},{house_rent},{house_charges},{furniture_and_furnishing},{bedding},{household_appliances},{house_hold_utensils_and_cookery},{tools},{services},{health},{transport},{recreation},{education},{personal})''')

            conn.commit()
        except Exception as e:
            print(e)

        
def data_display():
    st.markdown("# Display Stats📈")
    st.sidebar.markdown("# Display Stats📈")

    conn = sqlite3.connect("cpi.db")

    df = pd.read_sql_query("SELECT year,month,Cereals_and_products,intoxicants,household_appliances,cpi FROM Consumer_prices",conn)

    st.dataframe(df)

    st.subheader("BarChart:")

    st.write("Correlation between cpi changes and  month")

    st.bar_chart(df,y="cpi",x="month")

    st.subheader("LineChart:")

    st.write("line chat of Correlation between cpi changes and  month")

    st.line_chart(df,x="month",y="cpi")

      

    

    
page_names_to_funcs = {
    "Home🏠": home,
    "enter the prices":prices_of_all_sectors,
   "DATA-VISUALIZATION":data_display

    
}

selected_page = st.sidebar.selectbox("Select a page", page_names_to_funcs.keys())
page_names_to_funcs[selected_page]()


