function validation(){
    
    Rname=document.getElementById('rest_name').value
    RemailId=document.getElementById('rest_email').value
    RphoneNumber=document.getElementById('rest_number').value
    RcreatePass=document.getElementById('rest_create_pass').value
    RconfirmPass=document.getElementById('rest_confirm_pass').value

    if(Rname==""){
        alert("please enter Restaurant name")
        return false
    } else if(RemailId==""){
        alert('please enter email id')
        return false
    } else if(RphoneNumber==""){
        alert('please enter phone number')
        return false
    } else if(RcreatePass==""){
        alert('please create a password')
        return false
    } else if(RcreatePass.length < 5 ){
        alert('password must contain minimum 6 characters')
        return false
    } else if(RcreatePass !== RconfirmPass){
        alert('Invalid, try again')
        return false
    } else{
        alert("succesfully add your restaurant")
        return true
    }
}