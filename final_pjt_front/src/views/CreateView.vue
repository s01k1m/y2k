<template>
  <div class="create">
    <h1>스틸컷을 크리에이트하는 포스팅 페이지입니다. ^^</h1>
    <form>
      <v-file-input v-model="files" :multiple="false" placeholder="파일찾기" label="File input" :show-size="1000">d</v-file-input>
      <!-- 여러파일 보낼경우 multiple 사용 -->
      <button @click="sendImages">submit</button>
    </form>
    
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
      title: null,
      image: null,
      movie_id: null,
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
      } 
    },
    // sendImages(e) {
    // e.preventDefault()
    // const form = new FormData();
    // console.log(this.files)
    // // form.images = this.files
    // form.append('still_image', this.files);
    // console.log(form.images)
    // // axios({
    // //   method: "POST",
    // //   url: "http://127.0.0.1:8000/create/",
    // //   body: form,
    // //   headers: { "Content-Type": "multipart/form-data"},
    // // })
    // //   .then(function (response) {
    // //     console.log(response);
    // //   })
    // //   .catch(function (response) {
    // //     //handle error
    // //     console.log(response);
    // //   });
    // axios.post("http://127.0.0.1:8000/create/", form, {
    // headers: {
    //   "Content-Type": "multipart/form-data",
    // },
    // });
    // }
    sendImages() {
      const form = new FormData()
      form.append()
      this.files
    }
  }
}
</script>

<style>
#create {
  margin: 24px;
}
</style>