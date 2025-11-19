const mypromise = new Promise((resolve, reject) => {
	  setTimeout(()=> {
		  console.log('javascript is awesome with promises');
		  resolve('promise  fullfilled successfully');
	  }, 10);
});
mypromise.then(res => {
	console.log(res);
}).catch(err => {
	console.log(err);
});
