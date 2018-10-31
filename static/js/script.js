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


function getComment(id){

	$.ajax({
		url:'http://127.0.0.1:8000/comments/'+id+'/',
		method:'GET',
		dataType: 'JSON',
		success:function(comments){
			// comment = JSON.parse(comments)
			// alert(typeof(comments));
			M.toast({html: comments[0].fields.comment,  classes: 'green'});	
		}
	});
}



$(document).ready(function(){
	M.AutoInit();
	
	  $('.comments').on('click', function(){
	  		id = $('#k').text()
	  		getComment(id);
	  		
	  		
			        
	  });
	// $('#like').click(function() {
 //        $('#likes').html(+$('#likes').html()+1);

 //    });
 //    $('#dislike').click(function() {
 //        $('#dislike').html(+$('#dislikes').html()+1);

 //    });

      $('.dropdown-trigger').dropdown({
      	constrainWidth: false,
      });
});