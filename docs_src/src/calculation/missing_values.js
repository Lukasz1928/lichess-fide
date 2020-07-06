import ratingDiffs from '../resources/ranking-differences.json';


function calculate_missing_values(stats) {
    console.log(ratingDiffs);
    let variants = ['bullet', 'blitz', 'rapid', 'classical'];
    let established_threshold = 90;
    var filled_ratings = {};
    variants.forEach(v => {filled_ratings[v] = 1500;});
    let established = variants.filter(v => stats[v][1] <= established_threshold);
    if(established.length === 0) {
        return filled_ratings;
    }
    established.forEach(v => {filled_ratings[v] = stats[v][0];});
    let provisional = variants.filter(v => stats[v][1] > established_threshold);
    provisional.forEach(prov => {
        let expecteds = [];
        established.forEach(est => {
            const ex = stats[est][0] + ratingDiffs[est][prov];
            expecteds.push(ex);
        });
        filled_ratings[prov] = expecteds.reduce((a, b) => a + b, 0) / expecteds.length;
    });
    variants.forEach(v => {
       filled_ratings[v] = filled_ratings[v].toFixed(0);
    });
    return filled_ratings;
}

export default calculate_missing_values;