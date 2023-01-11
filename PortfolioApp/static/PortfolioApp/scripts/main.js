let header__container = document.querySelector('.header__container');
let a1 = document.querySelector('.a1');
let a2 = document.querySelector('.a2');
let a3 = document.querySelector('.a3');
let a4 = document.querySelector('.a4');
let burger = document.querySelector('.burger');

burger.addEventListener('click', function(){
	burger.classList.toggle('open--burger');
})

burger.addEventListener('click', function(){
	header__container.classList.toggle('active');
})
a1.addEventListener('click', function(){
	header__container.classList.remove('active');
	burger.classList.remove('open--burger');
})
a2.addEventListener('click', function(){
	header__container.classList.remove('active');
	burger.classList.remove('open--burger');
})
a3.addEventListener('click', function(){
	header__container.classList.remove('active');
	burger.classList.remove('open--burger');
})
a4.addEventListener('click', function(){
	header__container.classList.remove('active');
	burger.classList.remove('open--burger');
})