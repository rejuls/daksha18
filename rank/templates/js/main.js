// Responsive Nav
function countdown()
{
  var now=new Date();
  var e=new Date(2018,10,21);
  var cTime=now.getTime();
  var eTime=e.getTime();
  var d=eTime-cTime;
  var s=Math.floor(d/1000);
  var m=Math.floor(s/60);
  var h=Math.floor(m/60);
  var d=Math.floor(h/24);
  h%=24;
  m%=60;
  s%=60;
  h=(h<10) ? '0' + h : h;
  m=(m<10) ? '0' + m : m;
  s=(s<10) ? '0' + s : s;

  document.getElementById("days").innerText=d;
  document.getElementById("hours").innerText=h;
  document.getElementById("minutes").innerText=m;
  document.getElementById("seconds").innerText=s;
  setTimeout(countdown,1000);
}
$(document).ready(function(){
countdown();

});
