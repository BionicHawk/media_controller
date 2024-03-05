const title = document.getElementById("title");
const iconLogo = document.getElementById("iconLogo");

// Volume buttons
const VolumeMute = document.getElementById("VolumeMute");
const VolumeUp = document.getElementById("VolumeUp");
const VolumeDown = document.getElementById("VolumeDown");

// Video Buttons
const FullscreenBtn = document.getElementById("FullscreenBtn");
const NextTrackBtn = document.getElementById("NextTrackBtn");
const PrevTrackBtn = document.getElementById("PrevTrackBtn");
const RewindBtn = document.getElementById("RewindBtn");
const PlayPauseBtn = document.getElementById("PlayPauseBtn");
const ForwardBtn = document.getElementById("ForwardBtn");
const PrevItemBtn = document.getElementById("PrevItemBtn");
const NextItemBtn = document.getElementById("NextItemBtn");

// NavigationButtons
const EnterBtn = document.getElementById("EnterBtn");

// Typed Elements
const TextInput = document.getElementById("TextInput");
const SendTextForm = document.getElementById("SendTextForm");

const setVolumePath = "/set/volume/";
const setVideoPath = "/set/video/";
const setNavigationPath = "/set/navigation/";
const typingPath = "/typing";

function goToRoot() {
    open("/", "_self");
}

// Control listeners
// - Audio
VolumeMute.addEventListener("click", () => {
    fetch(`${setVolumePath}mute`, {method: "post"});
})

VolumeUp.addEventListener("click", () => {
    fetch(`${setVolumePath}up`, {method: "post"});
})

VolumeDown.addEventListener("click", () => {
    fetch(`${setVolumePath}down`, {method: "post"});
})

// - video
FullscreenBtn.addEventListener("click", () => {
    fetch(`${setVideoPath}fsn`, {method: "post"});
})

NextTrackBtn.addEventListener("click", () => {
    fetch(`${setVideoPath}next`, {method: "post"});
})

PrevTrackBtn.addEventListener("click", () => {
    fetch(`${setVideoPath}prev`, {method: "post"});
})

RewindBtn.addEventListener("click", () => {
    fetch(`${setVideoPath}rewind`, {method: "post"});
})

PlayPauseBtn.addEventListener("click", () => {
    fetch(`${setVideoPath}playpause`, {method: "post"});
})

ForwardBtn.addEventListener("click", () => {
    fetch(`${setVideoPath}forward`, {method: "post"});
})

// - Navigation
EnterBtn.addEventListener('click', () => {
    fetch(`${setNavigationPath}enter`, {method: "post"});
})

PrevItemBtn.addEventListener('click', () => {
    fetch(`${setNavigationPath}lb`, {method: "post"});
})

NextItemBtn.addEventListener('click', () => {
    fetch(`${setNavigationPath}rb`, {method: "post"});
})

// - Typed Listeners
SendTextForm.addEventListener("submit", (ev) => {
    ev.preventDefault();
    const value = TextInput.value;
    if (value.length > 0) {
        const request = {
            fromUser: "WebClient",
            query: value.toString()
        };

        fetch(typingPath, {
            headers: {
                "content-type": "application/json"
            },
            method: "post",
            body: JSON.stringify(request)
        })
            .then(() => TextInput.value = "");

    }
})

title.addEventListener("click", goToRoot);
iconLogo.addEventListener("click", goToRoot);