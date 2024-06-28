chrome.runtime.onMessage.addListener((request, sender, sendResponse) => {
  if (request.action === "predict") {
      console.log('Received URL:', request.url);
      fetch('http://localhost:8000/predict/', {
          method: 'POST',
          headers: {
              'Content-Type': 'application/json',
          },
          body: JSON.stringify({ url: request.url }),
      })
      .then(response => response.json())
      .then(data => {
          console.log('Prediction:', data);
          sendResponse(data);
      })
      .catch(error => {
          console.error('Error predicting:', error);
          sendResponse({ error: 'Prediction failed' });
      });
      return true;  // Keeps the message channel open until `sendResponse` is called
  }
});
