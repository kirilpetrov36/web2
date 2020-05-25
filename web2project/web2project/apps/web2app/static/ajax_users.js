const URL = 'http://127.0.0.1:8000/web2app/'

function make_admin(username) {
    $.get(URL + username, function(data, status) {});
    var temp_username = '';
    for (let index = 11; index < username.length; index++) {
        console.log(temp_username);
        temp_username += username[index];
    }
    document.getElementById(username + '/text').innerHTML = temp_username + ' - admin';

}

function delete_user(username) {
    $.get(URL + username, function(data, status) {});
    var temp_username = '';
    for (let index = 12; index < username.length; index++) {
        console.log(temp_username);
        temp_username += username[index];
    }
    document.getElementById('user-cont/' + temp_username).remove()

}