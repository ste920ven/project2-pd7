var today = new Date();
today.setHours(0);
today.setMinutes(0);
today.setSeconds(0);
today.setMilliseconds(0);
today = today.getTime();

var now = new Date();

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

/*

var conference = [
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

var special = [
    { "start": new Date(today+28800000), "end": new Date(today+31200000) },
    { "start": new Date(today+31440000), "end": new Date(today+33840000) },
    { "start": new Date(today+34080000), "end": new Date(today+36480000) },
    { "start": new Date(today+37560000), "end": new Date(today+39960000) },
    { "start": new Date(today+40200000), "end": new Date(today+42600000) },
    { "start": new Date(today+42840000), "end": new Date(today+45240000) },
    { "start": new Date(today+45480000), "end": new Date(today+47880000) },
    { "start": new Date(today+48120000), "end": new Date(today+50520000) },
    { "start": new Date(today+50760000), "end": new Date(today+53160000) },
    { "start": new Date(today+53400000), "end": new Date(today+55800000) }
];

*/

function getTime()
{
    now = new Date();
    return now.getHours()%12 + ":" +
	(now.getMinutes()<10 ? '0' : '') + now.getMinutes() + ":" +
	(now.getSeconds()<10 ? '0' : '') + now.getSeconds();
}

function tick()
{
    $('span#time').text(getTime());

    if (now<regular[0].start)
	$('span#period').text("Before School");

    if (regular[9].end<now)
	$('span#period').text("After School");

    for (var i=0; i<10; i++)
    {
	pd = regular[i];
	if (pd.start<now && now<pd.end)
	{
	    pdnum = i+1;
	    $('span#period').text("Period "+pdnum);
	    $('table#bell tr#period'+pdnum).css('color','red');
	}
    }

}

$(document).ready(function(){
    setInterval(tick,1000);
});