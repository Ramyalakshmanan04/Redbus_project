import pandas as pd
import mysql.connector
import streamlit as st
from streamlit_option_menu import option_menu
import plotly.express as px
import time
import pymysql

# kerala bus
lists_k=[]
df_k=pd.read_csv("df_kerala.csv")
for i,r in df_k.iterrows():
    lists_k.append(r["Route_name"])

#Andhra bus
lists_A=[]
df_A=pd.read_csv("df_andhra.csv")
for i,r in df_A.iterrows():
    lists_A.append(r["Route_name"])

#Telugana bus
lists_T=[]
df_T=pd.read_csv("df_telugana.csv")
for i,r in df_T.iterrows():
    lists_T.append(r["Route_name"])

#kadamba bus
lists_g=[]
df_G=pd.read_csv("df_kadamba.csv")
for i,r in df_G.iterrows():
    lists_g.append(r["Route_name"])

#Rajastan bus
lists_R=[]
df_R=pd.read_csv("df_rajasthan.csv")
for i,r in df_R.iterrows():
    lists_R.append(r["Route_name"])

# South bengal bus 
lists_SB=[]
df_SB=pd.read_csv("df_southbengal.csv")
for i,r in df_SB.iterrows():
    lists_SB.append(r["Route_name"])

# Himachalpradesh bus
lists_H=[]
df_H=pd.read_csv("df_himachal.csv")
for i,r in df_H.iterrows():
    lists_H.append(r["Route_name"])

#Assam bus
lists_AS=[]
df_AS=pd.read_csv("df_assam.csv")
for i,r in df_AS.iterrows():
    lists_AS.append(r["Route_name"])

#UP bus
lists_UP=[]
df_UP=pd.read_csv("df_uttarpradesh.csv")
for i,r in df_UP.iterrows():
    lists_UP.append(r["Route_name"])

#West bengal bus
lists_WB=[]
df_WB=pd.read_csv("df_westbengal.csv")
for i,r in df_WB.iterrows():
    lists_WB.append(r["Route_name"])

st.set_page_config(layout="wide")

web=option_menu(menu_title="🚌OnlineBus",
                options=["Home","📍Search Buses"],
                icons=["house","info-circle"],
                orientation="horizontal"
                )

if web=="Home":
    st.image("redbuslogo.png",width=200)
    st.title("Redbus-India's No. 1 Online Bus Ticket Booking Site")
    st.subheader("BOOK BUS TICKETS ONLINE:") 
    st.markdown("redBus is India's largest brand for online bus ticket booking and offers an easy-to-use online bus and train ticket booking; with over 36 million satisfied customers, 3500+ bus operators to choose from, and plenty of offers on bus ticket booking, redBus makes road journeys super convenient for travellers. A leading platform for booking bus tickets, redBus has been the leader in online bus booking over the past 17 years across thousands of cities and lakhs of routes in India.")
    st.markdown("Booking a bus ticket online on the redBus app or website is very simple. You can download the redBus app or visit redbus.in and enter your source, destination & travel date to check the top-rated bus services available. You can then compare bus prices, user ratings & amenities, select your preferred seat, boarding & dropping points and pay using multiple payment options like UPI, debit or credit card, net banking and more. With redBus, get assured safe & secure payment methods and guaranteed travel with the best seat and bus operator of your choice. Once the bus booking payment is confirmed, all you have to do is pack your bags and get ready to travel with the m-ticket, which you can show to the bus operator on your mobile before boarding the bus. Online bus ticket booking with redBus is that simple!")
    st.markdown("redBus also offers other exclusive benefits on online bus tickets like flexible ticket rescheduling options, easy & friendly cancellation policies, and instant payment refunds. With a live bus tracking feature, you can plan travel and never miss the bus. You can get the cheapest bus tickets by availing the best discounts for new & existing customers. With redDeals, you can also get exclusive & additional discounts on your online bus ticket booking. You will get 24/7 customer support on call, chat & help to resolve all your queries in English & local languages.")
    st.markdown("redBus offers Primo bus services, specially curated by redBus, which have highly rated buses and best-in-class service. With Primo by redBus, you can be assured of safe, comfortable, and on-time bus service at no additional cost. With multiple boarding and dropping points available across all major cities in India, you can select at your convenience and enjoy a smooth travel experience.")
    st.markdown("redBus operates in six countries, including India, Malaysia, Singapore, Indonesia, Peru, and Colombia. Through its website and app, it has sold over 220 million bus tickets worldwide. With over 36 million satisfied customers, redBus is committed to providing its users with a world-class online bus booking experience.")
    st.markdown("redBus offers bus tickets from some of the top private bus operators, such as Orange Travels, VRL Travels, SRS Travels, Chartered Bus, and Praveen Travels, and state government bus operators, such as APSRTC, TSRTC, GSRTC, Kerala RTC, TNSTC, RSRTC, UPSRTC, and more. With redBus, customers can easily book bus tickets for different bus types, such as AC/non-AC, Sleeper, Seater, Volvo, Multi-axle, AC Sleeper, Electric buses, and more.")


