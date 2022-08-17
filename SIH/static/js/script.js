const fontChangerBtns = document.querySelectorAll("#fontChanger button");
fontChangerBtns[0].onclick = decreaseFont;

function decreaseFont() {
  // currentFontSize += currentFontSize * 0.2;
  document.querySelector("body").style.fontSize = "20%";
}
