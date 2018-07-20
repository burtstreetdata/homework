    function animate(opts){
    var start = new Date;
    var id = setInterval(function(){

    var timePassed = new Date - start;

    var progress = timePassed / opts.duration

    if(progress > 1){

    progress = 1;

    }

    var delta = opts.delta(progress);

    opts.step(delta);

    if (progress == 1){

    clearInterval(id);

    opts.callback();

    }

    }, opts.dalay || 17);

    }





    var ul;

    var liItems; 

    var imageWidth;

    var imageNumber;

    var currentImage = 1;



    function init_slider(){



    ul = document.getElementById('image_slider');

    liItems = ul.children;

    imageNumber = liItems.length;

    imageWidth = liItems[0].children[0].offsetWidth;

    // set ul's width as the total width of all images in image slider.

    ul.style.width = parseInt(imageWidth * imageNumber ) + 'px';

    container = document.getElementsByClassName('container')[0];

    let pad = parseInt($(container).css("padding-left"));

    container.style.width = parseInt(2*pad + imageWidth)+ 'px';

    slider(ul);

    }

	window.onload = init_slider;




    function slider(ul){ 

    animate({

    delay:10,

    duration: 300,

    delta:function(p){return Math.max(0, -1 + 2 * p)},

    step:function(delta){

    ul.style.left = '-' + parseInt(currentImage * imageWidth + delta * imageWidth) + 'px';

    },

    callback:function(){

    currentImage++;

    // if it doesn't slied to the last image, keep sliding

    if(currentImage < imageNumber-1){

    slider(ul);

    }

    // if current image it's the last one, it slides back to the first one

    else{

    var leftPosition = (imageNumber - 1) * imageWidth;

    // after 2 seconds, call the goBack function to slide to the first image 

    setTimeout(function(){goBack(leftPosition)},1000); 

    setTimeout(function(){slider(ul)}, 2000);

    }

    }

    });

    }



    function goBack(leftPosition){

    currentImage = 0; 

    var id = setInterval(function(){

    if(leftPosition >= 0){

    ul.style.left = '-' + parseInt(leftPosition) + 'px';

    leftPosition -= imageWidth / 10;

    }

    else{

    clearInterval(id);

    } 

    }, 17);

    }



    window.onload = init_slider;index.getElementById('changeme').onclick = turnitred;   

    function turnitred() {
        index.body.style.color = "red";
        return false;
    }   
	
