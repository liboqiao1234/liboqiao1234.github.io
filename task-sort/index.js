function getList(){
  $.ajax({
    url:"data.json",
    success:function(res){
      res_j=JSON.parse(res);
      alert("欢迎！今天也要努力哦！"+res_j.user[0]);
    }
  })
};


$(document).ready(function(){
  getList();
});
