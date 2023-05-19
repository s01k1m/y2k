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
    // image 보내기
    sendImages(e) {
      e.preventDefault()
      console.log('sendImages 실행합니다.')
      var info = new FormData()
      if (this.files) {             // 파일 있으면
        info.images = this.files
      } else {
        console.log(
          '파일 없음'
        )
      }
      console.log('info: ', info)
      console.log('files: ', this.files)
      const token = localStorage.getItem("token") // token을 세션에 저장시켜 사용했기 때문에
      let config = {
        headers: {
          'Content-Type': 'multipart/form-data', // Content-Type을 변경해야 파일이 전송됨
          'Authorization': `token ${token}`,
          'Access-Control-Allow-Origin':'http://127.0.0.1:8000/create/'
          }
      }
      console.log(info)
      axios.post(
        'http://127.0.0.1:8000/create/', 
        info, config)
      .then((res) => {
        console.log('데이터를 http://127.0.0.1:8000/create/로 보내고 있음')
        console.log(res) // 필요한 것 넣어서 쓰면됨
      })
      .catch((err) => {
        console.log(err.response)
      })
    }
  }
}
</script>

<style>
#create {
  margin: 24px;
}

</style>