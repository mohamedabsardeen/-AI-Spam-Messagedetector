const messageBox = document.getElementById("message");
const predictBtn = document.getElementById("predictBtn");
const resultBox = document.getElementById("result");
const labelEl = document.getElementById("label");
const detailsEl = document.getElementById("details");
const barFill = document.getElementById("barFill");

predictBtn.addEventListener("click", async () => {
    const message = messageBox.value.trim();

    if (!message) {
        alert("Please enter a message first.");
        return;
    }

    predictBtn.disabled = true;
    predictBtn.textContent = "Checking...";

    try {
        const response = await fetch("/predict", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ message: message }),
        });

        const data = await response.json();

        if (!response.ok) {
            alert(data.error || "Something went wrong.");
            return;
        }

        resultBox.classList.remove("hidden", "spam", "ham");
        resultBox.classList.add(data.is_spam ? "spam" : "ham");

        labelEl.textContent = data.is_spam ? "🚫 Spam" : "✅ Not Spam";
        detailsEl.textContent =
            "Confidence: " + data.confidence + "%  |  Spam probability: " + data.spam_probability + "%";
        barFill.style.width = data.spam_probability + "%";
    } catch (error) {
        alert("Could not reach the server. Is Flask running on port 5000?");
    } finally {
        predictBtn.disabled = false;
        predictBtn.textContent = "Predict";
    }
});
