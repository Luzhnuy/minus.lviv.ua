import React, { Component } from "react";

class Search extends React.Component {
    constructor(props) {
        super(props);
        this.state  = {searchText: ""};
        this.onChange = this.onChange.bind(this);
    }

    onChange(e) {
        let value = e.target.value;
        this.setState({searchText: value});
        console.log(this.state.searchText);
    }

    render () {
        return (
                <div className="input-field col s12">
                    <i className="material-icons prefix">search</i>
                    <input id="search" type="text" onChange={this.onChange} value={this.state.searchText} name="search" className="validate" />
                    <label className="active" htmlFor="search">Пошук користувача</label>
                </div>
        )
    }
}

export default Search;