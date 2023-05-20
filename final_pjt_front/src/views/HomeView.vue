<template>
  <div class="home">
    <h1>이 페이지는 홈이면서, 스틸컷의 나열 페이지입니다.</h1>
    <StillCard></StillCard>
  </div>
</template>

<script>
import StillCard from '@/components/StillCard.vue'

export default {
  name: 'HomeView',
  components: {
    StillCard
  }
}
</script>
