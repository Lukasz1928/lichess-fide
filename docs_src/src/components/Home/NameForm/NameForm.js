import React from 'react';
import {withRouter} from "react-router";
import './NameForm.css';

class NameForm extends React.Component {
    constructor(props) {
        super(props);
        this.state = {id: ''};
        this.handleChange = this.handleChange.bind(this);
        this.handleSubmit = this.handleSubmit.bind(this);
    }

    handleChange(event) {
        this.setState({id: event.target.value});
    }

    handleSubmit(event) {
        this.props.history.push(`/result?id=${this.state.id}`);
    }

    render() {
        return (
            <form onSubmit={this.handleSubmit} className="App-form">
                <label>
                    Enter your lichess.org username below to check it out:<br/>
                    <input type="text" value={this.state.id} onChange={this.handleChange} />
                </label><br/>
                <input type="submit" value="Analyze!" />
            </form>
        );
    }
}

export default withRouter(NameForm);