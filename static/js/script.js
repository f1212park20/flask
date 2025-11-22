document.addEventListener("DOMContentLoaded", function() {
    const button = document.getElementById("btn");
    const msg = document.getElementById("msg");

    button.addEventListener("click", function() {
        msg.textContent = "버튼이 클릭되었습니다!";
    });
});