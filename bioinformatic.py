import pandas as pd
import streamlit as st
from PIL import Image
import altair as alt


image =Image.open("dna.jpg")

st.image(image,use_column_width=True)

st.write("""
# DNA nucleotide web counting app
#### This app count the nucleotide composition of every DNA query.
""")

#######################################################################
def DNA_nucleotide_Count(seq):
    d=dict([
        ("A",seq.count("A")),
        ("C",seq.count("C")),
        ("T",seq.count("T")),
        ("G",seq.count("G"))
    ])

    return d

def text_show(x):
    st.subheader("2.Text")
    st.write("There are " + str(x["A"]) +" adenine(A)")
    st.write("There are " + str(x["C"]) +" cytosine(C)")
    st.write("There are " + str(x["T"]) +" thynium(T)")
    st.write("There are " + str(x["G"]) +" guanine(G)")



def plot_data_frame():
    st.subheader("3.data frame display")
    df=pd.DataFrame.from_dict(x,orient="index")
    df=df.rename({0:'count'},axis="columns")
    df.reset_index(inplace=True)
    df=df.rename(columns={'index':'nucleotide'})
    st.write(df)
    

def plot_bar_chart():
    st.subheader("4.Display Bar Graph")
    df=pd.DataFrame.from_dict(x,orient="index")
    df=df.rename({0:'count'},axis="columns")
    df.reset_index(inplace=True)
    df=df.rename(columns={'index':'nucleotide'})
    p=alt.Chart(df).mark_bar().encode(
        x="nucleotide",
        y="count"
    )
    p=p.properties(width=alt.Step(80))
    st.write(p)


st.header("Enter DNA sequence ")

sequence=st.text_input("DNA Query")
x=DNA_nucleotide_Count(sequence)
x_label=list(x)
x_values=list(x.values())
st.subheader("1.DNA Count")
x
st.text_area("Input DNA Query",f"DNA Query>\n{sequence}",height=200,on_change=[DNA_nucleotide_Count(sequence),text_show(x),plot_data_frame(),plot_bar_chart()])




