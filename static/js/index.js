// ajax.
function give_minus(id){
  $.ajax({
    url:'http://127.0.0.1:8000/minusstore/give/'+id+'/',
		method:'GET',
		dataType: 'JSON',
		success:function(minus){
			   console.log(minus);
         console.log(minus.length);
         $("#"+id+"b").empty();
         for(var i = 0;i<=minus.length-1;i++ ){
           $('#'+id+"b").append("<div><p><a href='http://127.0.0.1:8000/minusstore/minus/"+minus[i].pk +"/' style='color:black;text-decoration: underline;'>"+minus[i].fields.title+"</a></p><audio src='/static/minus.mp3' controls controlsList='nodownload'></audio><p>(Аудіо) "+Number(minus[i].fields.filesize/1000000)+" мб "+ minus[i].fields.bitrate+"Кбіт/с  </p></div>");

         }
		}
  });
}

function likedislike(user_id,object_id,likeordislike){
    $.ajax({
      url:'http://127.0.0.1:8000/likedislike/'+user_id+'/'+object_id+'/'+17+'/'+likeordislike+'/',
		    method:'GET',
		      dataType: 'JSON',
		        success:function(likeanddislike){
			          console.log(likeanddislike);
                $('.like').empty();
                $('.like').append('<i class="material-icons left">mood</i>'+likeanddislike.likes);
                $('.dislike').empty();
                $('.dislike').append('<i class="material-icons left">mood_bad</i>'+likeanddislike.dislikes);
                console.log(likeanddislike.likes);
                console.log(likeanddislike.dislikes);

            }

      });
}
jQuery(document).ready(function(){
	M.AutoInit();

	  $('.gaveminus').on('click', function(event){
	  		var id = this.id;
        console.log(id);
	  		give_minus(id);



	  });
    $('.like').on('click', function(event){
      var user_id = $('#userl').text();
      var object_id = this.id;
      likedislike(user_id,object_id,1);
    });
    $('.dislike').on('click', function(event){
      var user_id = $('#userl').text();
      var object_id = this.id;
      likedislike(user_id,object_id,0);
    });


})
