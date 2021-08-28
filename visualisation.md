# <img border="0" src="/czarnewski/logos/data_wizard.png" width="40" height="40" style="vertical-align:middle;"> Visualisation

***

<br/>

One of my big interests is data visualisation. Great par of my work as a bioinformatician and as a teacher in advanced course is about turning data and numbers into graphically meaningful results!

I am currently working on this page, please come back later.


<div id="circle-orbit-container">
  <div id="middle-orbit">
    <img class="orbit1 rotate" src="/czarnewski/logos/data_wizard/plot1.png" width="80" height="80">
    <img class="orbit2 rotate" src="/czarnewski/logos/data_wizard/plot2.png" width="80" height="80">
    <img class="orbit3 rotate" src="/czarnewski/logos/data_wizard/plot3.png" width="80" height="80">
    <img class="orbit4 rotate" src="/czarnewski/logos/data_wizard/plot4.png" width="80" height="80">
    <img class="orbit5" src="/czarnewski/logos/data_wizard/plot5.png" width="80" height="80">
  </div>
<img class="wiz" src="/czarnewski/logos/data_wizard/wizard.png" width="180" height="160">
</div>





<style>

.wiz {
  position: absolute;
  top: 210px;
  left: 70px;
}

.orbit1 {
  position: absolute;
  top: 60px;
  left: 160px;
  height: 80px;
  width: 80px;
  /* border-radius: 100%;
  background-color: blue; */
  /* background-color: #4A437F; */
}
.orbit2 {
  position: absolute;
  top: 160px;
  left: 60px;
  height: 80px;
  width: 80px;
  /* border-radius: 100%;
  background-color: green; */
  /* background-color: #4A437F; */
}

.orbit3 {
  position: absolute;
  top: -40px;
  left: 60px;
  height: 80px;
  width: 80px;
  /* border-radius: 100%;
  background-color: red; */
  /* background-color: #4A437F; */
}
.orbit4 {
  position: absolute;
  top: 60px;
  left: -40px;
  height: 80px;
  width: 80px;
  /* border-radius: 100%;
  background-color: magenta; */
  /* background-color: #4A437F; */
}
.orbit5 {
  position: absolute;
  top: 60px;
  left: 60px;
  height: 80px;
  width: 80px;
  /* border-radius: 100%;
  background-color: magenta; */
  /* background-color: #4A437F; */
}

/* ---------- Container for the orbiting circles animation ---------- */
#circle-orbit-container {
  text-align: center
  position: relative;
  top: 25px;
  left: 25px;
  height: 300px;
  width: 300px;
}

/* ---------- Inner orbit - This is the circles closest to the central point ---------- */
#inner-orbit {
  position: absolute;
  top: 75px;
  left: 75px;
  width: 150px;
  height: 150px;
  border: 2px #4A437F dashed;
  border-radius: 100%;
  -webkit-animation: spin-right 10s linear infinite;
  animation: spin-right 10s linear infinite;
}

/* ---------- Repeating styles for the inner orbiting circles ---------- */
.inner-orbit-cirlces {
  position: absolute;
  top: 62px;
  left: -6px;
  height: 10px;
  width: 10px;
  border-radius: 100%;
  background-color: #9F98E6;
}

/* ---------- Middle orbit - This is the circles second closest to the central point ---------- */
#middle-orbit {
  position: absolute;
  top: 50px;
  left: 50px;
  width: 200px;
  height: 200px;
  border: 2px #4A437F dashed;
  border-radius: 100%;
  -webkit-animation: spin-right 15s linear infinite;
  animation: spin-right 15s linear infinite;
}

/* ---------- Repeating styles for the inner orbiting circles ---------- */
.middle-orbit-cirlces {
  position: absolute;
  top: 25px;
  left: 17px;
  height: 20px;
  width: 20px;
  border-radius: 100%;
  background-color: #4A437F;
}

/* ---------- Outer orbit - This is the circles furthest away from the central point ---------- */
#outer-orbit {
  position: absolute;
  top: 0;
  left: 0;
  width: 294px;
  height: 294px;
  border: 2px #4A437F dashed;
  border-radius: 100%;
  -webkit-animation: spin-right 20s linear infinite;
  animation: spin-right 20s linear infinite;
}

/* ---------- Repeating styles for the outer orbiting circles ---------- */
.outer-orbit-cirlces {
  position: absolute;
  top: -17px;
  left: 125px;
  height: 30px;
  width: 30px;
  border-radius: 100%;
  background-color: #00FFCA;
}

/* ---------- Animation ---------- */
@-webkit-keyframes spin-right {
  100% {
    -webkit-transform: rotate(360deg);
    -moz-transform: rotate(360deg);
    -ms-transform: rotate(360deg);
    -o-transform: rotate(360deg);
    transform: rotate(360deg);
  }
}

</style>
