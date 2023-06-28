let classique = 19000 /// nombre à changer en fonction du dernier chronout utilisé dans la plage classique

let randomNumber = Math.floor(Math.random() * 100) + 1;

let guesses = document.querySelector('.guesses');
let lastResult = document.querySelector('.lastResult');
let lowOrHi = document.querySelector('.lowOrHi');

let guessSubmit = document.querySelector('.guessSubmit');
let guessField = document.querySelector('.guessField');

let guessCount = 1;
let resetButton;
let message = "Voila le chiffre voulu "+randomNumber

function donation(){
    randomNumber++;
    /// voila la première idée d'incrémentation pour donner les chronoout
   message="Voila le chiffre voulu "+randomNumber;
    confirm(message);

}

// parce que il faut penser à une fausse manip et nous devant revenir en arrière
function retour(){
    randomNumber--;
     /// voila la première idée d'incrémentation pour les chronoout 
    message="Voila le chiffre voulu "+randomNumber;
    prompt(message)
}

function ecriture(){
    const fs = require('fs');

    const contenu = 'Contenu à écrire dans le fichier.';
    const cheminFichier = 'desincarne.txt';

    fs.writeFile(cheminFichier, contenu, (erreur) => {
  if (erreur) {
    console.error('Une erreur s\'est produite :', erreur);
  } else {
    console.log('Le fichier a été écrit avec succès !');
  }
});

}