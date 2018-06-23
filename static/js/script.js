// function gavetext(id){
// 		$.ajax({
// 			url:'/admin/show_practice.php',						
// 			method:'POST',
// 			dataType:'text',
// 			statbox:"status",
// 			data:{'id':id},
// 			success:function(msg){
// 				 $('#lol').text(msg);
// 			}
// 		}).done(function(){
// 			console.log('success');
// 		});
// }



function getComment(){

	$.ajax({
		url:'http://127.0.0.1:8000/comments',
		method:'GET',
		dataType: 'json',
		success:function(comments){
			alert(comments);
		}
	})
}



$(document).ready(function(){
	 M.AutoInit();
	  $('.comments').on('click', function(){
	  		getComment();
	  		M.toast({html: 'комент',  classes: 'green'});	
	  });
});