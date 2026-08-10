%% apchem-worksheet.cls -- practice sets sized to the 15-minute in-class window
%%
%% Three worksheet types (PLAN.md 4):
%%   A  skill drill        -- computational fluency, answer-only key
%%   B  conceptual         -- particulate diagrams, draw-and-explain
%%   C  AP-style FRQ       -- College Board voice, rubric visible to students

\NeedsTeXFormat{LaTeX2e}
\ProvidesClass{apchem-worksheet}[2026/08/08 v1.0 AP Chemistry worksheet]

\DeclareOption*{\PassOptionsToClass{\CurrentOption}{article}}
\ProcessOptions\relax
\LoadClass[11pt]{article}
\RequirePackage{apchem}

\setlength{\parindent}{0pt}
\setlength{\parskip}{0.4em}

\newcommand{\apc@wstype}{}
\newcommand{\wstype}[1]{\renewcommand{\apc@wstype}{#1}}

\newcommand{\wsheader}[1][]{%
  \apctitleblock
  \ifstrempty{#1}{}{%
    \noindent\begin{tcolorbox}[enhanced,colback=white,colframe=apcrule,
      boxrule=0.6pt,left=8pt,right=8pt,top=4pt,bottom=4pt,arc=1pt]
      {\sffamily\small\textbf{Directions.} #1}
    \end{tcolorbox}\vspace{0.3em}%
  }%
}

% Problems carry their CED topic so gaps are visible at a glance when you
% grade a stack and see the same tag failing.
\newcounter{apcprob}
\newcommand{\problem}[2][]{%
  \stepcounter{apcprob}%
  \needspace{3\baselineskip}%
  \par\vspace{0.5em}%
  \noindent{\sffamily\bfseries\color{apcaccent}\theapcprob.}%
  \ifstrempty{#1}{}{\hfill\ced{#1}}%
  \par\vspace{0.15em}%
  \noindent #2\par%
}

\newenvironment{parts}{%
  \begin{enumerate}[label=(\alph*),leftmargin=1.6em,itemsep=0.35em,topsep=2pt]%
}{\end{enumerate}}

\endinput
