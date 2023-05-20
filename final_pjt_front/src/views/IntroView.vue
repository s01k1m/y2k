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
            <div class="js-nametag">STEAL&nbsp;</div>
            <div class="js-nametag nametag2">&nbsp; STILL</div>
          </div>
          <div class="after-nametag">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;YOUR SHOW</div>
        </div>
        <div class="arrow bounce">
            <router-link to="/home" class="fa fa-arrow-down fa-2x">Let's go!</router-link>
          </div>
      </div>
    </div>
  </div>
</template>
  
<script>
export default {
  name: "IntroView",
};
</script>
<style scoped>

.fa{
  color: rgb(255, 255, 255);
  text-decoration: none;
  z-index: 10000;
  display: inline-block;
  }

.arrow {
  text-align: center;
  margin: 8% 0;
  color: rgb(255, 255, 255);
  text-decoration: none;
  z-index: 10000;
  display: inline-block
}
.bounce {
  -moz-animation: bounce 2s infinite;
  -webkit-animation: bounce 2s infinite;
  animation: bounce 2s infinite;
}

@keyframes bounce {
  0%, 20%, 50%, 80%, 100% {
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
  position: absolute;
  top: 0px;
  background-color: #2d2d37;
  width: 100vw;
  height: 100vh;
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
  margin: 0
}

div.intro-text {
  font-size: 40px;
  display: flex;
  justify-content:center;
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

}

.after-nametag{

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
    0%   {stroke-dashoffset: 230px;}
    100% {stroke-dashoffset: 0;}
}

div.intro-quote > {
}

img.to-home {
  position: absolute;
  width: 300px;
  display: inline-block;
  z-index: 1000;
  filter: invert(100%) sepia(0%) saturate(0%) hue-rotate(0deg) brightness(100%)
    contrast(100%);
}
</style>
