const displayIcon = document.querySelector('#display-icon');
const go = document.querySelector('#go');
const playAgain = document.querySelector('#play-again');
const choiceDisplay = document.querySelectorAll('.choice-display');
const resultIcon = document.querySelectorAll('.result-icon');
const playerChoiceBtn = document.querySelectorAll('.player-choice-btn');
const comChoiceBtn = document.querySelectorAll('.com-choice-btn');
var playerChoice;
var gameObject = [
    { index: 0, name: 'Rock', damage: 'crushes', class: 'fa-hand-rock' },
    { index: 1, name: 'Paper', damage: 'covers', class: 'fa-hand-paper' },
    { index: 2, name: 'Scissors', damage: 'cuts', class: 'fa-hand-scissors' }
];

// random computer choice
function comChoice() {
    var randomNum = Math.floor(Math.random() * 3);
    var randomChoice = gameObject[randomNum];
    return randomChoice;
}

// radio button functionality
playerChoiceBtn.forEach(function (choice, index) {
    choice.addEventListener('click', function () {
        playerChoice = index;
        for (let i = 0; i < playerChoiceBtn.length; i++) {
            if (playerChoiceBtn[i] == choice) {
                choice.classList.remove('btn-outline-secondary');
                choice.classList.add('btn-success');
                choiceDisplay[0].textContent = `Player chooses ${gameObject[playerChoice].name}.`;
                go.disabled = false;
                resultIcon.forEach(function (icon) {
                    icon.hidden = true;
                    icon.classList.add('fa-thumbs-up');
                    icon.classList.remove('fa-hand-rock');
                    icon.classList.remove('fa-hand-paper');
                    icon.classList.remove('fa-hand-scissors');
                });
                displayIcon.hidden = false;
                choiceDisplay[1].textContent = 'Ready?';
                comChoiceBtn.forEach(function (button) {
                    button.classList.remove('btn-success');
                    button.classList.add('btn-outline-secondary');
                });
            } else {
                playerChoiceBtn[i].classList.remove('btn-success');
                playerChoiceBtn[i].classList.add('btn-outline-secondary');
            }
        }
    });
});

function setIntervalX(callback, delay, repetitions) {
    var x = 0;
    var intervalID = window.setInterval(function () {
        callback();

        if (++x === repetitions) {
            window.clearInterval(intervalID);
        }
    }, delay);
}

