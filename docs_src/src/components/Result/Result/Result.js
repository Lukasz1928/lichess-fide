import * as React from "react";
import './Result.css';
import queryString from 'query-string';

import LichessRatingsDisplay from "../Stats/Lichess/Ratings/LichessRatingsDisplay";
import EstimatedRatingsDisplay from "../Stats/Estimated/Ratings/EstimatedRatingsDisplay";
import calculate_missing_values from "../../../calculation/missing_values";
import calculate_fide_rating from "../../../calculation/fide";
import FideRatingDisplay from "../Stats/Fide/FideRatingDisplay";


class Result extends React.Component {
    constructor(props) {
        super(props);
        this.player_id = queryString.parse(this.props.location.search).id;
        this.state = {
            lichess: {
                bullet: [],
                blitz: [],
                rapid: [],
                classical: []
            },
            estimates: {
                bullet: null,
                blitz: null,
                rapid: null,
                classical: null
            },
            fide: null
        };
    }

    componentDidMount() {
        const url = `https://lichess.org/api/user/${this.player_id}`;
        fetch(url)
            .then(response => response.json())
            .then(data => {
                let bullet_rating = [data['perfs']['bullet']['rating'], data['perfs']['bullet']['rd']];
                let blitz_rating = [data['perfs']['blitz']['rating'], data['perfs']['blitz']['rd']];
                let rapid_rating = [data['perfs']['rapid']['rating'], data['perfs']['rapid']['rd']];
                let classical_rating = [data['perfs']['classical']['rating'], data['perfs']['classical']['rd']];
                let ratings = {
                    bullet: bullet_rating,
                    blitz: blitz_rating,
                    rapid: rapid_rating,
                    classical: classical_rating
                };
                let est = calculate_missing_values(ratings);
                let fide_rating = calculate_fide_rating(est);

                this.setState({
                    lichess: ratings,
                    estimates: est,
                    fide: fide_rating
                });

            });
    }

    render() {
        return (
            <div className="Result">
                <header className="Result-header">
                    <label id="Top-info-text">{this.player_id} profile analysis</label>
                    <LichessRatingsDisplay id="Lichess-display" ratings={this.state['lichess']}/>
                    <EstimatedRatingsDisplay id="Estimated-display" ratings={this.state['estimates']}/>
                    <FideRatingDisplay id="Fide-display" rating={this.state['fide']}/>
                </header>
            </div>
        );
    }
}

export default Result;