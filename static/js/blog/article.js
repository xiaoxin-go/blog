$(function () {
    var _this = this;
    console.log('......');
    /** 换页按钮绑定事件 */
    $('.pagingUl li a').click(function () {
        $self = $(this);
        $self.parent().parent().find('.activP').removeClass('activP');
        $self.addClass('activP');
        _this.getContent($self.text());
        return false;
    });

    /* 首页按钮绑定事件 */
    $('.first').click(function(){
        $('.pagingUl').find('.activP').removeClass('activP');
        $('.pagingUl li a').first().addClass('activP');
        _this.getContent(1);
    });

    /* 末页按钮绑定事件 */
    $('.last').click(function(){
        $('.pagingUl').find('.activP').removeClass('activP');
        var $a =  $('.pagingUl li a').last();
        $a.addClass('activP');
        _this.getContent($a.text());
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
       _this.getContent(index)
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
       _this.getContent(index)
    });

    /* 调用接口，获取数据 */
    _this.getContent = function(index){
        $.get('/content/' + index, function (result) {
            _this.customTr(result);
        });
    };

    /* 渲染页面 */
    _this.customTr = function (result) {
        $content = $('.contentList');
        $content.empty();
        var len = result.length;
        for(var i=0;i<len;i++){
            var item = result[i];
            $div = '<div class="panel panel-default">' +
            '<div class="panel-body">' +
            '<h4><a class="title" href="#">'+ item["title"] +'</a></h4>' +
            '<p>'+ _this.getLabel(item['label']) +'</p>' +
            '<p class="overView">'+ item["content"] +'</p>' +
            '<p class="count_r"><span class="count">' +
            '<i class="glyphicon glyphicon-user"></i><a href="#">'+ item["user"] +'</a></span>' +
            '<span class="count"><i class="glyphicon glyphicon-eye-open"></i><a href="#">阅读:' + item['read'] + '</a></span>' +
            ' <span class="count"><i class="glyphicon glyphicon-comment"></i><a href="#">评论:'+ item['review']+ '</a></span>' +
            '<span class="count"><i class="glyphicon glyphicon-time"></i><a href="#">'+ item['addTime'] +'</a></span>' +
            '</p></div></div>';
            $content.append($div)
        }
    };

    /** 解析label */
    _this.getLabel = function(lab){
        var len = lab.length;
        var str = '';
        for(var i=0;i<len;i++){
            str += '<a href="#" class="label label-default">'+ lab[i] +'</a>'
        }
        return str
    }
});
