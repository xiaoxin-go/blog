$(function(){
    var _this = this;
    $('form').submit(function(){
        var flag;
        if($('#pwd').val() == '' && $('#uname').val() == ''){
            flag = 3;
        }
        else if($('#uname').val() == ''){
            flag = 1;
        }
        else if($('#pwd').val() == ''){
            flag = 2;
        }
        var msg = ['','用户名不能为空','密码不能为空','用户名和密码不能为空'];
        var $msg = $('.msg');
        if(flag){
            $msg.text(msg[flag]);
            return false;
        }
    })

});