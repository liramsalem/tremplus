function openNav() {
  document.getElementById("sideNavigationBar").style.width = "250px";
}

function closeNav() {
  document.getElementById("sideNavigationBar").style.width = "0";
}
//
// function openNav() {
//   document.getElementById("sideNavigationBar").style.width = "250px";
//   document.getElementById("main").style.marginLeft = "-250px";
//   document.getElementById("main").style.marginRight = "200px";
// }
//
// function closeNav() {
//   document.getElementById("sideNavigationBar").style.width = "0";
//   document.getElementById("main").style.marginLeft= "0";
//   document.getElementById("main").style.marginRight = "0";
// }
//
// //----------------------- close side nav When the user clicks anywhere outside ------------
//
// const sideNavigationBar = document.getElementById('sideNavigationBar')
// const main = document.getElementById('main')
// const TopNav = document.getElementById('TopNav')
// const footer = document.getElementById('footer')
//
// document.onclick= function (e){
//   if((e.target.id == 'main' || e.target.id == 'footer') && e.target.id != 'sideNavigationBar' && e.target.id !='TopNav' ){
//     document.getElementById("sideNavigationBar").style.width = "0";
//     document.getElementById("main").style.marginLeft= "0";
//   }
// }
