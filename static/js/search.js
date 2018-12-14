function usersearch(search){
  $.ajax({
    url:'http://127.0.0.1:8000/user/search/',
		method:'GET',
    data: search,
		dataType: 'JSON',
		success:function(users){
			   console.log(users);
         console.log(users.length);
         $(".list").empty();
         for(var i = 0;i<=users.length-1;i++ ){
           $('.list').append("<div><p><a href='http://127.0.0.1:8000/minusstore/minus/"+minus[i].pk +"/' style='color:black;text-decoration: underline;'>"+minus[i].fields.title+"</a></p><audio src='/static/minus.mp3' controls controlsList='nodownload'></audio><p>(Аудіо) "+Number(minus[i].fields.filesize/1000000)+" мб "+ minus[i].fields.bitrate+"Кбіт/с  </p></div>");

         }
		}
  });
}





jQuery(document).ready(function(){
  $('.validate .user_search').keyup(function(){
    var search = $('.user_search').text();
    console.log(search)
    usersearch(search);

  });

})
