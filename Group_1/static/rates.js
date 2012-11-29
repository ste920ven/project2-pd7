

function showrating(){
    var num = $("#number").text();
    var restaurant = $(this).text();
    var url = '/getrating/'+num+'/' + restaurant;
    TINY.box.show({url:url,animate:false,close:false,boxid:'frameless',top:5});

}

$(document).ready(function(){
    $("td").click(showrating);
});