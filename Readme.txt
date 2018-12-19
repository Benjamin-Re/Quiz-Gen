Quiz_Gen soll das Auswendiglernen ansprechender machen. 
Die Fragen werden aus der quest.db importiert. In die .db wurden sie manuell eingetragen (import aus CSV Datei mit regular expressions wäre auch denkbar, aber zu umständlich für das Projekt). 
Flask gibt die Fragen an quiz.html weiter, wo der user sie in einem Formular beantworten kann. Das Programm überprüft, ob die Antwort richtig war und gibt die nächste Frage an den Server (Flask). Die richtigen Antworten werden gezählt und als Punkte angezeigt. 

#Todo
## eine kleine Animation hinzufügen (JS), um anzuzeigen, ob die Antwort richtig oder falsch ist. (Jetzt wechselt das Programm zu schnell zur nächsten Frage).
## .db fügt automatisch eine leere row hinzu (auch nachdem sie gelöscht wurde). 
