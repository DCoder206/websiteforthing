// Set the initial time in seconds
let timeInSeconds = 45 * 60;

// Update the countdown timer
function updateCountdown() {
  const countdownElement = document.getElementById('timer');

  const minutes = Math.floor(timeInSeconds / 60);
  const seconds = timeInSeconds % 60;

  const formattedTime = `${minutes.toString().padStart(2, '0')}:${seconds.toString().padStart(2, '0')}`;
  countdownElement.textContent = formattedTime;

  // Decrement time by 1 second
  timeInSeconds--;

  if (timeInSeconds < 0) {
    clearInterval(countdownInterval);
    countdownElement.textContent = "Time's up!";
  }
}

// Call updateCountdown every second (1000 milliseconds)
const countdownInterval = setInterval(updateCountdown, 1000);