if web == "📍Search Buses":
    S = st.selectbox("States", ["Kerala", "Andhra Pradesh", "Telugana", "Goa", "Rajastan", 
                                          "South Bengal", "Himachal pradesh", "Assam", "Uttar Pradesh", "West Bengal"])
    
    col1,col2,col3=st.columns(3)
    with col1:
        select_type = st.radio("Select the Bustype", ("sleeper", "semi-sleeper","seater", "others"))
    with col2:
        select_fare = st.radio("Select the Busfare", ("0-500","500-1000", "1000-2000", "2000 and above"))
    with col3:
        select_rating = st.radio("Select the Rating",("1-2","2-3","3-4","4-5"))
    TIME=st.time_input("select the time")


#KERALA
    if S == "Kerala":
        K = st.selectbox("Routes",lists_k)

        def type_and_fare(bus_type, fare_range,rating):
            conn = pymysql.connect(host="localhost",user="root",password="Ramya",database="REDBUS_DATABASE")
            my_cursor = conn.cursor()
            
            # Define fare range based on selection
            if fare_range == "0-500":
                fare_min, fare_max = 0, 500
            elif fare_range == "500-1000":
                fare_min, fare_max = 500, 1000
            elif fare_range == "1000-2000":
                fare_min, fare_max = 1000, 2000
            else:
                fare_min, fare_max = 2000, 100000  

            if rating == "1-2":
                rating_condition = "Ratings BETWEEN 1 AND 2"
            elif rating == "2-3":
                rating_condition = "Ratings BETWEEN 2 AND 3"
            elif rating == "3-4":
                rating_condition = "Ratings BETWEEN 3 AND 4"
            else:
                rating_condition = "Ratings BETWEEN 4 AND 5"
            

            # Define bus type condition
            if bus_type == "sleeper":
                bus_type_condition = "Bus_type LIKE '%Sleeper%'"
            elif bus_type == "semi-sleeper":
                bus_type_condition = "Bus_type LIKE '%A/c Semi Sleeper %'"
            elif bus_type == "seater":
                bus_type_condition = "Bus_type LIKE '%Seater%'"
            else:
                bus_type_condition = "Bus_type NOT LIKE '%Sleeper%' AND Bus_type NOT LIKE '%Semi-Sleeper%'"

            query = f'''
                SELECT * FROM bus_details 
                WHERE Price BETWEEN {fare_min} AND {fare_max}
                AND Route_name = "{K}"
                AND {rating_condition}
                AND {bus_type_condition} AND Start_time>='{TIME}'
                ORDER BY Price and Start_time DESC
            '''
            my_cursor.execute(query)
            out = my_cursor.fetchall()
            conn.close()

            df = pd.DataFrame(out, columns=[
                "ID", "Bus_name", "Bus_type", "Start_time", "End_time", "Total_duration",
                "Price", "Seats_Available", "Ratings", "Route_link", "Route_name"
            ])
            return df

        df_result = type_and_fare(select_type, select_fare,select_rating)
        st.dataframe(df_result)


 #ANDHRA
    if S=="Andhra Pradesh":
        A=st.selectbox("Routes",lists_A)

        def type_and_fare_A(bus_type, fare_range, rating):
            conn = pymysql.connect(host="localhost",user="root",password="Ramya",database="REDBUS_DATABASE")
            my_cursor = conn.cursor()
            
            # Define fare range based on selection
            if fare_range == "0-500":
                fare_min, fare_max = 0, 500
            elif fare_range == "500-1000":
                fare_min, fare_max = 500, 1000
            elif fare_range == "1000-2000":
                fare_min, fare_max = 1000, 2000
            else:
                fare_min, fare_max = 2000, 100000  # assuming a high max value for "2000 and above"

            
            if rating == "1-2":
                rating_condition = "Ratings BETWEEN 1 AND 2"
            elif rating == "2-3":
                rating_condition = "Ratings BETWEEN 2 AND 3"
            elif rating == "3-4":
                rating_condition = "Ratings BETWEEN 3 AND 4"
            else:
                rating_condition = "Ratings BETWEEN 4 AND 5"
            

            # Define bus type condition
            if bus_type == "sleeper":
                bus_type_condition = "Bus_type LIKE '%Sleeper%'"
            elif bus_type == "semi-sleeper":
                bus_type_condition = "Bus_type LIKE '%A/c Semi Sleeper %'"
            elif bus_type == "seater":
                bus_type_condition = "Bus_type LIKE '%Seater%'"
            else:
                bus_type_condition = "Bus_type NOT LIKE '%Sleeper%' AND Bus_type NOT LIKE '%Semi-Sleeper%'"

            query = f'''
                SELECT * FROM bus_details 
                WHERE Price BETWEEN {fare_min} AND {fare_max}
                AND Route_name = "{A}"
                AND {rating_condition}
                AND {bus_type_condition} AND Start_time>='{TIME}'
                ORDER BY Price and Start_time DESC
            '''
            my_cursor.execute(query)
            out = my_cursor.fetchall()
            conn.close()

            df = pd.DataFrame(out, columns=[
                "ID", "Bus_name", "Bus_type", "Start_time", "End_time", "Total_duration",
                "Price", "Seats_Available", "Ratings", "Route_link", "Route_name"
            ])
            return df

        df_result = type_and_fare_A(select_type, select_fare,select_rating)
        st.dataframe(df_result)



