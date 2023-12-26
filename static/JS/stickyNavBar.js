var isSticky = false;
var lastScrollTop = 0;

window.onscroll = function() {
    var navbar = document.getElementById("navbar");
    var searchBar = document.getElementById("search-bar");
    var currentScrollTop = window.pageYOffset || document.documentElement.scrollTop;

    // Check if the user is scrolling down and the scroll position is beyond the original position of the navigation bar
    if (currentScrollTop > lastScrollTop && currentScrollTop > navbar.offsetTop) {
        // Make the navigation bar sticky
        if (!isSticky) {
            navbar.style.top = '0';
            navbar.classList.add("sticky-nav");
            isSticky = true;
        }
    } else if (currentScrollTop <= searchBar.offsetTop + searchBar.offsetHeight && isSticky) {
        // If scrolling up and the scroll position is above the search bar, unstick the navigation bar
        navbar.style.top = searchBar.offsetHeight + 'px';
        navbar.classList.remove("sticky-nav");
        isSticky = false;
    }

    lastScrollTop = currentScrollTop;
};