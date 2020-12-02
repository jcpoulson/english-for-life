// Side Bar Functions
const toDoList = document.querySelector(".navbar-toggler")
const sideBar = document.querySelector("#mySidenav")
const student1 = document.querySelector(".student1")
const student2 = document.querySelector(".student2")
const student3 = document.querySelector(".student3")

toDoList.addEventListener("click", function() {
    sideBar.style.width = "250px";
    console.log("You Clicked the button")
})
  
  
  function closeNav() {
    document.getElementById("mySidenav").style.width = "0";
  }
