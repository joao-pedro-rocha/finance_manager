let currentPath;
let homeButton;
let categoryButton;
let walletsButton;

currentPath = window.location.pathname;
homeButton = window.document.querySelector('#home-button');
categoryButton = window.document.querySelector('#category-button');
walletsButton = window.document.querySelector('#wallets-button');

if (currentPath == '/') {
    homeButton.classList.add('active');
} else if (currentPath == '/categories-list/') {
    categoryButton.classList.add('active');
} else if (currentPath == '/wallets-list/') {
    walletsButton.classList.add('active');
}