function controlHidden() {
    const show = document.getElementById("uploadPhoto");
    const upload = document.getElementById("showPhoto");
    show.classList.remove("hidden");
    upload.classList.add("hidden");
}

// function posting() {
//     let image = $('#title').val()
//     let file = $('#file')[0].files[0]
//     let form_data = new FormData()

//     form_data.append("title_give", title)
//     form_data.append("file_give", file)


const backend_base_url = 'http://127.0.0.1:5000'

async function posting() {
    const imageData = {
        image: document.getElementById('image').value
    }
    console.log(imageData)

    const response = await fetch(`${backend_base_url}/upload`, {
        method: "POST",
        body: JSON.stringify(imageData)
    })
    console.log(response)
}

function myFish(){
    window.location.replace(`${frontend_base_url}/dairy`);
}