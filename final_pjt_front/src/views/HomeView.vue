<template>
  <div class="home">
    <h1>이 페이지는 홈이면서, 스틸컷의 나열 페이지입니다.</h1>
    <h1>{{ colorChoice }}</h1>
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
  created() {
    axios
      .get(`http://127.0.0.1:8000/stills/${this.colorChoice}/`) // django에서 db에 저장된 해당 색상 stillcut 정보를 받아옴
      .then((response) => {
        console.log("response.data", response.data);
      })
      .catch((error) => {
        console.error(error);
      });
  },
  computed: {
    colorChoice() {
      return this.$route.params.colorChoice
    }
  },
}
</script>
