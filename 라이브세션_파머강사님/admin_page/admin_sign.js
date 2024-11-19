const form = document.getElementById("form");

// 아이디, 비밀번호, 이름, 전화번호, 이메일에 대한 유효성 검사를 설정합니다.
form.addEventListener("submit", function (event) {
    event.preventDefault(); // 기본 제출 기능 차단

    let userId = event.target.id.value.trim();
    let userPw1 = event.target.pw1.value.trim();
    let userPw2 = event.target.pw2.value.trim();
    let userName = event.target.name.value.trim();
    let userPhone = event.target.phone.value.trim();
    let userGender = event.target.gender.value;
    let userEmail = event.target.email.value.trim();

    // 유효성 검사 패턴
    const idPattern = /^[a-zA-Z0-9]{6,20}$/; // 6~20자 영문, 숫자
    const pwPattern = /^(?=.*[a-zA-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,30}$/; // 영문, 숫자, 특수문자 포함 8~30자
    const phonePattern = /^[0-9]{1,15}$/; // 전화번호 15자 이내 숫자만
    const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/; // 이메일 형식

    // 유효성 검사
    if (!idPattern.test(userId)) {
        alert("아이디는 6자 이상 20자 이하의 영문과 숫자로 입력하세요.");
        return;
    }
    if (!pwPattern.test(userPw1)) {
        alert("비밀번호는 영문, 숫자, 특수문자를 포함한 8자 이상 30자 미만이어야 합니다.");
        return;
    }
    if (userPw1 !== userPw2) {
        alert("비밀번호가 일치하지 않습니다.");
        return;
    }
    if (userName.length > 30) {
        alert("이름은 30자 이내로 입력하세요.");
        return;
    }
    if (!phonePattern.test(userPhone)) {
        alert("전화번호는 숫자만 15자 이내로 입력하세요.");
        return;
    }
    if (!emailPattern.test(userEmail) || userEmail.length > 35) {
        alert("유효한 이메일을 35자 이내로 입력하세요.");
        return;
    }

    // 성공 메시지 및 로컬 스토리지 저장 옵션
    const userData = {
        id: userId,
        password: userPw1,
        name: userName,
        phone: userPhone,
        gender: userGender,
        email: userEmail
    };

    // 로컬 스토리지에 JSON 형식으로 저장
    localStorage.setItem("userData", JSON.stringify(userData));
    alert("회원가입 정보가 저장되었습니다!");

    // 파일로 저장하는 옵션 (JSON 형식으로 다운로드)
    const userDataText = JSON.stringify(userData, null, 2);
    const blob = new Blob([userDataText], { type: "application/json" }); // JSON 형식
    const url = URL.createObjectURL(blob);
    const a = document.createElement("a");
    const fileName = userName.replace(/[^a-zA-Z0-9가-힣]/g, '_'); // 한글 및 영문, 숫자 이외의 문자를 '_'로 대체
    a.href = url;
    a.download = `${fileName}_userData.json`; // 파일 이름 설정
    document.body.appendChild(a);
    a.click();
    document.body.removeChild(a);

    window.location.href = "asd.html";

    // 환영 메시지 출력
    alert(`${userName}님 환영합니다.
          회원 가입 시 입력하신 내역은 다음과 같습니다.
          아이디: ${userId}
          전화번호: ${userPhone}
          이름: ${userName}
          성별: ${userGender}
          이메일: ${userEmail}`);
});
