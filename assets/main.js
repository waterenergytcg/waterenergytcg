(function(){
  var b=document.querySelector('.menu-btn'),n=document.getElementById('nav');
  if(b){b.addEventListener('click',function(){var o=n.classList.toggle('open');b.setAttribute('aria-expanded',o)});
    n.addEventListener('click',function(e){if(e.target.tagName==='A'){n.classList.remove('open');b.setAttribute('aria-expanded',false)}})}
  var y=document.getElementById('yr');if(y)y.textContent=new Date().getFullYear();
  var f=document.getElementById('contact-form');
  if(f){f.addEventListener('submit',function(e){e.preventDefault();
    var d=new FormData(f),note=document.getElementById('form-note');
    if(!d.get('name')||!d.get('email')||!/\S+@\S+\.\S+/.test(d.get('email'))||!d.get('message')){note.textContent='Please fill in all fields with a valid email.';return}
    var s=encodeURIComponent('Message from '+d.get('name')),
        body=encodeURIComponent(d.get('message')+'\n\nFrom: '+d.get('name')+' <'+d.get('email')+'>');
    note.textContent='Opening your email app…';
    window.location.href='mailto:'+f.dataset.email+'?subject='+s+'&body='+body;});}
})();
