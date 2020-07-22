var active = 'scd'

function getArticles(id) {
  $.get( "news/" + id, function( data ) {
    $('#articles').empty()
    toAdd = '<ul>';
    for (var i = 0; i < Math.min(data.length, 12); i++) {
      toAdd += '<a href="' + data[i] +'" class="embedly-card"></a>'
    }
    toAdd += '</ul>';
    $('#articles').append(toAdd);
    $('#' + active).removeClass("active");
    $('#' + id).addClass("active");
    active = id;
  });
}


$(function() {
  getArticles('scd');
});
