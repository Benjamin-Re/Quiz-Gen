<<<<<<< HEAD
Quiz_Gen soll eine CSV Datei nehmen und die Fragen plus Antworten in eine Datenbank �bernehmen (entweder von Hand oder durch ein kleines Programm, das aber noch fehlt).
Das eigentliche Programm nimmt die Fragen aus der DB und gibt sie an einen Webserver (?) weiter. Der gibt sie wieder weiter an index.html. So kann man im Browser auf die antworten klicken. Das Programm �berpr�ft, ob die Antwort richtig war und gibt die n�chste Frage an den Server (Flask). Zuletzt k�nnte man noch eine kleine Animation hinzuf�gen (JS), um anzuzeigen, ob die Antwort richtig oder falsch ist. 

=======
Quiz_Gen soll das Auswendiglernen ansprechender machen. 
Die Fragen werden aus der quest.db importiert. In die .db wurden sie manuell eingetragen (import aus CSV Datei mit regular expressions w�re auch denkbar, aber zu umst�ndlich f�r das Projekt). 
Flask gibt die Fragen an quiz.html weiter, wo der user sie in einem Formular beantworten kann. Das Programm �berpr�ft, ob die Antwort richtig war und gibt die n�chste Frage an den Server (Flask). Die richtigen Antworten werden gez�hlt und als Punkte angezeigt. 

#Todo
## eine kleine Animation hinzuf�gen (JS), um anzuzeigen, ob die Antwort richtig oder falsch ist. (Jetzt wechselt das Programm zu schnell zur n�chsten Frage).
## .db f�gt automatisch eine leere row hinzu (auch nachdem sie gel�scht wurde). 
>>>>>>> pureFlask
