// 제출 이벤트를 받는다 (이벤트 핸들링)
const form = document.getElementById("form")

form.addEventListener("submit", function (event) {
    event.preventDefault() // 기존 기능 차단

    let userId = event.target.id.value
    let userPw1 = event.target.pw1.value
    let userPw2 = event.target.pw2.value
    let userName = event.target.name.value
    let userPhone = event.target.phone.value
    let userPosition = event.target.position.value
    let userGender = event.target.gender.value
    let userEmail = event.target.email.value
    let userIntro = event.target.intro.value

    console.log(userId, userPw1, userPw2, userName, userPhone,
        userPosition, userGender, userEmail, userIntro)
})
// 제출된 입력 값들을 참조한다

// 입력값에 문제가 있는 경우 이를 감지한다

// 가입 환영 인사를 제공한다