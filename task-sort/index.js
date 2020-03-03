var data={};
function getList(){
  $.ajax({
    url:"data.json",
    success:function(res){
      data=res;
      $(".list_number").text(res.user[1]);
      $("#nick_name").text(res.user[0]);
      var a="";
      $(data.list).each(function(index,value){
        a=a+"<li class='list-group-item'><span class='badge'>"+value[1]+"</span>"+"<a href='#' class='list_detail' list_id="+(index+1)+"> "+value[0]+"</a></li>";
      });
      $("#list_show").html(a);
      alert("欢迎！今天也要努力哦！"+res.user[0]);
    }
  })
};

function list_sort(a1,a2){
  console.log(a1);
  if(a1[1]<a2[1]){
    return -1;
  }else if(a1[1]>a2[1]){
    return 1;
  }else{
    if(a1[2]<a2[2]){
      return 1;
    }else{
      return -1;
    }
  }
}
$(document).ready(function(){
  getList();
  $("body").delegate(".list_detail","click",function(){
    alert("click!");
    alert($(this).text());
    var a=0;
    a=$(this).attr("list_id");
    console.log("click:"+$(this).text());
    $("#now_list").text(data.list[a-1][0]);
    $("#now_list_num").text(data.list[a-1][1]);
    data.list[a-1][2].sort(list_sort);
    // var a="";
    // $(data.list[a-1][2]).each(function(index,value){
    //   a=a+"<li class='list-group-item todo_items' importance="+data.list[a-1][2][index][2]+">";
    // });

  });
});
