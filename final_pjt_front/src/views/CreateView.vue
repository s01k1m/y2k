<template>
  <div class="create">
    <h1>스틸컷을 크리에이트하는 포스팅 페이지입니다. ^^</h1>
    <form>
      <v-file-input v-model="files" :multiple="false" label="File input"></v-file-input>
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
    const form = new FormData();
    console.log(this.files)
    // form.images = this.files
    form.append('still_image', this.files);
    console.log(form.images)

    let token = localStorage.getItem("access_token")
    axios.post("http://127.0.0.1:8000/create/", form, {
    headers: {
      "Content-Type": "multipart/form-data",
      // 와 이거 하나땜에 몇시간을 ^0^ 하하하핳ㅋㅋㅋㅋ
      Authorization : 'Token ' + token
    },
    })
          .then(function (response) {
        console.log(response);
      })
      .catch(function (response) {
        //handle error
        console.log(response);
      });
    }
  }
}
</script>

<style scoped>
#create {
  margin: 24px;

}


form  {

  width: 400px;
  margin: 0 auto;
}
</style>