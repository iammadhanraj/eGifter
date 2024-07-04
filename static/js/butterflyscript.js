let score = 0;
let totalButterflies = 0;

var garden1 = "{% static 'img/butterflycatcher/garden1.jpg' %}";
var garden2 = "{% static 'img/butterflycatcher/garden2.jpg' %}";
var garden3 = "{% static 'img/butterflycatcher/garden3.jpg' %}";
var garden4 = "{% static 'img/butterflycatcher/garden4.jpg' %}";
var garden5 = "{% static 'img/butterflycatcher/garden5.jpg' %}";

var butterfly1 = "{% static 'img/butterflycatcher/butterfly-skyblue.gif' %}";
var butterfly2 = "{% static 'img/butterflycatcher/truth-and-tales-butterfly.gif' %}";
var butterfly3 = "{% static 'img/butterflycatcher/borboletas-butterflies-yellow.gif' %}";
var butterfly4 = "{% static 'img/butterflycatcher/borboletas-butterflies_pink_view.gif' %}";
var butterfly5 = "{% static 'img/butterflycatcher/borboletas-butterfly.gif' %}";
var butterfly6 = "{% static 'img/butterflycatcher/bf-darling.gif' %}";


function generateButterflies() {
    const garden = document.getElementById('garden');
    garden.innerHTML = ''; // Clear the garden
    score = 0;
    updateScore();

    const butterflyCount = parseInt(document.getElementById('butterflyCount').value);
    totalButterflies = butterflyCount;

    // Array of different garden background images
    const gardenImages = [garden1,garden2,garden3,garden4,garden5];

    // Randomly assign a garden background image
    const randomGardenImage = gardenImages[Math.floor(Math.random() * gardenImages.length)];
    garden.style.backgroundImage = `url(${randomGardenImage})`;

    // Array of different colored butterfly images
    const butterflyImages = [butterfly1,butterfly2,butterfly3,butterfly4,butterfly5,butterfly6];

    for (let i = 0; i < butterflyCount; i++) {
        const butterfly = document.createElement('div');
        butterfly.className = 'butterfly';
        
        // Random positions within the garden
        const top = Math.random() * (garden.clientHeight - 50); // Subtracting butterfly height
        const left = Math.random() * (garden.clientWidth - 50); // Subtracting butterfly width

        butterfly.style.top = `${top}px`;
        butterfly.style.left = `${left}px`;

        // Randomly assign a butterfly image
        const randomButterflyImage = butterflyImages[Math.floor(Math.random() * butterflyImages.length)];
        butterfly.style.backgroundImage = `url(${randomButterflyImage})`;

        butterfly.addEventListener('click', function() {
            garden.removeChild(butterfly);
            incrementScore();
            playFoundSound();
        });

        garden.appendChild(butterfly);
    }
}

function incrementScore() {
    score++;
    updateScore();
    if (score === totalButterflies) {
        showPopup();
        playCongratulationsSound();
    }
}

function updateScore() {
    document.getElementById('score').textContent = score;
}

function showPopup() {
    document.getElementById('popup').style.display = 'flex';
}

function restartGame() {
    document.getElementById('popup').style.display = 'none';
    document.getElementById('garden').innerHTML = '';
    score = 0;
    totalButterflies = 0;
    updateScore();
}

function playFoundSound() {
    const sound = document.getElementById('foundSound').cloneNode(true);
    sound.play();
}

function playCongratulationsSound() {
    const sound = document.getElementById('congratulationsSound');
    sound.play();
}
