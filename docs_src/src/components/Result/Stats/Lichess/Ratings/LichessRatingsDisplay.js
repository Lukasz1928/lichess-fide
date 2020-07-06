import * as React from "react";
import '../../../Result/Result.css';

import LichessRatingDisplay from "../Rating/LichessRatingDisplay";

class LichessRatingsDisplay extends React.Component {
    render() {
        let ratings = this.props.ratings;
        return (
            <div id="RatingDisplayContainer">
                Lichess.org stats:<br/>
                <LichessRatingDisplay variant="bullet" rating={ratings['bullet']}/>
                <LichessRatingDisplay variant="blitz" rating={ratings['blitz']}/>
                <LichessRatingDisplay variant="rapid" rating={ratings['rapid']}/>
                <LichessRatingDisplay variant="classical" rating={ratings['classical']}/>
            </div>
        );
    }
}

export default LichessRatingsDisplay;