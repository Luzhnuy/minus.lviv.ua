import React, { Component } from "react";
import ReactDOM from 'react-dom';
import Search from './react/messanger/component/search';
import UserList from './react/messanger/component/userList';

ReactDOM.render(
    <div className="row">
        <Search/>
        <UserList />
    </div>
    ,
    document.getElementById('userPanel')
);
