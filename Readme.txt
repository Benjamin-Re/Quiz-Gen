Quiz_Gen soll das Auswendiglernen ansprechender machen. 
Die Fragen werden aus der quest.db importiert. In die .db wurden sie manuell eingetragen (import aus CSV Datei mit regular expressions w�re auch denkbar, aber zu umst�ndlich f�r das Projekt). 
Flask gibt die Fragen an quiz.html weiter, wo der user sie in einem Formular beantworten kann. Das Programm �berpr�ft, ob die Antwort richtig war und gibt die n�chste Frage an den Server (Flask). Die richtigen Antworten werden gez�hlt und als Punkte angezeigt. 

#Todo
## eine kleine Animation hinzuf�gen (JS), um anzuzeigen, ob die Antwort richtig oder falsch ist. (Jetzt wechselt das Programm zu schnell zur n�chsten Frage).
## .db f�gt automatisch eine leere row hinzu (auch nachdem sie gel�scht wurde). 
