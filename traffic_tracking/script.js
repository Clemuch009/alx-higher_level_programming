// Track visits
function trackVisit() {
    let visits = localStorage.getItem('visits');
    visits = visits ? parseInt(visits) + 1 : 1;
    localStorage.setItem('visits', visits);
    console.log(`This device has visited ${visits} times`);
}

trackVisit();

// Simple signup mock
function signup() {
    alert("Thanks for signing up! We'll contact you soon.");
    // You can later push this to backend or email capture
}

