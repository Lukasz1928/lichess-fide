import React from "react";
import './LichessRatingDisplay.css';

class LichessRatingDisplay extends React.Component {
    render() {
        return (
            <div className="Rating-display">
                <label>Variant: {this.props.variant}</label><br/>
                <label>Rating: {this.props.rating[0]}</label><br/>
                <label>Rating deviation: {this.props.rating[1]}</label>
            </div>
        )
    }
}

export default LichessRatingDisplay;