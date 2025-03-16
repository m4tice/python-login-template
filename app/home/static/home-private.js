document.getElementById('button-signout').addEventListener('click', function(event) {
    event.preventDefault();
    redirect_signout();
});

function redirect_signout(){
    window.location.href = '/home';
}
