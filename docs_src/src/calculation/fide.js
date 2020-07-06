import * as regression from '../resources/regression';

function calculate_fide_rating(stats) {
    let coefs = regression['coefs'];
    let coefs_order = regression['coefs_order'];
    let fide = regression['intercept'];
    coefs.forEach((c, i) => {
        fide += c * stats[coefs_order[i]];
    });
    return fide.toFixed();
}

export default calculate_fide_rating;