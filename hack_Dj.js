function someFunction(){
    console.log("test XSS attack success!");
    console.log("Hi, I am @yagaoer from SCSE, BUAA~");
}

function hidePostContent(){
    document.querySelector('.post-content').style.display = 'none';
}

someFunction();
hidePostContent();