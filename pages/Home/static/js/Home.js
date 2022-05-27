
var myDate = new Date();
var hrs = myDate.getHours();
var greet;

function greet_text(){
    if (hrs < 12){
      greet = 'בוקר טוב, ';
    }
    else if (hrs >= 12 && hrs <= 17){
      greet = 'צהריים טובים, ';
    }
    else if (hrs >= 17 && hrs <= 21){
        greet = 'ערב טוב, ';
    }
    else if (hrs >= 21 && hrs <= 24){
        greet = 'לילה טוב, ';
    }
    document.getElementById('lblGreetings').innerHTML =
         greet;

}



