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


  let flag_name = false;
  let flag_email = false;
  let flag_phone = false;
  let flag_license_plate = false;
  let flag_car_company = false;
  let flag_car_color = false;

  var ifDriver =document.getElementById('driver_or_not').value;
  var name = document.getElementById('nickname').value;
  var email = document.getElementById('email').value;
  var phone =document.getElementById('phone').value;
  if(ifDriver=="driver"){
    var license_plate = document.getElementById('license_plate').value;
    var car_company = document.getElementById('car_company').value;
    var car_color = document.getElementById('car_color').value;
  }

  if(name.length==0){
    flag_name=  true;
  }else if(name.length<=1){
    document.getElementById('nickname').value= "";
    alert("שם משתמש חייב להיות באורך של 2 תווים ומעלה");
    flag_name=  false;
  }else{
    flag_name=  true;
  }


  if(email.length==0){
    flag_email=  true;
  }else if (email.length < 5 || !(email.includes('@')) || !(email.includes('.'))){
    document.getElementById('email').value = "";
    alert("כתובת אימייל לא תקינה.");
    flag_email=  false;
  }else{
    flag_email = true;
  }

  if(phone.length==0){
    flag_phone= true;
  }else{
      var phone_str= onlyNumbers(phone);
      if(phone_str.length!=10 && phone_str.length!=9){
        document.getElementById('phone').value = "";
        alert("מספר טלפון לא תקין. חייב להיות בן 9 או 10 ספרות");
        flag_phone = false;
      }else{
        document.getElementById('phone').value=phone_str;
        flag_phone= true;
      }
  }


  if(ifDriver=="driver") {

    if(license_plate.length == 0){
      flag_license_plate = true;
    }else{
      var license_plate_str = onlyNumbers(license_plate);
      if(license_plate_str.length != 8 && license_plate_str.length != 7){
        document.getElementById('license_plate').value = "";
        alert("מספר לוחית רישוי לא תקין. חייב להיות בן 7 או 8 ספרות");
        flag_license_plate = false;
      }else{
        document.getElementById('license_plate').value = license_plate_str;
        flag_license_plate = true;
      }
    }


    if(car_company.length == 0){
      flag_car_company = true;
    }else if (car_company.length <= 1){
      document.getElementById('car_company').value = "";
      alert("יצרן הרכב חייב להיות באורך של 2 תווים ומעלה");
      flag_car_company = false;
    }else{
      flag_car_company = true;
    }


    if(car_color.length == 0){
      flag_car_color = true;
    }else if(car_color.length <= 1){
      document.getElementById('car_color').value = "";
      alert("צבע הרכב חייב להיות באורך של 2 תווים ומעלה");
      flag_car_color = false;
    }else{
      flag_car_color = true;
    }


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


