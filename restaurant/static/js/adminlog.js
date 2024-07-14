function log_validation(){
    Remail=document.getElementById('email_rest').value
    Rpassword=document.getElementById('user_rest').value

    if(Remail==""){
        alert('please enter email-Id')
    } else if(Rpassword==""){
        alert('please enter password')
    } else{
        return true
    }
}