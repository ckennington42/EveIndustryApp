


$('.btn-clear-assets').click(function(){
    $.ajax(
    {
        type:"GET",
        url: "/inventory/clear/",
        data:{
        },
        success: function( data ) {
            location.reload()
        }
     });
});