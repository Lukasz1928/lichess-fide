import * as React from "react";
import NameForm from "../NameForm/NameForm";
import '../../../index.css';
import About from "../About/About";


class Home extends React.Component {
    render() {
        return (
            <div className="App">
                <header className="App-header">
                    <About/>
                    <NameForm/>
                </header>
            </div>
        );
    }
}

export default Home;