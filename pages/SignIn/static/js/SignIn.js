function validatesigninForm() {
  let res = false;
  res = checkEmail('email');          if (!res) return;
  res = checkPassword('password');    if (!res) return;
  document.getElementById("signinform").submit();
}

function checkEmail(id){
var x=document.getElementById(id).value;
if (x.length<5 || !(x.includes('@')) || !(x.includes('.'))){
  alert("כתובת אימייל לא תקינה.");
  document.getElementById(id).value="";
  return false;
}
return true;
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
