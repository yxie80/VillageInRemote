/**
 * Created by Yue on 2018/4/12.
 */

function keyLogin(event) {

    var browser = navigator.appName;
    var userAgent = navigator.userAgent;
    var code;
    if(browser.indexOf('Internet')>-1) //IE
    code = window.event.keyCode;
    else if(userAgent.indexOf("Firefox")>-1)  //firefox
    code = event.which;
    else  //other browser
    code = event.keyCode ? event.keyCode : event.which ? event.which : event.charCode;

    if ( code == 13)  //按Enter键的键值为13
        document.getElementById("btn_login").click();  //call the login button function
}


window.onload = function () {
    var btn_login = document.getElementById('btn_login');
    var btn_register = document.getElementById('btn_register');


    btn_login.onclick = function login() {

        var username = document.getElementById("username");
        var pass = document.getElementById("password");

        if (username.value == "") {

            alert("Type in username");

        } else if (pass.value == "") {

            alert("Type in password");

        } else if (username.value == "admin" && pass.value == "123456") {

            window.location.href = "welcome.html";

            ////  function for full screen
            //function fullScreen(element) {
            //    if (element.requestFullscreen) {
            //        element.requestFullscreen();
            //    } else if (element.mozRequestFullScreen) {
            //        element.mozRequestFullScreen();
            //    } else if (element.webkitRequestFullscreen) {
            //        element.webkitRequestFullscreen();
            //    } else if (element.msRequestFullscreen) {
            //        element.msRequestFullscreen();
            //    }
            //}
            //// Transform current page to full Screen
            //fullScreen(document.documentElement);

        } else {

            alert("The username and password can not match");

        }
    }

    btn_register.onclick = function register() {
        window.open("register.html");
    }
}


