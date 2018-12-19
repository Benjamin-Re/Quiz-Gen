<<<<<<< HEAD
Quiz_Gen soll eine CSV Datei nehmen und die Fragen plus Antworten in eine Datenbank übernehmen (entweder von Hand oder durch ein kleines Programm, das aber noch fehlt).
Das eigentliche Programm nimmt die Fragen aus der DB und gibt sie an einen Webserver (?) weiter. Der gibt sie wieder weiter an index.html. So kann man im Browser auf die antworten klicken. Das Programm überprüft, ob die Antwort richtig war und gibt die nächste Frage an den Server (Flask). Zuletzt könnte man noch eine kleine Animation hinzufügen (JS), um anzuzeigen, ob die Antwort richtig oder falsch ist. 

=======
Quiz_Gen soll das Auswendiglernen ansprechender machen. 
Die Fragen werden aus der quest.db importiert. In die .db wurden sie manuell eingetragen (import aus CSV Datei mit regular expressions wäre auch denkbar, aber zu umständlich für das Projekt). 
Flask gibt die Fragen an quiz.html weiter, wo der user sie in einem Formular beantworten kann. Das Programm überprüft, ob die Antwort richtig war und gibt die nächste Frage an den Server (Flask). Die richtigen Antworten werden gezählt und als Punkte angezeigt. 

#Todo
## eine kleine Animation hinzufügen (JS), um anzuzeigen, ob die Antwort richtig oder falsch ist. (Jetzt wechselt das Programm zu schnell zur nächsten Frage).
## .db fügt automatisch eine leere row hinzu (auch nachdem sie gelöscht wurde). 
>>>>>>> pureFlask
