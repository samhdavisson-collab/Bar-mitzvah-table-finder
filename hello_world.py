import streamlit as st
import csv

st.title("TableFinder 3.0")
guests = []
with open('data.csv', mode='r', newline='', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    for row in reader:
        guests.append(row)
        # Or print the entire dictionary row
        # print(row)


def find_by_last_name(last_name):
    return [g for g in guests if last_name.lower() in g["last_name"].lower() ]
def find_by_first_name(first_name):
    return [g for g in guests if first_name.lower() in g["first_name"].lower() ]


# selectbox = "Search by " + st.selectbox("", ["first name", "last name"], width=200)
selectbox = st.toggle("Seatch by first name")

if not selectbox:# == "Search by last name":
    matches = find_by_last_name(st.text_input("Your last name:"))
    for guest in matches:
        st.write(f"{guest['first_name']} {guest['last_name']} - {guest['table']}")
else:
    matches = find_by_first_name(st.text_input("Your first name:"))
    for guest in matches:
        st.write(f"{guest['first_name']} {guest['last_name']} - {guest['table']}")