var Cat = function (data){
  this.clickCount = ko.observable(data.clickCount);
  this.name = ko.observable(data.name);
  this.imgSrc = ko.observable(data.imgSrc);
  this.imgAttribution = ko.observable(data.imgAttribution);
  this.nickNames = ko.observableArray(data.nicknames);

  this.level = ko.computed(function(){
    if(this.clickCount() <= 19){
      return "Baby Cat";
    }
    else if (this.clickCount() > 19 && this.clickCount() <= 40)
    {
      return "Kitten Kid";
    }
    else if(this.clickCount() > 40) {
      return "Kitten God";
    }
  }, this);

}

var ViewModel = function() {

  this.currentCat = ko.observable(new Cat({
      clickCount: 0,
      name: 'Tabby',
      imgSrc: 'img/434164568_fea0ad4013_z.jpg',
      imgAttribution: 'https://wwww.flickr.com/photos/bigtallguy/434164568',
      nicknames: ['Kit Harrigton', 'Kat Dennings', 'Mew']
  }));

  this.incrementCounter = function(){
    this.clickCount(this.clickCount() + 1);
  };
}



ko.applyBindings(new ViewModel());
