window.onload = function () {
    const swiper = new Swiper('.swiper', {
        direction: 'horizontal',
        loop: true,
        pagination: {
            el: '.swiper-pagination',
            clickable: true,
        },
        // autoplay: {
        //   delay: 3000,
        // },
        navigation: {
            nextEl: '.swiper-button-next',
            prevEl: '.swiper-button-prev',
        },
    });
}
function navigation() {
    if (document.querySelector('.navigation').classList.contains('active')) {
        document.querySelector('.navigation').classList.remove('active')
        // document.querySelector('.navigation__burger').classList.remove('active')

    } else {
        document.querySelector('.navigation').classList.add('active')
        // document.querySelector('.navigation__burger').classList.add('active')
    }
}