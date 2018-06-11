$(document).ready(function(){
	if ($('#si_suelo').is(':checked')){
		$('.si_analisis').removeClass('ocultar');
		$('.no_analisis').addClass('ocultar');
	}
	if($('#no_suelo').is(':checked')){
		$('.no_analisis').removeClass('ocultar');
		$('.si_analisis').addClass('ocultar');
	}
	$(':radio').click(function(){
		if(this.id=='si_suelo' && $(this).is(':checked')){
			$('.si_analisis').removeClass('ocultar');
			$('.no_analisis').addClass('ocultar');
		}
		if (this.id=='no_suelo' && $(this).is(':checked')){
			$('.no_analisis').removeClass('ocultar');
			$('.si_analisis').addClass('ocultar');
		}
	});
});