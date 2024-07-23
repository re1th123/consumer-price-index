import calendar  # Core Python Module
from datetime import datetime  # Core Python Module

import plotly.graph_objects as go  # pip install plotly
import streamlit as st  # pip install streamlit
from streamlit_option_menu import option_menu  # pip install streamlit-option-menu

import database as db  # local import

# -------------- SETTINGS ------stra--------
incomes = ["Salary", "Blog", "Other Income"]
expense23= ["Rent", "Utilities", "Groceries", "Car", "Other Expenses", "Saving"]
currency = "USD"
page_title = "Income and Expense Tracker"
page_icon = ":money_with_wings:"  # emojis: https://www.webfx.com/tools/emoji-cheat-sheet/
layout = "centered"
# --------------------------------------

st.set_page_config(page_title=page_title, page_icon=page_icon, layout=layout)
st.title(page_title + " " + page_icon)

# --- DROP DOWN VALUES FOR SELECTING THE PERIOD ---
years = [datetime.today().year, datetime.today().year + 1]
months = list(calendar.month_name[1:])


# --- DATABASE INTERFACE ---
def get_all_periods():
    items = db.fetch_all_periods()
    periods = [item["key"] for item in items]
    return periods


# --- HIDE STREAMLIT STYLE ---
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

# --- NAVIGATION MENU ---
selected = option_menu(
    menu_title=None,
    options=["Data Entry", "Data Visualization"],
    icons=["pencil-fill", "bar-chart-fill"],  # https://icons.getbootstrap.com/
    orientation="horizontal",
)

# --- INPUT & SAVE PERIODS ---
if selected == "Data Entry":
    st.header(f"Data Entry in {currency}")
    with st.form("entry_form", clear_on_submit=True):
        col1, col2 = st.columns(2)
        col1.selectbox("Select Month:", months, key="month")
        col2.selectbox("Select Year:", years, key="year")

        "---"
        with st.expander("Income"):
            for income in incomes:
                st.number_input(f"{income}:", min_value=0, format="%i", step=10, key=income)
        with st.expander("Expenses"):
            for expense in expenses:
                st.number_input(f"{expense}:", min_value=0, format="%i", step=10, key=expense)
        with st.expander("Comment"):
            comment = st.text_area("", placeholder="Enter a comment here ...")

        "---"
        submitted = st.form_submit_button("Save Data")
        if submitted:
            period = str(st.session_state["year"]) + "_" + str(st.session_state["month"])
            incomes = {income: st.session_state[income] for income in incomes}
            expenses = {expense: st.session_state[expense] for expense in expenses}
            db.insert_period(period, incomes, expenses, comment)
            st.success("Data saved!")


# --- PLOT PERIODS ---
if selected == "Data Visualization":
    st.header("Data Visualization")
    with st.form("saved_periods"):
        period = st.selectbox("Select Period:", get_all_periods())
        submitted = st.form_submit_button("Plot Period")
        if submitted:
            # Get data from database
            period_data = db.get_period(period)
            comment = period_data.get("comment")
            expenses = period_data.get("expenses")
            incomes = period_data.get("incomes")

            # Create metrics
            total_income = sum(incomes.values())
            total_expense = sum(expenses.values())
            remaining_budget = total_income - total_expense
            col1, col2, col3 = st.columns(3)
            col1.metric("Total Income", f"{total_income} {currency}")
            col2.metric("Total Expense", f"{total_expense} {currency}")
            col3.metric("Remaining Budget", f"{remaining_budget} {currency}")
            st.text(f"Comment: {comment}")

            # Create sankey chart
            label = list(incomes.keys()) + ["Total Income"] + list(expenses.keys())
            source = list(range(len(incomes))) + [len(incomes)] * len(expenses)
            target = [len(incomes)] * len(incomes) + [label.index(expense) for expense in expenses.keys()]
            value = list(incomes.values()) + list(expenses.values())

            # Data to dict, dict to sankey
            link = dict(source=source, target=target, value=value)
            node = dict(label=label, pad=20, thickness=30, color="#E694FF")
            data = go.Sankey(link=link, node=node)

            # Plot it!
            fig = go.Figure(data)
            fig.update_layout(margin=dict(l=0, r=0, t=5, b=5))
            st.plotly_chart(fig, use_container_width=True)











            def food():
    st.subheader("select the deesired food item")
   
    food_item= st.selectbox("as per the food id",["Cereals and products","Meat and fis","Milk and product","Oils and fats","Fruits","Vegetable","Pulses and products","Sugar and Confectionery","Spices","Prepared meals, snacks, sweets etc"])
    st.subheader("enter the price of selected product")
    food_price = st.number_input("or elese give the average price of the items",0)   
    form_submit = st.button("Submit")
