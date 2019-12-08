import React, { Component } from "react";

class UserList extends React.Component {
    constructor(props) {
        super(props);
        this.state = { selected: false, newMessage: false, userMessage: {} };
    }

    render() {
        return (
            <ul className="user-list col s12 " id="userList">

            </ul>
        )

    }
}

export default UserList;