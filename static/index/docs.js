$(function() {
	$("a").click(function() {
		$("a").removeClass("active");
		$(this).attr("class", "active");
	});

});
