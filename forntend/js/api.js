async function signup() {
    const signData = {
        id : document.getElementById("floatingInput").value,
        password : document.getElementById("floatingPassword").value
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


// 충돌 빵
















// 충돌 빵