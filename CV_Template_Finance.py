
\documentclass[a4paper,8pt]{article}

\usepackage{parskip} 
\usepackage{hologo}
\usepackage{fontspec}

%other packages for formatting
\RequirePackage{color}
\RequirePackage{graphicx}
\usepackage[usenames,dvipsnames]{xcolor}
\usepackage[scale=0.9, top=.4in, bottom=.4in]{geometry}
\usepackage{enumitem}


%tabularx environment
\usepackage{tabularx}

%for lists within experience section
\usepackage{enumitem}

% centered version of 'X' col. type
\newcolumntype{C}{>{\centering\arraybackslash}X} 

%to prevent spillover of tabular into next pages
\usepackage{supertabular}
\usepackage{tabularx}
\newlength{\fullcollw}
\setlength{\fullcollw}{0.42\textwidth}

%custom \section
\usepackage{titlesec}				
\usepackage{multicol}
\usepackage{multirow}

%CV Sections inspired by: 
%http://stefano.italians.nl/archives/26
\titleformat{\section}{\Large\scshape\raggedright}{}{0em}{}[\titlerule]
\titlespacing{\section}{1pt}{2pt}{2pt}

%for publications
\usepackage[style=authoryear,sorting=ynt, maxbibnames=2]{biblatex}

%Setup hyperref package, and colours for links
\usepackage[unicode, draft=false]{hyperref}
\color[HTML]{110223}%{1C033C}
\addbibresource{citations.bib}
\setlength\bibitemsep{1em}

%for social icons
\usepackage{fontawesome5}
% \usepackage{times}

% For underline
\usepackage[normalem]{ulem}

\setmainfont{Arial}  % Set it to whatever you like

\documentclass[a4paper,8pt]{article}

\usepackage{parskip} 
\usepackage{hologo}
\usepackage{fontspec}

%other packages for formatting
\RequirePackage{color}
\RequirePackage{graphicx}
\usepackage[usenames,dvipsnames]{xcolor}
\usepackage[scale=0.9, top=.4in, bottom=.4in]{geometry}

%tabularx environment
\usepackage{tabularx}

%for lists within experience section
\usepackage{enumitem}

% centered version of 'X' col. type
\newcolumntype{C}{>{\centering\arraybackslash}X} 

%to prevent spillover of tabular into next pages
\usepackage{supertabular}
\usepackage{tabularx}
\newlength{\fullcollw}
\setlength{\fullcollw}{0.42\textwidth}

%custom \section
\usepackage{titlesec}				
\usepackage{multicol}
\usepackage{multirow}


%CV Sections inspired by: 
%http://stefano.italians.nl/archives/26
\titleformat{\section}{\Large\scshape\raggedright}{}{0em}{}[\titlerule]
\titlespacing{\section}{1pt}{2pt}{2pt}

%for publications
\usepackage[style=authoryear,sorting=ynt, maxbibnames=2]{biblatex}

%Setup hyperref package, and colours for links
% \usepackage[unicode, draft=false]{hyperref}
\color[HTML]{110223}%{1C033C}
\addbibresource{citations.bib}
\setlength\bibitemsep{1em}

%for social icons
\usepackage{fontawesome5}
% \usepackage{times}

% For underline
\usepackage[normalem]{ulem}

\setmainfont{Arial}  % Set it to whatever you like

\begin{document}

% non-numbered pages
\pagestyle{empty} 


\begin{tabularx}{\linewidth}{@{} C @{}}
\color[HTML]{1C033C} \Huge{\textbf{Julian Gottstein}} \\[6pt]
\\
\textcolor[HTML]{1C033C}{Address: Rorschacher Strasse 116, 900 St. Gallen}

\textcolor[HTML]{1C033C}{Mobile: +49 (157) 54058312 $|$}
\textcolor[HTML]{1C033C}{Email: juliangottstein@gmx.com}
\end{tabularx}

% Education
\section{EDUCATION}
\textbf{university_school_name1} \hfill \textbf{\color[HTML]{1C033C} location_us1} \\[-3ex]
\begin{itemize}[label={\large\textbullet}, left=0pt, itemsep=0.5ex, parsep=0.5ex]
    \item namemajor \hfill \color[HTML]{1C033C} timeus1 \\[-3ex]
\end{itemize}
\begin{itemize}[label=$\circ$,itemsep=0.5ex,parsep=0.5ex]
    \item Courses: courses1
    \item GPA: gpa1
    \item clubs1
\end{itemize}

\textbf{university_school_name2} \hfill \textbf{\color[HTML]{1C033C} location_us2} \\[-3ex]
\begin{itemize}[label={\large\textbullet}, left=0pt, itemsep=0.5ex, parsep=0.5ex]
    \item namemajor \hfill \color[HTML]{1C033C} timeus2 \\[-3ex]
\end{itemize}
\begin{itemize}[label=$\circ$,itemsep=0.5ex,parsep=0.5ex]
    \item Courses: courses2
    \item GPA: gpa2
    \item clubs2
\end{itemize}




%Professional Experience
\section{PROFESSIONAL EXPERIENCE}
    \textbf{experiencename1} \hfill \textbf{\color[HTML]{1C033C} location_e1} \\[-3ex]
\begin{itemize}[label={\large\textbullet}, left=0pt, itemsep=0.5ex, parsep=0.5ex]
    \item \textit{position_name1} \hfill \color[HTML]{1C033C} timee1 \\[-3ex]

\end{itemize}
\begin{itemize}[label=$\circ$,itemsep=0.5ex,parsep=0.5ex]
    \item task1.1
    \item task1.2
    \item task1.3
\end{itemize}

    \textbf{experiencename2} \hfill \textbf{\color[HTML]{1C033C} location_e2} \\[-3ex]
\begin{itemize}[label={\large\textbullet}, left=0pt, itemsep=0.5ex, parsep=0.5ex]
    \item \textit{position_name2} \hfill \color[HTML]{1C033C} timee2 \\[-3ex]

\end{itemize}
\begin{itemize}[label=$\circ$,itemsep=0.5ex,parsep=0.5ex]
    \item Task2.1
    \item Task2.2
    \item Task2.3
\end{itemize}

    \textbf{experiencename3} \hfill \textbf{\color[HTML]{1C033C} location_e3} \\[-3ex]
\begin{itemize}[label={\large\textbullet}, left=0pt, itemsep=0.5ex, parsep=0.5ex]
    \item \textit{position_name3} \hfill \color[HTML]{1C033C} timee3 \\[-3ex]

\end{itemize}
\begin{itemize}[label=$\circ$,itemsep=0.5ex,parsep=0.5ex]
    \item Task3.1
    \item Task3.2
    \item Task3.3
\end{itemize}
%Extracurriculat Activities / Engagement
\section{EXTRACURRICULAR ACTIVITIES / ENGAGEMENT}
\begin{itemize}[label={\large\textbullet}, left=0pt, itemsep=0.5ex, parsep=0.5ex]
    \item Extracurricular: extracurricular1
    \item Additional Education: additionaleducation1 
    \item Certificate \& Achievements: certificatesachievements1
\end{itemize}

% Skills & Interest
\section{SKILLS \& INTEREST}
\begin{itemize}[label={\large\textbullet}, left=0pt, itemsep=0.5ex, parsep=0.5ex]
    \item Languages: languages1
    \item Computer: languages2
    \item Interests: languages3
\end{itemize}

\end{document}




