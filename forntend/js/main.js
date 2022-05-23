// console.log('메인페이지') //연결 확인
// console.log(localStorage.getItem("token"))  // 토큰값 확인
function myFish() {
    window.location.replace(`http://127.0.0.1:5500/diary.html`);
}


function posting() {
    let image = $('#inputImage')[0].files[0]
    let form_data = new FormData()

    form_data.append("image_give", image)

// 경로 이동확인-슬기버전
$.ajax({
    type: "POST",
    url: "http://127.0.0.1:5000/upload",
    data: form_data,
    cache: false,
    contentType: false,
    processData: false,
    success: function (response) {
        const save_to = response["save_to"]
        console.log(save_to)
        const image = document.getElementById("img")

        image.src = '../backend/' + save_to
        console.log(image)
    }
    }
);
}
// 경로 이동확인-대근버전
//     $.ajax({
//         type: "POST",
//         url: "http://127.0.0.1:5000/upload",
//         data: form_data,
//         cache: false,
//         contentType: false,
//         processData: false,
//         success: function (response) {
//             const save_to = response["save_to"]
//             console.log(save_to)
//             const image = document.getElementById("img")

//             console.log(save_to)
//             image.src = save_to
//             console.log(image)
//         }
//     }
// );
// }


