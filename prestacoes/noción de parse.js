$('#tabela_analitica tbody').first().find('tr').each(function(index, value){
	console.log($(value).find('td').first().text()); 
});