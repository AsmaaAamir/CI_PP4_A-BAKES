//Timer for the message on actions //
setTimeout(function (){
    let messages = document.getElementById("msg");
    let alert = new bootstrap.Alert(messages);
    alert.close(); 
    }, 5000
    );

    
//Jave script for nav bar//
const navbarToggle = navbar.querySelector("#navbar-toggle");
const navbarMenu = document.querySelector("#navbar-menu");
const navbarLinksContainer = navbarMenu.querySelector(".navbar-links");
let isNavbarExpanded = navbarToggle.getAttribute("aria-expanded") === "true";
    
const toggleNavbarVisibility = () => {
    isNavbarExpanded = !isNavbarExpanded;
    navbarToggle.setAttribute("aria-expanded", isNavbarExpanded);
};
    
navbarToggle.addEventListener("click", toggleNavbarVisibility);
    
navbarLinksContainer.addEventListener("click", (e) => e.stopPropagation());
navbarMenu.addEventListener("click", toggleNavbarVisibility);