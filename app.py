import streamlit as st
import requests

# Streamlit UI for collecting user inputs
st.write("# CV Generator")

name = st.text_input("Name", "Julian Gottstein")
address = st.text_input("Address", "Rorschacher Strasse 116, 900 St. Gallen")
mobile = st.text_input("Mobile", "+49 (157) 54058312")
email = st.text_input("Email", "juliangottstein@gmx.com")

if st.button("Generate CV"):
    # Generate LaTeX code with placeholders for user information
    latex_code = fr"""
    \documentclass[a4paper,8pt]{{article}}

    % ... (rest of the LaTeX preamble remains the same)

    \begin{{document}}

    \begin{{tabularx}}{{\linewidth}}{{@{{}} C @{{}}}}
    \color[HTML]{{1C033C}} \Huge{{\textbf{{{name}}}}} \\[6pt]
    \\
    \textcolor[HTML]{{1C033C}}{{Address: {address}}} \\
    \textcolor[HTML]{{1C033C}}{{Mobile: {mobile} $|$}}
    \textcolor[HTML]{{1C033C}}{{Email: {email}}}
    \end{{tabularx}}

    \end{{document}}
    """

    # Make an HTTP POST request to Overleaf's API
    response = requests.post("https://www.overleaf.com/docs", data={"snip_uri": latex_code})

    if response.status_code == 200:
        st.success("CV generated successfully on Overleaf! You can access it there.")
        st.write("You can download the generated PDF from the following link:")
        overleaf_url = response.json().get("url")
        st.write(f"[Download CV PDF from Overleaf]({overleaf_url})")
    else:
        st.error("Error generating CV. Please try again later.")
