import streamlit as st
import requests

latex_preamble = r"""
\documentclass[a4paper,8pt]{article}

\usepackage{parskip} 
\usepackage{hologo}
\usepackage{fontspec}
% ... (rest of the preamble remains the same)
"""

def compile_pdf(name, address, mobile, email):
    latex_code = fr"""
    \documentclass[a4paper,8pt]{{article}}

    \usepackage{{parskip}} 
    \usepackage{{hologo}}
    \usepackage{{fontspec}}

    %other packages for formatting
    \RequirePackage{{color}}
    \RequirePackage{{graphicx}}
    \usepackage[usenames,dvipsnames]{{xcolor}}
    \usepackage[scale=0.9, top=.4in, bottom=.4in]{{geometry}}
    \usepackage{{enumitem}}

    %tabularx environment
    \usepackage{{tabularx}}

    %for lists within experience section
    \usepackage{{enumitem}}

    % centered version of 'X' col. type
    \newcolumntype{{C}}{{>{{\centering\arraybackslash}}X}} 

    %to prevent spillover of tabular into next pages
    \usepackage{{supertabular}}
    \usepackage{{tabularx}}
    \newlength{{\fullcollw}}
    \setlength{{\fullcollw}}{{0.42\textwidth}}

    %custom \section
    \usepackage{{titlesec}}                
    \usepackage{{multicol}}
    \usepackage{{multirow}}

    %CV Sections inspired by: 
    %http://stefano.italians.nl/archives/26
    \titleformat{{\section}}{{\Large\scshape\raggedright}}{{}}{{0em}}{{}}[\titlerule]
    \titlespacing{{\section}}{{1pt}}{{2pt}}{{2pt}}

    %for publications
    \usepackage[style=authoryear,sorting=ynt, maxbibnames=2]{{biblatex}}

    %Setup hyperref package, and colours for links
    \usepackage[unicode, draft=false]{{hyperref}}
    \color[HTML]{{110223}}%{{1C033C}}
    \addbibresource{{citations.bib}}
    \setlength{{\bibitemsep}}{{1em}}

    %for social icons
    \usepackage{{fontawesome5}}
    % \usepackage{{times}}

    % For underline
    \usepackage[normalem]{{ulem}}

    \setmainfont{{Arial}}  % Set it to whatever you like

    \begin{{document}}

    % non-numbered pages
    \pagestyle{{empty}} 


    \begin{{tabularx}}{{\linewidth}}{{@{{}} C @{{}}}}
    \color[HTML]{{1C033C}} \Huge{{\textbf{{{name}}}}} \\[6pt]
    \\
    \textcolor[HTML]{{1C033C}}{{Address: {address}}} \\
    \textcolor[HTML]{{1C033C}}{{Mobile: {mobile} $|$}}
    \textcolor[HTML]{{1C033C}}{{Email: {email}}}
    \end{{tabularx}}
    \end{{document}}
    """

    data = {
        "compiler": "pdflatex",
        "code": latex_code,
    }

    response = requests.post("https://www.overleaf.com/project", data=data)
    
    if response.status_code == 200:
        pdf_data = response.content
        return pdf_data
    else:
        st.error("Error compiling PDF")



st.write("# Applify")
st.latex(r"\LaTeX")

st.write("Enter your information here:")
name = st.text_input("Name", "Julian Gottstein")
address = st.text_input("Address", "Rorschacher Strasse 116, 900 St. Gallen")
mobile = st.text_input("Mobile", "+49 (157) 54058312")
email = st.text_input("Email", "juliangottstein@gmx.com")

if st.button("Compile PDF"):
    pdf_data = compile_pdf(name, address, mobile, email)
    if pdf_data is not None:
        st.download_button("Download PDF", pdf_data, file_name='CV.pdf', mime='application/pdf')