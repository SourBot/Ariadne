  $(document).ready(function () {
    $(".thingOne").css("background-color", "red");
    function update() {
      var date = new Date();
      var hours = date.getHours() == 0
                    ? 12
                    : date.getHours() > 12
                      ? date.getHours() - 12
                      : date.getHours();
      var minutes = date.getMinutes() < 10 ? "0" + date.getMinutes() : date.getMinutes();
      var seconds = date.getSeconds() < 10 ? "0" + date.getSeconds() : date.getSeconds();


      $("#hours").text(hours);
      $("#minutes").text(minutes);
      $("#seconds").text(seconds);
    }
    window.setInterval(update, 1000);
  });
