var amountScrolled = 300;

$(window).scroll(function() {
    if ( $(window).scrollTop() > amountScrolled ) {
        $('a.back-to-top').fadeIn('slow');
    } else {
        $('a.back-to-top').fadeOut('slow');
    }
});

$('a.back-to-top').click(function() {
    $('html, body').animate({
        scrollTop: 0
    }, 700);
    return false;
});

$(function() {
  menu();
})


function menu() {
  const $window = $(window),
    $menu = $('.menu'),
    $button = $menu.find('.menu_button'),
    $menuContent = $menu.find('.menu_content');

  $window.on('scroll', onScroll);
  $button.on('click', toggleMenu);

  function onScroll() {
    $menu.toggleClass('shrink', $window.scrollTop() > 0);
  }

  function toggleMenu() {
    $menuContent.toggleClass('show');
  }
}
