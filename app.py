import streamlit as st
import pickle
import numpy as np

#import the model
pipe = pickle.load(open('pipe (1).pkl','rb'))
df = pickle.load(open('df (1).pkl','rb'))

st.title('who is most likely to have depression prediction')

# Education
education = st.selectbox('Education',['Less than high school', 'High school', 'University degree', 'Graduate degree'])

# Urban
urban = st.selectbox('Urban',['Rural', 'Suburban', 'Urban'])

#gender
gender = st.selectbox('Gender',['Male','Female', 'Other'])

#engnat
engnat = st.selectbox('Engnat',['Yes','No'])


#VCL
VCL = st.number_input('VCL')

#age
age  = st.number_input('Age')

#religion
religion = st.selectbox('Religion',['Agnostic', 'Atheist', 'Buddhist', 'Christian', 'Hindu', 'Jewish', 'Muslim', 'Sikh', 'Other'])

#orientation
orientation = st.selectbox('Orientation',['Heterosexual', 'Bisexual', 'Homosexual', 'Asexual', 'Other'])

#race
race = st.selectbox('Race',['Asian', 'Arab', 'Black', 'Indigenous Australian','Native American', 'White', 'Other'])

#Votes
voted = st.selectbox('Voted',['Yes','No'])

#married
married = st.selectbox('Married',['Never married', 'Currently married', 'Previously married'])

#familysize
familysize = st.number_input('Familysize')

#screensize
screensize = st.selectbox('Screens',['device with small screen (phone, etc)', 'device with big screen (laptop, desktop, etc)'])

#peronality
personality = st.number_input('Personality')

if st.button('Predict'):

    if education == 'Less than high school':
        education = 1
    elif education == 'High school':
        education =2
    elif education == 'University degree':
        education=3
    elif education=='Graduate degree':
        education=4

    if urban == 'Rural':
        urban = 1
    elif urban == 'Suburban':
        urban = 2
    elif urban == 'Urban':
        urban = 3

    if gender == 'Male':
        gender = 1
    elif gender == 'Female':
        gender = 2
    elif gender == 'Other':
        gender = 3

    if engnat=='Yes':
        engnat =1
    elif engnat=='No':
        engnat =2


    if religion == 'Agnostic':
        religion = 1
    elif religion == 'Atheist':
        religion =2
    elif religion == 'Buddhist':
        religion=3
    elif religion=='Christian':
        religion=4
    elif religion=='Hindu':
        religion=8
    elif religion=='Jewish':
        religion=9
    elif religion=='Muslim':
        religion=10
    elif religion=='Sikh':
        religion=11
    elif religion=='Other':
        religion=12

    if orientation=='Heterosexual':
        orientation =1
    elif orientation=='Bisexual':
        orientation =2
    elif orientation=='Homosexual':
        orientation =3
    elif orientation=='Asexual':
        orientation =4
    elif orientation=='Other':
        orientation=5

    if race == 'Asian':
        race = 10
    elif race == 'Arab':
        race = 20
    elif race == 'Black':
        race = 30
    elif race == 'Indigenous Australian':
        race = 40
    elif race == 'Native American':
        race = 50
    elif race == 'White':
        race = 60
    elif race == 'Other':
        race = 70

    if voted == 'Yes':
        voted = 1
    elif voted == 'No':
        voted =2

    if married == 'Never married':
        married = 1
    elif married == 'Currently married':
        married =2
    elif married == 'Previously married':
        married =3



    if screensize == 'device with small screen (phone, etc)':
        screensize = 1
    elif screensize == 'device with big screen (laptop, desktop, etc)':
        screensize =2


    query = np.array([VCL,education,urban,gender,engnat,age,religion,orientation,race,voted,married,familysize,screensize,personality])
    query = query.reshape(1,14)

    res = int(pipe.predict(query))
    if res == 1:
        st.title("Yes")
    elif res ==0:
        st.title("No")




