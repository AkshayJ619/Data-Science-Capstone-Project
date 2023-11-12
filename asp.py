import streamlit as st
import pickle
import numpy as np

lr1 = pickle.load(open('lr1_model_8N.pkl','rb'))
dt1 = pickle.load(open('dt1_model_8N.pkl','rb'))
rf1 = pickle.load(open('lr1_model_8N.pkl','rb'))

st.title(' Web App')
st.subheader('Fill the below Details to find the right price')
model = st.sidebar.selectbox('Select the ML Model',['Lin_Reg','DT_Reg','RF_Reg'])

Transmission = st.selectbox('Transmission',['Automatic','Mannual'])
Owner = st.selectbox('Owner',['First Owner','Second Owner','Third Owner','Fourth and above owner','Test Drive car'])
Fuel = st.selectbox('Fuel',['Diesel','Petrol','CNG','LPG','Electric'])
year=st.slider('Year',1992,2020)
km_dr=st.slider('Kilometers_Driven',1,806599)
seller_type=st.selectbox('Sellar_Type',['Dealer','Individual','Trustmark_Dealer'])
name=st.selectbox('Car_Name',['Hyundai EON Era Plus','Maruti Alto 800 LXI', 'Maruti Alto LX','Maruti Alto LXi','Maruti Swift Dzire VDI','Maruti Swift VDI BSIV','Maruti Wagon R VXI BS IV','Others'])




if st.button('Predict Car Price'):
    if Transmission == 'Automatic':
        transmission = 0
    else:
        transmission = 1

    if Fuel == "Diesel":
        Fuel = 1
       # Petrol = 0
       # CNG = 0
       # LPG = 0
       # Electric=0

    elif Fuel == "Petrol":
       # Diesel = 0
        Fuel = 4
       # CNG = 0
       # LPG = 0
       # Electric=0
        
    elif Fuel == "CNG":
       # Diesel = 0
       # Petrol = 0
        Fuel = 0
       # LPG = 0
       # Electric=0
    elif Fuel == "LPG":
        # Diesel = 0
        # Petrol = 0
        # CNG = 0
         Fuel = 3
        # Electric=0   
    else:
       # Diesel = 0
       # Petrol = 0
       # CNG = 0
       # LPG = 0
        Fuel=2    

    if Owner == "First Owner":
        Owner = 0
       # Petrol = 0
       # CNG = 0
       # LPG = 0
       # Electric=0

    elif Owner == "Second Owner":
       # Diesel = 0
        Owner = 2
       # CNG = 0
       # LPG = 0
       # Electric=0
        
    elif Owner == "Third Owner":
       # Diesel = 0
       # Petrol = 0
        Owner = 4
       # LPG = 0
       # Electric=0
    elif Owner == "Fourth and above Owner":
        # Diesel = 0
        # Petrol = 0
        # CNG = 0
         Owner = 1
        # Electric=0   
    else:
       # Diesel = 0
       # Petrol = 0
       # CNG = 0
       # LPG = 0
        Owner=3

#new    
    if seller_type == "Individual":
        Individual = 1
        Dealer= 0
        Trustmark_dealer= 0
       

    elif seller_type == "Dealer":
        Individual = 0
        Dealer= 1
        Trustmark_dealer= 0
        
    else:
        Individual = 0
        Dealer= 0
        Trustmark_dealer= 1
#new
    if name == "Hyundai EON Era Plus":
        Hyundai_EON_Era_Plus = 1
        Maruti_Alto_800_LXI=0 
        Maruti_Alto_LX=0
        Maruti_Alto_LXi=0 
        Maruti_Swift_Dzire_VDI=0
        Maruti_Swift_VDI_BSIV=0 
        Maruti_Wagon_R_VXI_BS_IV=0
        Others=0

    elif name == "Maruti Alto 800 LXI":
        Hyundai_EON_Era_Plus = 0
        Maruti_Alto_800_LXI=1 
        Maruti_Alto_LX=0
        Maruti_Alto_LXi=0 
        Maruti_Swift_Dzire_VDI=0
        Maruti_Swift_VDI_BSIV=0 
        Maruti_Wagon_R_VXI_BS_IV=0
        Others=0
        
    elif name == "Maruti Alto LX":
        Hyundai_EON_Era_Plus = 0
        Maruti_Alto_800_LXI=0 
        Maruti_Alto_LX=1
        Maruti_Alto_LXi=0 
        Maruti_Swift_Dzire_VDI=0
        Maruti_Swift_VDI_BSIV=0 
        Maruti_Wagon_R_VXI_BS_IV=0
        Others=0
    elif name == "Maruti Alto LXi":
        Hyundai_EON_Era_Plus = 0
        Maruti_Alto_800_LXI=0 
        Maruti_Alto_LX=0
        Maruti_Alto_LXi=1 
        Maruti_Swift_Dzire_VDI=0
        Maruti_Swift_VDI_BSIV=0 
        Maruti_Wagon_R_VXI_BS_IV=0
        Others=0
        
    elif name == "Maruti Swift Dzire VDI":
        Hyundai_EON_Era_Plus = 0
        Maruti_Alto_800_LXI=0 
        Maruti_Alto_LX=0
        Maruti_Alto_LXi=0 
        Maruti_Swift_Dzire_VDI=1
        Maruti_Swift_VDI_BSIV=0 
        Maruti_Wagon_R_VXI_BS_IV=0
        Others=0
    
    elif name == "Maruti Swift VDI BSIV":
        Hyundai_EON_Era_Plus = 0
        Maruti_Alto_800_LXI=0 
        Maruti_Alto_LX=0
        Maruti_Alto_LXi=0 
        Maruti_Swift_Dzire_VDI=0
        Maruti_Swift_VDI_BSIV=1 
        Maruti_Wagon_R_VXI_BS_IV=0
        Others=0

    elif name == "Maruti Wagon R VXI BS IV":
        Hyundai_EON_Era_Plus = 0
        Maruti_Alto_800_LXI=0 
        Maruti_Alto_LX=0
        Maruti_Alto_LXi=0 
        Maruti_Swift_Dzire_VDI=0
        Maruti_Swift_VDI_BSIV=0
        Maruti_Wagon_R_VXI_BS_IV=1
        Others=0
    else:
        Hyundai_EON_Era_Plus = 0
        Maruti_Alto_800_LXI=0 
        Maruti_Alto_LX=0
        Maruti_Alto_LXi=0 
        Maruti_Swift_Dzire_VDI=0
        Maruti_Swift_VDI_BSIV=0
        Maruti_Wagon_R_VXI_BS_IV=1
        Others=0

    test = np.array([year,km_dr,Fuel, transmission, Owner, Individual, Dealer,Trustmark_dealer, Hyundai_EON_Era_Plus, Maruti_Alto_800_LXI,Maruti_Alto_LX, Maruti_Alto_LXi, Maruti_Swift_Dzire_VDI,Maruti_Swift_VDI_BSIV, Maruti_Wagon_R_VXI_BS_IV, Others])
    test = test.reshape(1,16)

    if model == "Lin_Reg":
        st.success(lr1.predict(test)[0])
    elif model == "DT_Reg":
        st.success(dt1.predict(test)[0])
    else:
        st.success(rf1.predict(test)[0])
  

    

