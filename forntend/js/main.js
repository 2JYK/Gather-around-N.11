// console.log('메인페이지') //연결 확인
console.log(localStorage.getItem("token"))  // 토큰값 확인
function myFish() {
    window.location.replace(`${frontend_base_url}/diary.html`);
}
// 경로 이동확인


function controlHidden() {
    const show = document.getElementById("uploadPhoto");
    const upload = document.getElementById("showPhoto");
    show.classList.remove("hidden");
    upload.classList.add("hidden");
}


function posting() {
    let image = $('#inputImage')[0].files[0]
    // let title = $('#upload-title').val()
    let form_data = new FormData()

    form_data.append("image_give", image)
    // console.log(form_data);
    // form_data.append("title_give", title)

    $.ajax({
        type: "POST",
        url: "http://127.0.0.1:5000/upload",
        data: form_data,
        cache: false,
        contentType: false,
        processData: false,
        success: function (response) {
            // console.log(response)
            alert(response["abs_path"])

            const abs_path = response["abs_path"]
            // console.log(abs_path)
            const image = document.getElementById("image")
            // console.log(image)
            // // response_json = await response.json()
            // // console.log(response_json.abs_path)

    //         "background-image": "url(" + window.URL.createObjectURL(files[0]) + ")",
    //         "outline": "none",
    // "background-size": "100% 100%"
            image[0].style.backgroundImage = "url(/" + abs_path + ")"
            // abs_path.setAttribute("src", "url(/" + abs_path + ")")

        }
    });
}

// .css({
//     "background-image": "url(" + window.URL.createObjectURL(files[0]) + ")",
//     "outline": "none",
//     "background-size": "100% 100%"});