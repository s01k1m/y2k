<template>
  <div class="home">
    <h1>이 페이지는 홈이면서, 스틸컷의 나열 페이지입니다.</h1>
    <h1>{{ colorChoice }}</h1>
    <div v-for="(still, index) in stillBasedOnColor" :key="index">
      {{ still }}
    </div>
    <StillCard></StillCard>
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

    axios
      .get(`http://127.0.0.1:8000/stills/${this.colorChoice}/`) // django에서 db에 저장된 해당 색상 stillcut 정보를 받아옴
      .then((response) => {
        this.stillBasedOnColor = response.data
      })
      .catch((error) => {
        console.error(error);
      });
  },
  computed: {
    colorChoiceFromIntro() {
      return this.$route.params.colorChoice
    }
  },
}
</script>
