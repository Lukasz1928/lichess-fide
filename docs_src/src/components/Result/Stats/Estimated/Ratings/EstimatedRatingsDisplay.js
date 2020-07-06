import * as React from "react";
import EstimatedRatingDisplay from "../Rating/EstimatedRatingDisplay";


class EstimatedRatingsDisplay extends React.Component {
    render() {
        let ratings = this.props.ratings;
        return (
            <div id="RatingDisplayContainer">
                Estimated stats:<br/>
                <EstimatedRatingDisplay variant="bullet" rating={ratings['bullet']}/>
                <EstimatedRatingDisplay variant="blitz" rating={ratings['blitz']}/>
                <EstimatedRatingDisplay variant="rapid" rating={ratings['rapid']}/>
                <EstimatedRatingDisplay variant="classical" rating={ratings['classical']}/>
            </div>
        );
    }
}

export default EstimatedRatingsDisplay;