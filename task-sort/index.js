var data={};
function getList(){
  $.ajax({
    url:"data.json",
    success:function(res){
      data=res;
      $(".list_number").text(res.user[1]);
      var a="";
      $(data.list).each(function(index,value){
        a=a+"<li class='list-group-item'><a href='#' class='list_detail' list_id='"+(index+1)+"'> "+value[0]+"</a></li>";
        alert(index+" "+value);
      });
      $.("#list_show").val(a);
      alert("欢迎！今天也要努力哦！"+res.user[0]);
    }
  })
};


$(document).ready(function(){
  getList();
});
$(".list_detail").on("click",function(){
  alert($(this).text());
  console.log("click:"+$(this).text());
});
