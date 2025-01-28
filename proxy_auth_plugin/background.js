chrome.webRequest.onAuthRequired.addListener(
    function(details, callback) {
      callback({
        authCredentials: {
          username: "khalid05kKL",  // Replace with your proxy username
          password: "KrGQkpmMiQ"   // Replace with your proxy password
        }
      });
    },
    { urls: ["http://*/*", "https://*/*"] },
    ["blocking"]
  );
  