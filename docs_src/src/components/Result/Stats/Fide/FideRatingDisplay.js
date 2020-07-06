import * as React from "react";


class FideRatingDisplay extends React.Component {
    render() {
        let rating = this.props.rating;
        return (
            <div id="RatingDisplayContainer">
                Estimated FIDE rating:<br/>
                <label>{rating}</label>
            </div>
        );
    }
}

export default FideRatingDisplay;