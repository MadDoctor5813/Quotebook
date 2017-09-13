var nouns = [
    "app",
    "fish",
    "charity",
    "hat",
    "pair of glasses",
    "vegetable patch",
    "drug",
    "school",
    "snack",
    "book",
    "secret society",
    "television",
    "group of friends",
    "break room",
    "subcommittee on national parks",
    "pope",
    "wig",
    "coffee maker",
    "toaster",
    "floor joist",
    "left pinky toe"
]

var actions = [
    "turns lead into gold",
    "ends world hunger",
    "parallel parks",
    "cures diabetes",
    "solves the square root of 2",
    "knows what The Rock is cooking",
    "juggles chainsaws",
    "makes people believe God is real",
    "makes people believe God isn't real",
    "makes people believe this whole God thing isn't that important",
    "fixes the elevator",
    "tells you if your fly's down",
    "disarms North Korea",
    "builds the wall",
    "charges your iPhone",
    "does the dishes",
    "makes America great again",
    "cooks dinner",
    "ruins dinner",
    "never forgets"
]

function choose(choices) {
    var index = Math.floor(Math.random() * choices.length);
    return choices[index];
}

var noun_text;
var action_text;

function generate_idea() {
    noun_text.text(choose(nouns));
    action_text.text(choose(actions));
}

$(document).ready(function() {
    noun_text = $("#idea-noun");
    action_text = $("#idea-action");
    generate_idea(noun_text, action_text)
});
