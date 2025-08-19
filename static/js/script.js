$(document).ready(function () {
  $(".btn-danger").on("click", function (e) {
    e.preventDefault();
    const link = $(this).attr("href");
    $(this)
      .closest(".card")
      .fadeOut(300, function () {
        window.location.href = link;
      });
  });
});
document.addEventListener("DOMContentLoaded", () => {
  const congrats = document.getElementById("congrats-message");
  if (congrats) {
    var duration = 3 * 1000;
    var end = Date.now() + duration;

    (function frame() {
      confetti({
        particleCount: 5,
        angle: 60,
        spread: 55,
        origin: { x: 0 },
      });
      confetti({
        particleCount: 5,
        angle: 120,
        spread: 55,
        origin: { x: 1 },
      });

      if (Date.now() < end) {
        requestAnimationFrame(frame);
      }
    })();
  }
});
