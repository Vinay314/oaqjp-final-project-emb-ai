let RunSentimentAnalysis = () => {
    let textToAnalyze = document.getElementById("textToAnalyze").value;

    let xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        if (this.readyState == 4) {
            if (this.status == 200) {
                const response = JSON.parse(xhttp.responseText);
                document.getElementById("system_response").innerHTML = response.output;
            } else {
                document.getElementById("system_response").innerHTML = 'Invalid text! Please try again!';
            }
        }
    };

    xhttp.open("POST", "/emotionDetector", true); // Change to POST
    xhttp.setRequestHeader("Content-Type", "application/x-www-form-urlencoded"); // Set content type
    xhttp.send("statement=" + encodeURIComponent(textToAnalyze)); // Send the text
}
