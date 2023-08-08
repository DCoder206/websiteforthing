function redirect(loc) {
    window.location.href = loc;
}
const but = document.querySelector("#button")
but.addEventListener("click",(event) => {
    event.preventDefault();
    const inp = document.querySelector("#schName").value
    if (inp.length !== 0) {
        redirect("abc/")
    }
    else {
        const div = document.querySelector("#msg");
        div.innerHTML = "Invalid input<br>Enter your school name"
    }
})