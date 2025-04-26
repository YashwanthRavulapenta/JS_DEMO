// Helper function to check if a string is a palindrome
function isPalindrome(s) {
    return s === s.split('').reverse().join('');
  }
  
  // Main function to find the longest palindromic substring
  function findLongestPalindrome(str) {
    let maxLength = 0;
    let longest = "";
  
    // Check every possible substring
    for (let i = 0; i < str.length; i++) {
      for (let j = i + 1; j <= str.length; j++) {
        const substring = str.substring(i, j);
  
        if (isPalindrome(substring) && substring.length > maxLength) {
          maxLength = substring.length;
          longest = substring;
        }
      }
    }
  
    return longest;
  }
let input = "yashwannnawhs";
let result = findLongestPalindrome(input);
console.log("Input: " + input);
console.log("Longest Palindromic Substring: " + result);