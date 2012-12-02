$(document).ready( function() {
    $("tr").click(move);
    updateprice();
});

function move(){
    if($(this).attr('type') == 'n') {
	$(this).attr('type','h');
	$('#have').append($(this));
	updateprice();
    }
    else {
	$(this).attr('type', 'n');
	$('#need').append($(this));
	updateprice();
    }
    updateprice();
}

function updateprice(){
    var sum = 0.0;
    $.each($('#need tr'), function(){
	sum += parseFloat($(this).attr('cost'));
    }
	  );
    var sumString = Math.round(sum * 100) / 100;
    sumString = String(sumString);
    var decimalpos = sumString.indexOf('.');
    while(sumString.substring(decimalpos).length < 3)
	sumString += '0';
    if(sumString == '000')
	sumString = '0.00';
    $('#total').text('$' + sumString);
}
