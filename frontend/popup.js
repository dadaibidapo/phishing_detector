document.addEventListener('DOMContentLoaded', function () {
  chrome.storage.local.get('prediction', function (data) {
      const resultDiv = document.getElementById('result');
      console.log('Stored prediction:', data);
      if (data.prediction && data.prediction.rf_prediction && data.prediction.svm_prediction) {
          resultDiv.textContent = `Prediction: ${data.prediction.rf_prediction}`;
      } else {
          resultDiv.textContent = 'No prediction available.';
      }
  });
});
