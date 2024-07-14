function form_validation(){
    // alert('worked')
    userName=document.getElementById('user_name').value
    emailId=document.getElementById('user_email').value
    phoneNumber=document.getElementById('user_number').value
    Address=document.getElementById('user_address').value
    createPass=document.getElementById('user_create_pass').value
    confirmPass=document.getElementById('user_confirm_pass').value

    if(userName==""){
        alert("please enter username")
        return false
    } else if(emailId==""){
        alert('please enter email id')
        return false
    } else if(phoneNumber==""){
        alert('please enter phone number')
        return false
    } else if(Address==""){
        alert('please enter address')
        return false
    } else if(createPass==""){
        alert('please create a password')
        return false
    } else if(createPass.length < 8 ){
        alert('password must contain minimum 8 characters')
        return false
    } else if(createPass !== confirmPass){
        alert('Invalid, try again')
        return false
    } else{
        alert("succesfully created new account")
        return true
    }
}