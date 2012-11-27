var mediaQuery = "only screen and (-webkit-min-device-pixel-ratio : 1.5), only screen and (min-device-pixel-ratio : 1.5), only screen and (max-width: 500px), only screen and (max-device-width: 500px)";

$(document).ready(function(){

    if (matchMedia)
    { 
	var mq = window.matchMedia(mediaQuery);  
	mq.addListener(WidthChange);  
	WidthChange(mq);  
    }

    function WidthChange(mq)
    {  
	//change to small
	if (mq.matches)
	{  
	    $('div#sidebar').css('right','0');
	    $('div#sidebar div#toggle').css('left','0').unbind();
	    $('div.main').css({padding:"0",width:"100%"});
	} 
	
	//change to big
	else
	{  
	    $('div.main').css({padding:"4%",width:"62%"});
	    $('div#sidebar div#toggle').html("&raquo;").toggle(function(){
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
	}  
    } 

});