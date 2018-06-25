$(function(){
    $('#nav_menu ul li').on('click','a',function(){
        var $self = $(this);
        $self.parent().parent().find('.active').removeClass('active');
        $self.addClass('active');
    })
});