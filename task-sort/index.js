var data={};
function getList(){
  $.ajax({
    url:"data.json",
    success:function(res){
      data=res;
      $(".list_number").text(res.user[1]);
      $(data.list).each(function(index,value){
        alert(index+" "+value);
      });
      alert("欢迎！今天也要努力哦！"+res.user[0]);
    }
  })
};


$(document).ready(function(){
  getList();
});
$(".list_detail").on("click",function(){

});
