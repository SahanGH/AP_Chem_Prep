%% apchem-exam.cls -- AP-mirror unit exams
%%
%% Mirrors the real exam's structure so May holds no format surprises:
%%   Section I  multiple choice, NO CALCULATOR, ~1.5 min/question
%%   Section II free response, calculator permitted, long = 10 pts / short = 4 pts
%%
%% Answers, distractor rationales, and rubric points all live inline beside the
%% question and appear only under \ISKEY -- the key cannot drift from the exam.

\NeedsTeXFormat{LaTeX2e}
\ProvidesClass{apchem-exam}[2026/08/08 v1.0 AP Chemistry unit exam]

\DeclareOption*{\PassOptionsToClass{\CurrentOption}{article}}
\ProcessOptions\relax
\LoadClass[11pt]{article}
\RequirePackage{apchem}

\setlength{\parindent}{0pt}
\setlength{\parskip}{0.35em}

\newcounter{apcmcq}
\newcounter{apcfrq}
\newcounter{apcpoints}

% ------------------------------------------------------------ section banners
\newcommand{\examsection}[4]{%
  \needspace{5\baselineskip}%
  \par\vspace{0.6em}%
  \begin{tcolorbox}[enhanced,colback=apcbanner,colframe=apcbanner,boxrule=0pt,
      left=10pt,right=10pt,top=6pt,bottom=6pt,arc=2pt]
    {\sffamily\bfseries\large\color{apcbannertext} SECTION #1 \textbullet\ #2}\\[1pt]
    {\sffamily\small\color{apcbannertext} #3}
  \end{tcolorbox}%
  \ifstrempty{#4}{}{%
    \vspace{-0.2em}%
    \begin{tcolorbox}[enhanced,colback=apcwarnbg,colframe=apcwarn,boxrule=1pt,
        left=8pt,right=8pt,top=4pt,bottom=4pt,arc=1pt]
      {\sffamily\bfseries\color{apcwarn} #4}
    \end{tcolorbox}%
  }%
  \vspace{0.3em}%
}

% Students sit the real calculator policy from Unit 1 onward. A year of
% calculator-assisted multiple choice produces a May disaster.
\newcommand{\nocalculator}{NO CALCULATOR PERMITTED ON THIS SECTION}
\newcommand{\calculatorok}{Calculator permitted. Equations sheet and periodic table provided.}

% ------------------------------------------------------------- multiple choice
% \choices opens the option list inside the mcq body and the environment's end
% code closes it -- low-level \enumerate/\endenumerate forms are used so the
% open/close pair does not fight LaTeX's \begin/\end name matching.
\newenvironment{mcq}{%
  \stepcounter{apcmcq}\addtocounter{apcpoints}{1}%
  \needspace{5\baselineskip}%
  \par\vspace{0.55em}%
  \noindent{\sffamily\bfseries\color{apcaccent}\theapcmcq.}~\ignorespaces
}{%
  \endenumerate\par\vspace{0.1em}%
}

\newcommand{\choices}{%
  \par\vspace{0.15em}%
  \enumerate[label=(\Alph*),leftmargin=1.9em,itemsep=0.12em,topsep=1pt]%
}

\newcommand{\choice}[1]{\item #1}

\newcommand{\correct}[1]{%
  \item \iftoggle{apcKey}{%
    {\bfseries\color{apcans}#1}\ {\color{apcans}\raisebox{0.05em}{$\blacktriangleleft$}}%
  }{#1}%
}

% Why students pick the wrong one -- the most useful thing on a key when you
% are deciding what to reteach Wednesday.
\newcommand{\why}[1]{\keyonly{%
  \par\vspace{0.15em}%
  \noindent{\sffamily\footnotesize\color{apcans}\textbf{Why:} #1}\par}%
}
\newcommand{\distractor}[2]{\keyonly{%
  \par\noindent{\sffamily\footnotesize\color{apcgray}\textbf{(#1)} #2}\par}%
}

% -------------------------------------------------------------- free response
% \frq{long}{10}{topic}
\newcommand{\frq}[3]{%
  \stepcounter{apcfrq}\addtocounter{apcpoints}{#2}%
  \needspace{6\baselineskip}%
  \par\vspace{0.7em}%
  \begin{tcolorbox}[enhanced,colback=apclight,colframe=apcaccent,boxrule=0.9pt,
      left=8pt,right=8pt,top=4pt,bottom=4pt,arc=1pt]
    {\sffamily\bfseries\color{apcaccent} Question \theapcfrq\ \textbullet\ #1 response}%
    \hfill{\sffamily\bfseries\color{apcaccent} #2 points}\\[1pt]
    {\sffamily\footnotesize\color{apcgray} #3}
  \end{tcolorbox}%
  \vspace{0.2em}%
}

\newenvironment{parts}{%
  \begin{enumerate}[label=(\alph*),leftmargin=1.8em,itemsep=0.5em,topsep=3pt]%
}{\end{enumerate}}

% Rubrics use real AP point language. Students who have never seen a rubric
% write essays instead of earning points, so Type C worksheets show this too.
% environ collects the body UNEXECUTED, so the student build can drop it
% without ever running the \item commands inside.
\RequirePackage{environ}
\NewEnviron{rubric}{%
  \iftoggle{apcKey}{%
    \needspace{4\baselineskip}%
    \begin{tcolorbox}[enhanced,breakable,colback=apcansbg,colframe=apcans,
      boxrule=0.9pt,left=6pt,right=6pt,top=4pt,bottom=4pt,
      title={\sffamily\bfseries\small SCORING RUBRIC},
      coltitle=apcbannertext,colbacktitle=apcbannerans]%
    \begin{itemize}[leftmargin=*,itemsep=0.3em,topsep=2pt,label={}]%
      \BODY
    \end{itemize}%
    \end{tcolorbox}%
  }{}%
}

\newcommand{\rpoint}[2]{%
  \item{\sffamily\bfseries\color{apcans}#1 pt:}\ #2%
}

\newcommand{\examtotal}{%
  \par\vspace{0.8em}%
  \noindent\begin{tcolorbox}[enhanced,colback=apclight,colframe=apcaccent,
      boxrule=0.9pt,left=8pt,right=8pt,top=4pt,bottom=4pt,arc=1pt]
    {\sffamily\bfseries\color{apcaccent} Total: \theapcmcq\ multiple choice
     \textbullet\ \theapcfrq\ free response \textbullet\ \theapcpoints\ points}
  \end{tcolorbox}%
}

\endinput
