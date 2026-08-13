let contador = 1;


function proximo(text, num, classe){
    const img = document.getElementById(classe);

    contador++;
    if(contador > num){
        contador = 1;
    }
    
    img.classList.add("imgfadeo");
    setInterval(()=>{
        img.src = text+ contador + ").png";
        img.classList.remove("imgfadeo");
    },100);
    
    
    img.classList.add("imgfadei");
    setInterval(()=>{
        img.classList.remove("imgfadei");
    },500);
};


function anterior(text, num, classe){
    const img = document.getElementById(classe);

    contador--;

    if(contador < 2){
        contador = num;
    }

    img.classList.add("imgfadeo");
    setInterval(()=>{
        img.src = text+ contador + ").png";
        img.classList.remove("imgfadeo");
    },100);
    
    
    img.classList.add("imgfadei");
    setInterval(()=>{
        img.classList.remove("imgfadei");
    },500);
};


//setInterval(()=>{

    //proximo();

//},10000);

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
