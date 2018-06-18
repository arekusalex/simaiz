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

	// $('#fecha_siembra').change(function(){cambiar_fecha();});
	$('#fecha_siembra').change(function(){
		console.log('adentro')
		fecha=new Date($('#fecha_siembra').val());
		console.log();
		f1=new Date();
		f2=new Date();
		f3=new Date();
		idSem='#'+'s'+$('#select_sem').val();
		diasCiclo=$(idSem).html();
		f1.setDate(fecha.getDate()+diasCiclo*1);
		f2.setDate(fecha.getDate()+diasCiclo*2);
		f3.setDate(fecha.getDate()+diasCiclo*3);
		$('#ap_1').text(f1.getDate()+'/'+(f1.getMonth()+1)+'/'+f1.getFullYear());
		$('#ap_2').text(f2.getDate()+'/'+(f2.getMonth()+1)+'/'+f2.getFullYear());
		$('#ap_3').text(f3.getDate()+'/'+(f3.getMonth()+1)+'/'+f3.getFullYear());
	});
	// $('#select_sem').change(cambiar_fecha());
});

function cambiar_fecha(){
	fecha=new Date($('#fecha_siembra').val());
	f1=new Date();
	f2=new Date();
	f3=new Date();
	idSem='#'+'s'+$('#select_sem').val();
	diasCiclo=$(idSem).html();
	f1.setDate(fecha.getDate()+diasCiclo*1);
	f2.setDate(fecha.getDate()+diasCiclo*2);
	f3.setDate(fecha.getDate()+diasCiclo*3);
	$('#ap_1').text(f1.getDate()+'/'+(f1.getMonth()+1)+'/'+f1.getFullYear());
	$('#ap_2').text(f2.getDate()+'/'+(f2.getMonth()+1)+'/'+f2.getFullYear());
	$('#ap_3').text(f3.getDate()+'/'+(f3.getMonth()+1)+'/'+f3.getFullYear());
}