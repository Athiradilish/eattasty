function login_validation(){
    Email=document.getElementById('email_id').value
    Password=document.getElementById('user_pass').value

    if(Email==""){
        alert('please enter email-Id')
    } else if(Password==""){
        alert('please enter password')
    } else{
        return true
    }
}