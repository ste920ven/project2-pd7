var today = new Date();
today.setHours(0);
today.setMinutes(0);
today.setSeconds(0);
today.setMilliseconds(0);
today = today.getTime();

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
    { "start": new Date(today+28800000), "end": new Date(today+31800000) },
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

var special = [
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

function loadBellSchedule(bellDay)
{
    if (bellDay=="Regular")
    {
	bellSchedule = regular;
	$('table#regular').removeClass('hide');
    }

    if (bellDay=="Homeroom")
    {
	bellSchedule = homeroom;
	$('table#homeroom').removeClass('hide');
    }

    if (bellDay=="Conference")
    {
	bellSchedule = conference;
	$('table#conference').removeClass('hide');
    }

    if (bellDay=="Special")
    {
	bellSchedule = special;
	$('table#special').removeClass('hide');
    }

    if (bellDay=="Closed")
    {
	$('table#closed').removeClass('hide');
    }
}

function getTime()
{
    now = new Date();
    return (now.getHours()==12 ? 12 : now.getHours()%12) + ":" +
	(now.getMinutes()<10 ? '0' : '') + now.getMinutes() + ":" +
	(now.getSeconds()<10 ? '0' : '') + now.getSeconds();
}

function tick()
{
    $('span#time').text(getTime());

    if (now<bellSchedule[0].start)
	$('span#period').text("Before School");

    if (bellSchedule[9].end<now)
	$('span#period').text("After School");

    for (var i=0; i<10; i++)
    {
	pd = bellSchedule[i];
	if (pd.start<now && now<pd.end)
	{
	    pdnum = i+1;
	    $('span#period').text("Period "+pdnum);
	    $('table.bell tr#period'+pdnum).css('color','red');
	}
    }

}

$(document).ready(function(){
    if (bellDay=="Unknown") 
	$('table#unknown').removeClass('hide');
    else
	loadBellSchedule(bellDay);

    setInterval(tick,1000);

    $('table#unknown button').click(function(){
	loadBellSchedule($(this).text());
	$(this).parent().parent().parent().parent().addClass('hide');
    });

});