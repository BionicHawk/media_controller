const OpenPageBtn = document.getElementById("OpenPageBtn");
const OpenAVControlsBtn = document.getElementById("OpenAVControlsBtn");
const title = document.getElementById("title");
const iconLogo = document.getElementById("iconLogo");

function goToRoot() {
    open("/", "_self");
}

OpenPageBtn.addEventListener('click', () => {
    open('/static/open_web.html', '_self');
});

OpenAVControlsBtn.addEventListener('click', () => {
    open('/static/av_controls.html', '_self');
});

title.addEventListener("click", goToRoot);
iconLogo.addEventListener("click", goToRoot);