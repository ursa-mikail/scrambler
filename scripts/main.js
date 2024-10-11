const digits = 100; // Change this to the desired number of digits

/*
function generateRandomKey(digits) {
    const min = Math.pow(10, digits - 1);
    const max = Math.pow(10, digits) - 1;
    const randomNumber = Math.floor(Math.random() * (max - min + 1)) + min;
    return randomNumber.toFixed(0); // Converts the number to string without decimal points
}
*/

function generateRandomKey(digits) {
    let randomNumber = '';
    for (let i = 0; i < digits; i++) {
        randomNumber += Math.floor(Math.random() * 10); // Generates a random digit from 0 to 9
    }
    return randomNumber; // Returns the constructed string of digits
}

/*
function runRandomNumbers() {
    const blackScreen = document.getElementById('black-screen');
    const digits = 50; // Change this to the desired number of digits
    let intervalId = setInterval(() => {
        let randomNumber = generateRandomKey(digits);
        blackScreen.innerText = randomNumber;
    }, 1000);

    setTimeout(() => {
        clearInterval(intervalId);
    }, 10000); // Run for 10 seconds
}
*/

function runRandomNumbers() {
    const blackScreen = document.getElementById('black-screen');
    let intervalId = setInterval(() => {
        let randomNumber = generateRandomKey(digits);
        blackScreen.innerText = randomNumber;
    }, 1000);

    setTimeout(() => {
        clearInterval(intervalId);
    }, 10000); // Run for 10 seconds
}

function shuffleKeypad() {
    let number_of_keys = 20;
    let keys = Array.from(Array(number_of_keys).keys());
    for (let i = keys.length - 1; i > 0; i--) {
        const j = Math.floor(Math.random() * (i + 1));
        [keys[i], keys[j]] = [keys[j], keys[i]];
    }
    return keys;
}

function renderKeypad() {
    let scrambledKeys = shuffleKeypad();
    let keypad = document.getElementById('keypad');
    keypad.innerHTML = '';
    scrambledKeys.forEach(key => {
        let keyElement = document.createElement('div');
        keyElement.className = 'key';
        keyElement.innerText = key;
        keyElement.onclick = function() {
            alert('Key pressed: ' + key);
        };
        keypad.appendChild(keyElement);
    });
}



document.addEventListener('DOMContentLoaded', () => {
    renderKeypad();
    document.getElementById('run-random').addEventListener('click', runRandomNumbers);
});
