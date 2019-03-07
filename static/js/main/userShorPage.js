
class UserShortProfile extends React.Component {
	constructor(props) {
    	super(props);
    	this.state = {
      		error: null,
     	 	isLoaded: false,
     	 	items: []
    	};
    
  	}
  

  

	componentDidMount() {
    	fetch('http://127.0.0.1:8000/user/get_user/'+this.props.userId[0].textContent + '/').then(res => res.json()).then((result) => {


          		this.setState({
            	isLoaded: true,
            	items: result
          	});
         },
         (error) => {
         	 this.setState({
            	isLoaded: true,
            	error,
         });
       }
     )
  }


	render(){

    	// const { error, isLoaded, items } = this.state;
		  return (
			 <div className="usershortprofile" style={{width:'100%'}}>
					<div className="avatar" style={{float:'left',marginRight:'10%'}}>
					   <img src="/static/avatar_mini.jpg" alt="avatar"/>
				  </div>
				<div className="userinfo" style={{float:'left',}}>
					   <p className="username">{this.state.items.username}</p>
             <p className="first_name">{this.state.items.first_name}  </p>
              <p className="last_name">{this.state.items.last_name}</p>

				  </div>

			 </div>
		);	
	}
}


function getUserShortPage(){
      let position = this.getBoundingClientRect();
      let positionLeftX = position.x;
      let positionTopY = position.y;
			let div = document.createElement('div');
			div.style.width = '100%';
			this.style.display = 'block';
			// div.style.display = "block";
      div.id= "user_short_page";
      this.appendChild(div);
      let user_id = this.getElementsByTagName('span');
      ReactDOM.render(<UserShortProfile userId={user_id} />,document.getElementById('user_short_page'));

      

}

function removeUserShortPage(){
    let div = document.getElementById('user_short_page');
    div.parentNode.removeChild(div);
}




var users = document.getElementsByClassName('user');
// var users_online = document.getElementsByClassName('user_online');
for(let i = 0;i<users.length;i++){
  console.log("event");
  users[i].addEventListener("mouseover",getUserShortPage,true);
  users[i].addEventListener("mouseout",removeUserShortPage,true);
}   

// for(let i = 0;i<users_online.length;i++){
//   console.log("event");
//   users_online[i].addEventListener("mouseover",getUserShortPage,true);
//   users_online[i].addEventListener("mouseout",removeUserShortPage,true);
// }   




