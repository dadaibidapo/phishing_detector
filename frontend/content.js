chrome.runtime.sendMessage({ action: "predict", url: window.location.href }, function(response) {
  if (response.error) {
      console.error('Error predicting:', response.error);
      return;
  }
  console.log('Received prediction:', response);
  // Store the response in chrome storage
  chrome.storage.local.set({ 'prediction': response }, function() {
      console.log('Prediction stored in local storage.');
  });
});
