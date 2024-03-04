const sender_form = document.getElementById("sender_form");
const url_input = document.getElementById("url_input");
const route = "/open/web";

sender_form.addEventListener('submit', async (ev) => {
    ev.preventDefault();
    const url = url_input.value;
    console.log('pasando por aqui')
    if (url.length > 0) {
        const request = {
            "fromUser": "WebClient",
            "url": url.toString()
        };
        await fetch(route, {
            method: 'post',
            headers: {
                "Content-type": "application/json"
            },
            body: JSON.stringify(request)})
            .then(() => alert('Hecho!'));
    }
})