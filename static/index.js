/**
 * @file Handles all frontend JavaScript logic for the OpenDex application.
 * This script is responsible for capturing user input, sending it to the
 * backend API, and displaying the results.
 */

// --- DOM Element Selection ---

/**
 * The main submit button for the prompt form.
 * @type {HTMLElement}
 */
const submitButton = document.getElementById('submit');

/**
 * The loader element (spinner) that is displayed during API requests.
 * @type {HTMLElement}
 */
const loader = document.getElementById('loader');

/**
 * The HTML div element where the API response will be displayed.
 * @type {HTMLElement}
 */
const responseDiv = document.getElementById('response');

// --- Event Listener ---

/**
 * Attaches a 'click' event listener to the submit button to handle form submission.
 *
 * When the button is clicked, this function orchestrates the entire process of
 * sending a user's prompt to the API and displaying the result. It handles UI
 * state changes (like showing/hiding the loader), gathers all necessary data
 * from the form, and initiates the asynchronous API call.
 *
 * @param {Event} event - The click event object from the browser.
 */
submitButton.addEventListener('click', (event) => {
    // 1. Update UI to indicate loading and prevent multiple submissions
    loader.style.display = 'block';
    submitButton.style.display = 'none';
    responseDiv.innerHTML = ''; // Clear previous results

    console.log('submit button clicked');
    event.preventDefault(); // Prevent the default form submission behavior

    // 2. Gather all required data from the form fields
    const prompt = document.getElementById('prompt').value;
    const apikey = document.getElementById('key').value;
    const model = document.getElementById('model').value;

    // 3. Create and configure the XMLHttpRequest to send data to the backend
    const xhr = new XMLHttpRequest();
    xhr.open('POST', '/api');
    xhr.responseType = 'json';
    xhr.setRequestHeader('Content-Type', 'application/json');

    /**
     * Defines the callback function to execute when the API request finishes.
     *
     * This anonymous function is the core of the response handling logic. It
     * is triggered once the server has responded to the XMLHttpRequest.
     *
     * It first checks the HTTP status of the response. If the status is 200 (OK),
     * it extracts the `output` from the JSON response and displays it to the user.
     * If the status indicates an error, it displays a generic error message along
     * with the specific error returned by the API.
     *
     * Finally, regardless of the outcome, it reverts the UI to its original state
     * by hiding the loader and showing the submit button, allowing the user to
     * make another request.
     */
    xhr.onload = () => {
        const response = xhr.response;
        if (xhr.status === 200) {
            // Success case: Display the API's output
            console.log(response);
            responseDiv.innerHTML = response.output;
        } else {
            // Error case: Display the error message
            responseDiv.innerHTML = 'Error\n' + response.error;
            console.error(response);
        }
        // 4. Restore the UI to its initial state
        loader.style.display = 'none';
        submitButton.style.display = 'block';
    };

    // 5. Send the request with the JSON-stringified payload
    xhr.send(JSON.stringify({ prompt: prompt, key: apikey, model: model }));
});