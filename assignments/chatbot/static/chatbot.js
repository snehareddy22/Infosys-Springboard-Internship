const chatInput = document.getElementById("chatInput");
const chatSend = document.getElementById("chatSend");
const chatReply = document.getElementById("chatReply");
const langSel = document.getElementById("langSel");

async function sendToAI() {
  const message = chatInput.value.trim();
  if (!message) return;

  chatReply.textContent = "Thinking...";

  try {
    const res = await fetch("/chat", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        message: message,
        lang: langSel.value
      })
    });

    if (!res.ok) {
      chatReply.textContent = "Server error.";
      return;
    }

    const data = await res.json();
    chatReply.textContent = data.reply || "No reply from AI.";
  } catch (err) {
    console.error(err);
    chatReply.textContent = "Could not connect to server.";
  }
}

chatSend.addEventListener("click", sendToAI);
chatInput.addEventListener("keydown", (e) => {
  if (e.key === "Enter") sendToAI();
});
