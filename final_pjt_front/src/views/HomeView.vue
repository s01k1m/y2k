<template>
  <div class="home">
    <div id="category">
      <button @click="changeColor('ALL')" class="ALL">ALL</button>
      <button @click="changeColor('RED')" class="RED">RED</button>
      <button @click="changeColor('ORANGE')" class="ORANGE">ORANGE</button>
      <button @click="changeColor('YELLOW')" class="YELLOW">YELLOW</button>
      <button @click="changeColor('GREEN')" class="GREEN">GREEN</button>
      <button @click="changeColor('BLUE')" class="BLUE">BLUE</button>
      <button @click="changeColor('PINK')" class="PINK">PINK</button>
      <button @click="changeColor('PURPLE')" class="PURPLE">PURPLE</button>
      <button @click="changeColor('WHITE')" class="WHITE">WHITE</button>
      <button @click="changeColor('GREY')" class="GREY">GREY</button>
      <button @click="changeColor('BLACK')" class="BLACK">BLACK</button>
    </div>
    <div v-show="!stillBasedOnColor.length" class="noContents">There's no Stills!
    <br>
    :'(
    </div>
    <div id="columns">
      <figure v-for="(still, index) in stillBasedOnColor" :key="index">
        <StillCard :still="still" :index="index"></StillCard>
      </figure>
    </div>
  </div>
</template>

<script>
import StillCard from '@/components/StillCard.vue'
import axios from "axios"

export default {
  name: 'HomeView',
  components: {
    StillCard
  },
  data() {
    return {
      colorChoice : null,
      stillBasedOnColor : [],
    }
  },
  created() {
    if (!this.colorChoiceFromIntro) { // 선택된 색상이 없을 때 -> 인트로를 거치지 않고, 주소로 바로 들어왔을 때
      this.colorChoice = 'ALL' // 전부 보여주기
      console.log('선택 색상이 없음!!')
    } else {
      this.colorChoice = this.colorChoiceFromIntro
    }
    console.log('HomeView created 진입!')
    console.log(this.colorChoice)

    this.filterColor()
  },
  computed: {
    colorChoiceFromIntro() {
      return this.$route.params.colorChoice
    }
  },
  watch: {
    colorChoice() {
      console.log('watch 진입!!')
      this.filterColor()
    }
  },
  methods: {
    changeColor(color) {
      this.colorChoice = color
      console.log('color: ', color)
    },
    filterColor() {
      axios
      .get(`http://127.0.0.1:8000/stills/${this.colorChoice}/`) // django에서 db에 저장된 해당 색상 stillcut 정보를 받아옴
      .then((response) => {
        this.stillBasedOnColor = response.data
        console.log('this.stillBasedOnColor: ', this.stillBasedOnColor)
      })
      .catch((error) => {
        console.error(error);
      });
    },
  }
}
</script>

<style scoped>

#category {
  margin-bottom: 25px;
}

#columns{
    column-width:350px;
    column-gap: 15px;
    margin: 0 10px;
}
#columns figure{
  display: inline-block;
  /* border:1px solid rgba(0,0,0,0.2); */
  margin:0;
  margin-bottom: 15px;
  border-radius: 20px;
  /* box-shadow: 2px 2px 5px rgba(0,0,0,0.5);; */
}
#columns figure img{
  border-radius: 20px;
  width:100%;
}
#columns figure figcaption{
  border-top:1px solid rgba(0,0,0,0.2);
  padding:10px;
  margin-top:11px;
}
.noContents {
  margin: 200px 200px;
  font-size: x-large;
}
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
  background-color: rgb(49, 49, 49);
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