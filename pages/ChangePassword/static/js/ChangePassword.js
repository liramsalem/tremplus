function validateChangePswForm() {
  let res = false;
  res = checkPassword('current_psw');    if (!res) return;
  res = checkPassword('new_psw');    if (!res) return;
  res = checkPassword('confirm_psw');    if (!res) return;
  document.getElementById("update_password").submit();
}

function checkPassword(id){
var x=document.getElementById(id).value;
if (x.length<6){
  alert("סיסמא חייבת להכיל לפחות 6 תווים");
  document.getElementById(id).value="";
  return false;
}
return true;
}
