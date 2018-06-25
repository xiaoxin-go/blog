$(function () {
    var _this = this;
    /** 换页按钮绑定事件 */
    $('.pagingUl li a').click(function () {
        $self = $(this);
        $self.parent().parent().find('.activP').removeClass('activP');
        $self.addClass('activP');
        _this.getMoodList($self.text());
        return false;
    });

    /* 首页按钮绑定事件 */
    $('.first').click(function(){
        $('.pagingUl').find('.activP').removeClass('activP');
        $('.pagingUl li a').first().addClass('activP');
        _this.getMoodList(1);
    });

    /* 末页按钮绑定事件 */
    $('.last').click(function(){
        $('.pagingUl').find('.activP').removeClass('activP');
        var $a =  $('.pagingUl li a').last();
        $a.addClass('activP');
        _this.getMoodList($a.text());
    });

    /* 上一页按钮切换事件 */
    $('.prv').click(function(){
       $self = $('.pagingUl .activP');
       var index = $self.parent().prev().text();
       if(!index){
           return
       }
       $self.removeClass('activP');
       $self.parent().prev().find('a').addClass('activP');
       _this.getMoodList(index)
    });

    /* 下一页按钮切换事件 */
    $('.next').click(function(){
       $self = $('.pagingUl .activP');
       var index = $self.parent().next().text();
       if(!index){
           return
       }
       $self.removeClass('activP');
       $self.parent().next().find('a').addClass('activP');
       _this.getMoodList(index)
    });

    /* 调用接口，获取数据 */
    _this.getMoodList = function(index){
        $.get('/moodList/' + index, function (result) {
            _this.customTr(result);
        });
    };

    /* 渲染页面 */
    _this.customTr = function (result) {
        $content = $('.bloglist');
        $content.empty();
        $content.append(result);
    };
});
