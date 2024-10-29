document.getElementById("ttsModalButton").addEventListener("click", () => {
  const title = document.getElementById("instrumentTitle").innerText;
  const description = document.getElementById(
    "instrumentDescription"
  ).innerText;
  const text = `${title}. ${description}`; // 제목과 설명을 결합

  getSpeechAudio(text);
});

async function getSpeechAudio(text) {
  const subscriptionKey = "516cb868c787467581b7189d5ab4bbbd"; // 구독 키
  const region = "eastus"; // 지역

  const tokenResponse = await fetch(
    `https://${region}.api.cognitive.microsoft.com/sts/v1.0/issueToken`,
    {
      method: "POST",
      headers: {
        "Ocp-Apim-Subscription-Key": subscriptionKey,
        "Content-Type": "application/x-www-form-urlencoded",
        "Content-Length": "0",
      },
    }
  );

  const accessToken = await tokenResponse.text();

  const ssml = `<speak version='1.0' xml:lang='ko-KR'>
        <voice xml:lang='ko-KR' xml:gender='Female' name='ko-KR-SunHiNeural'>
            ${text}
        </voice>
    </speak>`;

  const response = await fetch(
    `https://${region}.tts.speech.microsoft.com/cognitiveservices/v1`,
    {
      method: "POST",
      headers: {
        Authorization: `Bearer ${accessToken}`,
        "Content-Type": "application/ssml+xml",
        "X-Microsoft-OutputFormat": "audio-24khz-48kbitrate-mono-mp3",
      },
      body: ssml,
    }
  );

  if (response.ok) {
    const audioBlob = await response.blob();
    const audioUrl = URL.createObjectURL(audioBlob);
    const audio = new Audio(audioUrl);
    audio.play();
  } else {
    console.error("TTS 요청 실패:", response.statusText);
  }
}

async function getSpeechAudio(text) {
  const subscriptionKey = "516cb868c787467581b7189d5ab4bbbd"; // 구독 키
  const region = "eastus"; // 지역

  const tokenResponse = await fetch(
    `https://${region}.api.cognitive.microsoft.com/sts/v1.0/issueToken`,
    {
      method: "POST",
      headers: {
        "Ocp-Apim-Subscription-Key": subscriptionKey,
        "Content-Type": "application/x-www-form-urlencoded",
        "Content-Length": "0",
      },
    }
  );

  const accessToken = await tokenResponse.text();

  const ssml = `<speak version='1.0' xml:lang='ko-KR'>
        <voice xml:lang='ko-KR' xml:gender='Female' name='ko-KR-SunHiNeural'>
            ${text}
        </voice>
    </speak>`;

  const response = await fetch(
    `https://${region}.tts.speech.microsoft.com/cognitiveservices/v1`,
    {
      method: "POST",
      headers: {
        Authorization: `Bearer ${accessToken}`,
        "Content-Type": "application/ssml+xml",
        "X-Microsoft-OutputFormat": "audio-24khz-48kbitrate-mono-mp3",
      },
      body: ssml,
    }
  );

  if (response.ok) {
    const audioBlob = await response.blob();
    const audioUrl = URL.createObjectURL(audioBlob);
    const audio = new Audio(audioUrl);
    audio.play();
  } else {
    console.error("TTS 요청 실패:", response.statusText);
  }
}
