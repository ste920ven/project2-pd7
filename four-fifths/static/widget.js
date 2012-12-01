$(document).ready(function(){
    resize();
    $(window).resize(resize);
});

function resize()
{
    var currWidth = $('div#statusbar').width();
    $('div#statusbar').css({
	'height': currWidth/10+'px',
	'border-radius': currWidth/20+'px',
	'border-width': currWidth/200+1+'px',
	'font-size': currWidth/36+'px'
    });
    $('div#weather').css({
	'width':  currWidth*0.18+'px',
	'height': currWidth*0.18+'px',
	'line-height': currWidth*0.18+'px',
	'font-size': currWidth*0.07+'px',
	'border-radius': currWidth*0.09+'px',
	'border-width': currWidth/200+1+'px',
	'top': -currWidth*0.04-2+'px'
    });
    $('p#period, p#time').css({
	'line-height': currWidth/10+'px',
	'font-size': currWidth/17+'px',
	'padding-bottom': currWidth*0.005+'px'
    });
}