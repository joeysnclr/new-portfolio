function toggleMobileNav() {
    if (screen.width <= 991) {
        console.log("toggling")
        $(".navigation-section").toggle();
    }
}

document.querySelectorAll(".navigation-menu a").forEach(function (link) {
    link.addEventListener("click", toggleMobileNav);
})