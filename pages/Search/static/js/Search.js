// function myFunction() {
//     var input, filter, ul, li, a, i, txtValue;
//     input = document.getElementById("myInput");
//     filter = input.value.toUpperCase();
//     ul = document.getElementById("myUL");
//     li = ul.getElementsByTagName("li");
//     for (i = 0; i < li.length; i++) {
//         a = li[i].getElementsByTagName("a")[0];
//         txtValue = a.textContent || a.innerText;
//         if (txtValue.toUpperCase().indexOf(filter) > -1) {
//             li[i].style.display = "";
//         } else {
//             li[i].style.display = "none";
//         }
//     }
// }

function setMinDate() {
  var today= new Date()
  var today_for_min = today.toISOString().split('T')[0];
  document.getElementsByName("drive_date")[0].setAttribute('min', today_for_min);
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

