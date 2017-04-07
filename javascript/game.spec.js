const Game = require('./game.js').Game;
const assert = require('assert')
const _ = require('lodash')

describe("AskQuestion", function() {
    const expectedPlaceCategoryMapping = {
        0 : "Pop",
        1 : "Science",
        2 : "Sports",
        3 : "Rock",
        4 : "Culture",
        5 : "History",
        6 : "Pop",
        7 : "Science",
        8 : "Sports",
        9 : "Rock",
        10: "Culture",
        11: "History",
        12: "Pop",
        13: "Science",
        14: "Sports",
        15: "Rock",
        16: "Culture",
        17: "History",
    };
    _.forEach(expectedPlaceCategoryMapping, function (category, place) {
       it("provides the correct category", () => {
           assert.equal(Game.askQuestion(), category)
       })
    })
  it("provides the correct category", function() {
    expect(true).toBe(true);
  });

  it("should access game", function() {
    expect(Game).toBeDefined();
  });
});

describe("Your specs...", function() {
  // it ...
});