#TELUGANA
    if S=="Telugana":
        T=st.selectbox("Routes",lists_T)

        def type_and_fare_T(bus_type, fare_range, rating):
            conn = pymysql.connect(host="localhost",user="root",password="Ramya",database="REDBUS_DATABASE")
            my_cursor = conn.cursor()


            # Define fare range based on selection
            if fare_range == "0-500":
                fare_min, fare_max = 0, 500
            elif fare_range == "500-1000":
                fare_min, fare_max = 500, 1000
            elif fare_range == "1000-2000":
                fare_min, fare_max = 1000, 2000
            else:
                fare_min, fare_max = 2000, 100000  # assuming a high max value for "2000 and above"

            
            if rating == "1-2":
                rating_condition = "Ratings BETWEEN 1 AND 2"
            elif rating == "2-3":
                rating_condition = "Ratings BETWEEN 2 AND 3"
            elif rating == "3-4":
                rating_condition = "Ratings BETWEEN 3 AND 4"
            else:
                rating_condition = "Ratings BETWEEN 4 AND 5"
            

            # Define bus type condition
            if bus_type == "sleeper":
                bus_type_condition = "Bus_type LIKE '%Sleeper%'"
            elif bus_type == "semi-sleeper":
                bus_type_condition = "Bus_type LIKE '%A/c Semi Sleeper %'"
            elif bus_type == "seater":
                bus_type_condition = "Bus_type LIKE '%Seater%'"
            else:
                bus_type_condition = "Bus_type NOT LIKE '%Sleeper%' AND Bus_type NOT LIKE '%Semi-Sleeper%'"
            
            query = f'''
                SELECT * FROM bus_details 
                WHERE Price BETWEEN {fare_min} AND {fare_max}
                AND Route_name = "{T}"
                AND {rating_condition}
                AND {bus_type_condition} AND Start_time>='{TIME}'
                ORDER BY Price and Start_time DESC
            '''
            my_cursor.execute(query)
            out = my_cursor.fetchall()
            conn.close()

            df = pd.DataFrame(out, columns=[
                "ID", "Bus_name", "Bus_type", "Start_time", "End_time", "Total_duration",
                "Price", "Seats_Available", "Ratings", "Route_link", "Route_name"
            ])
            return df

        df_result = type_and_fare_T(select_type, select_fare,select_rating)
        st.dataframe(df_result)


