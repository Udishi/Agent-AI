async function sendMessage(){

const input = document.getElementById("userInput");

const message = input.value;

if(message==="") return;

const chatBox = document.getElementById("chat-box");


chatBox.innerHTML +=
`
<div class="user">
${message}
</div>
`;


input.value = "";


const response = await fetch("http://127.0.0.1:8000/chat",{

method:"POST",

headers:{
"Content-Type":"application/json"
},

body:JSON.stringify({

message:message

})

});


const data = await response.json();


chatBox.innerHTML +=
`
<div class="bot">
${data.response}
</div>
`;


chatBox.scrollTop = chatBox.scrollHeight;

}
