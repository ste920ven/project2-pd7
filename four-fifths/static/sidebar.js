$(document).ready(function(){
    $('div#sidebar div#toggle').toggle(function(){
	$('div#sidebar').animate({right:"-30%"},1200,function(){
	    $('div#sidebar div#toggle').html("&laquo;").animate({left:"-70px"},500).addClass('hidden');
       	});
	$('div.main').animate({padding:"4% 12.5%",width:"75%"},1200);
    },function(){
	$('div#sidebar div#toggle').animate({left:"0px"},500,function(){
	    $(this).html("&raquo;");
 	    $('div#sidebar').animate({right:"0%"},1200);
	    $('div.main').animate({padding:"4%",width:"62%"},1200);
	}).removeClass('hidden');
    });
});