#KADAMBA
    if S=="Goa":
        G=st.selectbox("Routes",lists_g)

        def type_and_fare_G(bus_type, fare_range,rating):
            conn = pymysql.connect(host="localhost",user="root",password="Ramya",database="REDBUS_DATABASE")
            my_cursor = conn.cursor()

            
            # Define fare range based on selection
            if fare_range == "0-500":
                fare_min, fare_max = 0, 500
            elif fare_range == "500-1000":
                fare_min, fare_max = 500, 1000
            elif fare_range == "1000-2000":
                fare_min, fare_max = 1000, 2000
            else:
                fare_min, fare_max = 2000, 100000  # assuming a high max value for "2000 and above"

            
            if rating == "1-2":
                rating_condition = "Ratings BETWEEN 1 AND 2"
            elif rating == "2-3":
                rating_condition = "Ratings BETWEEN 2 AND 3"
            elif rating == "3-4":
                rating_condition = "Ratings BETWEEN 3 AND 4"
            else:
                rating_condition = "Ratings BETWEEN 4 AND 5"
            

            # Define bus type condition
            if bus_type == "sleeper":
                bus_type_condition = "Bus_type LIKE '%Sleeper%'"
            elif bus_type == "semi-sleeper":
                bus_type_condition = "Bus_type LIKE '%A/c Semi Sleeper %'"
            elif bus_type == "seater":
                bus_type_condition = "Bus_type LIKE '%Seater%'"
            else:
                bus_type_condition = "Bus_type NOT LIKE '%Sleeper%' AND Bus_type NOT LIKE '%Semi-Sleeper%'"


            query = f'''
                SELECT * FROM bus_details 
                WHERE Price BETWEEN {fare_min} AND {fare_max}
                AND Route_name = "{G}"
                AND {rating_condition}
                AND {bus_type_condition} AND Start_time>='{TIME}'
                ORDER BY Price and Start_time DESC
            '''
            my_cursor.execute(query)
            out = my_cursor.fetchall()
            conn.close()

            df = pd.DataFrame(out, columns=[
                "ID", "Bus_name", "Bus_type", "Start_time", "End_time", "Total_duration",
                "Price", "Seats_Available", "Ratings", "Route_link", "Route_name"
            ])
            return df

        df_result = type_and_fare_G(select_type, select_fare, select_rating)
        st.dataframe(df_result)


    
#RAJASTHAN
    if S=="Rajastan":
        R=st.selectbox("Routes",lists_R)

        def type_and_fare_R(bus_type, fare_range,rating):
            conn = pymysql.connect(host="localhost",user="root",password="Ramya",database="REDBUS_DATABASE")
            my_cursor = conn.cursor()
            
            # Define fare range based on selection
            if fare_range == "0-500":
                fare_min, fare_max = 0, 500
            elif fare_range == "500-1000":
                fare_min, fare_max = 500, 1000
            elif fare_range == "1000-2000":
                fare_min, fare_max = 1000, 2000
            else:
                fare_min, fare_max = 2000, 100000  # assuming a high max value for "2000 and above"

            
            if rating == "1-2":
                rating_condition = "Ratings BETWEEN 1 AND 2"
            elif rating == "2-3":
                rating_condition = "Ratings BETWEEN 2 AND 3"
            elif rating == "3-4":
                rating_condition = "Ratings BETWEEN 3 AND 4"
            else:
                rating_condition = "Ratings BETWEEN 4 AND 5"
            

            # Define bus type condition
            if bus_type == "sleeper":
                bus_type_condition = "Bus_type LIKE '%Sleeper%'"
            elif bus_type == "semi-sleeper":
                bus_type_condition = "Bus_type LIKE '%A/c Semi Sleeper %'"
            elif bus_type == "seater":
                bus_type_condition = "Bus_type LIKE '%Seater%'"
            else:
                bus_type_condition = "Bus_type NOT LIKE '%Sleeper%' AND Bus_type NOT LIKE '%Semi-Sleeper%'"


            query = f'''
                SELECT * FROM bus_details 
                WHERE Price BETWEEN {fare_min} AND {fare_max}
                AND Route_name = "{R}"
                AND {rating_condition}
                AND {bus_type_condition} AND Start_time>='{TIME}'
                ORDER BY Price and Start_time DESC
            '''
            my_cursor.execute(query)
            out = my_cursor.fetchall()
            conn.close()

            df = pd.DataFrame(out, columns=[
                "ID", "Bus_name", "Bus_type", "Start_time", "End_time", "Total_duration",
                "Price", "Seats_Available", "Ratings", "Route_link", "Route_name"
            ])
            return df

        df_result = type_and_fare_R(select_type, select_fare, select_rating)
        st.dataframe(df_result)



