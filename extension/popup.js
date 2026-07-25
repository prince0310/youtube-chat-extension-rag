const API_BASE = "http://127.0.0.1:8000";

let currentVideoId = null;

const videoIdDiv = document.getElementById("videoId");
const askBtn = document.getElementById("askBtn");
const questionBox = document.getElementById("question");
const chatContainer = document.getElementById("chatContainer");


function addMessage(text, cls) {

    const div = document.createElement("div");

    div.className = `message ${cls}`;

    div.innerText = text;

    chatContainer.appendChild(div);

    chatContainer.scrollTop = chatContainer.scrollHeight;

}


async function getVideoId() {

    const tabs = await chrome.tabs.query({
        active: true,
        currentWindow: true
    });

    if (!tabs.length) {
        videoIdDiv.innerText = "No Active Tab";
        return;
    }

    const tab = tabs[0];

    // Check if it's a YouTube watch page
    if (!tab.url || !tab.url.includes("youtube.com/watch")) {
        videoIdDiv.innerText = "Open a YouTube video";
        return;
    }

    // Inject content script if needed
    await chrome.scripting.executeScript({
        target: { tabId: tab.id },
        files: ["content.js"]
    });

    chrome.tabs.sendMessage(
        tab.id,
        { type: "GET_VIDEO_ID" },
        async (response) => {

            if (chrome.runtime.lastError) {
                console.error(chrome.runtime.lastError.message);
                videoIdDiv.innerText = "Cannot access page";
                return;
            }

            if (!response || !response.videoId) {
                videoIdDiv.innerText = "Video ID not found";
                return;
            }

            currentVideoId = response.videoId;
            videoIdDiv.innerText = currentVideoId;

            await fetch(`${API_BASE}/index`, {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify({
                    video_id: currentVideoId
                })
            });
        }
    );
}


askBtn.addEventListener("click", async () => {

    const question = questionBox.value.trim();

    if (question === "") return;

    addMessage(question, "user");

    questionBox.value = "";

    const loading = document.createElement("div");

    loading.className = "message ai";

    loading.innerText = "Thinking...";

    chatContainer.appendChild(loading);

    chatContainer.scrollTop = chatContainer.scrollHeight;

    const response = await fetch(`${API_BASE}/chat`, {

        method: "POST",

        headers: {
            "Content-Type": "application/json"
        },

        body: JSON.stringify({

            video_id: currentVideoId,

            question: question

        })

    });

    const data = await response.json();

    loading.remove();

    addMessage(data.answer, "ai");

});


getVideoId();