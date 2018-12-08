$(document).ready(function () {

	document.getElementById("a").innerHTML = "CHANGE";
	document.getElementById("quest").innerHTML = "Hello World!";
	function myFunction() {
	   document.getElementById("b").innerHTML = "Paragraph changed.";
	}

	myFunction();

	function test(){
		document.getElementById("quest").innerHTML = "q changed";
		document.getElementById("a").innerHTML = "a changed";
		document.getElementById("b").innerHTML = "b changed";
		document.getElementById("c").innerHTML = "c changed";
		document.getElementById("d").innerHTML = "d changed";
	};

	document.getElementById("next").addEventListener("click", test);

	$.getJSON("testJson.js", function(json) {
			console.log("JSON Data: " + json[1]);
		});
	
	
});