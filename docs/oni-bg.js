(function(){
var NS="http://www.w3.org/2000/svg";
var box=document.createElement("div");box.id="oni-bg";
var shape='<path d="M27 32 L20 4 L44 22 Z"/><path d="M73 32 L80 4 L56 22 Z"/>'+
'<path fill-rule="evenodd" d="M18 52 a32 32 0 1 0 64 0 a32 32 0 1 0 -64 0 Z M29 45 L45 52 L31 57 Z M71 45 L55 52 L69 57 Z M30 66 L70 66 L66 73 L62 68 L58 76 L50 69 L42 76 L38 68 L34 73 Z"/>';
var n=Math.max(14,Math.round(innerWidth*innerHeight/45000));
for(var i=0;i<n;i++){
 var s=document.createElementNS(NS,"svg"),z=44+Math.random()*80;
 s.setAttribute("viewBox","0 0 100 90");s.setAttribute("width",z);s.setAttribute("height",z*.9);
 s.style.left=(Math.random()*100-4)+"%";s.style.top=(Math.random()*100-4)+"%";
 s.style.transform="rotate("+(Math.random()*60-30)+"deg)";
 s.innerHTML=shape;box.appendChild(s);
}
document.body.insertBefore(box,document.body.firstChild);
})();
