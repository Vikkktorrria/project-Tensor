window.onload = function () {
    const swiper = new Swiper('.swiper', {
        direction: 'horizontal',
        loop: true,
        pagination: {
            el: '.swiper-pagination',
            clickable: true,
        },
        autoplay: {
          delay: 3000,
        },
        navigation: {
            nextEl: '.swiper-button-next',
            prevEl: '.swiper-button-prev',
        },
    });
}
function navigation() {
    if (document.querySelector('.navigation').classList.contains('active')) {
        document.querySelector('.navigation').classList.remove('active')
        document.querySelector('.navigation__burger').classList.remove('active')
    } else {
        document.querySelector('.navigation').classList.add('active')
        document.querySelector('.navigation__burger').classList.add('active')
    }
}

function checkRegistrationForm() {
    const name = document.getElementById('name');
    const lastName = document.getElementById('lastName');
    const email = document.getElementById('email');
    const phone = document.getElementById('phone');
    const password = document.getElementById('password');
    const repeatPassword = document.getElementById('repeatPassword');
    const notification = document.getElementById('notification');
    const consent = document.getElementById('consent');
    var regexEmail = /[A-Z0-9._%+-]+@[A-Z0-9-]+.+.[A-Z]{2,4}/igm;
    var regexPhone = /^\+?\d{1,3}?[- .]?\(?(?:\d{2,3})\)?[- .]?\d\d\d[- .]?\d\d\-?\d\d$/;
    var regexPassword = /^(?=.*[0-9])(?=.*[!@#$%^&*])[a-zA-Z0-9!@#$%^&*]{6,16}$/;

    if (name.value.trim() === ''){setErrorFor(name, "Поле имя не может быть пустым")}
    else {setSuccess(name)};
    if (lastName.value.trim() === ''){setErrorFor(lastName, "Поле фамилия не может быть пустым")}
    else {setSuccess(lastName)};
    if (email.value.trim() === ''){setErrorFor(email, "Поле почта не может быть пустым")}
    else if (!regexEmail.test(email.value.trim())) {setErrorFor(email, "Поле почта не корректно")}
    else {setSuccess(email)};
    if (phone.value.trim() === ''){setErrorFor(phone, "Поле телефон не может быть пустым")}
    else if (!regexPhone.test(phone.value.trim())) {setErrorFor(phone, "Поле телефон не корректно")}
    else {setSuccess(phone)};
    if (password.value.trim() === ''){setErrorFor(password, "Поле пароль не может быть пустым")}
    else if (!regexPassword.test(password.value.trim())) {setErrorFor(password, "Поле пароль не корректно (необходим спец. симфол, цифра и буква)")}
    else {setSuccess(password)};
    if (repeatPassword.value.trim() === ''){setErrorFor(repeatPassword, "Поле повторный пароль не может быть пустым")}
    else if (repeatPassword.value.trim() !== password.value.trim()) {setErrorFor(repeatPassword, "Пароли не совпадают")}
    else {setSuccess(repeatPassword)};
    if (!consent.checked){setErrorFor(consent, "Подтвердите согласие")}
    else {setSuccess(consent)};
}

function checkAuthForm() {
    const email = document.getElementById('email');
    const password = document.getElementById('password');
    var regexEmail = /[A-Z0-9._%+-]+@[A-Z0-9-]+.+.[A-Z]{2,4}/igm;
    var regexPassword = /^(?=.*[0-9])(?=.*[!@#$%^&*])[a-zA-Z0-9!@#$%^&*]{6,16}$/;

    if (email.value.trim() === ''){setErrorFor(email, "Поле почта не может быть пустым")}
    else if (!regexEmail.test(email.value.trim())) {setErrorFor(email, "Поле почта не корректно")}
    else {setSuccess(email)};
    if (password.value.trim() === ''){setErrorFor(password, "Поле пароль не может быть пустым")}
    else if (!regexPassword.test(password.value.trim())) {setErrorFor(password, "Поле пароль не корректно (необходим спец. симфол, цифра и буква)")}
    else {setSuccess(password)};
}


function setErrorFor(input, message) {
    const formControl = input.parentElement;
    const small = formControl.querySelector('small');
    small.innerText = message;
    formControl.classList.add('error');
    if (formControl.classList.contains('success')) {formControl.classList.remove('success')}
}

function setSuccess(input, message) {
    const formControl = input.parentElement;
    formControl.classList.add('success');
    if (formControl.classList.contains('error')) {formControl.classList.remove('error')}
}