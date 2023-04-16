// Retrieve the current visitor count from local storage
var visitorCount = localStorage.getItem('visitorCount');
		
// If the visitor count is not found in local storage, set it to zero
if (!visitorCount) {
    visitorCount = 0;
}

// Increment the visitor count and store it back in local storage
visitorCount++;
localStorage.setItem('visitorCount', visitorCount);

// Update the visitor count displayed on the page
document.getElementById('counter').textContent = visitorCount;