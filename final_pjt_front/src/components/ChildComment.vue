<template>
  <div>
    {{ comment }}
  </div>
</template>

<script>
export default {
  name: 'ChildComment',
  props: {
    comment: Object,
  },
}
</script>

<style>

</style>