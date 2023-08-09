function timer(duration,elementId) {
    let time = duration * 60;
    const timerele = document.querySelector("#" + elementId);
    const interval = setInterval(() => {
        if (time >= 0) {
            const minutes = Math.floor(time / 60);
            const seconds = time % 60;
            timerele.innerHTML = `Time left<br>${minutes.toString().padStart(2, '0')}:${seconds.toString().padStart(2, '0')}`;
            time--;
        }
        else {
            timerele.innerHTML = "Time's up";
            clearInterval(interval);
        }
    }, 1000);
}
document.addEventListener("DOMContentLoaded", () => {
    document.documentElement.requestFullscreen();
})
const timeDiv = "timer";
timer(90,timeDiv);
