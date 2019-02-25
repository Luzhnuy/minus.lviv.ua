
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
	  		id = this.id
	  		getComment(id);
	  });


      $('.dropdown-trigger').dropdown({
      	constrainWidth: false,
      });
});
