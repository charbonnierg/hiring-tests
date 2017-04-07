"use strict"

const Game = require('./game.js').Game;
const assert = require('chai').assert;
const _ = require('lodash')

describe("AskQuestion", function() {
    const expectedPlaceCategoryMapping = {
        0 : "Pop",
        1 : "Science",
        2 : "Sports",
        3 : "Rock",
        4 : "Pop",
        5 : "Science",
        6 : "Sports",
        7 : "Rock",
        8 : "Pop",
        9 : "Science",
        10: "Sports",
        11: "Rock",
    };
    _.forEach(expectedPlaceCategoryMapping, function (category, place) {
       it("provides the correct category", () => {

           let game = new Game();
           game.places[0] = place;
           assert.include(game._askQuestion(), category);
       })
    })
});
