function setMinDate() {
  var today= new Date()
  var today_for_min = today.toISOString().split('T')[0];
  document.getElementsByName("drive_date")[0].setAttribute('min', today_for_min);
  document.getElementsByName("drive_date")[0].setAttribute('value', today_for_min);
  var hh = today.getHours();
  var mm = today.getMinutes();
  current_time= hh + ':' + mm;
  document.getElementsByName("departure_hour")[0].setAttribute('value',current_time);
  var dd_for_max = today.getDate();
  var mm_for_max = today.getMonth() + 1; //January is 0!
  var yyyy_for_max = today.getFullYear()+2;
  if (dd_for_max < 10) {
     dd_for_max = '0' + dd_for_max;
  }
  if (mm_for_max < 10) {
     mm_for_max = '0' + mm_for_max;
  }
  today_for_max = yyyy_for_max + '-' + mm_for_max + '-' + dd_for_max;
  document.getElementById("drive_date").setAttribute("max", today_for_max);

}


function validateNewDriveForm(){
  let res = false;
  res = checkOrigin('origin');          if (!res) return;
  res = checkDestination('destination');          if (!res) return;
  res = checkFreeSeat('max_seats');          if (!res) return;
  document.getElementById("NewDrive_form").submit();
}


function validateNewDriverForm() {
  let res = false;
  res = checkLicensePlate('license_plate');           if (!res) return;
  res = checkCompany('car_company');          if (!res) return;
  res = checkColor('car_color');          if (!res) return;
  res = checkIfHasImage('licence_driver_img');          if (!res) return;
  document.getElementById("NewDriver_form").submit();
}

function checkIfHasImage(id) {
var x = document.getElementById(id).value;
if(x.length==0){
  alert("על מנת להיות נהג יש להעלות רישיון נהיגה");
  document.getElementById(id).value="";
  return false;
}
return true;
}


function checkCompany(id) {
var x = document.getElementById(id).value;
if(x.length<=1){
  alert("יצרן הרכב חייב להיות באורך של 2 תווים ומעלה");
  document.getElementById(id).value="";
  return false;
}
return true;
}

function checkColor(id) {
var x = document.getElementById(id).value;
if(x.length<=1){
  alert("צבע הרכב חייב להיות באורך של 2 תווים ומעלה");
  document.getElementById(id).value="";
  return false;
}
return true;
}

function checkOrigin(id) {
var x = document.getElementById(id).value;
if(x.length<=1){
  alert("מוצא חייב להיות באורך של 2 תווים ומעלה");
  document.getElementById(id).value="";
  return false;
}
return true;
}

function checkDestination(id) {
var x = document.getElementById(id).value;
if(x.length<=1){
  alert("יעד חייב להיות באורך של 2 תווים ומעלה");
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


function checkLicensePlate(id){
var x=document.getElementById(id).value;
var y=onlyNumbers(x);
if (y.length!=8 && y.length!=7 ){
  alert("מספר לוחית רישוי לא תקין. חייב להיות בן 7 או 8 ספרות");
  document.getElementById(id).value="";
  return false;
}
else{
  document.getElementById(id).value=y;
  return true;
}
}

function onlyNumbers_forFreeSeat(num){
var ans="";
var i;
for (i = 0; i < num.length; i++) {
  var digit = num[i];
  if ( digit=='1' || digit=='2' || digit=='3' || digit=='4' || digit=='5' || digit=='6'){
    ans += num[i];
  }
}
return ans;
}

function checkFreeSeat(id){
var x=document.getElementById(id).value;
var y=onlyNumbers_forFreeSeat(x);
if (y.length!=1 ){
  alert("רכב יכול להכיל עד 6 מקומות פנויים");
  document.getElementById(id).value="";
  return false;
}
else{
  document.getElementById(id).value=y;
  return true;
}
}
