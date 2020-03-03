function getList(){
  $.ajax({
    url:"data.json",
    success:function(res){
      $(".list_number").val(res.user[1]);
      alert("欢迎！今天也要努力哦！"+res.user[0]);
    }
  })
};


$(document).ready(function(){
  getList();
});
