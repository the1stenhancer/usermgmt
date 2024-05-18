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

// Language related js
const languageDropdown = document.querySelector(".nav-2 .language-dropdown");
const languagesContainer = document.querySelector(".nav-2 .language-dropdown .supported-languages");
const languages = document.querySelectorAll(".languages span");
const currentLanguage = document.querySelectorAll(".current-language span")[0];
languageDropdown.addEventListener("mouseenter", (e) => {
    languagesContainer.classList.remove("desktop-hide");
    languagesContainer.classList.add("choose-language");
});
languageDropdown.addEventListener("mouseleave", (e) => {
    languagesContainer.classList.remove("choose-language");
    languagesContainer.classList.add("desktop-hide");
});
languages.forEach((lang) => {
    const baseUrl = window.location.origin + "/";
    const langText = lang.textContent;
    const pathName = window.location.pathname.split(currentLanguage.textContent)[1];
    lang.addEventListener("click", (e) => {
        window.location.href = baseUrl + langText + pathName;
    });
});
