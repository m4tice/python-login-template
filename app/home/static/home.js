document.getElementById('button-signout').addEventListener('click', function(event) {
    event.preventDefault();
    signout();
})

function signout(){
    window.location.href = '/auth/login';
}