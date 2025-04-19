function formatCurrency(amount, currencyCode) {
    // Map currency codes to their respective locales
    const currencyLocales = {
      USD: 'en-US',    // United States
      INR: 'en-IN',    // India
      EUR: 'de-DE',    // Germany
      GBP: 'en-GB',    // United Kingdom
      JPY: 'ja-JP',    // Japan
      AUD: 'en-AU',    // Australia
      CAD: 'en-CA'     // Canada
    };
  
    // Fallback to 'en-US' if currency code not mapped
    const locale = currencyLocales[currencyCode] || 'en-US';
  
    return new Intl.NumberFormat(locale, {
      style: 'currency',
      currency: currencyCode,
      minimumFractionDigits: 2,
      maximumFractionDigits: 2
    }).format(amount);
}
    console.log(formatCurrency(15000987.5, 'USD'));
    console.log(formatCurrency(15000987.5, 'INR'));
    console.log(formatCurrency(15000987.5, 'EUR'));
    console.log(formatCurrency(15000987.5, 'JPY'));
    console.log(formatCurrency(15000987.5, 'GBP'));
    console.log(formatCurrency(15000987.5, 'AUD'));
    console.log(formatCurrency(15000987.5, 'CAD')); 
    