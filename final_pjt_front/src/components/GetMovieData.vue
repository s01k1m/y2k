<template>
  <div class="GetMovieData">
    <div class="options" @click="emitMovieId">
      
      {{ movie.movie_title }}
      {{movie.id}}
    </div>
  </div>
</template>

<script>
export default {
  name: 'GetMovieData',
  props: ['movie'],
  methods: {
  emitMovieId(event) {
    let dv = event.currentTarget;
    dv.classList.add('check')
    console.log(dv)
    console.log("선택한 무비의 id는", this.movie.id)
    // this.$emit('select-movie', this.movie.id)
  }
},
}

</script>

<style>
.GetMovieData{
  background-color: aquamarine;
}

.check{
  background-color: purple
}
</style>
