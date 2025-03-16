document.getElementById('button-logout').addEventListener('click', function(event) {
    event.preventDefault();
    logout();
})

function logout(){
    window.location.href = '/auth/login';
}