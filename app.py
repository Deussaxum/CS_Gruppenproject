import streamlit as st
import requests

# Streamlit-Benutzeroberfläche
st.title("CV-Generator")

# Persönliche Informationen
st.header("Personal Information")
name = st.text_input("Name")
address = st.text_input("Adresse")
phone = st.text_input("Telefonnummer")
email = st.text_input("E-Mail")

# Education
st.header("Education")
university1 = st.text_input("Universität/Schule 1")
location_us1 = st.text_input("Standort 1")
majorus1 = st.text_input("Studiengang 1")
timeus1 = st.text_input("Zeitraum 1")
courses1 = st.text_input("Kurse 1")
gpa1 = st.text_input("GPA 1")
clubs1 = st.text_input("Clubs/Aktivitäten 1")

university2 = st.text_input("Universität/Schule 2", "")
location_us2 = st.text_input("Standort 2", "")
majorus2 = st.text_input("Studiengang 2", "")
timeus2 = st.text_input("Zeitraum 2", "")
courses2 = st.text_input("Kurse 2", "")
gpa2 = st.text_input("GPA 2", "")
clubs2 = st.text_input("Clubs/Aktivitäten 2", "")

# Professional Experience
st.header("Professional Experience")
experience1 = st.text_input("Erfahrung 1")
location_e1 = st.text_input("Standort Erfahrung 1")
position1 = st.text_input("Position 1")
timee1 = st.text_input("Zeitraum Erfahrung 1")
task11 = st.text_area("Aufgaben 1", height=100)
task12 = st.text_area("Aufgaben 2", height=100)
task13 = st.text_area("Aufgaben 3", height=100)

experience2 = st.text_input("Erfahrung 2", "")
location_e2 = st.text_input("Standort Erfahrung 2", "")
position2 = st.text_input("Position 2", "")
timee2 = st.text_input("Zeitraum Erfahrung 2", "")
task21 = st.text_area("Aufgaben 1", height=100)
task22 = st.text_area("Aufgaben 2", height=100)
task23 = st.text_area("Aufgaben 3", height=100)

experience3 = st.text_input("Erfahrung 3", "")
location_e3 = st.text_input("Standort Erfahrung 3", "")
position3 = st.text_input("Position 3", "")
timee3 = st.text_input("Zeitraum Erfahrung 3", "")
task31 = st.text_area("Aufgaben 1", height=100)
task32 = st.text_area("Aufgaben 2", height=100)
task33 = st.text_area("Aufgaben 3", height=100)

# Extracurriculat Activities / Engagement
st.header("Extracurriculat Activities / Engagement")
extracurricular1 = st.text_input("Extrakurrikulare Aktivitäten")
additionaleducation1 = st.text_input("Zusätzliche Bildung")
certificates1 = st.text_input("Zertifikate und Errungenschaften")

# Skills & Interest
st.header("Skills & Interest")
languages1 = st.text_input("Sprachen")
computer1 = st.text_input("Computerkenntnisse")
interests1 = st.text_input("Interessen")

# Button zum Erstellen des CVs
if st.button("CV Erstellen"):
    # Hier die Logik zum Einsetzen der Daten in die LaTeX-Vorlage und deren Verarbeitung hinzufügen
    # ...

    st.success("CV erfolgreich erstellt!")
