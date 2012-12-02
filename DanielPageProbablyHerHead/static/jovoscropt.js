//this sets up the slideything
$(function(){
	$('.slide-out-div').tabSlideOut({
		tabHandle: '.handle',                     //class of the element that will become your tab
		pathToTabImage: '../static/arrows.jpg', 			  //path to the image for the tab //Optionally can be set using css
		imageHeight: '122px',                     //height of tab image           //Optionally can be set using css
		imageWidth: '40px',                       //width of tab image            //Optionally can be set using css
		tabLocation: 'left',                      //side of screen where tab lives, top, right, bottom, or left
		speed: 300,                               //speed of animation
		action: 'hover',                          //options: 'click' or 'hover', action to trigger animation
		topPos: '0px',                          //position from the top/ use if tabLocation is left or right
		leftPos: '20px',                          //position from left/ use if tabLocation is bottom or top
		fixedPosition: false                      //options: true makes it stick(fixed position) on scroll
	});
});

//this gets a generated image and displays it in generated-art
function gen(){
	console.log("generate is clicked");
}

function edit(){
	pixlr.edit({
		image:''
		, title:'Example image 3'
		, service:'express'
		, target:'www.google.com'
		, exit:'www.google.com'
	});
	console.log('edit is clicked');
}

$(document).ready(
	function() {
		$('#generate').click(gen);
		$('#edit').click(edit);
	}
);
