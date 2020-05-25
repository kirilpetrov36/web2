let array = {};

function loadPage(name) {
    rq = new XMLHttpRequest();
    rq.open('GET', 'form.html', true);
    rq.onload = function() {
        document.getElementById('dynamic')
            .innerHTML = rq.responseText;
    }
    rq.send();
}


function loadMainPage(data) {
    $(document).ready(function() {
        $("form:first").submit();
    });
}

function submit_login() {

    $(document).on('submit', '#login-form', function(e) {
        e.preventDefault();

        $.ajax({
            type: 'POST',
            datatype: "json",
            url: 'http://127.0.0.1:8000/web2app/check_login',
            data: {
                username: $('#username').val(),
                password: $('#password').val(),
                csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
            },
            success: function(data) {
                test = data['bool'];
                if (test === false) {
                    console.log('lol2');
                    console.log(data['username']);
                    document.getElementById('login_error').innerHTML = 'Invalid login or password';
                } else {
                    console.log('lol1');
                    $("#dynamic").html(data);
                    $(document).ready(function() {
                        $("form:first").submit();
                    });
                }

            }
        });
    });

}

submit_login();