go.addEventListener('click', () => {
    var comSelection = comChoice();
    var playerSelection = gameObject[playerChoice];
    // console.log(playerSelection.name);
    // console.log(comSelection.name);
    go.disabled = true;
    displayIcon.hidden = false;
    resultIcon.forEach(function (icon) {
        icon.hidden = true;
        icon.classList.add('fa-thumbs-up');
        icon.classList.remove('fa-hand-rock');
        icon.classList.remove('fa-hand-paper');
        icon.classList.remove('fa-hand-scissors');
    });
    playerChoiceBtn.forEach(function (button) {
        button.disabled = true;
    });
    choiceDisplay[1].textContent = '1, 2, 3...';

    let i = 0;
    setIntervalX(
        function () {
            displayIcon.classList.toggle('animate__bounce');
            i++;

            // cycle the btn-success class over the com choice buttons
            setIntervalX(
                function () {
                    comChoiceBtn.forEach(function (choice) {
                        if (comChoiceBtn[(i - 1) % 3] == choice) {
                            choice.classList.remove('btn-outline-secondary');
                            choice.classList.add('btn-success');
                        } else if (i == 8) {
                            comChoiceBtn.forEach(function (button) {
                                if (
                                    comChoiceBtn[comSelection.index] == button
                                ) {
                                    button.classList.add('btn-success');
                                    button.classList.remove(
                                        'btn-outline-secondary'
                                    );
                                } else {
                                    button.classList.remove('btn-success');
                                    button.classList.add(
                                        'btn-outline-secondary'
                                    );
                                }
                            });
                        } else {
                            for (let j = 0; j < comChoiceBtn.length; j++) {
                                if ((i - 1) % 3 != j) {
                                    comChoiceBtn[j].classList.add(
                                        'btn-outline-secondary'
                                    );
                                    comChoiceBtn[j].classList.remove(
                                        'btn-success'
                                    );
                                }
                            }
                        }
                    });
                },
                200,
                3
            );

            // console.log(i);
            // do stuff on specific interval iterations
            if (i === 2) {
                choiceDisplay[1].textContent = 'Rock!';
                displayIcon.classList.remove('fa-thumbs-up');
                displayIcon.classList.add('fa-hand-rock');
            } else if (i === 4) {
                choiceDisplay[1].textContent = 'Paper!';
                displayIcon.classList.remove('fa-hand-rock');
                displayIcon.classList.add('fa-hand-paper');
            } else if (i === 6) {
                choiceDisplay[1].textContent = 'Scissors!';
                displayIcon.classList.remove('fa-hand-paper');
                displayIcon.classList.add('fa-hand-scissors');
            } else if (i === 8) {
                choiceDisplay[2].textContent = `Computer chooses ${comSelection.name}.`;

                // game logic
                if (playerSelection.name === comSelection.name) {
                    choiceDisplay[1].textContent = "It's a Draw";
                } else if (playerSelection.name === 'Rock') {
                    // console.log('you rock');
                    if (comSelection.name === 'Paper') {
                        choiceDisplay[1].textContent =
                            'Computer Wins: Paper covers Rock.';
                    } else if (comSelection.name === 'Scissors') {
                        choiceDisplay[1].textContent =
                            'Player Wins: Rock crushes Scissors.';
                    }
                } else if (playerSelection.name === 'Paper') {
                    if (comSelection.name === 'Scissors') {
                        choiceDisplay[1].textContent =
                            'Computer Wins: Scissors cuts Paper.';
                    } else if (comSelection.name === 'Rock') {
                        choiceDisplay[1].textContent =
                            'Player Wins: Paper covers Rock.';
                    }
                } else if (playerSelection.name === 'Scissors') {
                    if (comSelection.name === 'Rock') {
                        choiceDisplay[1].textContent =
                            'Computer Wins: Rock crushes Scissors.';
                    } else if (comSelection.name === 'Paper') {
                        choiceDisplay[1].textContent =
                            'Player Wins: Scissors cuts Paper.';
                    }
                }

                // result
                go.hidden = true;
                playAgain.hidden = false;
                displayIcon.classList.remove('fa-hand-scissors');
                displayIcon.classList.add('fa-thumbs-up');
                displayIcon.hidden = true;
                resultIcon[0].classList.remove('fa-thumbs-up');
                if (playerChoice === 0) {
                    resultIcon[0].classList.add('fa-hand-rock');
                } else if (playerChoice === 1) {
                    resultIcon[0].classList.add('fa-hand-paper');
                } else if (playerChoice === 2) {
                    resultIcon[0].classList.add('fa-hand-scissors');
                }
                resultIcon[0].hidden = false;
                resultIcon[1].classList.remove('fa-thumbs-up');
                resultIcon[1].classList.add(comSelection.class);
                resultIcon[1].hidden = false;
            }
        },
        600,
        8
    );
});

// reset after a play
playAgain.addEventListener('click', function () {
    playerChoiceBtn.forEach(function (button) {
        button.classList.remove('btn-success');
        button.classList.add('btn-outline-secondary');
        button.disabled = false;
    });
    comChoiceBtn.forEach(function (button) {
        button.classList.remove('btn-success');
        button.classList.add('btn-outline-secondary');
    });
    choiceDisplay[0].textContent = `Make your choice.`;
    choiceDisplay[2].textContent = `Computer chooses randomly.`;
    playAgain.hidden = true;
    go.hidden = false;
});
