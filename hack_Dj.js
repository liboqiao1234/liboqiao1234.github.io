function someFunction(){
    console.log("test XSS attack success!");
    console.log("Hi, I am @yagaoer from SCSE, BUAA~");
}

function hidePostContent(){
    document.querySelector('.post-content').style.display = 'none';
}

function showPostContent(){
    document.querySelector('.post-content').style.display = '';

}

function blinkPostContent(times){
    times = times*1000;
    setInterval(()=>{
        if (document.querySelector('.post-content').style.display !== 'none'){
            document.querySelector('.post-content').style.display = 'none';
        } else {
            document.querySelector('.post-content').style.display = '';
        }
    }, times);
}

someFunction();
//hidePostContent();