#SOUTHBENGAL
    if S=="South Bengal":
        SB=st.selectbox("Routes",lists_SB)

        def type_and_fare_SB(bus_type, fare_range,rating):
            conn = pymysql.connect(host="localhost",user="root",password="Ramya",database="REDBUS_DATABASE")
            my_cursor = conn.cursor()
            
            # Define fare range based on selection
            if fare_range == "0-500":
                fare_min, fare_max = 0, 500
            elif fare_range == "500-1000":
                fare_min, fare_max = 500, 1000
            elif fare_range == "1000-2000":
                fare_min, fare_max = 1000, 2000
            else:
                fare_min, fare_max = 2000, 100000  # assuming a high max value for "2000 and above"

            
            if rating == "1-2":
                rating_condition = "Ratings BETWEEN 1 AND 2"
            elif rating == "2-3":
                rating_condition = "Ratings BETWEEN 2 AND 3"
            elif rating == "3-4":
                rating_condition = "Ratings BETWEEN 3 AND 4"
            else:
                rating_condition = "Ratings BETWEEN 4 AND 5"
            

            # Define bus type condition
            if bus_type == "sleeper":
                bus_type_condition = "Bus_type LIKE '%Sleeper%'"
            elif bus_type == "semi-sleeper":
                bus_type_condition = "Bus_type LIKE '%A/c Semi Sleeper %'"
            elif bus_type == "seater":
                bus_type_condition = "Bus_type LIKE '%Seater%'"
            else:
                bus_type_condition = "Bus_type NOT LIKE '%Sleeper%' AND Bus_type NOT LIKE '%Semi-Sleeper%'"

            query = f'''
                SELECT * FROM bus_details 
                WHERE Price BETWEEN {fare_min} AND {fare_max}
                AND Route_name = "{SB}"
                AND {rating_condition}
                AND {bus_type_condition} AND Start_time>='{TIME}'
                ORDER BY Price and Start_time DESC
            '''
            my_cursor.execute(query)
            out = my_cursor.fetchall()
            conn.close()

            df = pd.DataFrame(out, columns=[
                "ID", "Bus_name", "Bus_type", "Start_time", "End_time", "Total_duration",
                "Price", "Seats_Available", "Ratings", "Route_link", "Route_name"
            ])
            return df

        df_result = type_and_fare_SB(select_type, select_fare,select_rating)
        st.dataframe(df_result)



