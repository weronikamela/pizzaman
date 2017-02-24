// using jQuery
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}


//var csrftoken = getCookie('csrftoken');

//
//$("#checkout-button").click(function(){
//
//    var http = new XMLHttpRequest();
//
//    var name = document.getElementById("name").value;
//    var surname = document.getElementById("surname").value;
//    var phone = document.getElementById("phone").value;
//    var email = document.getElementById("email").value;
//    var city = document.getElementById("city").value;
//    var street = document.getElementById("street").value;
//    var postalCode = document.getElementById("postalCode").value;
//
//    http.open("POST", url, true);
//
//    //Send the proper header information along with the request
//    http.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
//
//
//    http.onreadystatechange = function() {//Call a function when the state changes.
//        if(http.readyState == 4 && http.status == 200) {
//            alert(http.responseText);
//        }
//    }
//    http.send(name, surname, phone, email, city, street, postal-code);
//
//});