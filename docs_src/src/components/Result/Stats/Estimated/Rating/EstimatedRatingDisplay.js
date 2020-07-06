import React from "react";
import './EstimatedRatingDisplay.css';

class EstimatedRatingDisplay extends React.Component {
    render() {
        return (
            <div className="Rating-display">
                <label>Variant: {this.props.variant}</label><br/>
                <label>Estimated rating: {this.props.rating}</label><br/>
            </div>
        )
    }
}

export default EstimatedRatingDisplay;