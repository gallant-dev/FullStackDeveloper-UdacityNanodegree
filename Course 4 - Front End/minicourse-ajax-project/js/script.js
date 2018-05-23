
function loadData() {

    var $body = $('body');
    var $wikiElem = $('#wikipedia-links');
    var $nytHeaderElem = $('#nytimes-header');
    var $nytElem = $('#nytimes-articles');
    var $greeting = $('#greeting');

    // clear out old data before new request
    $wikiElem.text("");
    $nytElem.text("");

    // load streetview

    var streetStr = $('#street').val();
    var cityStr = $('#city').val();
    var address = streetStr + ', ' + cityStr;

    $greeting.text('So, you want to live at ' + address + '?');

    var streetViewURL = 'http://maps.googleapis.com/maps/api/streetview?size=600x400&location=' + address;

    $body.append('<img class="bgimg" src="'+ streetViewURL +  '">');

    // Load NYtimes articles

    var nYTimesURL = "https://api.nytimes.com/svc/search/v2/articlesearch.json";
    nYTimesURL += '?' + $.param({
      'api-key': "bc840b3ba5c14521a25db6fecec7f509",
      'q': cityStr
    });

    $.getJSON( nYTimesURL, function( data ) {
      //var items = [];

      $nytHeaderElem.text('New York Times Articles About' + cityStr);

      articles = data.response.docs;

      for(var i = 0; i < articles.length; i++) {
        var article = articles[i];
        $nytElem.append('<li class="article">'+'<a href="'+article.web_url+'">'+article.headline.main+'</a>'+
        '<p>'+article.snippet + '</p>' +
        '</li>');
      }

    }).fail(function(){
      $nytHeaderElem.text('No Articles could be loaded...')
    });

    //Load wikipedia
    var wikiURL = 'https://en.wikipedia.org/w/api.php?action=opensearch&format=json&callback=wikiCallback&search='+ cityStr;

    var wikiRequestTimeout = setTimeout(function(){
      $wikiElem.text("failed to get wikipedia resources");
    }, 8000);

    $.ajax({
      url : wikiURL,
      dataType : 'jsonp',
      success : function(response){
        var articleList = response[1];
        for (var i = 0; i < articleList.length; i++) {
          articleStr = articleList[i];
          var url = 'http://en.wikipedia.org/wiki/' + articleStr;
          $wikiElem.append('<li><a href="'+url+'">'+articleStr+'</a></li>')
        };

        clearTimeout(wikiRequestTimeout);
      }

    });


    return false;
};

$('#form-container').submit(loadData);
