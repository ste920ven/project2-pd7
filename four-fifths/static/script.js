var today = getToday();
var now = new Date();

var bellSchedule;

var regular = [
    { "start": new Date(today+28800000), "end": new Date(today+31260000) },
    { "start": new Date(today+31500000), "end": new Date(today+33960000) },
    { "start": new Date(today+34200000), "end": new Date(today+36900000) },
    { "start": new Date(today+37140000), "end": new Date(today+39600000) },
    { "start": new Date(today+39840000), "end": new Date(today+42300000) },
    { "start": new Date(today+42540000), "end": new Date(today+45000000) },
    { "start": new Date(today+45240000), "end": new Date(today+47700000) },
    { "start": new Date(today+47940000), "end": new Date(today+50400000) },
    { "start": new Date(today+50640000), "end": new Date(today+53100000) },
    { "start": new Date(today+53340000), "end": new Date(today+55800000) }
];

var homeroom = [
    { "start": new Date(today+28800000), "end": new Date(today+31260000) },
    { "start": new Date(today+31500000), "end": new Date(today+33960000) },
    { "start": new Date(today+34200000), "end": new Date(today+36900000) },
    { "start": new Date(today+37140000), "end": new Date(today+39600000) },
    { "start": new Date(today+39840000), "end": new Date(today+42300000) },
    { "start": new Date(today+42540000), "end": new Date(today+45000000) },
    { "start": new Date(today+45240000), "end": new Date(today+47700000) },
    { "start": new Date(today+47940000), "end": new Date(today+50400000) },
    { "start": new Date(today+50640000), "end": new Date(today+53100000) },
    { "start": new Date(today+53340000), "end": new Date(today+55800000) }
];

var conference = [
    { "start": new Date(today+28800000), "end": new Date(today+31020000) },
    { "start": new Date(today+31260000), "end": new Date(today+33480000) },
    { "start": new Date(today+33720000), "end": new Date(today+35940000) },
    { "start": new Date(today+36180000), "end": new Date(today+38400000) },
    { "start": new Date(today+38640000), "end": new Date(today+40860000) },
    { "start": new Date(today+41100000), "end": new Date(today+43320000) },
    { "start": new Date(today+43560000), "end": new Date(today+45780000) },
    { "start": new Date(today+46020000), "end": new Date(today+48240000) },
    { "start": new Date(today+48480000), "end": new Date(today+50700000) },
    { "start": new Date(today+50940000), "end": new Date(today+53160000) }
];

var special = [
    { "start": new Date(today+28800000), "end": new Date(today+31080000) },
    { "start": new Date(today+31320000), "end": new Date(today+33600000) },
    { "start": new Date(today+33840000), "end": new Date(today+36240000) },
    { "start": new Date(today+36480000), "end": new Date(today+38760000) },
    { "start": new Date(today+39000000), "end": new Date(today+41280000) },
    { "start": new Date(today+41520000), "end": new Date(today+43800000) },
    { "start": new Date(today+44040000), "end": new Date(today+46320000) },
    { "start": new Date(today+46560000), "end": new Date(today+48840000) },
    { "start": new Date(today+49080000), "end": new Date(today+51360000) },
    { "start": new Date(today+51600000), "end": new Date(today+53880000) }
];

function getToday()
{
    var today = new Date(); 
    today.setHours(0);
    today.setMinutes(0);
    today.setSeconds(0);
    today.setMilliseconds(0);
    today = today.getTime();
    return today;
}

function loadBellSchedule(bellDay)
{
    if (bellDay=="Regular")
    {
	bellSchedule = regular;
	$('span#schedule').text('Regular Schedule');
	$('table#regular').removeClass('hide');
    }

    if (bellDay=="Homeroom")
    {
	bellSchedule = homeroom;
	$('span#schedule').text('Homeroom Schedule');
	$('table#homeroom').removeClass('hide');
    }

    if (bellDay=="Conference")
    {
	bellSchedule = conference;
	$('span#schedule').text('Conference Schedule');
	$('table#conference').removeClass('hide');
    }

    if (bellDay=="Special")
    {
	bellSchedule = special;
	$('span#schedule').text('Special Schedule');
	$('table#special').removeClass('hide');
    }

    if (bellDay=="Weekend")
    {
	$('p#period').text('Weekend');
	$('p#currschedule').addClass('hide');
    }

    if (bellDay=="Closed")
    {
	$('p#period').text('Closed');
	$('p#currschedule').addClass('hide');
    }
}

function getTime()
{
    now = new Date();
    return (now.getHours()%12==0 ? 12 : now.getHours()%12) + ":" +
	(now.getMinutes()<10 ? '0' : '') + now.getMinutes() + ":" +
	(now.getSeconds()<10 ? '0' : '') + now.getSeconds();
}

function tick()
{
    now = new Date();

    if (now-today>86400000)
    {
	today = getToday();
	window.location.reload();
    }

    $('p#time').text(getTime());

    //reset period
    $('table.bell tr').removeClass('active');
    $('p#time').removeClass('warning');

    if (now<bellSchedule[0].start)
	$('p#period').text("Before School");

    if (bellSchedule[9].end<now)
	$('p#period').text("After School");

    var found = false;
    for (var i=0; i<10; i++)
    {
	pd = bellSchedule[i];
	if (pd.start<now && now<pd.end)
	{
	    found = true;
	    pdnum = i+1;
	    $('p#period').text("Period "+pdnum);
	    $('table.bell tr#period'+pdnum).addClass('active');
	    
	    //if less than 5 minutes left
	    if (pd.end-now<300000)
		$('p#time').addClass('warning');
	}
    }

    if (found==false)
    {
	for (var i=0; i<9; i++)
	{
	    prevPD = bellSchedule[i];
	    nextPD = bellSchedule[i+1];
	    if (prevPD.end<now && now<nextPD.start)
	    {
		prevPDnum = i+1;
		nextPDnum = i+2;
		$('table.bell tr#period'+prevPDnum).addClass('active');
		$('table.bell tr#period'+nextPDnum).addClass('active');	
		$('p#period').text("Passing");	
	    }
	}
    }

}

$(document).ready(function(){
    
    $('a').attr('target','_blank');

    $('div#weather').css('background-image','url('+forecastURL+')');

    if (bellDay=="Unknown") 
    {
	$('div#unknown').removeClass('hide');
	$('p#period').text('Unknown');
	$('span#schedule').text('Schedule Select');
    }
    else
	loadBellSchedule(bellDay);

    setInterval(tick,1000);

    $('div#unknown button').click(function(){
	loadBellSchedule($(this).text());
	$(this).parent().addClass('hide');
    });

});