#Himachal
    # Haryana bus fare filtering
    if S=="Himachal pradesh":
        H=st.selectbox("Routes",lists_H)

        def type_and_fare_H(bus_type, fare_range,rating):
            conn = pymysql.connect(host="localhost",user="root",password="Ramya",database="REDBUS_DATABASE")
            my_cursor = conn.cursor()

            
            # Define fare range based on selection
            if fare_range == "0-500":
                fare_min, fare_max = 0, 500
            elif fare_range == "500-1000":
                fare_min, fare_max = 500, 1000
            elif fare_range == "1000-2000":
                fare_min, fare_max = 1000, 2000
            else:
                fare_min, fare_max = 2000, 100000  # assuming a high max value for "2000 and above"

            
            if rating == "1-2":
                rating_condition = "Ratings BETWEEN 1 AND 2"
            elif rating == "2-3":
                rating_condition = "Ratings BETWEEN 2 AND 3"
            elif rating == "3-4":
                rating_condition = "Ratings BETWEEN 3 AND 4"
            else:
                rating_condition = "Ratings BETWEEN 4 AND 5"
            

            # Define bus type condition
            if bus_type == "sleeper":
                bus_type_condition = "Bus_type LIKE '%Sleeper%'"
            elif bus_type == "semi-sleeper":
                bus_type_condition = "Bus_type LIKE '%A/c Semi Sleeper %'"
            elif bus_type == "seater":
                bus_type_condition = "Bus_type LIKE '%Seater%'"
            else:
                bus_type_condition = "Bus_type NOT LIKE '%Sleeper%' AND Bus_type NOT LIKE '%Semi-Sleeper%'"

            query = f'''
                SELECT * FROM bus_details 
                WHERE Price BETWEEN {fare_min} AND {fare_max}
                AND Route_name = "{H}"
                AND {rating_condition}
                AND {bus_type_condition} AND Start_time>='{TIME}'
                ORDER BY Price and Start_time DESC
            '''
            my_cursor.execute(query)
            out = my_cursor.fetchall()
            conn.close()

            df = pd.DataFrame(out, columns=[
                "ID", "Bus_name", "Bus_type", "Start_time", "End_time", "Total_duration",
                "Price", "Seats_Available", "Ratings", "Route_link", "Route_name"
            ])
            return df

        df_result = type_and_fare_H(select_type, select_fare,select_rating)
        st.dataframe(df_result)



#ASSAM
    if S=="Assam":
        AS=st.selectbox("Routes",lists_AS)

        def type_and_fare_AS(bus_type, fare_range,rating):
            conn = pymysql.connect(host="localhost",user="root",password="Ramya",database="REDBUS_DATABASE")
            my_cursor = conn.cursor()

            
            # Define fare range based on selection
            if fare_range == "0-500":
                fare_min, fare_max = 0, 500
            elif fare_range == "500-1000":
                fare_min, fare_max = 500, 1000
            elif fare_range == "1000-2000":
                fare_min, fare_max = 1000, 2000
            else:
                fare_min, fare_max = 2000, 100000  # assuming a high max value for "2000 and above"

            
            if rating == "1-2":
                rating_condition = "Ratings BETWEEN 1 AND 2"
            elif rating == "2-3":
                rating_condition = "Ratings BETWEEN 2 AND 3"
            elif rating == "3-4":
                rating_condition = "Ratings BETWEEN 3 AND 4"
            else:
                rating_condition = "Ratings BETWEEN 4 AND 5"
            

            # Define bus type condition
            if bus_type == "sleeper":
                bus_type_condition = "Bus_type LIKE '%Sleeper%'"
            elif bus_type == "semi-sleeper":
                bus_type_condition = "Bus_type LIKE '%A/c Semi Sleeper %'"
            elif bus_type == "seater":
                bus_type_condition = "Bus_type LIKE '%Seater%'"
            else:
                bus_type_condition = "Bus_type NOT LIKE '%Sleeper%' AND Bus_type NOT LIKE '%Semi-Sleeper%'"

            query = f'''
                SELECT * FROM bus_details 
                WHERE Price BETWEEN {fare_min} AND {fare_max}
                AND Route_name = "{AS}"
                AND {rating_condition}
                AND {bus_type_condition} AND Start_time>='{TIME}'
                ORDER BY Price and Start_time DESC
            '''
            my_cursor.execute(query)
            out = my_cursor.fetchall()
            conn.close()

            df = pd.DataFrame(out, columns=[
                "ID", "Bus_name", "Bus_type", "Start_time", "End_time", "Total_duration",
                "Price", "Seats_Available", "Ratings", "Route_link", "Route_name"
            ])
            return df

        df_result = type_and_fare_AS(select_type, select_fare, select_rating)
        st.dataframe(df_result)



