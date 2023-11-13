function generateText() {
  var prompt = document.getElementById("prompt").value;
  var xhr = new XMLHttpRequest();
  xhr.open("POST", "/generate", true);
  xhr.setRequestHeader("Content-Type", "application/json");
  xhr.onreadystatechange = function () {
    if (xhr.readyState === 4 && xhr.status === 200) {
      var response = JSON.parse(xhr.responseText);
      // document.getElementById("response").innerText = response.text;
      typeResponse(response.text);
    }
  };
  var data = JSON.stringify({ text: prompt });
  xhr.send(data);
}

function typeResponse(responseText) {
  const responseContainer = document.getElementById("response");
  responseContainer.innerText = ""; // Clear previous response
  let i = 0;
  const speed = 1; // Speed of typing in milliseconds

  function typeWriter() {
    if (i < responseText.length) {
      responseContainer.innerHTML += responseText.charAt(i);
      i++;
      setTimeout(typeWriter, speed);
    }
  }

  typeWriter();
}
