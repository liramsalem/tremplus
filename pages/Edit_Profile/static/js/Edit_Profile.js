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

function validateEditProfile(){

  console.log("khr")

  let flag_name = false;
  let flag_email = false;
  let flag_phone = false;
  let flag_license_plate = false;
  let flag_car_company = false;
  let flag_car_color = false;

  var ifDriver =document.getElementById('driver_or_not').value;
  console.log(ifDriver)
  var name = document.getElementById('nickname').value;
  console.log(name)
  console.log(typeof name)
  console.log(name.length)
  var email = document.getElementById('email').value;
  console.log(email)
  console.log(typeof email)
  console.log(email.length)
  var phone =document.getElementById('phone').value;
  console.log(phone)
  console.log(typeof phone)
  console.log(phone.length)
  if(ifDriver=="driver"){
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
  }
  console.log("ללל")

  if(name.length==0){
    flag_name=  true;
    console.log("name=0")
  }else if(name.length<=1){
    console.log("name>01")
    // flag_name=  false;
    document.getElementById('nickname').value= "";
    alert("שם משתמש חייב להיות באורך של 2 תווים ומעלה");
    flag_name=  false;
    console.log(flag_name)
    document.getElementById('nickname').value= "";
    console.log("name>02")
  }else{
    flag_name=  true;
  }

  console.log("ans_name")
  console.log(flag_name)

  if(email.length==0){
    flag_email=  true;
  }else if (email.length < 5 || !(email.includes('@')) || !(email.includes('.'))){
       // document.getElementById("note2").innerHTML = "כתובת אימייל לא תקינה.";
    console.log("email>01")
    document.getElementById('email').value = "";
    alert("כתובת אימייל לא תקינה.");
    flag_email=  false;
    console.log(flag_email)
    console.log("email>02")
  }else{
    flag_email = true;
  }

  console.log("ans_email")
  console.log(flag_email)
  console.log(phone)

  if(phone.length==0){
    flag_phone= true;
  }else{
      var phone_str= onlyNumbers(phone);
      console.log(phone_str)
      if(phone_str.length!=10 && phone_str.length!=9){
        console.log("phone>01")
        document.getElementById('phone').value = "";
        alert("מספר טלפון לא תקין. חייב להיות בן 9 או 10 ספרות");
        flag_phone = false;
        console.log(flag_phone)
        console.log("phone>02")
      }else{
        document.getElementById('phone').value=phone_str;
        flag_phone= true;
      }
  }

  console.log("ans_phone")
  console.log(flag_phone)

  if(ifDriver=="driver") {

    if(license_plate.length == 0){
      flag_license_plate = true;
    }else{
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
    }

    console.log("ans_license_plate")
    console.log(flag_license_plate)

    if(car_company.length == 0){
      flag_car_company = true;
    }else if (car_company.length <= 1){
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

    if(car_color.length == 0){
      flag_car_color = true;
    }else if(car_color.length <= 1){
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

    if(flag_name == true && flag_email == true && flag_phone == true && flag_license_plate == true && flag_car_company == true && flag_car_color == true  ){// document.getElementById("update_details").submit();
      return true
    }else{
      return false
    }

  }

  if(flag_name == true && flag_email == true && flag_phone == true){// document.getElementById("update_details").submit();
    return true
  }else{
    return false
  }

}



// מה שהיה לפנייייייייייייייי


// function validateEditProfileForm() {
//   let res = false;
//   res = checkName('nickname');         if (!res) return;
//   res = checkEmail('email');         if (!res) return;
//   res = checkPhone('phone');          if (!res) return;
//   res = checkLicensePlate('license_plate');           if (!res) return;
//   res = checkName('car_company');          if (!res) return;
//   res = checkName('car_color');          if (!res) return;
//   document.getElementById("update_details").submit();
// }
//
//
// function checkName(id) {
// var x = document.getElementById(id).value;
//   if(x.length==0) {
//     return true;
//   }
//   if(x.length<=1){
//   alert("שם חייב להיות באורך של 2 תווים ומעלה");
//   document.getElementById(id).value="";
//   return false;
//   }
//   return true;
// }
//
//
// function checkEmail(id) {
//   var x = document.getElementById(id).value;
//   if(x.length==0) {
//     return true;
//   }
//     if (x.length < 5 || !(x.includes('@')) || !(x.includes('.'))) {
//       alert("כתובת אימייל לא תקינה.");
//       document.getElementById(id).value = "";
//       return false;
//     }
//     return true;
// }
//
// function onlyNumbers(num){
// var ans="";
// var i;
// for (i = 0; i < num.length; i++) {
//   var digit = num[i];
//   if (digit=='0' || digit=='1' || digit=='2' || digit=='3' || digit=='4' || digit=='5' || digit=='6' || digit=='7' || digit=='8' || digit=='9'){
//     ans += num[i];
//   }
// }
// return ans;
// }
//
//
// function checkPhone(id){
// var x=document.getElementById(id).value;
//   var y=onlyNumbers(x);
//   if(y.length==0) {
//     return true;
//   }
//   if (y.length!=10 && y.length!=9 ){
//     alert("מספר טלפון לא תקין. חייב להיות בן 9 או 10 ספרות");
//     document.getElementById(id).value="";
//     return false;
//   }
//   else{
//     document.getElementById(id).value=y;
//     return true;
//   }
//   }
//
// function checkLicensePlate(id){
// var x=document.getElementById(id).value;
// var y=onlyNumbers(x);
//  if(y.length==0) {
//     return true;
//   }
//   if (y.length!=8 && y.length!=7 ){
//     alert("מספר לוחית רישוי לא תקין. חייב להיות בן 7 או 8 ספרות");
//     document.getElementById(id).value="";
//     return false;
//   }
//   else{
//     document.getElementById(id).value=y;
//     return true;
//   }
// }