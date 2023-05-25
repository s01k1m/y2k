<template>
  <div class="intro">
    <div class="intro-content">
      <div class="intro-bg">
        <img class="intro-logo" src="../assets/logo.svg" />
        <div class="intro-name">
          <span>STILLER</span>
        </div>
        <div class="intro-text">
          <div class="parent-nametag">
            <div class="js-nametag">STEAL</div>
            <div class="js-nametag nametag2">&nbsp;STILL</div>
          </div>
          <div class="after-nametag">
            &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;YOUR
            SHOW
          </div>
        </div>
        <div class="palette">
          <div class="arrow bounce">
            <router-link :to="{ name: 'home' }" class="fa fa-arrow-down fa-2x"
              >Let's go!</router-link
            ><br />
          </div>
          <div>
            <button @click="selectColor('RED')" class="RED">RED</button>
            <button @click="selectColor('ORANGE')" class="ORANGE">ORANGE</button>
            <button @click="selectColor('YELLOW')" class="YELLOW">YELLOW</button>
            <button @click="selectColor('GREEN')" class="GREEN">GREEN</button>
            <button @click="selectColor('BLUE')" class="BLUE">BLUE</button>
            <button @click="selectColor('PINK')" class="PINK">PINK</button>
            <button @click="selectColor('PURPLE')" class="PURPLE">PURPLE</button>
            <button @click="selectColor('WHITE')" class="WHITE">WHITE</button>
            <button @click="selectColor('GREY')" class="GREY">GREY</button>
            <button @click="selectColor('BLACK')" class="BLACK">BLACK</button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
  
<script>
export default {
  name: "IntroView",
  methods: {
    selectColor(colorChoice) {
      this.$router.push({ name: "home", params: { colorChoice: colorChoice } });
    },
  },
};
</script>
<style scoped>

/* Let's go 애니메이션 */
.fa {
  color: rgb(255, 255, 255);
  text-decoration: none;
  z-index: 10000;
  display: inline-block;
}

.arrow {
  text-align: center;
  margin: 8px 0;
  color: rgb(255, 255, 255);
  text-decoration: none;
  z-index: 10000;
  display: inline-block;
}
.bounce {
  -moz-animation: bounce 2s infinite;
  -webkit-animation: bounce 2s infinite;
  animation: bounce 2s infinite;
}

@keyframes bounce {
  0%,
  20%,
  50%,
  80%,
  100% {
    transform: translateY(0);
  }
  40% {
    transform: translateY(-30px);
  }
  60% {
    transform: translateY(-15px);
  }
}

div.intro {
  text-align: center;
}

div.intro-bg {
  width: 100%;
  height: 100%;
  position: absolute;
  top: 0px;
  background-color: #2d2d37;
  z-index: 0;
  display: flex;
  justify-content: center;
  align-items: center;
  flex-direction: column;
}

div.intro-content {
  color: white;
  z-index: 1000;
  background-color: aliceblue;
}

div.intro-name {
  position: relative;
  display: flex;
  align-items: center;
  justify-content: center;
}

div.intro-name > span {
  font-size: 150px;
  padding-bottom: 0;
  /* line-height: 200px; */
}

div.intro-text {
  font-size: 40px;
  display: flex;
  justify-content: center;
  padding-bottom: 70px;

}

img.intro-logo {
  filter: invert(100%) sepia(0%) saturate(0%) hue-rotate(0deg) brightness(100%)
    contrast(100%);
  width: 200px;
  margin: 30px 0 0 0;
}

.js-nametag {
  font-weight: 900;
  position: absolute;
}
.parent-nametag {
  display: inline-block;

}

.after-nametag {
  margin-left: 20px;
}

.js-nametag:nth-child(1) {
  animation-name: fade;
  animation-fill-mode: both;
  animation-iteration-count: infinite;
  animation-duration: 5s;
  animation-direction: alternate-reverse;
}

