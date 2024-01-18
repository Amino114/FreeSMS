const toggleApi = document.getElementById('toggle-api');
const apiKey = document.getElementById('api-key');
const apiSecret = document.getElementById('api-secret');

// Reset the toggle button state when the page loads
toggleApi.checked = false;
apiKey.style.display = apiSecret.style.display = 'none';

toggleApi.addEventListener('change', () => {
  apiKey.style.display = apiSecret.style.display = toggleApi.checked ? 'flex' : 'none';
});

// Clear all text input and textarea fields when the page loads
window.onload = function() {
    const inputs = document.getElementsByTagName('input');
    for(let i = 0; i < inputs.length; i++) {
        if(inputs[i].type.toLowerCase() == 'text') {
            inputs[i].value = '';
        }
    }
    const textareas = document.getElementsByTagName('textarea');
    for(let i = 0; i < textareas.length; i++) {
        textareas[i].value = '';
    }
}