def intoxicants():
    st.subheader("select the deesired product")
   
    intoxicants_item= st.selectbox("as per the  id",["intoxicants","pan and ingredients","tobaco products"])
    st.subheader("enter the price of selected product")
    intoxicants_price = st.number_input("or elese give the average price of the items",0)
    form_submit = st.button("Submit")     
def clothfoot():
    st.subheader("select the deesired product")
   
    intoxicants_item= st.selectbox("as per the  id",["cloth","foot"])
    st.subheader("enter the price of selected product")
    intoxicants_price = st.number_input("or elese give the average price of the items",0)
    form_submit = st.button("Submit")     
def housing():
    st.subheader("select the deesired option")
   
    intoxicants_item= st.selectbox("as per the  id",["house rent","house charges"])
    st.subheader("enter the price of selected product")
    intoxicants_price = st.number_input("or elese give the average price of the items",0)
    form_submit = st.button("Submit")   
    
def miscellaneous():
    st.subheader("select the deesired type")
   
    food_item= st.selectbox("as per the food id",["furniture and furnishing","bedding","household appliances","house hold utensils and cookery","tools equipment for house","other household items","house hold services","health","transport","recreation and service of items","education","personal care and effects like ornaments rings all makup ..."])
    st.subheader("enter the price of selected product")
    food_price = st.number_input("or elese give the average price of the items",0)
    form_submit = st.button("Submit")        
INSERT INTO other_prices VALUES(2023,'JAN',3500,5000,5000,2000,5000,2000,1000,1000,5000,7000,800,10000,1000);
INSERT INTO other_prices VALUES(2023,'FEB',4000,5500,5200,1800,5500,2300,900,1200,5400,7500,700,11000,900);
INSERT INTO other_prices VALUES(2023,'MAR',3000,4500,5500,2200,4800,2400,1100,1300,5700,7100,850,10500,1100);
INSERT INTO other_prices VALUES(2023,'APR',4500,5200,6000,2500,5100,1900,1200,1100,5800,7200,870,10700,950);
INSERT INTO other_prices VALUES(2023,'MAY',3000,5700,5900,3000,5400,2500,800,1000,5600,7300,790,10200,1050);
INSERT INTO other_prices VALUES(2023,'JUN',2500,6000,6200,2900,5800,2600,1100,900,5200,6900,820,10100,1100);
INSERT INTO other_prices VALUES(2023,'JUL',4100,4900,4800,1900,5300,2100,700,800,4900,7100,840,10900,990);
INSERT INTO other_prices VALUES(2023,'AUG',3700,5200,5100,2200,5600,2000,1200,1100,5000,7500,850,10100,1040);
INSERT INTO clothandfoot_prices VALUES(2023,'JAN',1000,800);
INSERT INTO clothandfoot_prices VALUES(2023,'FEB',1200,1000);
INSERT INTO clothandfoot_prices VALUES(2023,'MAR',1100,1100);
INSERT INTO clothandfoot_prices VALUES(2023,'APR',900,700);
INSERT INTO clothandfoot_prices VALUES(2023,'MAY',1500,900);
INSERT INTO clothandfoot_prices VALUES(2023,'JUN',1300,1000);
INSERT INTO clothandfoot_prices VALUES(2023,'AUG',1000,1050);
INSERT INTO clothandfoot_prices VALUES(2023,'OCT',1200,950);