// Solusi 1
// function spinWords(string){
//     let strArr = string.split(" ");
//     let newArr = [];
//     strArr.forEach((word) => word.length >= 5 ? newArr.push(word.split("").reverse("").join("")) : newArr.push(word))
//     return newArr.join(" ");
// };

// function spinWords(string){
//     return string.split(" ").map((word) => word.length >= 5 ? word.split("").reverse("").join("") : word);
// };

// solusi one liner
const spinWords = (string) => string.split(" ").map((word) => word.length >= 5 ? word.split("").reverse("").join("") : word).join(" ");


console.log(
    spinWords("nama saya adalah daffa marchbhi febhiakbar")
);
// function spinWords (string) {
//     let newArr = [];
//     newArr = string.split(" ").map((word) =>  {
//         if(word.length >= 5){
//             word.split("").reverse("").join("")
//         }else{
//             word
//         }
//     })
//     return newArr;
// };
