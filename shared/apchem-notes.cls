%% apchem-notes.cls -- guided notes, organised by 90-minute BLOCK LESSON
%%
%% Notes are chunked by block, not by CED topic, because nobody absorbs 90
%% minutes of lecture. Each block carries the fixed rhythm from PLAN.md 3.1:
%%   5 warm-up / 25 instruction A / 15 practice / 20 instruction B / 20 application / 5 exit

\NeedsTeXFormat{LaTeX2e}
\ProvidesClass{apchem-notes}[2026/08/08 v1.0 AP Chemistry guided notes]

\DeclareOption*{\PassOptionsToClass{\CurrentOption}{article}}
\ProcessOptions\relax
\LoadClass[11pt]{article}
\RequirePackage{apchem}

\setlength{\parindent}{0pt}
\setlength{\parskip}{0.45em}
\linespread{1.06}

% ------------------------------------------------------------- block lessons
\newcounter{apcblock}

% \blocklesson{title}{day}  -- opens a block, prints the timing plan
\newcommand{\blocklesson}[2]{%
  % first block continues the title page; later blocks start fresh
  \ifnum\value{apcblock}>0 \clearpage\fi
  \stepcounter{apcblock}%
  \needspace{6\baselineskip}%
  \begin{tcolorbox}[enhanced,colback=apcbanner,colframe=apcbanner,
      boxrule=0pt,left=10pt,right=10pt,top=6pt,bottom=6pt,arc=2pt]
    {\sffamily\bfseries\large\color{apcbannertext} BLOCK \theapcblock\ \textbullet\ #1}\\[1pt]
    {\sffamily\small\color{apcbannertext} #2 \textbullet\ 90 minutes}
  \end{tcolorbox}
  \vspace{0.3em}%
}

% \segment{label}{minutes}{title}
\newcommand{\segment}[3]{%
  \needspace{3\baselineskip}%
  \par\vspace{0.5em}%
  \noindent\begin{tcolorbox}[enhanced,colback=apclight,colframe=apcrule,
      boxrule=0.6pt,left=8pt,right=8pt,top=3pt,bottom=3pt,arc=1pt,
      before skip=2pt,after skip=6pt]
    {\sffamily\bfseries\small\color{apcaccent} #1}%
    \hfill{\sffamily\small\color{apcgray} #2 min}\\[1pt]
    {\sffamily\bfseries\normalsize #3}
  \end{tcolorbox}%
}

% Objectives strip at the top of each block
\newenvironment{objectives}{%
  \begin{tcolorbox}[enhanced,breakable,colback=white,colframe=apcrule,
    boxrule=0.6pt,left=6pt,right=6pt,top=4pt,bottom=4pt,
    title={\sffamily\bfseries\small BY THE END OF THIS BLOCK YOU CAN\ldots},
    coltitle=apcaccent,colbacktitle=apclight]%
  \begin{itemize}[leftmargin=*,itemsep=0.2em,topsep=2pt]%
}{%
  \end{itemize}\end{tcolorbox}\vspace{0.3em}%
}

% Reading assignment -- always a page range, never a bare chapter number.
% Unit 3 alone draws on seven separate locations in Zumdahl; "read chapter 10"
% would hand a student a fraction of the unit.
\newcommand{\reading}[2]{%
  \par\noindent{\sffamily\small\color{apcgray}%
  \textbf{Read:} #1 \textbullet\ PDF pp.~#2}\par\vspace{0.2em}%
}

\newcommand{\notesection}[2]{%
  \needspace{3\baselineskip}%
  \par\vspace{0.6em}%
  \noindent{\sffamily\bfseries\large\color{apcaccent}#1}\hfill\ced{#2}%
  \par\vspace{-0.4em}%
  \noindent\textcolor{apcrule}{\rule{\linewidth}{0.8pt}}%
  \par\vspace{0.3em}%
}

% Chapter-track variant: tags the Zumdahl section instead of a CED topic.
\newcommand{\notesectionz}[2]{%
  \needspace{3\baselineskip}%
  \par\vspace{0.6em}%
  \noindent{\sffamily\bfseries\large\color{apcaccent}#1}\hfill\zsec{#2}%
  \par\vspace{-0.4em}%
  \noindent\textcolor{apcrule}{\rule{\linewidth}{0.8pt}}%
  \par\vspace{0.3em}%
}

\newcommand{\notesub}[1]{%
  \needspace{2\baselineskip}%
  \par\vspace{0.35em}%
  \noindent{\sffamily\bfseries\color{apcgray}#1}\par\vspace{0.15em}%
}

\endinput
