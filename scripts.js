let contador = 1;


function proximo(){
    const img = document.getElementById("imag");

    contador++;
    if(contador > 7){
        contador = 1;
    }
    
    img.classList.add("imgfadeo");
    setInterval(()=>{
        img.src = "imagens/lasthope ("+ contador + ").png";
        img.classList.remove("imgfadeo");
    },100);
    
    
    img.classList.add("imgfadei");
    setInterval(()=>{
        img.classList.remove("imgfadei");
    },500);
};


function anterior(){
    const img = document.getElementById("imag");

    contador--;

    if(contador < 2){
        contador = 7;
    }

    img.classList.add("imgfadeo");
    setInterval(()=>{
        img.src = "imagens/lasthope ("+ contador + ").png";
        img.classList.remove("imgfadeo");
    },100);
    
    
    img.classList.add("imgfadei");
    setInterval(()=>{
        img.classList.remove("imgfadei");
    },500);
};


setInterval(()=>{

    proximo();

},10000);

const links = document.querySelectorAll("a.link");

links.forEach(link => {
    
    link.addEventListener("click", function(event) {
        event.preventDefault();

        document.body.classList.add("fade-out");

        setTimeout(() => {
            window.location.href = this.href;
        }, 2000);
    });
});
