const getUserUrl = 'http://127.0.0.1:8000/user/get_user/555/';


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
    	fetch(getUserUrl).then(res => res.json()).then((result) => {
          		this.setState({
            	isLoaded: true,
            	items: result.items
          	});
         },
         (error) => {
         	 this.setState({
            	isLoaded: true,
            	error
         });
       }
     )
  }


	render(){

    	const { error, isLoaded, items } = this.state;
		console.log(this.state.items);	
		return (
			<div className="usershortprofile">
				<div className="avatar">
					<img src="/static/avatar_mini.jpg" alt="avatar"/>
				</div>
				<div className="userinfo">
					<p className="username">{items}</p>

				</div>

			</div>
		);	
	}
}





// ReactDOM.render(<UserShortProfile />,document.getElementById('users_and_rate'));
