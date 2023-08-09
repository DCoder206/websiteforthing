function redirect(loc) {
    window.location.href = loc;
}
const but = document.querySelector("#button")
but.addEventListener("click",(event) => {
    event.preventDefault();
    const inp = document.querySelector("#schName").value.toLowerCase()
    if (inp.length !== 0 && inp.includes("school")) {
        redirect("../main_page/index.html")
    }
    else {
        const div = document.querySelector("#msg");
        div.innerHTML = "Invalid input<br>Enter your school name"
    }
})
