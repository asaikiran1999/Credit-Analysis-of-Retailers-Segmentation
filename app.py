
import streamlit as st
import pandas as pd
import pickle
import json
from matplotlib import pyplot as plt
st.title('Credit Analysis of Retailers Segmentation')
filename = 'rfm_dataset2.sav'
try:
    df = pd.read_pickle(filename)
except Exception as e:
    print("Error loading pickled file:", e)
st.text('dataset loaded')


f = open('retailersnames.json')
list1 = json.load(f)
f = open('retailersmoney.json')
x = json.load(f)

name = list1[0:10]
price = x[0:10]
  
fig = plt.figure(figsize = (10, 5))
 
# creating the bar plot
plt.bar(name, price, color ='blue',
        width = 0.2)
plt.xticks(rotation='vertical')
plt.xlabel("x")
plt.ylabel("y")
plt.title("top retailers according to monetary")
plt.show()
#fig1,ax1= plt.subplots()
			
			#ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
st.pyplot(fig)
#______________________________________________________________________________________________________________monetary
f = open('retailersnames1.json')
list1 = json.load(f)
f = open('retailersfrequency.json')
x = json.load(f)

name = list1[0:20]
price = x[0:20]
  
fig = plt.figure(figsize = (10, 5))
 
# creating the bar plot
plt.bar(name, price, color ='blue',
        width = 0.2)
plt.xticks(rotation='vertical')
plt.xlabel("x")
plt.ylabel("y")
plt.title("top retailers according to frequency")
plt.show()
st.pyplot(fig)
#_____________________________________________________________________________________________________________________
st.text('Recency of Retailers')
df2=df.sort_values(by=['recency'], ascending=False)
st.dataframe(data=df2, width=None, height=None)
x = st.text_input("Enter the retailer name","")
if st.button('analyse'):
	list2 = []
	tuple1= tuple()
	for j in range(df.shape[0]):
	  if df['retailer_names'][j]==x:
	    tuple1 = (x,df['recency_rank'][j],df['frequency_rank'][j],df['monetary_rank'][j])
	    break

	fig = plt.figure()

	langs = ['Rencency score', 'Frequency_score', 'Monetary_score']
	students = [round(tuple1[1]),round(tuple1[2]),round(tuple1[3])]
	plt.bar(langs,students)
	xlocs=[i for i in range(0,3)]
	plt.xticks(rotation='vertical')
	for i, v in enumerate(students):
	    plt.text(xlocs[i] - 0.25, v + 0.01, str(v))
	plt.xlabel("x")
	plt.ylabel("y")
	plt.title("RFM Score of "+str(tuple1[0]))
	plt.show()
	st.pyplot(fig)
x = st.text_input("Enter the retailer name","")
if st.button('analyse'):
	list2 = []
	tuple1= tuple()
	for j in range(df.shape[0]):
	  if df['retailer_names'][j]==x:
	    tuple1 = (x,df['recency_rank'][j],df['frequency_rank'][j],df['monetary_rank'][j])
	    break

	fig = plt.figure()

	langs = ['Rencency score', 'Frequency_score', 'Monetary_score']
	students = [round(tuple1[1]),round(tuple1[2]),round(tuple1[3])]
	plt.bar(langs,students)
	xlocs=[i for i in range(0,3)]
	plt.xticks(rotation='vertical')
	for i, v in enumerate(students):
	    plt.text(xlocs[i] - 0.25, v + 0.01, str(v))
	plt.xlabel("x")
	plt.ylabel("y")
	plt.title("RFM Score of "+str(tuple1[0]))
	plt.show()
	st.pyplot(fig)
st.write("""
<script>
function keepAlive() {
    fetch(window.location.href, { mode: 'no-cors' });
}
setInterval(keepAlive, 5 * 60 * 1000);
</script>
""")
