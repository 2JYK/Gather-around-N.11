const backend_base_url = "http://127.0.0.1:5000"
const frontend_base_url = "http://127.0.0.1:5500"

// 회원가입
async function signup() {
    const signData = {
        id: document.getElementById("floatingInput").value,
        password: document.getElementById("floatingPassword").value
    }

    const response = await fetch(`${backend_base_url}/sub`, {
        method: "POST",
        body: JSON.stringify(signData)
    })
    response_json = await response.json()

    if (response.status == 201) {
        alert("환영 합니다")
        window.location.reload();
    } else {
        alert("다시 확인해주세요")
        window.location.reload();
    }
}

// 로그인
async function login() {
    const loginData = {
        id: document.getElementById("floatingInput").value,
        password: document.getElementById("floatingPassword").value
    }

    const response = await fetch(`${backend_base_url}/login`, {
        method: "POST",
        body: JSON.stringify(loginData)
    })

    if (response.status == 200) {
        alert('환영합니다!')
        window.location.replace(`${frontend_base_url}/main.html`);
    } else {
        alert('아이디와 비밀번호를 다시 입력해주세요.')
    }

    response_json = await response.json()
    localStorage.setItem("token", response_json.token)
}


// 유저 아이디 받아오기
async function getName() {
    const response = await fetch(`${backend_base_url}/getuserinfo`, {
        headers: {
            'Authorization': localStorage.getItem("token")
        }
    }
    )

    if (response.status == 200) {
        response_json = await response.json()
        // console.log(response_json)
        return response_json.id
    }
    else {
        alert("로그인이 필요한 페이지 입니다.")
        window.location.replace(`${frontend_base_url}/sub.html`)
        return null
    }
}


// // diary 불러오기
// async function getArticles() {
//     const response = await fetch(`${backend_base_url}/diary`, {
//         method: 'GET'
//     }
//     )

//     response_json = await response.json()

//     return response_json.articles
// }

// // diary 삭제
// async function deleteArticle() {
//     const response = await fetfch(`${backend_base_url}/diary`, {
//         headers: {
//             'Authorization': localStorage.getItem("token")
//         },
//         method: 'DELETE'
//     }
//     )

//     if (response.status == 200) {
//         window.location.reload;
//     }

// }






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


// function posting() {
//     let image = $('#title').val()
//     let file = $('#file')[0].files[0]
//     let form_data = new FormData()

//     form_data.append("title_give", title)
//     form_data.append("file_give", file)


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

            image[0].style.backgroundImage = "url(/" + abs_path + ")"
        
        }
    });
}

async function show_image() {
    const response = await fetch(`${backend_base_url}/upload`, {
        method: "GET"
    })

    response_json = await response.json()
    console.log(response_json)

    return response_json.image
}