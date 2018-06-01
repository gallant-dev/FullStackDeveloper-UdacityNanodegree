var model = {
  currentCat: 0,
  cats: [{
      name: 'Grumpy Cat',
      clicks: 0
    },{
      name: 'Fat Cat',
      clicks: 0
    },{
      name: 'Ugly Kitten',
      clicks: 0
    },{
      name: 'Warrior Cat',
      clicks: 0
    },{
      name: 'Polite Kitty',
      clicks: 0
    },{
      name: 'Two-Face Cat',
      clicks: 0
    }]
}

var controller = {
  init: function() {
    catListView.init();
    catView.init();
    adminView.init();
  },

  getCurrentCat: function(){
    return model.currentCat;
  },

  setCurrentCat: function(cat){
    model.currentCat = cat;
  },

  updateCat: function(name, click){
    var nameValue = name.value;
    var clickValue = click.value;
    model.cats[model.currentCat].name = nameValue;
    model.cats[model.currentCat].clicks = clickValue;

    catListView.render();
    catView.render();
  },

  incrementCounter: function(){
    model.cats[model.currentCat].clicks++;
    catView.render();
  }
}

var adminView = {
  init: function() {
    var adminButton = document.createElement('button');
    var adminDisplay = document.getElementById('admin-section');
    adminButton.id = "admin-button";
    adminButton.innerHTML = "Admin";
    adminDisplay.appendChild(adminButton);

    var adminForm = document.createElement('form');
    adminForm.id = "admin-form";

    var nameLabel = document.createElement('label');
    nameLabel.innerHTML = "Name: "
    var nameInput = document.createElement('input');
    nameInput.id = "name-input";
    adminForm.appendChild(nameLabel);
    adminForm.appendChild(nameInput);

    var clickLabel = document.createElement('label');
    clickLabel.innerHTML = "Clicks: ";
    var clickInput = document.createElement('input');
    clickInput.id = "click-input";
    clickInput.placeholder = model.cats[model.currentCat].clicks;
    adminForm.appendChild(clickLabel);
    adminForm.appendChild(clickInput);

    var saveButton = document.createElement('button');
    saveButton.id = "save-button";
    saveButton.type = "button";
    saveButton.innerHTML = "Save";
    saveButton.addEventListener('click', function(){
      if(nameInput.value != null || clickInput.value != null){
        controller.updateCat(nameInput, clickInput);
      }
      else {
        alert("Please enter a new name or click value!");
      }
    });
    adminForm.appendChild(saveButton);

    var cancelButton = document.createElement('button');
    cancelButton.id = "cancel-button";
    cancelButton.innerHTML = "Cancel";
    adminForm.appendChild(cancelButton);

    adminForm.style.display = "none";
    adminDisplay.appendChild(adminForm);


    adminButton.addEventListener('click', function(){
      if (adminForm.style.display == "none"){
        adminForm.style.display = "block";
      }
      else {
        adminForm.style.display = "none";
      }
    });

    this.render();
  },

  render: function() {
      var nameInput = document.getElementById('name-input');
      var clickInput = document.getElementById('click-input');
      nameInput.placeholder = model.cats[model.currentCat].name;
      clickInput.placeholder = model.cats[model.currentCat].clicks;
  }
}

var catView = {
  init: function() {
    var catDisplay = document.getElementById('cat-display');
    var catImage = document.createElement('img');
    catImage.classList.add('pic');
    catImage.id = 'cat-image';

    var clickElem = document.createElement('div');
    clickElem.classList.add('cat-clicks');
    var clickText = document.createElement('text');
    clickText.id = 'click-text';
    clickText.textContent = "Click A Cat!";
    clickElem.appendChild(clickText);
    catDisplay.appendChild(clickElem);
    catDisplay.appendChild(catImage);

    this.render();

    catImage.addEventListener('click', function(){
      controller.incrementCounter();

    });
  },

  render: function() {
    var clickText = document.getElementById('click-text');
    var catImage = document.getElementById('cat-image');
    if(model.cats[model.currentCat].clicks > 0){
      document.getElementById('click-text').textContent = model.cats[model.currentCat].clicks;
    }
    else {
      document.getElementById('click-text').textContent = "Click A Cat!";
    }
    catImage.src = 'cat'+model.currentCat+'.jpg';
  }
}

var catListView = {
  init: function() {
    this.render();
  },

  render: function() {
    var catList = document.getElementById('cat-list');

    catList.innerHTML = '';

    for (var i = 0; i < model.cats.length; i++) {
      var catName = model.cats[i].name;
      var catNum = i;

      var nameElem = document.createElement('div');
      nameElem.classList.add('menu-item');
      nameElem.id = 'menu-item-' + i;

      var nameText = document.createElement('text');
      nameText.classList.add('name-text');
      nameElem.appendChild(nameText);

      nameText.textContent = catName;

      nameElem.addEventListener('click', (function(catCopy) {
          return function() {
              document.getElementById('menu-item-'+model.currentCat).style.backgroundColor = 'orange';
              document.getElementById('cat-image').src = "cat"+ catCopy + ".jpg";
              document.getElementById('menu-item-'+catCopy).style.backgroundColor = 'red';

              model.currentCat = catCopy;
              catView.render();
              adminView.render();
          };
      })(catNum));

      catList.appendChild(nameElem);
    }
  }
}

controller.init();
