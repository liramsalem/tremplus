let ifDriver = true;
console.log(ifDriver)

function ifDriverFun(){
var checkBox = document.getElementById("myCheck");
var text = document.getElementById("idDriver");

// If the checkbox is not checked, display the output text
if (checkBox.checked == false){
  text.style.display = "block"; // driver
  console.log("block")
  ifDriver= true;
  console.log(ifDriver)
} else {
  text.style.display = "none";  //not driver
  ifDriver= false;
  console.log("none")
  console.log(ifDriver)
}
}

//--------------------------- Form Validation -----------------------------------
  function validateRegisterForm(){
    console.log("ifDriver from checkbox")
    console.log(ifDriver)
    let res = false;
    res = checkFirstName('fname');           if (!res) return;
    res = checkLastName('lname');           if (!res) return;
    res = checkNickName('nickname');           if (!res) return;
    res = checkUserId('user_id');           if (!res) return;
    res = checkPhone('phone');          if (!res) return;
    res = checkEmail('email');          if (!res) return;
    res = checkPassword('password');    if (!res) return;
    if(ifDriver==true){
      console.log("im driver")
      let flag_license_plate = false;
      let flag_car_company = false;
      let flag_car_color = false;
      let flag_licence_driver_img= false;
      var license_plate = document.getElementById('license_plate').value;
      console.log(license_plate)
      console.log(typeof license_plate)
      console.log(license_plate.length)
      var car_company = document.getElementById('car_company').value;
      console.log(car_company)
      console.log(typeof car_company)
      console.log(car_company.length)
      var car_color = document.getElementById('car_color').value;
      console.log(car_color)
      console.log(typeof car_color)
      console.log(car_color.length)
      var licence_driver_img = document.getElementById('licence_driver_img').value;
      console.log(licence_driver_img)
      console.log(typeof licence_driver_img)
      console.log(licence_driver_img.length)
      console.log("ללל")

      var license_plate_str = onlyNumbers(license_plate);
      if(license_plate_str.length != 8 && license_plate_str.length != 7){
        console.log("license_plate>01")
        document.getElementById('license_plate').value = "";
        alert("מספר לוחית רישוי לא תקין. חייב להיות בן 7 או 8 ספרות");
        flag_license_plate = false;
        console.log(flag_license_plate)
        console.log("license_plate>02")
      }else{
        document.getElementById('license_plate').value = license_plate_str;
        flag_license_plate = true;
      }

      console.log("ans_license_plate")
      console.log(flag_license_plate)

      if(car_company.length <= 1){
        console.log("car_company>01")
        document.getElementById('car_company').value = "";
        alert("יצרן הרכב חייב להיות באורך של 2 תווים ומעלה");
        flag_car_company = false;
        console.log(flag_car_company)
        console.log("car_company>02")
      }else{
        flag_car_company = true;
      }

      console.log("car_company")
      console.log(flag_car_company)

      if(car_color.length <= 1){
        console.log("car_color>01")
        document.getElementById('car_color').value = "";
        alert("צבע הרכב חייב להיות באורך של 2 תווים ומעלה");
        flag_car_color = false;
        console.log(flag_car_color)
        console.log("car_color>02")
      }else{
        flag_car_color = true;
      }

      console.log("car_color")
      console.log(flag_car_color)

      if (licence_driver_img.length == 0){
        console.log("licence_driver_img>01")
        alert("על מנת להירשם חייב לעלות תצלום רישיון נהיגה");
        flag_licence_driver_img = false;
        console.log(flag_licence_driver_img)
        console.log("licence_driver_img>02")
      }else{
        flag_licence_driver_img = true;
      }

      console.log("licence_driver_img")
      console.log(flag_licence_driver_img)

      if(flag_license_plate == true && flag_car_company == true && flag_car_color == true && flag_licence_driver_img == true  ){// document.getElementById("update_details").submit();
        document.getElementById("registerform").submit();
      }else{
        return;
      }
    }
    document.getElementById("registerform").submit();
}

function checkFirstName(id) {
var x = document.getElementById(id).value;
if(x.length<=1){
  alert("שם פרטי חייב להיות באורך של 2 תווים ומעלה");
  document.getElementById(id).value="";
  return false;
}
return true;
}

function checkLastName(id) {
var x = document.getElementById(id).value;
if(x.length<=1){
  alert("שם משפחה חייב להיות באורך של 2 תווים ומעלה");
  document.getElementById(id).value="";
  return false;
}
return true;
}

function checkNickName(id) {
var x = document.getElementById(id).value;
if(x.length<=1){
  alert("שם משתמש חייב להיות באורך של 2 תווים ומעלה");
  document.getElementById(id).value="";
  return false;
}
return true;
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

function onlyNumbers(num){
var ans="";
var i;
for (i = 0; i < num.length; i++) {
  var digit = num[i];
  if (digit=='0' || digit=='1' || digit=='2' || digit=='3' || digit=='4' || digit=='5' || digit=='6' || digit=='7' || digit=='8' || digit=='9'){
    ans += num[i];
  }
}
return ans;
}


function checkPhone(id){
var x=document.getElementById(id).value;
var y=onlyNumbers(x);
if (y.length!=10 && y.length!=9 ){
  alert("מספר טלפון לא תקין. חייב להיות בן 9 או 10 ספרות");
  document.getElementById(id).value="";
  return false;
}
else{
  document.getElementById(id).value=y;
  return true;
}
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

function checkUserId(id){
var x=document.getElementById(id).value;
var y=onlyNumbers(x);
if (y.length!=8 && y.length!=9 ){
  alert("תעודת זהות הינה בת 8 או 9 ספרות");
  document.getElementById(id).value="";
  return false;
}
else{
  document.getElementById(id).value=y;
  return true;
}
}