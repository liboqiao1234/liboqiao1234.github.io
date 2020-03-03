function getList(){
  $.ajax({
    url:"data.json",
    success:function(res){
      // res_j=JSON.parse(res);
      // console.log(res_j);
      alert("欢迎！今天也要努力哦！"+res.user[0]);
    }
  })
};


$(document).ready(function(){
  getList();
});
