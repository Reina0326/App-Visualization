import streamlit as st
import pandas as pd
import altair as alt
import numpy as np

st.header("""
Хүн амын эрүүл мэндийн их өгөгдөл (Population based health big data)         
""")

st.subheader("Амьдралын хэв маягийн өгөгдөл (Lifestyle data)")

st.subheader("Стресст өртөх магадлал / ISMA ")

st.text("0 -ээс 4 = Стресст өртөх магадлал бага\n5 -өөс 14 = Стресст өртөх магадлал өндөр\n14 ба түүнээс их = Стрессийн түвшин өндөр")

# url = 'https://raw.githubusercontent.com/Reina0326/App-Visualization/main/modified_Responses.xlsx'
url = 'https://github.com/Reina0326/App-Visualization/main/modified_Responses.xlsx'
df = pd.read_excel(url)

# Нийт оролцогчдын тоо
parts = len(df["Row of Sum"])

minimum_counter = 0
middle_counter = 0
high_counter = 0

def assign_description(row_sum):
    global minimum_counter, middle_counter, high_counter

    if row_sum <= 4:
        minimum_counter += 1
        return "Магадлал бага"
    elif row_sum < 14:
        middle_counter += 1
        return "Магадлал өндөр"
    else:
        high_counter += 1
        return "Стрессийн түвшин өндөр"

# Өгөгдлүүдийг тайлбар болгон хувиргах
df['Description'] = df['Row of Sum'].apply(assign_description)
                  
# Бар чарт үүсгэх функц
def create_bar_chart():
    source = pd.DataFrame({
        'Category': ["Магадлал бага", "Магадлал өндөр", "Стрессийн түвшин өндөр"],
        'Count': [minimum_counter, middle_counter, high_counter]
    })

    bar_chart = alt.Chart(source).mark_bar(size=50,color='skyblue').encode(
        x='Category',
        y='Count'
    ).properties(
        title=f"Судалгаанд оролцсон хүмүүсийн ангилал (Нийт оролцогчид: {parts})",
        width=600,  
        height=400
    )

    st.altair_chart(bar_chart, use_container_width=True)

# Бокс чарт үүсгэх функц
def create_box_chart():
    box_chart = alt.Chart(df).mark_boxplot(size=60, color='pink').encode(
        y=alt.Y('Row of Sum', title='Row of Sum')
    ).properties(
        title="Стрессийн түвшний тархалт (Box Chart)"
    )

    st.altair_chart(box_chart, use_container_width=True)

def create_pie_chart():
    # Өгөгдлийг бэлдэх
    source = pd.DataFrame({
        'Category': ["Магадлал бага", "Магадлал өндөр", "Стрессийн түвшин өндөр"],
        'Count': [minimum_counter, middle_counter, high_counter]
    })

    # Нийт оролцогчдын тоо
    source['Percentage'] = (source['Count'] / parts) * 100

    # Pie Chart үүсгэх
    pie_chart = alt.Chart(source).mark_arc(innerRadius=50).encode(
        theta=alt.Theta('Count', type='quantitative', title=''),
        color=alt.Color('Category:N', legend=None),
        tooltip=['Category', 'Count', 'Percentage']
    ).properties(
        width=400,
        height=400,
        title="Судалгаанд оролцсон хүмүүсийн статистик"
    )

    st.altair_chart(pie_chart, use_container_width=True)

def create_histogram():
    # Histogram үүсгэх
    histogram = alt.Chart(df).mark_bar(color='skyblue').encode(
        alt.X('Row of Sum:Q', bin=alt.Bin(maxbins=20), title='Row of Sum Утгууд'),
        alt.Y('count()', title='Давтамж'),
        tooltip=['count()']
    ).properties(
        width=600,
        height=400,
        title="Нийт хүн амын стрессийн түвшин"
    )

    # Histogram-ийг харуулах
    st.altair_chart(histogram, use_container_width=True)

def create_scatter():
        # Scatter үүсгэх
    scatter = alt.Chart(df).mark_point(color='goldenrod').encode(
        alt.X('Row of Sum:Q', bin=alt.Bin(maxbins=20), title='Row of Sum Утгууд'),
        alt.Y('count()', title='Давтамж'),
        tooltip=['count()']
    ).properties(
        width=600,
        height=400,
        title="Нийт хүн амын стрессийн түвшин"
    )

    # Scatter-ийг харуулах
    st.altair_chart(scatter, use_container_width=True)


# Графикуудыг харуулах
create_bar_chart()
create_box_chart()
create_pie_chart()
create_histogram()
create_scatter()