#UTTAR PRADESH
    if S=="Uttar Pradesh":
        UP=st.selectbox("Routes",lists_UP)

        def type_and_fare_UP(bus_type, fare_range, rating):
            conn = pymysql.connect(host="localhost",user="root",password="Ramya",database="REDBUS_DATABASE")
            my_cursor = conn.cursor()

            
            # Define fare range based on selection
            if fare_range == "0-500":
                fare_min, fare_max = 0, 500
            elif fare_range == "500-1000":
                fare_min, fare_max = 500, 1000
            elif fare_range == "1000-2000":
                fare_min, fare_max = 1000, 2000
            else:
                fare_min, fare_max = 2000, 100000  # assuming a high max value for "2000 and above"

            
            if rating == "1-2":
                rating_condition = "Ratings BETWEEN 1 AND 2"
            elif rating == "2-3":
                rating_condition = "Ratings BETWEEN 2 AND 3"
            elif rating == "3-4":
                rating_condition = "Ratings BETWEEN 3 AND 4"
            else:
                rating_condition = "Ratings BETWEEN 4 AND 5"
            

            # Define bus type condition
            if bus_type == "sleeper":
                bus_type_condition = "Bus_type LIKE '%Sleeper%'"
            elif bus_type == "semi-sleeper":
                bus_type_condition = "Bus_type LIKE '%A/c Semi Sleeper %'"
            elif bus_type == "seater":
                bus_type_condition = "Bus_type LIKE '%Seater%'"
            else:
                bus_type_condition = "Bus_type NOT LIKE '%Sleeper%' AND Bus_type NOT LIKE '%Semi-Sleeper%'"

            query = f'''
                SELECT * FROM bus_details 
                WHERE Price BETWEEN {fare_min} AND {fare_max}
                AND Route_name = "{UP}"
                AND {rating_condition}
                AND {bus_type_condition} AND Start_time>='{TIME}'
                ORDER BY Price and Start_time DESC
            '''
            my_cursor.execute(query)
            out = my_cursor.fetchall()
            conn.close()

            df = pd.DataFrame(out, columns=[
                "ID", "Bus_name", "Bus_type", "Start_time", "End_time", "Total_duration",
                "Price", "Seats_Available", "Ratings", "Route_link", "Route_name"
            ])
            return df

        df_result = type_and_fare_UP(select_type, select_fare,select_rating)
        st.dataframe(df_result)




#WEST BENGAL
    if S=="West Bengal":
        WB=st.selectbox("Routes",lists_WB)

        def type_and_fare_WB(bus_type, fare_range,rating):
            conn = pymysql.connect(host="localhost",user="root",password="Ramya",database="REDBUS_DATABASE")
            my_cursor = conn.cursor()

            
            # Define fare range based on selection
            if fare_range == "0-500":
                fare_min, fare_max = 0, 500
            elif fare_range == "500-1000":
                fare_min, fare_max = 500, 1000
            elif fare_range == "1000-2000":
                fare_min, fare_max = 1000, 2000
            else:
                fare_min, fare_max = 2000, 100000  # assuming a high max value for "2000 and above"

            
            if rating == "1-2":
                rating_condition = "Ratings BETWEEN 1 AND 2"
            elif rating == "2-3":
                rating_condition = "Ratings BETWEEN 2 AND 3"
            elif rating == "3-4":
                rating_condition = "Ratings BETWEEN 3 AND 4"
            else:
                rating_condition = "Ratings BETWEEN 4 AND 5"
            

            # Define bus type condition
            if bus_type == "sleeper":
                bus_type_condition = "Bus_type LIKE '%Sleeper%'"
            elif bus_type == "semi-sleeper":
                bus_type_condition = "Bus_type LIKE '%A/c Semi Sleeper %'"
            elif bus_type == "seater":
                bus_type_condition = "Bus_type LIKE '%Seater%'"
            else:
                bus_type_condition = "Bus_type NOT LIKE '%Sleeper%' AND Bus_type NOT LIKE '%Semi-Sleeper%'"

            query = f'''
                SELECT * FROM bus_details 
                WHERE Price BETWEEN {fare_min} AND {fare_max}
                AND Route_name = "{WB}"
                AND {rating_condition}
                AND {bus_type_condition} AND Start_time>='{TIME}'
                ORDER BY Price and Start_time  DESC
            '''
            my_cursor.execute(query)
            out = my_cursor.fetchall()
            conn.close()

            df = pd.DataFrame(out, columns=[
                "ID", "Bus_name", "Bus_type", "Start_time", "End_time", "Total_duration",
                "Price", "Seats_Available", "Ratings", "Route_link", "Route_name"
            ])
            return df

        df_result = type_and_fare_WB(select_type, select_fare, select_rating)
        st.dataframe(df_result)

