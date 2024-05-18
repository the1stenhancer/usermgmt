// Navigation bar related js
const navLogo = document.querySelector(".nav-1 a");
navLogo.addEventListener("click", (e) => {
    sessionStorage.clear();
});

const navLinks = document.querySelectorAll("nav .nav-2 ul li a");
navLinks.forEach((link) => {
    link.addEventListener("click", (e) => {
        const linkName = link.textContent;
        sessionStorage.clear();
        sessionStorage.setItem("active-link", linkName);
    })
});

navLinks.forEach((link) => {
    const linkName = link.textContent;
    if (linkName === sessionStorage.getItem("active-link")) {
        link.classList.add("highlight-navlink");
    } else {
        link.classList.remove("highlight-navlink");
    }
});
