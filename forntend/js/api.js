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
    })

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


// 게시글 GET 함수
async function getImg () {
    const response = await fetch(`${backend_base_url}/diary`, {
        method : "GET",
        headers: {
            'Authorization': localStorage.getItem("token")
        }
    })

    // img = response_json["images"][0]["image"].split("/")[2]
    // console.log(img)


    let response_json = await response.json()
    console.log("85번", response_json["save_to_to"])

    response_json_len = response_json['images'].length

    response_json = response_json['images'][response_json_len-1]['image']
    console.log('88번 줄',response_json.split("/")[2])
    for (let i = 0; i < response_json.length; i++) {
        console.log("리스트 나오면 성공 :", response_json[i]["image"])

        append_temp_html(
            response_json[i].image
            )
    }
    function append_temp_html(img, name, info) {
    temp_html =  `
    <li>
    <div class="card" style="width: 18rem;">
      <div class="card-img" style="background-image:
      url(../css/img/fish/${img});">
      <div class="card-delete" onclick="removeArticle()">
        X
      </div>
      </div>
      <div class="card-body">
        <hr>
        <h5 class="card-title">물고기 이름</h5>
        <hr>
        <p class="card-text">
          물고기 설명
        </p>
      </div>
    </div>
  </li>
    `

    $("#card").append(temp_html)
    }
}
getImg()
// DB : image 를 불러와서 이미지 를 불러오려 했으나 언디파인드 or 오브젝트 값으로 뜸



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

        image.src = '../backend/fish' + save_to
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