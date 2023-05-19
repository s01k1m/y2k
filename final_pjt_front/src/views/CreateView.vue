<template>
  <div class="create">
    <h1>스틸컷을 크리에이트하는 포스팅 페이지입니다. ^^</h1>
    <form>
      <v-file-input v-model="files" :multiple="false" placeholder="파일찾기" label="File input" :show-size="1000">d</v-file-input>
      <!-- 여러파일 보낼경우 multiple 사용 -->
      <button @click="sendImages">submit</button>
    </form>
    <!-- <form @submit.prevent="sendImages">
      <input type="text" v-model="still_image">
      <input type="text" v-model="still_color">
      <input type="submit" id="submit">
    </form>  -->
    
  </div>
</template>
<script>
import axios from 'axios'
// import fs from 'fs';
import FormData from 'form-data';

export default {
  name: 'CreateView',
  data() {
    return {
      files: null,
    }
  },
  computed: {
    isLogin() {
      return localStorage.getItem("access_token")
    }
  },
  created() {
    this.isLogined()
  },
  methods: {
    isLogined() {
      if (!this.isLogin) {
        console.log('if')
        alert('로그인이 필요합니다.')
        this.$router.push({ name: 'login' })
      } else {
        if (!this.$store.state.token) {
          this.$store.dispatch('getMemberInfo')
        }
      }
    },
    sendImages(e) {
    e.preventDefault()
    const form = new FormData()
    console.log(this.files)
    // form.images = this.files
    form.still_image = this.files
    console.log(form)
    console.log('token: ', this.$store.state.token)
    // axios({
    //   method: "POST",
    //   url: "http://127.0.0.1:8000/create/",
    //   data: { form },
    //   headers: { 
    //     "Content-Type": "multipart/form-data",
    //     Authorization: `Token ${this.$store.state.token}`
    //   },
    // })
    //   .then(function (response) {
    //     console.log(response)
    //   })
    //   .catch(function (response) {
    //     //handle error
    //     console.log(response)
    //   })
    axios.post("http://127.0.0.1:8000/create/", {form}, {
      headers: {
        "Content-Type": "multipart/form-data",
        Authorization: `Token ${this.$store.state.token}`
      },
    });
    // }
    // sendImages() {
    //   const still_image = this.still_image
    //   const still_color = this.still_color
    //   // let form = new FormData()
    //   // form.append('still_image', this.files)
    //   // console.log('form', form)
    //   axios({
    //     method: 'post',
    //     url: 'http://127.0.0.1:8000/create/',
    //     data: { still_image, still_color },
    //     headers: {
    //       // "Content-Type": "multipart/form-data",
    //       Authorization: `Token ${this.$store.state.token}`
    //     }, // 01024133215
    //     // withCredentials: true 
    //   })
    //   .then(() => {
    //     alert('sendImages 요청 성공')
    //     this.$router.push({ name: 'home '})
    //   })
    //   .catch((err) => {
    //     alert('sendImages 요청 실패')
    //     console.log(err)
    //   })
    }
  }
}
</script>

<style>
#create {
  margin: 24px;
}
</style>