var data={};
function getList(){
  $.ajax({
    url:"data.json",
    success:function(res){
      data=res;
      $(".list_number").text(res.user[1]);
      var a="";
      $(data.list).each(function(index,value){
        a=a+"<li class='list-group-item'><span class='badge'>"+value[1]+"<a href='#' class='list_detail' list_id="+(index+1)+"> "+value[0]+"</a></li>";
        alert(index+" "+value);
      });
      $("#list_show").html(a);
      alert("欢迎！今天也要努力哦！"+res.user[0]);
    }
  })
};


$(document).ready(function(){
  getList();
});
$(".list_detail").on("click",function(){
  alert("click!");
  alert($(this).text());
  var a=0;
  a=$(this).attr("list_id");
  console.log("click:"+$(this).text());
  $("#now_list").text(data.list[a-1][0]);
  $("#now_list_num").text(data.list[a-1][1]);
});
