async function signup() {
    const signData = {
        id: document.getElementById("floatingInput").value,
        password: document.getElementById("floatingPassword").value
    }

    const response = await fetch("http://127.0.0.1:5000/sub", {
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


async function login() {
    const loginData = {
        id: document.getElementById("floatingInput").value,
        password: document.getElementById("floatingPassword").value
    }

    const response = await fetch("http://127.0.0.1:5000/login", {
        method: "POST",
        body: JSON.stringify(loginData)
    })

    if (response.status == 200) {
        alert('환영합니다!')
        window.location.replace(`http://127.0.0.1:5500/main.html`);
    } else {
        alert('아이디와 비밀번호를 다시 입력해주세요.')
    }

    response_json = await response.json()
    console.log(response_json)
    localStorage.setItem("token", response_json.token)
}

