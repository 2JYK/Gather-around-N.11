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
