const btnPopup = document.querySelector('.btnLogin');
const loginLink = document.querySelector('.login-link');
const registerLink= document.querySelector('.register-link');
const iconClose = document.querySelector('.icon-close');
const ulId=document.getElementById("ul-id");
const checkBtn=document.getElementsByClassName("check_btn");
const coverBox=document.getElementById("cover_box");

   

function deactivateCoverBox() {
   
    var homeContentRight = document.querySelector('.home-content-right');
    homeContentRight.style.display = 'block';
    var coverBox = document.querySelector('#cover_box');
    coverBox.style.display = 'none';
    coverBox.classList.remove('active');
    var logInn = document.querySelector('#login');
    logInn.style.display = 'none';
    var registerr = document.querySelector('#register');
    registerr.style.display = 'none';  
   
    
}
function activatelogin()
{

    var homeContentRight = document.querySelector('.home-content-right');
    homeContentRight.style.display = 'none';
    var coverBox = document.querySelector('#cover_box');
    coverBox.classList.remove('active');
    coverBox.style.display = 'flex';
    coverBox.style.marginLeft='500px';
    coverBox.style.marginTop='10px';
    coverBox.style.height = '440px';
    var logInn = document.querySelector('#login');
    logInn.style.display = 'block';
    var registerr = document.querySelector('#register');
    registerr.style.display = 'block';
      //}
}
function activateregister()
{
    var homeContentRight = document.querySelector('.home-content-right');
    homeContentRight.style.display = 'none';
    var coverBox = document.querySelector('#cover_box');
    coverBox.style.display = 'block';
    coverBox.classList.add('active');
    coverBox.style.height = '500px';
    coverBox.style.marginLeft= '500px';
    var logInn = document.querySelector('#login');
    logInn.style.display = 'none';
    var registerr = document.querySelector('#register');
    registerr.style.display = 'block';
}
registerLink.addEventListener('click',activateregister);
loginLink.addEventListener('click',activatelogin);
btnPopup.addEventListener('click',activatelogin);
iconClose.addEventListener('click',deactivateCoverBox);


var typed = new Typed('.typing', {
    strings:['','Ask Us','Learn From Us','Ask Us'],
    typeSpeed:100,
    BackSpeed:60,
    loop:true
})
