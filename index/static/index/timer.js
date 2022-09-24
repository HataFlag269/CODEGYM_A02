document.addEventListener('DOMContentLoaded', function(){
   // 10秒後に実行  
   setTimeout(() => {
      var form = document.getElementById("answer_form");
      form.submit();
   }, 10*1000);
});