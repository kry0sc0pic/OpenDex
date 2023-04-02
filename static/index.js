const submitButton = document.getElementById('submit');
const loader = document.getElementById('loader');
const responseDiv = document.getElementById('response');
submitButton.addEventListener('click', (event) => {
    loader.style.display = 'block';
    submitButton.style.display = 'none';
    responseDiv.innerHTML = '';
    console.log('submit button clicked');
    event.preventDefault();
    // prevent default form submission
    const prompt = document.getElementById('prompt').value;
    const xhr = new XMLHttpRequest();
    xhr.open('POST', '/api');
    xhr.responseType = 'json';
    xhr.setRequestHeader('Content-Type', 'application/json');
    xhr.onload = () => {
        const response = xhr.response;
        if (xhr.status === 200) {
            console.log(response);

            responseDiv.innerHTML = response.output;
        } else {
            responseDiv.innerHTML = 'Error\n' + response.error;
            console.error(response);
        }
        loader.style.display = 'none';
        submitButton.style.display = 'block';
    };
    xhr.send(JSON.stringify({ prompt: prompt }));


});