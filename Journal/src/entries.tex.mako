<%!
  import re
  import os
  from pathlib import Path
%>\
<%
  total_hours = 0.
%>
% for year in sorted(os.listdir(PATH)):
  % for month in sorted(os.listdir(os.path.join(PATH, year))):
    % for day in sorted(os.listdir(os.path.join(PATH, year, month))):

\newday{${year}/${month}/${day}}

<%
  daypath = os.path.join(PATH, year, month, day)
%>
      % for entry in sorted(os.listdir(daypath)):
        % if entry.lower().endswith('.tex'):
        <%
           filename = os.path.join(PATH, year, month, day, entry)
           with open(filename, 'r') as file_object:
             total_hours += float(re.search(
               '{(\d*[.,]?\d*)\s+[Hh]our.*}', file_object.read()).group(1))
        %>
\def\time{${os.path.splitext(entry)[0]}}
\input{${'/'.join(['entries', year, month, day, entry])}}
        % endif
      % endfor
    % endfor
  % endfor
%endfor

\clearpage

~\vfill

\textbf{\LARGE Total Project Hours \hfill ${round(total_hours, 1)} Hours}

\vfill
\vfill