.js-nametag:nth-child(2) {
  animation-name: fade;
  animation-fill-mode: both;
  animation-iteration-count: infinite;
  animation-duration: 5s;
  animation-direction: alternate;
}

@keyframes fade {
  0%,
  50% {
    opacity: 0;
  }
  100% {
    opacity: 1;
  }
}

.ani3 {
  animation: ani3 1s infinite linear alternate-reverse;
  stroke-dasharray: 230px;
  stroke-dashoffset: 230px;
}
@keyframes ani3 {
  0% {
    stroke-dashoffset: 230px;
  }
  100% {
    stroke-dashoffset: 0;
  }
}

img.to-home {
  position: absolute;
  width: 300px;
  display: inline-block;
  z-index: 1000;
  filter: invert(100%) sepia(0%) saturate(0%) hue-rotate(0deg) brightness(100%)
    contrast(100%);
}

div.palette {
  display: flex;
  justify-content: center;
  align-items: center;
  flex-direction: column;
}



/*             <button @click="selectColor('RED')" class="RED">RED</button> |
            <button @click="selectColor('ORANGE')" class="ORANGE">ORANGE</button> |
            <button @click="selectColor('YELLOW')" class="YELLOW">YELLOW</button> |
            <button @click="selectColor('GREEN')" class="GREEN">GREEN</button> |
            <button @click="selectColor('BLUE')" class="BLUE">BLUE</button> |
            <button @click="selectColor('PINK')" class="PINK">PINK</button> |
            <button @click="selectColor('PURPLE')" class="PURLE">PURPLE</button> |
            <button @click="selectColor('WHITE')" class="WHITE">WHITE</button> |
            <button @click="selectColor('GREY')" class="GREY">GREY</button> |
            <button @click="selectColor('BLACK')" class="BLACK">BLACK</button> | */
            button.ALL {
  background-image: linear-gradient(to right, #ff9092,  #ffeb77, #8dccf0);
  color: white;
  padding: 8px 10px;
  margin: 10px;
  border-radius: 30px;
}

button.RED {
  background-color: #ff9092;
  color: white;
  padding: 8px 10px;
  margin: 10px;
  border-radius: 30px;
}

button.ORANGE {
  background-color: #ffb76e;
  color: white;
  padding: 8px 10px;
  margin: 10px;
  border-radius: 30px;
}

button.YELLOW {
  background-color: #ffeb77;
  color: white;
  padding: 8px 10px;
  margin: 10px;
  border-radius: 30px;
}

button.GREEN{
  background-color: #81e98f;
  color: white;
  padding: 8px 10px;
  margin: 10px;
  border-radius: 30px;
}

button.BLUE{
  background-color:#8dccf0;
  color: white;
  padding: 8px 10px;
  margin: 10px;
  border-radius: 30px;
}

button.PURPLE {
  background-color: #ad99e2;
  color: white;
  padding: 8px 10px;
  margin: 10px;
  border-radius: 30px;
}

button.PINK {
  background-color: #fc9ddf;
  color: white;
  padding: 8px 10px;
  margin: 10px;
  border-radius: 30px;
}

button.WHITE{
  background-color: rgb(255, 255, 255);
  padding: 8px 10px;
  color: rgb(172, 172, 172);
  margin: 10px;
  border-radius: 30px;
  border: solid 0.5px #e2e2e2;
}

button.GREY{
  background-color: rgb(172, 172, 172);
  color: white;
  padding: 8px 10px;
  margin: 10px;
  border-radius: 30px;
}

button.BLACK{
  background-color: rgb(0, 0, 0);
  color: white;
  padding: 8px 10px;
  margin: 10px;
  border-radius: 30px;
}

button:focus {
  animation: shine 0.6s ease forwards;
}

@keyframes shine {
  0% {
    transform: scale(1);
  }
  50% {
    transform: scale(1);
  }
  100% {
    transform: scale(1);
    box-shadow: 0 4px 8px 0 rgb(172, 172, 172);
  }
}
</style>
