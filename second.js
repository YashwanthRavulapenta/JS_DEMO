
function processObjectsDelayed(arr, delay) {
    arr.forEach(obj => {
      setTimeout(() => {
        obj.process();
      }, delay);
    });
  }
  const items = [
    { name: "Alpha", process: function() { console.log(Processing: ${this.name}); } },
    { name: "Beta", process: function() { console.log(Task for ${this.name} done.); } },
    { name: "Gamma", process: function() { console.log(Task for ${this.name} done.); } }
  ];
  
  processObjectsDelayed(items, 1000); // Waits 1 second, then processes Alpha and Beta