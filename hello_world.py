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

matches = find_by_last_name(st.text_input("Your last name:"))
for guest in matches:
    st.write(f"{guest['first_name']} {guest['last_name']} - {guest['table']}")