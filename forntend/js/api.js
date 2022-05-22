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