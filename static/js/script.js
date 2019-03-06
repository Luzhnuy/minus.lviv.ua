
function getComment(id,click_count){

	$.ajax({
		url:'http://127.0.0.1:8000/comments/'+id+'/',
		method:'GET',
		dataType: 'JSON',
		success:function(comments){
			// comment = JSON.parse(comments)
			// alert(typeof(comments));
			console.log(comments);
			M.toast({html: comments[click_count].comment,  classes: 'green'});
		}
	});
}



$(document).ready(function(){
	M.AutoInit();
	var click_count = 0;
	  $('.comments').on('click', function(){
	  		id = this.id
	  		getComment(id,click_count);
	  		click_count++;
	  });


      $('.dropdown-trigger').dropdown({
      	constrainWidth: false,
      });
});
