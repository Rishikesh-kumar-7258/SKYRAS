// some variables
let visibleFormNumber = 1;
const insideBar = document.querySelector(".inside");
const buttons = document.querySelectorAll("button")

//preventing forms from getting submitted
// document.querySelectorAll("form").forEach((e) => {
//   e.addEventListener("submit", (t) => {
//     t.preventDefault();
//   });
// });

// clicking on first button
console.log(buttons);
buttons.forEach((e,i) => {

  e.addEventListener("click", function() {
    if (i&1 === 0) {
      visibleFormNumber++;
    }
    else{
      visibleFormNumber--;
    }
  })

  showForm(visibleFormNumber);
})

// onclicking the circle
document.querySelectorAll(".circle").forEach((e, i) => {
  e.onclick = function () {
    // not allowing to click on uncompleted circle
    if (i + 1 > visibleFormNumber) {
      return;
    }

    // Going to the clicked form section
    visibleFormNumber = i + 1;
    showForm(visibleFormNumber);
  };
});


// clicking on the submit button

// function to show only the selected form
function showForm(number) {
  // checking for in range form count
  if (number < 1 || number > 3) {
    return;
  }

  // for green line grow
  if (number === 1) {
    insideBar.style.width = "0%";
  } else if (number === 2) {
    insideBar.style.width = "48%";
  } else {
    insideBar.style.width = "95%";
  }

  // making the circles green
  document.querySelectorAll(".circle").forEach((e, i) => {
    if (i + 1 < number) {
      e.classList.add("completed-circle");
    } else {
      e.classList.remove("completed-circle");
    }
  });

  // making all forms invisible
  document.querySelectorAll("form").forEach((e, i) => {
    if (i + 1 === number) {
      e.classList.remove("d-none");
    } else {
      e.classList.add("d-none");
    }
  });
}
