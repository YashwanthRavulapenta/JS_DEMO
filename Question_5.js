function evaluateConditions(obj) {
    if (obj.age > 18 && obj.hasLicense) {
      return "Eligible to drive";
    }
  
    if (obj.temperature > 30 || obj.humidity > 70) {
      return "Warning: High discomfort level";
    }
  
    if ((obj.role === "admin" || obj.role === "editor") && obj.isActive) {
      return "Access granted";
    }
  
    if (!obj.isLoggedIn) {
      return "User not logged in";
    }
  
    if (obj.score >= 90 && obj.hasCertificate) {
      return "Qualified for advanced level";
    }
  
    if (obj.country === "India" || obj.country === "USA" || obj.country === "UK") {
      return "Allowed region";
    }
  
    if (!obj.isBanned && obj.accountAge > 1) {
      return "Account in good standing";
    }
  
    return "No specific condition met";
  }
  
  let user = {
    age: 20,
    hasLicense: true,
    temperature: 28,
    humidity: 60,
    role: "editor",
    isActive: true,
    isLoggedIn: true,
    score: 95,
    hasCertificate: true,
    country: "India",
    isBanned: false,
    accountAge: 2
  };
  
  console.log(evaluateConditions(user)); // Output: "Eligible to drive"
  console.log(evaluateConditions(user)); // Output: "User not logged in"
  console.log(evaluateConditions({ age: 25, hasLicense: true, temperature: 25, humidity: 50, role: "admin", isActive: true, isLoggedIn: true, score: 92, hasCertificate: true, country: "USA", isBanned: false, accountAge: 3 })); // Output: "Eligible to drive"
  console.log(evaluateConditions({ age: 30, hasLicense: true, temperature: 32, humidity: 75, role: "viewer", isActive: false, isLoggedIn: true, score: 88, hasCertificate: false, country: "UK", isBanned: false, accountAge: 2 })); // Output: "Warning: High discomfort level"
  console.log(evaluateConditions({ age: 22, hasLicense: true, temperature: 28, humidity: 60, role: "admin", isActive: true, isLoggedIn: true, score: 95, hasCertificate: true, country: "India", isBanned: false, accountAge: 2 })); // Output: "Eligible to drive"
  
  